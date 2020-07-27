class Tree():
    def __init__(self,data):
        self.root = Node(data)
                    

class Node():
    def __init__(self, data, numOfChild = 7):
        self.data = data
        self.child = [None] * numOfChild
        self.arrayCounter = 0
        self.arraySize = numOfChild

    def add_child(self, data):
        if self.arrayCounter >= self.arraySize:
            raise Exception("Child already has 7 child")
        else:
            self.child[self.arrayCounter] = data
            self.arrayCounter += 1

    def get_previous_added_child(self):
        if self.arrayCounter == 0:
            raise Exception("This node has no child yet")
        else: 
            return self.arrayCounter - 1





# x = Tree(1)
# print(x.root.data)
# x.root.add_child(2)
# print(x.root.child)
# x.root.add_child(3)
# print(x.root.child)
