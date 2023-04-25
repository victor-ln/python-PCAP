#!/usr/bin/python3

class Stack:

    # The mandatory parameter is usually called 
    # 'self' - it's just a convention, but you must follow it

    def __init__(self): # constructor function

        # Any changes you make inside the constructor that modify the state 
        # of the 'self' parameter will be reflected in the newly created object.

        # public variable would be:
        # self.stack_list = []

        # When any class component has a name that starts 
        # with two underscores (__), it becomes private
        self.__stack_list = []

    # Whenever Python invokes a method, 
    # it implicitly sends the current object as the first argument.

    def push(self, val):
        self.__stack_list.append(val)


    # All methods must have the 'self' parameter.
    # It allows the method to access entities 
    # (properties and activities/methods) performed by the current object.

    def pop(self): 
        val = self.__stack_list[-1]
        del self.__stack_list[-1]
        return val


stack_object = Stack()
try:
    print(len(stack_object.__stack_list))
except:
    print('AttributeError')

stack_object.push(3)
stack_object.push(2)
stack_object.push(1)

print(stack_object.pop())
print(stack_object.pop())
print(stack_object.pop())

