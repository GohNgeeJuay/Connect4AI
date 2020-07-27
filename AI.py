from Tree import *


class Connect4AI():
    def __init__(self,board,depth = 3,lastPiece):
    
        self.tree = Tree(board)
        self.depth = 0
        self.lastPiece = lastPiece

        while self.depth < depth:
            

        
        
    def insert(self)    
        #Need to create the graph 
        DIRECTIONS = (
        (-1, -1), (-1, 0), (-1, 1),
        ( 0, -1),          ( 0, 1),
        ( 1, -1), ( 1, 0), ( 1, 1),
        )

        



      




    # #Minimax function reference: https://www.youtube.com/watch?v=l-hh51ncgDI&list=WL&index=32&t=0s
    # def minimax(position, depth, alpha, beta, maximisingPlayer):
    #     if depth = 0 or game over in position:



x = Connect4AI([['x',' ',' ',' ',' ',' ',' '],[' ',' ',' ',' ',' ',' ',' '],[' ',' ',' ',' ',' ',' ',' '],[' ',' ',' ',' ',' ',' ',' '],[' ',' ',' ',' ',' ',' ',' ']
,[' ',' ',' ',' ',' ',' ',' '],[' ',' ',' ',' ',' ',' ',' ']], lastPiece= [0,0])

print(x.tree.root.data)

