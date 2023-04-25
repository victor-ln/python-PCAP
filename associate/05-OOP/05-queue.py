#!/usr/bin/python3

class QueueError(LookupError):
    def __init__(self):
        LookupError.__init__(self, "Tried to use get() method on empty Queue")

class Queue:
    def __init__(self):
        self.__queue = []
        self.__len = 0

    def put(self, elem):
        self.__queue.append(elem)
        self.__len += 1

    def get(self):
        if self.__len == 0:
            raise QueueError()
        self.__len -= 1
        return self.__queue.pop(0)

que = Queue()
que.put(1)
que.put("dog")
que.put(False)
try:
    for i in range(4):
        print(que.get())
except:
    print("Queue error")
