Business Hours
==============

A Python module that calculates working time between two given datetimes. Opening and closing time and the weekend days are configurable.

There are 3 methods available:

getminutes()

Returns the number of working minutes between the two datetimes.

gethours()

Returns the number of full hours worked based on the number of working minutes divided by 60. Reminder minutes will be truncated, if remainder minutes are required perform a modulus of getminutes().

getdays()

Returns the number of full days worked based on the number of working minutes divided by the number in hours in a working day.
