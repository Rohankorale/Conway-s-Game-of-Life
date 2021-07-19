import pygame
import os
import grid


# The OS module in Python provides functions for interacting with the operating system.
# Like getting to CWD, changing/creating directory

os.environ['SDL_VIDEO_CENTERED'] = '1'

# environ object returns dictionary of environment variables

#An environment variable is a dynamic-named value that can affect the way running processes will behave on a computer.
#They are part of the environment in which a process runs.
# #For example, a running process can query the value of the TEMP environment variable
# to discover a suitable location to store temporary files, or the HOME or
#USERPROFILE variable to find the directory structure owned by the user running the process.

width,height = 1000,600
size = (width,height)

pygame.init()

pygame.display.set_caption("Conway's Game of Life")
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
fps = 60

black = (0,0,0)
blue = (0,14,21)
white = (255,255,255)

scaler = 10
offset = 1

Grid = grid.Grid(width,height,scaler,offset)
Grid.random_2d_array()

run = True
pause = False
while run :
    clock.tick(fps)
    screen.fill(black)

    for event in pygame.event.get():
        if event.type == pygame.QUIT :
            run = False

        if event.type == pygame.KEYUP :
            if event.type == pygame.K_ESCAPE :
                run = False

            if event.type == pygame.K_SPACE :
                pause = not pause


    Grid.Conway(off_color=white, on_color=blue,surface=screen)

    if pygame.mouse.get_pressed()[0] :
        mouse_x, mouse_y = pygame.mouse.get_pos()
        Grid.Handle_mouse(mouse_x,mouse_y)

    pygame.display.update()

pygame.quit()



