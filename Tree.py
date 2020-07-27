class Tree():
    def __init__(self,data):
        self.root = Node(data)
        self.root.data = data
            

class Node():
    def __init__(self, data, size = 7):
        self.data = data
        self.child = [None] * size
        self.arrayCounter = 0
        self.arraySize = size

    def add_child(self, data):
        if self.arrayCounter >= self.arraySize:
            raise Exception("Child already has 7 child")
        else:
            self.child[self.arrayCounter] = data
            self.arrayCounter += 1





x = Tree(1)
print(x.root.data)
x.root.add_child(2)
print(x.root.child)
x.root.add_child(3)
print(x.root.child)
