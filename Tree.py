#from Connect4 import Connect4Board
import numpy

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

    def evaluate_window(self,window, piece):
        pieces = {'x','o'}    #All pieces available
        curr_piece = {piece}    
        opp_piece = pieces - curr_piece    #Get difference 
        opp_piece = opp_piece.pop()    #To get the opponent piece


        if window.count(piece) == 4:
            self.value += 100
        
        elif window.count(piece) == 3 and window.count(' ') == 1:
            self.value += 10

        elif window.count(piece) == 2 and window.count(' ') == 2:
            self.value += 5
        
        if window.count(opp_piece) == 3 and window.count(' ') ==1:
            self.value -= 80


    #Heuristics reference: https://www.youtube.com/watch?v=MMLtza3CZFM&list=WL&index=34&t=441s
    def scoring(self,lastPiece,n_seq=4):
        #center
        center_count = 0
        for r in range(len(self.data)):
            if self.data[r][len(self.data[0])//2] == self.data[lastPiece[0]][lastPiece[1]]:
                center_count += 1
        self.value += center_count * 6

        
        #horizontal
        for r in range(len(self.data)):    #Need to move a window from left to right of every row
            row_array = self.data[r].copy()
            for c in range(len(row_array)-n_seq+1):    #-3 for window size of 4 in 7 column board
                window = row_array[c:c+n_seq]

                self.evaluate_window(window, piece= self.data[lastPiece[0]][lastPiece[1]])

        #vertical
        for c in range(len(self.data[0])):
            
            col_array = []    #create the col_array manually
            for r in range(len(self.data)):
                col_array.append(self.data[r][c])

            for r in range(len(col_array)-n_seq+1):
                window = col_array[r:r+n_seq]

                self.evaluate_window(window,piece= self.data[lastPiece[0]][lastPiece[1]])

               
        #downwards slope
        for r in range(len(self.data)-n_seq+1):
            for c in range(len(self.data[0])-n_seq+1):
                window = [self.data[r+i][c+i] for i in range(n_seq)]
               
                self.evaluate_window(window,piece= self.data[lastPiece[0]][lastPiece[1]])

        #upwards slope
        for r in range(len(self.data)-1,n_seq-2,-1):
            for c in range(len(self.data[0])-n_seq,-1,-1):
                window = [self.data[r-i][c+i] for i in range(n_seq)]
                    
                self.evaluate_window(window,piece= self.data[lastPiece[0]][lastPiece[1]])



                

