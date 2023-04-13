#!/usr/bin/env python3

# Objective:
# 
# Your task is to prepare a simple code that can evaluate the final 
# time of a time period given as a number of minutes (which can be arbitrarily large). 
# The initial time is given as a pair of hours (0.. 23) and minutes (0.. 59). The result should be printed to the console.
# For example, if an event starts at 12:17 and lasts for 59 minutes, it will end at 13:16.
# Don't worry about any imperfections in your 
# code - it's okay if it accepts an invalid time - the most important thing 
# is that the code produces valid results for valid input data.
#

# Sample Input:
# 12
# 17
# 59

# Expected output: 13:16

# Sample Input:
# 23
# 58
# 642

# Expected output: 10:40

# Sample Input:
# 0
# 1
# 2939

# Expected output: 1:0

hour = int(input("Starting time (hours): "))
mins = int(input("Starting time (minutes): "))
dura = int(input("Event duration (minutes): "))

mins += dura
hour += mins // 60

hour %= 24
mins %= 60

print(hour, ":", mins, sep='')
