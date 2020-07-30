import copy

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


        for i in range(len(self.tree.root.child)):    #Second round growing for Human Player
            self.grow_width(self.tree.root.child[i], Connect4Object.piece_one)

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
        

        Variables: self.tree: Contains the tree structure of the possible decisions to make.
        @param:     Connect4Object
        @return:    None
        @raises:    None

        '''

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
                currentNode.add_child(Node(copyBoard))    #create a new node for the child with new board as data

                #check if this newly added step produces a winning condition. Change the attribute isLeaf
                DIRECTIONS = (
                (-1, -1), (-1, 0), (-1, 1),
                ( 0, -1),          ( 0, 1),
                ( 1, -1), ( 1, 0), ( 1, 1),
                )
        
                newChildIndex = currentNode.get_previous_added_child()
                newChildBoard = currentNode.child[newChildIndex].data

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
                
                if found_winner == True:
                    currentNode.child[newChildIndex].isLeaf = True

                #give a score to the board
                currentNode.scoring((r,c))    #Pass in the recently added position into the function for evaluation
                
    




# #Minimax function reference: https://www.youtube.com/watch?v=l-hh51ncgDI&list=WL&index=32&t=0s    
# Need to implement in a new function. 
# Come up with the heuristics function first, then general min max function.
# Have not utilise the depth in __init__. Only goes through max depth = 3. Have to add some proper function calls based on depth argument

board = Connect4Board()

board.drop_piece(0,'x')
board.drop_piece(1,'o')
board.drop_piece(2,'x')
board.drop_piece(1,'o')
board.drop_piece(0,'x')
board.drop_piece(1,'o')
board.drop_piece(2,'x')


x = Connect4AI(board)

