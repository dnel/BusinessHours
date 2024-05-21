# Business Hours

A Python module that calculates working time between two given 
datetimes. Opening and closing time, weekend days and holidays are 
configurable.

## Origin

This was initially a fork of solar345's [BusinessHours](https://pypi.org/project/BusinessHours/) module to add the 
getminutes() function providing the minute-level resolution I needed. 
It was then easier to make gethours() and getdays() a derivative of this 
and by then I had rewritten the module leaving only superficial 
similarities to Solar345's original module.

This was originally written for Python 2 but works fine on Python 3.

## Closures

Non-business days can be added as a list of datetimes or the output from
the python-holidays module.

### Regional holidays
It optionally supports [python-holidays](https://github.com/vacanza/python-holidays/) to respect free holidays 
specific to a country or even a region.
```
import holidays
holidays = holidays.country_holidays('DE', subdiv="BW")
myHours = BusinessHours(start_time, end_time, holidays=holidays)
```
