#!/usr/bin/env python3

km_per_mile = 1.609344
gallon_liters = 3.785411784

def liters_100km_to_miles_gallon(liters):
    return (100 / km_per_mile) / (liters / gallon_liters)

def miles_gallon_to_liters_100km(miles):
    return (gallon_liters / miles) / km_per_mile * 100

print(liters_100km_to_miles_gallon(3.9))
print(liters_100km_to_miles_gallon(7.5))
print(liters_100km_to_miles_gallon(10.))
print(miles_gallon_to_liters_100km(60.3))
print(miles_gallon_to_liters_100km(31.4))
print(miles_gallon_to_liters_100km(23.5))
