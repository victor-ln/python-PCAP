#!/usr/bin/env python3

# Demonstrating the endswith() method:
if "epsilon".endswith("on"):
    print("yes")
else:
    print("no")

t = "zeta"
print(t.endswith("a"))
print(t.endswith("A"))
print(t.endswith("et"))
print(t.endswith("eta"))
print()

# Demonstrating the startswith() method:
print("omega".startswith("meg"))
print("omega".startswith("om"))
