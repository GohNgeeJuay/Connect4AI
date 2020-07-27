from Tree import *
from Connect4 import *
import copy


class Connect4AI():
    def __init__(self,board,lastPiece,depth = 3):
    
        self.board = board
        self.tree = Tree(board)
        self.depth = 3
        self.lastPiece = lastPiece
        
        self.insert(self.tree.root)
        
        # #insert into individual columns
        # for i in range(board.ncolumns):
        #     self.insert(self.tree.root)
        
        
    def grow(self, currentNode, depth = 0,length = 1):    
        
        c = 0    #For column 0
        r = self.board.previous_row(0)    #Get the previous row used. If column empty use index 0 as row
        if r == False:    
            r = 0
                

        
        if r not in range(0,len(currentNode.data)):    #check if within boundary of board. If not stop adding in that column.
            return 
        
        winning_pos = self.board.check_piece(r,0)    #stop if the current 
        if winning_pos != False:    
            return

               
        
        else:
            
            copyBoard = copy.deepcopy(currentNode.data) #create copy of the board
            copyBoard[r][c] = 'o' #add the new piece
            currentNode.add_child(Node(copyBoard))    #create a new node for the child with new board as data

            prevChildIndex = currentNode.get_previous_added_child()    #change the currentNode to child for recursion
            currentNode = currentNode.child[prevChildIndex]

            depth += 1
            if depth >= self.depth:
                return
            else:
                self.grow(currentNode, depth, length + 1)

    # #Minimax function reference: https://www.youtube.com/watch?v=l-hh51ncgDI&list=WL&index=32&t=0s
    # def minimax(position, depth, alpha, beta, maximisingPlayer):
    #     if depth = 0 or game over in position:



board = Connect4Board()
board.drop_piece(0,'o')

x = Connect4AI(board, lastPiece= (0,0))

print(x.tree.root.data)

# x = [['x',' ',' ',' ',' ',' ',' '],[' ',' ',' ',' ',' ',' ',' '],[' ',' ',' ',' ',' ',' ',' '],[' ',' ',' ',' ',' ',' ',' '],[' ',' ',' ',' ',' ',' ',' ']
# ,[' ',' ',' ',' ',' ',' ',' '],[' ',' ',' ',' ',' ',' ',' ']]

# y = copy.deepcopy(x)
# print(y)
# y[0][1] = 'o'
# print(y)