from flood import *
from board import *
import sys
import pygame as pyg

if __name__ == '__main__':
    #Specify properties of board
    x_dim, y_dim = tuple(int(i) for i in raw_input("What are the dimensions? ").strip('\n').split(' '))
    color = tuple(int(i) for i in raw_input("What is the start color (RGB integers)?: ").strip('\n').split(' '))

    #Set up screen and initial board
    screen = pyg.display.set_mode((x_dim, y_dim))
    array_img = board(x_dim, y_dim, (255,0,255))
    pyg.surfarray.blit_array(screen, array_img)
    pyg.display.flip()

    #Event loop for flood recursion
    while True:
        event = pyg.event.wait()
        if event.type == pyg.QUIT or (event.type == pyg.KEYDOWN and event.key == pyg.K_q): #To quit program
            sys.exit()
        elif event.type == pyg.KEYDOWN and event.key == pyg.K_f: #Floods board
            color = tuple(int(i) for i in raw_input('Please specify RGB coordinates: ').strip('\n').split(' '))
            flood_fill(array_img, (x_dim/2, y_dim/2), color) #Flood starts in the middle
            pyg.surfarray.blit_array(screen, array_img)
            pyg.display.flip()	
							
