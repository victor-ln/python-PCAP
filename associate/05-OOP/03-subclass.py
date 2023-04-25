#!/usr/bin/python3

class Stack:
    def __init__(self):
        self.__stack_list = []

    def push(self, val):
        self.__stack_list.append(val)

    def pop(self):
        val = self.__stack_list[-1]
        del self.__stack_list[-1]
        return val

# Gets all components defined by its superclass
class AddingStack(Stack):

    def __init__(self):
        # Unlike many other languages, 
        # Python forces you to explicitly invoke a superclass's constructor.
        Stack.__init__(self)

        # it is generally best practice to invoke the superclass constructor 
        # before any other initializations you wish to perform within the subclass
        self.__sum = 0

    def push(self, val):
        self.__sum += val

        # - We have to specify the name of the superclass; this is necessary to 
        #   clearly indicate the class containing the method,
        #   to avoid confusing it with any other function of the same name;
        #
        # - We have to specify the target object and pass it as the first 
        #   argument (it is not implicitly added to the invocation in this context).
        Stack.push(self, val)

    def pop(self):
        val = Stack.pop(self)
        self.__sum -= val
        return val
    
    def get_sum(self):
        return self.__sum


stack_object = AddingStack()

for i in range(5):
    stack_object.push(i)
print(stack_object.get_sum())

for i in range(5):
    print(stack_object.pop())