#Reference:
#https://www3.nd.edu/~pbui/teaching/cdt.30010.fa16/project01.html


import time
import pygame
import sys
import math
from AI import *


class Connect4Board:
    def __init__(self,rows=6, columns=7):
        ''' Creates empty Connect 4 board 
        @param:     rows. Number of rows for the board. Default = 6
        @param:     columns. Number of columns for the board. Default = 7
        @return:    None
        @raises:    None

        '''
        self.board = []
        self.nrows = rows
        self.ncolumns = columns
        self.piece_one  = 'x'
        self.piece_two  = 'o'

        self.SQUARESIZE = 100    #parameters for the board
        self.COLUMN_COUNT = self.ncolumns
        self.ROW_COUNT = self.nrows
        self.width = self.COLUMN_COUNT * self.SQUARESIZE
        self.height = (self.ROW_COUNT+1) * self.SQUARESIZE
        self.size = (self.width,self.height)
        self.screen = pygame.display.set_mode(self.size)

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
            for i in range(self.nrows-1,-1,-1):
                if self.board[i][column] == ' ':
                    self.board[i][column] = piece
                    return True
            
            raise Exception("Not a valid input for column: " + str(column))         
            #When the column has already been fully occupied
        except IndexError:
            print('Not a valid column. Valid columns: 0 to ' + str(self.ncolumns-1))


    def has_winner(self,piece, n_seq = 4,): 
        ''' Returns the position of first winning sequence encountered or False if none encountered in board
        @param      board: The Connect 4 board instance
        @param      n_seq: Number of pieces for winning sequence. Default = 4
        @return:    Position of winning sequence or False if board does not have winning sequence.
        @raises:    None 
        '''
        found = False
        for row in range(self.nrows):
            for col in range(self.ncolumns):
                if self.board[row][col] == piece:
                    
                    retVal = self.check_piece(row,col,n_seq)
                    if retVal != False:
                        return True
        return found
        
        

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
            
                
                if r not in range(0,self.nrows) or c not in range(0,self.ncolumns):    #check if within boundary of board. If not stop checking that direction and move on to next direction.
                    found_winner = False
                    break
                 
                else:    
                    
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
                return "Player 2"
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
        if abs(column) >= self.ncolumns:
            raise Exception("Column does not exist in the board. Must be between 0 and " + str(self.ncolumns-1))
        
        
        for i in range(0,self.nrows,1):
            if self.board[i][column] == self.piece_one or self.board[i][column] == self.piece_two:
                return i
        return False
        

    def draw_board(self):
        ''' Create a user interface of the connect 4 board
        @param      None
        @return:    None
        @raises:    None
        '''
        for c in range(self.ncolumns):
            for r in range(self.nrows):
                pygame.draw.rect(self.screen, (0,0,255), (c*self.SQUARESIZE, r*self.SQUARESIZE + self.SQUARESIZE, self.SQUARESIZE, self.SQUARESIZE))    #draw rectangle

                if self.board[r][c] == ' ':    #if position does not have any input, draw black circle
                    pygame.draw.circle(self.screen,  (0,0,0), (int(c*self.SQUARESIZE + self.SQUARESIZE/2), int(r*self.SQUARESIZE + self.SQUARESIZE + self.SQUARESIZE/2)), int(self.SQUARESIZE/2 - 5))
                elif self.board[r][c] == self.piece_one:    #if contains player 1 input, draw red circle
                    pygame.draw.circle(self.screen,  (255,0,0), (int(c*self.SQUARESIZE + self.SQUARESIZE/2), int(r*self.SQUARESIZE + self.SQUARESIZE + self.SQUARESIZE/2)), int(self.SQUARESIZE/2 - 5))
                else:    #if contains player 2 input, draw yellow circle
                    pygame.draw.circle(self.screen,  (255,255,0), (int(c*self.SQUARESIZE + self.SQUARESIZE/2), int(r*self.SQUARESIZE + self.SQUARESIZE + self.SQUARESIZE/2)), int(self.SQUARESIZE/2 - 5))
        pygame.display.update() #update to show changes



