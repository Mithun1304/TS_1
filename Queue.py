class Queue:

    def init(self): # create
        self.items = []

    def is_empty(self):
        return self.items == []

    def enqueue(self,item):
        self.items.insert(0,item)

    def dequeue(self):
        return self.items.pop()


    def size(self):
        return len(self.items)

    def peek(self):
        return self.items[len(self.items)-1]

    def size(self):
        return len(self.items)

d=Queue()
d.enqueue(10)
d.enqueue(20)
print(d.size())
d.dequeue()
print(d.peek())