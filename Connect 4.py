#Reference:
#https://www3.nd.edu/~pbui/teaching/cdt.30010.fa16/project01.html


from IPython.display import display, HTML, clear_output
import random
import time
import pygame
import sys

class Connect4Board:
    def __init__(self,rows=6, columns=7):
        ''' Creates empty Connect 4 board 
        @param:     rows. Number of rows for the board. Default = 6
        @param:     columns. Number of columns for the board. Default = 7
        @return:    None
        @raises:    None

        '''
        self.board = []
        self.piece_one  = 'x'
        self.piece_two  = 'o'

        for row in range(rows):
            board_row = []
            for column in range(columns):
                board_row.append(' ')
            self.board.append(board_row)

        


    def print_board(self):
        ''' Prints Connect 4 board in nice format '''
        for row in self.board:
            print ("|" + "|" .join(row) + "|")


    def drop_piece(self,column, piece): 
        ''' Attempts to drop specified piece into the board at the
        specified column. If this succeeds, return True. 
        @param      column: The column to insert on
        @param      piece: The piece to be inserted
        @return:    True if piece successfully dropped.
        @raises:    Exception. When the column is fully occupied. 
        '''
    
        try:
            nrows = len(self.board)
            for i in range(nrows-1,-1,-1):
                if self.board[i][column] == ' ':
                    self.board[i][column] = piece
                    return True
            
            raise Exception("Not a valid input for column: " + str(column))         
            #When the column has already been fully occupied
        except IndexError:
            print('Not a valid column. Valid columns: 0 to 6')


    def has_winner(self,n_seq = 4): 
        ''' Returns the position of first winning sequence encountered or False if none encountered in board
        @param      board: The Connect 4 board instance
        @param      n_seq: Number of pieces for winning sequence. Default = 4
        @return:    Position of winning sequence or False if board does not have winning sequence.
        @raises:    None 
        '''
        rows = len(self.board)
        columns = len(self.board[0])
        
        for row in range(rows):
            for col in range(columns):
                if (self.board[row][col] == self.piece_one) or (self.board[row][col] == self.piece_two):
                    
                    return self.check_piece(row,col, n_seq)
        
        

    def check_piece(self,row,column,n_seq = 4):
        ''' Check whether there is a winning sequence of 4 pieces at position (row,column) in board
        @param      row: index of row in the board
        @param      column: index of column in the board
        @param      n_seq: Number of pieces for winning sequence. Default = 4
        @return:    (row,column) parameters if it is part of a 4 sequence or False otherwise
        @raises:    None 
        '''

        DIRECTIONS = (
        (-1, -1), (-1, 0), (-1, 1),
        ( 0, -1),          ( 0, 1),
        ( 1, -1), ( 1, 0), ( 1, 1),
        )
        
        for dr, dc in DIRECTIONS:
            found_winner = True
            
            for i in range(1,n_seq):
                r = row + dr*i
                c = column + dc*i
            
                
                if r not in range(0,len(self.board)) or c not in range(0,len(self.board[0])):    #check if within boundary of board. If not stop checking that direction and move on to next direction.
                    found_winner = False
                    break
                 
                else:    
                    #print(self.board[r][c])    #for checking
                    #print(self.board[row][column])
                    if self.board[r][c] != self.board[row][column]:    #check if the current checked cell has same cell as original point
                        found_winner = False
                        break
                
            
            if found_winner == True:
                return (row,column)
        
        return False


    def get_winner(self,row,column):
        ''' Returns the winner (player1 or player2) who forms a 4 squence at position row,column in board
        @param      row: index of row in the board
        @param      column: index of column in the board
        @return:    String: "Player 1" or "Player 2"
        @raises:    Exception: if the position is empty. Used only for cases where called outside game loop. 
        '''
        try:
            if self.board[row][column] == "x":
                return "Player 1"
            elif self.board[row][column] == "o":
                return "Player 1"
            else:
                raise Exception("Position at " + str(row) + "," + str(column) + " is empty." )

        except IndexError:
            print("get_winner called with wrong winning position")


    
    def previous_row(self,column):
        ''' Returns the index of the row which is the highest (last played/last inserted) in a particular column
        @param      column: index of column in the board
        @return:    int: index of row. If column has no pieces return False
        @raises:    Exception: if column outside of boundary of board
        '''
        if abs(column) >= len(self.board[0]):
            raise Exception("Column does not exist in the board. Must be between 0 and " + str(len(self.board[0]-1)))
        
        nrows = len(self.board)
        for i in range(0,nrows,1):
            if self.board[i][column] == self.piece_one or self.board[i][column] == self.piece_two:
                return i
        return False

    def draw_board(self):
        pass



