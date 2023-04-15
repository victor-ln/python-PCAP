#!/usr/bin/env python3

# step 1: create an empty list named beatles;
# step 2: use the append() method to add the following band members to the list: John Lennon, Paul McCartney, and George Harrison;
# step 3: use the for loop and the append() method to prompt the user to add the following band members to the list: Stu Sutcliffe, and Pete Best;
# step 4: use the del statement to remove Stu Sutcliffe and Pete Best from the list;
# step 5: use the insert() method to add Ringo Starr to the beginning of the list.

# step 1
beatles = []

print("Step 1:", beatles)

# step 2

beatles.append('John Lennon')
beatles.append('Paul McCartney')
beatles.append('George Harrison')

print("Step 2:", beatles)

# step 3
print('Add the following members: Stu Sutcliffe and Pete Best')
for i in range(2):
    beatles.append(input())

print("Step 3:", beatles)

# step 4
del beatles[-2:]
print("Step 4:", beatles)

# step 5
beatles.insert(0, 'Ringo Starr')
print("Step 5:", beatles)


# testing list legth
print("The Fab", len(beatles))
