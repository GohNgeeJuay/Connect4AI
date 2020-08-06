import copy

import random
from Connect4 import *
from Tree import *


class Connect4AI():
    def __init__(self,Connect4Object):
        ''' Creates a Connect4AI instance. Will initialize a tree of depth 3. Might introduce a better form of growing the tree. 
        Variables: self.tree: Contains the tree structure of the possible decisions to make.
        @param:     Connect4Object
        @return:    None
        @raises:    None

        '''
        self.tree = Tree(Connect4Object.board)     #Put the array representation of board into the tree instead of the Connect4 object
        self.grow_width(self.tree.root, Connect4Object.piece_two)       #grow the tree
        #Temporarily. Choose from the next best 7 positions
        

        for i in range(len(self.tree.root.child)):    #Second round growing for Human Player
            self.grow_width(self.tree.root.child[i], Connect4Object.piece_one)

            if self.tree.root.child[i] == None:
                print("No Child")
                continue
            
            #Third round growing for AI
            for j in range(len(self.tree.root.child[i].child)):
                if self.tree.root.child[i].child[j] != None:    #if there is a child, then grow
                    self.grow_width(self.tree.root.child[i].child[j],Connect4Object.piece_two)
                    break
       
        
        
    def grow_width(self, currentNode, piece, n_seq = 4):    
        ''' Grows the tree sideways (ie the 7 new possible new states for the board for the currentNode as children). 
        If the currentNode is a leaf, will not grow the tree. 
        1) Looks at the next possible row for each column to insert a new piece. 
        2) Create a copy of the currentNode board and add the new piece. New board will become data for new node
        3) Check if the new node is a leaf(terminal node) based on winning condition, if True, change the attribute isLeaf for that node
        4) Give a score to the new node
        
        @param:     currentNode. current node for which its children will be expanded upon.
        @param:     piece. Piece to be added in the board
        @param:     n_seq. The winning condition for connect sequence. Default = 4.
        @return:    None
        @raises:    None

        '''

        if currentNode is None:
            return
            
        if currentNode.isLeaf == True:    #if node is a terminal node, do not grow it further
            return
                 
        #insert into individual columns at each iteration
        for c in range(0,len(currentNode.data[0]),1):

            r = 0    #Get the previous row used.
            while r < len(currentNode.data):
                if currentNode.data[r][c] == 'x' or currentNode.data[r][c] == 'o':
                    break
                else:
                    r += 1
            r -= 1     #Use the next row available


            if r < 0:   #If the columns already fully occupied, move on to next possible column
                continue
            
            
                                    
            else:
                
                copyBoard = copy.deepcopy(currentNode.data) #create copy of the board
                copyBoard[r][c] = piece  #add the new piece for AI
                
                currentNode.add_child(Node(copyBoard),c)
                #currentNode.add_child(Node(copyBoard))    #create a new node for the child with new board as data

                #check if this newly added step produces a winning condition. Change the attribute isLeaf
                DIRECTIONS = (
                (-1, -1), (-1, 0), (-1, 1),
                ( 0, -1),          ( 0, 1),
                ( 1, -1), ( 1, 0), ( 1, 1),
                )
        
                c = c
                newChildBoard = currentNode.child[c].data

                #If there is no possible moves, the node is a leaf
                #check the topmost row if there are any empty spots left
                boardIsFull = False
                for i in range(len(newChildBoard)):
                    if newChildBoard[0][i] == ' ':
                        boardIsFull = True
                currentNode.child[c].isLeaf = boardIsFull

                for dr, dc in DIRECTIONS:
                    found_winner = True
                    
                    for i in range(1,n_seq):
                        checkR = r + dr*i
                        checkC = c + dc*i
                    
                        
                        if checkR not in range(0,len(newChildBoard)) or checkC not in range(0,len(newChildBoard[0])):    #check if within boundary of board. If not stop checking that direction and move on to next direction.
                            found_winner = False
                            break
                        
                        else:    
                            
                            if newChildBoard[checkR][checkC] != newChildBoard[r][c]:    #check if the current checked cell has same cell as original point
                                found_winner = False
                                break
                        
                    
                    if found_winner == True:
                        break
                
                if found_winner == True or boardIsFull == True:
                    currentNode.child[c].isLeaf = True

                

                #give a score to the board
                currentNode.child[c].scoring((r,c))    #Pass in the recently added position into the function for evaluation
                
    
    #Temporarily. Choose from the next best 7 positions
    def pick_best_move(self):
        
        #initialize best_col to a random column
        best_col = random.randint(0,6)
        while self.tree.root.child[best_col] == None:
            best_col = random.randint(0,6)    #Make sure the random chosen column valid

        best_score = -10000000
        for child in range(len(self.tree.root.child)):

            if self.tree.root.child[child] == None:
                continue

            if self.tree.root.child[child].value > best_score:
                best_col = child
                best_score = self.tree.root.child[child].value
        
        return best_col

    def minimax(self, currentNode, depth, maximisingPlayer):
        if depth == 0 or currentNode.isLeaf:
            return (None,currentNode.value)
        
        if maximisingPlayer == True:
            value = -math.inf
            
            #initialize best_col to a random column
            best_col = random.randint(0,6)
            while currentNode.child[best_col] == None:
                best_col = random.randint(0,6)    #Make sure the random chosen column valid

            #iterate through child to find max value
            for i in range(len(currentNode.child)):
                if currentNode.child[i] == None:    #If there is no child for that index
                    continue
                else:    #if there is child
                    newVal = self.minimax(currentNode.child[i], depth-1, False)[1]
                    if  newVal > value:
                        value = newVal
                        bestCol = i
            return (bestCol, value)

        if maximisingPlayer == False:
            value = math.inf
            
            #initialize best_col to a random column
            best_col = random.randint(0,6)
            while currentNode.child[best_col] == None:
                best_col = random.randint(0,6)    #Make sure the random chosen column valid

            #iterate through child to find min value
            for i in range(len(currentNode.child)):
                if currentNode.child[i] == None:    #If there is no child for that index
                    continue
                else:    #if there is child
                    newVal = self.minimax(currentNode.child[i], depth-1, True)[1]
                    if newVal < value:
                        value = newVal
                        bestCol = i
            return (bestCol, value)
        
        

                     




# #Minimax function reference: https://www.youtube.com/watch?v=l-hh51ncgDI&list=WL&index=32&t=0s    
# Need to implement in a new function. 
# Come up with the heuristics function first, then general min max function.
# Have not utilise the depth in __init__. Only goes through max depth = 3. Have to add some proper function calls based on depth argument


