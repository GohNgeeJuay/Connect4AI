class Tree():
    def __init__(self,data):
        ''' Creates a Tree instance. Contains the root node of the tree
        @param:     data. Intended to contain the array representation of Connect4Board
        @return:    None
        @raises:    None

        '''
        self.root = Node(data)
                    

class Node():
    def __init__(self, data, numOfChild = 7):
        ''' Creates a Node instance. 
        Variables: 
        data.           Contains the array representation of Connect4Board
        child.          Array containing the 7 children. Could contain None if not fully occupied.
        arrayCounter.   int indicating the next empty space in the child array.
        isLeaf.         Boolean indicating whether the node is a terminal node and shouldn't be grown further
        value.          Contain the value of the board used for minmax algorithm

        @param:     data. Intended to contain the array representation of Connect4Board
        @param:     numOfChild: int for size of the array for number of children a node has. Default = 7.
        @return:    None
        @raises:    None

        '''

        self.data = data
        self.child = [None] * numOfChild
        self.arrayCounter = 0
        self.arraySize = numOfChild
        self.isLeaf = False    #Attribute to terminate growing
        self.value = 0    #value of the data(board) initialize to 0. Will change based on evaluation from scoring.

    def add_child(self, data):
        ''' Adds a child into the child array.  
        @param:     data. Intended to contain the array representation of Connect4Board
        @return:    None
        @raises:    Exception. If the child array fully occupied.

        '''
        if self.arrayCounter >= self.arraySize:
            raise Exception("Child already has 7 child")
        else:
            self.child[self.arrayCounter] = data
            self.arrayCounter += 1

    def get_previous_added_child(self):
        ''' Returns the index of previously added child in the child array.  
        @param:     None
        @return:    None
        @raises:    Exception. If the child array is empty.

        '''
        if self.arrayCounter == 0:
            raise Exception("This node has no child yet")
        else: 
            return self.arrayCounter - 1


    def scoring(self, lastPiece):
        ''' Returns the score of a board of a particular node  
        @param:     None
        @return:    None
        @raises:    Exception. If the child array is empty.

        '''
        return