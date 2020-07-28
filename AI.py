import copy

from Connect4 import *
from Tree import *


class Connect4AI():
    def __init__(self,Connect4Object,lastPiece,depth = 3):
    
        self.board = Connect4Object.board    #
        self.tree = Tree(Connect4Object.board)     #Put the array representation of board into the tree instead of the Connect4 object
        self.depth = 3
        self.lastPiece = lastPiece    #last move made by AI
        self.grow_width(self.tree.root, Connect4Object.piece_two)       #grow the tree


        for i in self.tree.root.child:    #Second round growing for Human Player
            self.grow_width(i, Connect4Object.piece_one)
        
        
        
        
    def grow_width(self, currentNode, piece):    
        
                 
        #insert into individual columns
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

                



    #winning_pos = self.board.check_piece(r,0)    #stop if the current 
    # if winning_pos != False:    
    #     return
    #prevChildIndex = currentNode.get_previous_added_child()    #change the currentNode to child for recursion
    #currentNode = currentNode.child[prevChildIndex]

    # depth += 1
    # if depth >= self.depth:
    #     return
    # else:
    #     self.grow(currentNode, depth, length + 1)

    # #Minimax function reference: https://www.youtube.com/watch?v=l-hh51ncgDI&list=WL&index=32&t=0s
    # def minimax(position, depth, alpha, beta, maximisingPlayer):
    #     if depth = 0 or game over in position:

board = Connect4Board()

board.drop_piece(0,'o')
board.drop_piece(0,'x')

x = Connect4AI(board, lastPiece= (4,0))




# x = [['x',' ',' ',' ',' ',' ',' '],[' ',' ',' ',' ',' ',' ',' '],[' ',' ',' ',' ',' ',' ',' '],[' ',' ',' ',' ',' ',' ',' '],[' ',' ',' ',' ',' ',' ',' ']
# ,[' ',' ',' ',' ',' ',' ',' '],[' ',' ',' ',' ',' ',' ',' ']]

# y = copy.deepcopy(x)
# print(y)
# y[0][1] = 'o'
# print(y)