def main():
    board = Connect4Board(6,7)
    game_over = False
    turn = 0
    
    #reference for GUI: https://www.youtube.com/watch?v=SDz3P_Ctm7U&t=7s
    pygame.init()            
    board.draw_board()    #draw the empty board based on the instance dimension
    pygame.display.update()    #update based on draw_board function

    myfont = pygame.font.SysFont("monospace", 75)
    #game loop
    board.print_board()

    while not game_over:
    
        for event in pygame.event.get():    #allow to quit by clicking exit button
            if event.type == pygame.QUIT:    
                sys.exit()
            
            if event.type == pygame.MOUSEMOTION:    #add animation of moving the piece
                pygame.draw.rect(board.screen, (0,0,0) , (0,0, board.width,board.SQUARESIZE))    #draw black rectangle to remove overlapping circles
                posx = event.pos[0]
                if turn == 0: #player 1 turn, draw red circle
                    pygame.draw.circle(board.screen, (255,0,0), (posx, int(board.SQUARESIZE/2 )),int(board.SQUARESIZE/2 - 5))
                else: #player 2 turn, draw red circle
                    pygame.draw.circle(board.screen, (255,255,0), (posx, int(board.SQUARESIZE/2 )),int(board.SQUARESIZE/2 - 5))
            pygame.display.update()


            if event.type == pygame.MOUSEBUTTONDOWN:    #event where mouse clicked
                pygame.draw.rect(board.screen, (0,0,0) , (0,0, board.width,board.SQUARESIZE))    #draw black rectangle to remove overlapping circles
                #print(event.pos)
                # #Player 1 input
                if turn == 0:
                    posx = event.pos[0]    #access the x position of tuple
                    userInput = int(math.floor(posx/board.SQUARESIZE))    #first column = 0 to 100, sec col = 100 to 200, etc. 
                    #userInput = input("Which column selected?: ")
                    
                    try:
                        board.drop_piece(int(userInput),board.piece_one)
                        board.print_board()
                        board.draw_board()
                        #check_winner = board.has_winner()    #Might change this to check only the last inserted location instead of all the positions in board
                        
                        #prevRow = board.previous_row(int(userInput))
                        check_winner = board.has_winner(piece= board.piece_two)      #Need to check all possible locations. Cannot check just starting from the last inserted position
                        #check_winner = board.check_piece(prevRow,int(userInput))
                        
                        if check_winner == True: #if current turn results in winning state, end. else continue
                            game_over = True
                            
                            # #Get the winner at position check_winner[0],check_winner[1]
                            # player_winner = board.get_winner(check_winner[0],check_winner[1])
                        
                            # print("Game Over. The winner is: " + player_winner)
                            
                            #Leave it as player1, since anyway player2 makes a winning move this round, otherwise would have detected player1 before or earlier
                            print("Game Over. The winner is: Player 1")
                            
                            label = myfont.render("Player 1 Wins!",1, (255,0,0))    #show on screen
                            board.screen.blit(label, (40,10))
                            pygame.display.update() #update to show changes
                            pygame.time.wait(3000) #give 3 seconds before automatic close window
                            
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

                    
            #AI input
            if turn == 1:
                               
                #AI input
                boardAI = Connect4AI(board) #Pass in the board to the AI to create the tree. 
                userInput = boardAI.pick_best_move()

                #userInput = int(math.floor(posx/board.SQUARESIZE))    #first column = 0 to 100, sec col = 100 to 200, etc. GUI user input
                #userInput = input("Which column selected?: ")    #Manual input in console
                
                try:
                    board.drop_piece(int(userInput),board.piece_two)
                    board.print_board()
                    board.draw_board()

                    #check_winner = board.has_winner()    #Might change this to check only the last inserted location instead of all the positions in board

                    #prevRow = board.previous_row(int(userInput))
                    check_winner = board.has_winner(piece = board.piece_two)      #Need to check all possible locations. Cannot check just starting from the last inserted position
                    #check_winner = board.check_piece(prevRow,int(userInput))

                    if check_winner == True: #if current turn results in winning state, end. else continue
                        game_over = True
                        #Get the winner at position check_winner[0],check_winner[1]
                        #player_winner = board.get_winner(check_winner[0],check_winner[1])

                        #print("Game Over. The winner is: " + player_winner)    
                        #Leave it as player2, since anyway player2 makes a winning move this round, otherwise would have detected player1 before or earlier
                        print("Game Over. The winner is: Player 2")

                        label = myfont.render("Player 2 Wins!",1, (255,255,0))    #show on screen
                        board.screen.blit(label, (40,10))
                        pygame.display.update() #update to show changes
                        pygame.time.wait(3000) #give 3 seconds before automatic close window

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


    



        