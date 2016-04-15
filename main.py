from flood import *
from board import *
import sys
import pygame as pyg

if __name__ == '__main__':
    while True:
        #Specify a board, dimensions and main color
        which_board = int(raw_input("What type of board would you like to generate (choose a number)? \n 1) Single color board \n 2) Single color board with random blocks \n 3) Single color board with square outline on the board \n 4) Striped board \n >>> ").strip('\n'))
        x_dim, y_dim = tuple(int(i) for i in raw_input("What are the dimensions? ").strip('\n').split(' '))
        color = tuple(int(i) for i in raw_input("What is the start color (RGB integers)?: ").strip('\n').split(' ')) #Doesn't work for striped board


        #Set up screen and initial board
        board_options = {
                    1: single_color_board, 
                    2: single_color_board_with_random_blocks,
                    3: single_color_board_with_square_outline,  
                    4: striped_board,
        }
        screen = pyg.display.set_mode((x_dim, y_dim))
        image = board_options[which_board](x_dim, y_dim, color) 
        pyg.surfarray.blit_array(screen, image)
        pyg.display.flip()


        #Event loop for flood recursion
        while True:
            event = pyg.event.wait()
            if event.type == pyg.QUIT or (event.type == pyg.KEYDOWN and event.key == pyg.K_q): 
                #To quit program
                sys.exit()
            elif event.type == pyg.KEYDOWN and event.key == pyg.K_f: 
                #Floods board (unanimated)
                color = tuple(int(i) for i in raw_input('Please specify RGB coordinates: ').strip('\n').split(' '))
                flood_fill(image, (x_dim/2, y_dim/2), color) 
                pyg.surfarray.blit_array(screen, image)
                pyg.display.flip()
            elif event.type == pyg.KEYDOWN and event.key == pyg.K_a: 
                #Section of code that handles an animated flood	
                pass
            elif event.type == pyg.KEYDOWN and event.key == pyg.K_n:
                break                
