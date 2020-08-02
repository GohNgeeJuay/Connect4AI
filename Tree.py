#from Connect4 import Connect4Board

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

    def add_child(self, data, index):
        ''' Adds a child into the child array.  
        @param:     data. Intended to contain the array representation of Connect4Board
        @return:    None
        @raises:    Exception. If the child array fully occupied.

        '''
        # if self.arrayCounter >= self.arraySize:
        #     raise Exception("Child already has 7 child")
        # else:
        self.child[index] = data
        self.arrayCounter += 1

    def get_previous_added_child(self):    #Not used. Each next possible column in the proper index
        ''' Returns the index of previously added child in the child array.  
        @param:     None
        @return:    None
        @raises:    Exception. If the child array is empty.

        '''
        if self.arrayCounter == 0:
            raise Exception("This node has no child yet")
        else: 
            return self.arrayCounter - 1


    # def scoring(self, lastPiece,n_seq = 4):
    #     ''' Returns the score of a board of a particular node  
    #     @param:     lastPiece, Tuple containing the row,column position of the last piece added into board
    #     @param:     n_seq, The winning condition for connect sequence. Default = 4.
    #     @return:    None
    #     @raises:    Exception. If the child array is empty.

    #     '''
    #     #Center column
    #     if lastPiece[1] == 3:
    #         self.value += 4
        
    #     #Lines of two/three/win
    #     DIRECTIONS = (
    #             (-1, -1), (-1, 0), (-1, 1),
    #             ( 0, -1),          ( 0, 1),
    #             ( 1, -1), ( 1, 0), ( 1, 1),
    #             )


    #     for i in range(1,n_seq):
    #         count = 0     #count of matches
    #         for dr, dc in DIRECTIONS:
    #             checkR = lastPiece[0] + dr*i
    #             checkC = lastPiece[1] + dc*i

    #             if checkR not in range(0,len(self.data)) or checkC not in range(0,len(self.data[0])):
    #                 count = 0    #Go out of bounds in this direction. So should not be counted
    #                 break

    #             else:
    #                 if self.data[lastPiece[0]][lastPiece[1]] == self.data[checkR][checkC]:
    #                     count += 1
                
    #         #Scoring for different number of counts. 1 direction would only increase self.value by 1 value. 
    #         # (no overlapping increments) 
    #         if count == 1:    #lines of 2
    #             self.value += 2

    #         elif count == 2:    #lines of 3
    #             self.value += 4
            
    #         elif count == 3:    #winning condition
    #             self.value += 1000



            
    #     return

    #Heuristics reference: https://www.youtube.com/watch?v=MMLtza3CZFM&list=WL&index=34&t=441s
    def scoring(self,lastPiece,n_seq=4):
        #horizontal
        #score = 0
        for r in range(len(self.data)):    #Need to move a window from left to right of every row
            row_array = self.data[r].copy()
            for c in range(len(row_array)-3):    #-3 for window size of 4 in 7 column board
                window = row_array[c:c+n_seq]

                if window.count(self.data[lastPiece[0]][lastPiece[1]]) == 4:
                    self.value += 100

                elif window.count(self.data[lastPiece[0]][lastPiece[1]]) == 3 and window.count(' ') == 1:
                    self.value += 10            

                elif window.count(self.data[lastPiece[0]][lastPiece[1]]) == 2 and window.count(' ') == 2:
                    self.value += 5

                

