# Business Hours

A Python module that calculates working time between two given datetimes. Opening and closing time and the weekend days are configurable.

## Usage
There are 3 methods available:

getminutes()

Returns and integer of the number of working minutes between the two datetimes.

gethours()

Returns an integer of the number of full hours worked. calculated from the return of getminutes() divided by 60. Aways rounded down, reminder minutes are truncated by the integer conversion, if remainder minutes are required perform a modulus of getminutes().

getdays()

Returns an integrer of the number of full days worked calculated from the return of getminutes() divided by the number of available minutes in a working day.



## Regional holidays
It optionally supports [python-holidays](https://github.com/vacanza/python-holidays/) to respect free holidays specific to a country or even a region.
```
import holidays
holidays = holidays.country_holidays('DE', subdiv="BW")
myHours = BusinessHours(start_time, end_time, holidays=holidays)
```
