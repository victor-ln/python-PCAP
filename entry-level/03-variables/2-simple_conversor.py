#!/usr/bin/env python3

# Expected Output:
#
# 7.38 miles is 11.88 kilometers
# 12.25 kilometers is 7.61 miles
#

kilometers = 12.25
miles = 7.38

miles_to_kilometers = miles *  1.61
kilometers_to_miles = kilometers / 1.61

print(miles, "miles is", round(miles_to_kilometers, 2), "kilometers")
print(kilometers, "kilometers is", round(kilometers_to_miles, 2), "miles")
