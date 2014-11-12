import datetime


class BusinessHours:

    def __init__(self, datetime1, datetime2, worktiming=[9, 17],
                 weekends=[6, 7]):
        self.weekends = weekends
        self.worktiming = worktiming
        self.datetime1 = datetime1
        self.datetime2 = datetime2
        self.day_minutes = (self.worktiming[1]-self.worktiming[0])*3600

    def getdays(self):
        """
        Return the difference in days.
        """
        days = (self.datetime2-self.datetime1).days
        # exclude any day in the week marked as holiday (ex: saturday , sunday)
        noofweeks = days / 7
        extradays = days % 7
        startday = self.datetime1.isoweekday()
        days = days - (noofweeks * self.weekends.__len__())
        for weekend in self.weekends:
            if(startday == weekend):
                days = days - 1
            else:
                if(weekend >= startday):
                    if(startday+extradays >= weekend):
                        days = days - 1
                else:
                    if(7-startday+extradays >= weekend):
                        days = days - 1
        return days

    def gethours(self):
        """
        Return the difference in hours.
        """
        days = self.getdays()
        #  calculate hours
        days = days - 2  # -2 to remove the start day and the last day
        hoursinaday = self.worktiming[1]-self.worktiming[0]
        hours = days * hoursinaday
        # To calculate working hours in the first day.
        if(self.datetime1.hour < self.worktiming[0]):
            hoursinfirstday = hoursinaday
        elif(self.datetime1.hour > self.worktiming[1]):
            hoursinfirstday = 0
        else:
            hoursinfirstday = self.worktiming[1]-self.datetime1.hour
        # To calculate working hours in the last day
        if(self.datetime2.hour > self.worktiming[1]):
            hoursinlastday = hoursinaday
        elif(self.datetime2.hour < self.worktiming[0]):
            hoursinlastday = 0
        else:
            hoursinlastday = self.datetime2.hour - self.worktiming[0]
        hours = hours + hoursinfirstday + hoursinlastday
        return hours

    def getminutes(self):
        """
        Return the difference in minutes.
        """
        # Set initial default variables
        dt_start = self.datetime1  # datetime of start
        dt_end = self.datetime2    # datetime of end
        worktime = 0               # remaining minutes after full days

        if dt_start.date() == dt_end.date():
            # starts and ends on same workday
            full_days = 0
            if self.is_weekend(dt_start):
                return 0
            else:
                if dt_start.hour < self.worktiming[0]:
                    # set start time to opening hour
                    dt_start = datetime.datetime(
                        year=dt_start.year,
                        month=dt_start.month,
                        day=dt_start.day,
                        hour=self.worktiming[0],
                        minute=0)
                if dt_start.hour >= self.worktiming[1] or \
                        dt_end.hour < self.worktiming[0]:
                    return 0
                if dt_end.hour >= self.worktiming[1]:
                    dt_end = datetime.datetime(
                        year=dt_end.year,
                        month=dt_end.month,
                        day=dt_end.day,
                        hour=self.worktiming[1],
                        minute=0)
                worktime = (dt_end-dt_start).total_seconds()
        elif (dt_end-dt_start).days < 0:
            # ends before start
            return 0
        else:
            current_day = dt_start  # marker for counting workdays
            while not current_day.date() == dt_end.date():
                if not self.is_weekend(current_day):
                    if current_day == dt_start:
                        # increment hours of first day
                        if current_day.hour < self.worktiming[0]:
                            worktime += self.day_minutes  # add 1 day
                        elif current_day.hour >= self.worktiming[1]:
                            pass  # no time on first day
                        else:
                            dt_currentday_close = datetime.datetime(
                                year=dt_start.year,
                                month=dt_start.month,
                                day=dt_start.day,
                                hour=self.worktiming[1],
                                minute=0)
                            worktime += (dt_currentday_close
                                         - dt_start).total_seconds()
                    else:
                        # increment one full day
                        worktime += self.day_minutes
                current_day += datetime.timedelta(days=1)  # next day
            # Time on the last day
            if not self.is_weekend(dt_end):
                if dt_end.hour >= self.worktiming[1]:  # finish after close
                    # Add a full day
                    worktime += self.day_minutes
                elif dt_end.hour < self.worktiming[0]:  # close before opening
                    pass  # no time added
                else:
                    # Add time since opening
                    dt_end_open = datetime.datetime(
                        year=dt_end.year,
                        month=dt_end.month,
                        day=dt_end.day,
                        hour=self.worktiming[0],
                        minute=0)
                    worktime += (dt_end-dt_end_open).total_seconds()
        return int(worktime / 60)

    def is_weekend(self, datetime):
        """
        Returns True if datetime lands on a weekend.
        """
        for weekend in self.weekends:
            if datetime.isoweekday() == weekend:
                return True
        return False
