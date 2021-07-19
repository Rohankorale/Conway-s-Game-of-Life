import pygame
import numpy as np
import random


class Grid :
    def __init__(self,width,height,scale,offset):
        self.scale = scale
        self.columns = int(height/scale)
        self.rows = int(width/scale)
        self.size = (self.rows,self.columns)
        self.grid_array = np.ndarray(shape=(self.size))
        self.offset = offset


    # Creating the 2D Grid
    def random_2d_array(self):
        for x in range(self.rows) :
            for y in range(self.columns) :
                self.grid_array[x][y] = random.randint(0,1)


    # Setting up the rules and calculating the next generation
    def Conway(self,on_color, off_color, surface):
        for x in range(self.rows) :
            for y in range(self.columns) :
                x_pos = x*self.scale
                y_pos = y*self.scale

                if self.grid_array[x][y] == 1 :
                    pygame.draw.rect(surface,on_color,[x_pos,y_pos,self.scale-self.offset,self.scale-self.offset])
                else :
                    pygame.draw.rect(surface, off_color,[x_pos, y_pos, self.scale - self.offset, self.scale - self.offset])

        next = np.ndarray(shape=(self.size))
        for x in range(self.rows) :
            for y in range(self.columns) :
                state = self.grid_array[x][y]
                neighbours = self.get_neighbours(x,y)
                if state == 0 and neighbours == 3 :  # coming alive by reproduction
                    next[x][y] = 1

                elif state == 1 and (neighbours < 2 or neighbours > 3) :  # dying off due to less or over population
                    next[x][y] = 0

                else :
                    next[x][y] = state

        self.grid_array = next


    # Mouse Operations
    def Handle_mouse(self,x,y):
        _x = int(x // self.scale)
        _y = int(y // self.scale)

        # If condition to ensure that the mouse position is not lying out of the game-screen
        if self.grid_array[_x][_y] != None :
            self.grid_array[_x][_y] = 1


    # Calculating total alive neighbours at a given (x,y)
    def get_neighbours(self,x,y):
        total = 0

        for i in range(-1,2) :
            for j in range(-1,2) :
                x_edge = (x+i+self.rows)%self.rows
                y_edge = (y+j+self.columns)%self.columns
                total += self.grid_array[x_edge][y_edge]

        total -= self.grid_array[x][y]
        return total



