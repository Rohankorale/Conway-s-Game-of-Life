import pygame
import os
import grid


os.environ['SDL_VIDEO_CENTERED'] = '1'

# Screen - setup
width,height = 1000,600
size = (width,height)
screen = pygame.display.set_mode(size)

pygame.init()

pygame.display.set_caption("Conway's Game of Life")
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

    # Tracking the events and exit
    for event in pygame.event.get():
        if event.type == pygame.QUIT :
            run = False

        if event.type == pygame.KEYUP :
            if event.type == pygame.K_ESCAPE :
                run = False

            if event.type == pygame.K_SPACE :
                pause = not pause


    Grid.Conway(off_color=white, on_color=blue,surface=screen)

    # For drawing the patterns
    if pygame.mouse.get_pressed()[0] :
        mouse_x, mouse_y = pygame.mouse.get_pos()
        Grid.Handle_mouse(mouse_x,mouse_y)

    pygame.display.update()

pygame.quit()



