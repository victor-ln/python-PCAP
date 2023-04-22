#!/usr/bin/env python3

# Demonstrating the find() method:
print("Eta".find("ta"))
print("Eta".find("mma"))
print()

t = 'theta'
print(t.find('eta'))
print(t.find('et'))
print(t.find('the'))
print(t.find('ha'))
print()

print('kappa'.find('a', 2))
print()

the_text = """A variation of the ordinary lorem ipsum
text has been used in typesetting since the 1960s 
or earlier, when it was popularized by advertisements 
for Letraset transfer sheets. It was introduced to 
the Information Age in the mid-1980s by the Aldus Corporation, 
which employed it in graphics and word-processing templates
for its desktop publishing program PageMaker (from Wikipedia)"""

fnd = the_text.find('the')
while fnd != -1:
    print(fnd)
    fnd = the_text.find('the', fnd + 1)

print()
print('kappa'.find('a', 1, 4))
print('kappa'.find('a', 2, 4))
