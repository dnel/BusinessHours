# Business Hours

A Python module that calculates working time between two given 
datetimes. Opening and closing time, weekend days and holidays are 
configurable.

## Origin

This was initially a fork of solar345's [BusinessHours](https://pypi.org/project/BusinessHours/) module to add the 
getminutes() function providing the minute-level resolution I needed. 
It was then easier to make gethours() and getdays() a derivative of this 
and by then I had replaced the all the functional code leaving only 
superficial similarities to Solar345's original module.

This was originally written for Python 2 but works fine on Python 3.

## Example usage

```
from datetime import datetime
import BusinessHours as bh
import holidays

hols = holidays.UK()

start = datetime(2024,3,25)
end = datetime(2024,4,3)

test = bh.BusinessHours(start, end)
holiday_test = bh.BusinessHours(start, end, holidays=hols)

print(test.getdays())  # output: 7
print(holiday_test.getdays()) # output: 6
```

## Holiday Closures

Non-business days can be added as a list of datetimes or the output from
the [python-holidays](https://github.com/vacanza/python-holidays/) module.
