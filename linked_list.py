
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class LinkedList:
    def __init__(self):
        self.top = None

    def push(self, data):
        nd = Node(data)
        nd.next = self.top
        self.top = nd

    def display(self):
        if self.top == None:
            print("The stack is empty")
            return
        top = self.top
        while top is not None:
            print(top.data)
            top = top.next

