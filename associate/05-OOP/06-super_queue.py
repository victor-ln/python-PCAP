#!/usr/bin/python3

class QueueError(LookupError):
    def __init__(self):
        LookupError.__init__(self, "Tried to use get() method on empty Queue")

class Queue:
    def __init__(self):
        self.__queue = []
        self._len = 0

    def put(self, elem):
        self.__queue.append(elem)
        self._len += 1

    def get(self):
        if self._len == 0:
            raise QueueError()
        self._len -= 1
        return self.__queue.pop(0)

class SuperQueue(Queue):
    def __init__(self):
        Queue.__init__(self)

    def isempty(self):
        return self._len == 0

que = SuperQueue()
que.put(1)
que.put("dog")
que.put(False)
for i in range(4):
    if not que.isempty():
        print(que.get())
    else:
        print("Queue empty")