# def display_html(s):
#     ''' Display string as HTML '''
#     display(HTML(s))

# def create_board_svg(board, radius):
#     ''' Return SVG string containing graphical representation of board '''

#     rows     = len(board)
#     columns  = len(board[0])
#     diameter = 2*radius

#     svg  = '<svg height="{}" width="{}">'.format(rows*diameter, columns*diameter)
#     svg += '<rect width="100%" height="100%" fill="blue"/>'

#     for row in range(rows):
#         for column in range(columns):
#             piece = board[row][column]
#             color = PIECE_COLOR_MAP[piece]
#             cx    = column*diameter + radius
#             cy    = row*diameter + radius
#             svg += '<circle cx="{}" cy="{}" r="{}" fill="{}"/>'.format(cx, cy, radius*.75, color)

#     svg += '</svg>'

#     return svg




def main():
    board = Connect4Board()
    game_over = False
    turn = 0
    
    #reference for GUI: https://www.youtube.com/watch?v=SDz3P_Ctm7U&t=7s
    pygame.init()    #create the window by specifying dimensions
    SQUARESIZE = 100
    COLUMN_COUNT = 7
    ROW_COUNT = 6
    
    width = COLUMN_COUNT * SQUARESIZE
    height = (ROW_COUNT+1) * SQUARESIZE
    size = (width,height)
    screen = pygame.display.set_mode(size)


    #game loop
    board.print_board()
    while not game_over:
    
        for event in pygame.event.get():    #allow to quit by clicking exit button
            if event.type == pygame.QUIT:
                sys.exit()


        #Player 1 input
        if turn == 0:
            userInput = input("Which column selected?: ")
            
            try:
                board.drop_piece(int(userInput),board.piece_one)
                board.print_board()
                #check_winner = board.has_winner()    #Might change this to check only the last inserted location instead of all the positions in board
                
                prevRow = board.previous_row(int(userInput))
                check_winner = board.check_piece(prevRow,int(userInput))
                
                if check_winner != False: #if current turn results in winning state, end. else continue
                    game_over = True
                    
                    # #Get the winner at position check_winner[0],check_winner[1]
                    # player_winner = board.get_winner(check_winner[0],check_winner[1])
                
                    # print("Game Over. The winner is: " + player_winner)
                    
                    #Leave it as player1, since anyway player2 makes a winning move this round, otherwise would have detected player1 before or earlier
                    print("Game Over. The winner is: Player 1")
                    
                else:
                    turn = 1

            except IndexError:
                print("Try Again")
                board.print_board()
                continue

            except Exception:    #If didn't insert correctly
                print("Try Again")
                board.print_board()
                continue

            
        #Player 2 input
        elif turn == 1:
            userInput = input("Which column selected?: ")
            try:
                board.drop_piece(int(userInput),board.piece_two)
                board.print_board()

                #check_winner = board.has_winner()    #Might change this to check only the last inserted location instead of all the positions in board

                prevRow = board.previous_row(int(userInput))
                check_winner = board.check_piece(prevRow,int(userInput))

                if check_winner != False: #if current turn results in winning state, end. else continue
                    game_over = True
                    #Get the winner at position check_winner[0],check_winner[1]
                    #player_winner = board.get_winner(check_winner[0],check_winner[1])

                    #print("Game Over. The winner is: " + player_winner)    
                    #Leave it as player2, since anyway player2 makes a winning move this round, otherwise would have detected player1 before or earlier
                    print("Game Over. The winner is: Player 2")

                else:
                    turn = 0
            
            except IndexError:
                print("Try Again")
                board.print_board()
                continue

            except Exception:    #If didn't insert correctly
                print("Try Again")
                board.print_board()
                continue

            


if __name__ == '__main__':
    main()
        
        
# board = Connect4Board()
# print(board.board)
# board.drop_piece(1,board.piece_one)
# print(board.board)
# print(board.board[0][1] == board.piece_one)
# print(type(board.piece_one))
# print(board.piece_one)
# print(board.board[5][1])

        

    



        