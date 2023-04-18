#!/usr/bin/env python3

from platform import (platform, machine, processor, system, version)

print(platform(), machine(), processor(), system(), version(), sep='\n')
print()

from platform import python_implementation, python_version_tuple

print(python_implementation())

for atr in python_version_tuple():
    print(atr)
