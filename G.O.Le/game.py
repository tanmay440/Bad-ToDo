import pygame
import time
import random
import numpy as np
import os

class Grid:
    def __init__(self, width, height, scale, offset, win, winstate):
        self.scale = scale
        self.win = win
        self.columns = int(height/scale)
        self.rows = int(width/scale)

        self.size = (self.rows, self.columns)
        self.grid_array = np.ndarray(shape=(self.size))
        self.offset = offset
        self.enemies = winstate
        self.winstate = [[21, 8]]


    def random2d_array(self):
        for x in range(self.rows):
            for y in range(self.columns):
                self.grid_array[x][y] = 0
        for x in self.enemies:
            for i , j in x:
                self.grid_array[i][j] = 1
            

    def Conway(self, off_color, on_color, surface, pause, randcol, overdrive):
        
        
        for x in range(self.rows):
            for y in range(self.columns):
                y_pos = y * self.scale
                x_pos = x * self.scale
                random_color = (random.randint(10, 255), random.randint(10, 255), random.randint(10, 255))
                if self.grid_array[x][y] == 1:
                    if randcol:
                        pygame.draw.rect(surface, random_color, [x_pos, y_pos, self.scale-self.offset, self.scale-self.offset])
                    else:
                        if [x, y] == self.winstate[0]:
                            self.win.blit(pygame.image.load("G.O.L.e/win_sprite_active.png"), [x_pos, y_pos, self.scale-self.offset, self.scale-self.offset])
                        else:
                            self.win.blit(pygame.image.load("G.O.L.e/cell_alive.png"), [x_pos, y_pos, self.scale-self.offset, self.scale-self.offset])
                elif overdrive == 0:
                    if [x, y] == self.winstate[0]:
                        self.win.blit(pygame.image.load("G.O.L.e/win_sprite_unactive.png"), [x_pos, y_pos, self.scale-self.offset, self.scale-self.offset])
                    else:
                        pygame.draw.rect(surface, off_color, [x_pos, y_pos, self.scale-self.offset, self.scale-self.offset])
                else:
                    self.win.blit(pygame.image.load("G.O.L.e/cell_dead.png"), [x_pos, y_pos, self.scale-self.offset, self.scale-self.offset])
        next = np.ndarray(shape=(self.size))
        if pause == False:
            for x in range(self.rows):
                for y in range(self.columns):
                    state = self.grid_array[x][y]
                    neighbours = self.get_neighbours( x, y)
                    if state == 0 and neighbours == 3:
                        next[x][y] = 1
                    elif state == 1 and (neighbours < 2 or neighbours > 3):
                        next[x][y] = 0
                    else:
                        next[x][y] = state
            self.grid_array = next
            
    def HandleMouse(self, x, y, right = False):
        _x = x//self.scale
        _y = y//self.scale

        if self.grid_array[_x][_y] != None and right == False:
            self.grid_array[_x][_y] = 1
            

    def get_neighbours(self, x, y):
        total = 0
        for n in range(-1, 2):
            for m in range(-1, 2):
                x_edge = (x+n+self.rows) % self.rows
                y_edge = (y+m+self.columns) % self.columns
                total += self.grid_array[x_edge][y_edge]

        total -= self.grid_array[x][y]
        return total
    def has_won(self):
        for x , y in self.winstate:
            if self.grid_array[x][y] == 1:
                return True
        return False
#===============imports===================
#===============setup======================
os.environ["SDL_VIDEO_CENTERED"]='1'
width, height = 1920,1080
size = (width, height)
stage = [[[[19, 4], [19, 5], [20, 5], [20, 4], [10, 8], [10, 8], [10, 9], [11, 10], [12, 10], [13, 9], [13, 9], [13, 8], [12, 7], [11, 7], [21, 11], [21, 12], [22, 12], [23, 11], [23, 10], [22, 10], [5, 3], [6, 2], [7, 2], [8, 3], [7, 4], [6, 4]]], [[(19, 7), (19, 7), (19, 7), (19, 7), (19, 8), (19, 8), (19, 8), (18, 9), (18, 9), (18, 9), (18, 9), (17, 9), (17, 9), (17, 9), (16, 8), (16, 8), (16, 8), (16, 7), (16, 7), (18, 6), (18, 6), (18, 6), (18, 6), (18, 6), (17, 6), (17, 6), (17, 6), (17, 6), (17, 6), (15, 6), (15, 6), (15, 6), (14, 6), (14, 6), (14, 6), (14, 6), (13, 7), (13, 7), (13, 7), (13, 7), (13, 8), (13, 8), (14, 9), (14, 9), (14, 9), (14, 9), (15, 9), (12, 9), (12, 9), (12, 9), (12, 9), (11, 9), (11, 9), (11, 9), (11, 9), (10, 8), (10, 8), (10, 8), (10, 8), (10, 7), (10, 7), (10, 7), (12, 6), (12, 6), (12, 6), (12, 6), (11, 6), (11, 6), (11, 6), (13, 5), (13, 5), (13, 5), (13, 4), (13, 4), (13, 4), (13, 4), (13, 4), (14, 3), (14, 3), (14, 3), (14, 3), (14, 3), (15, 3), (15, 3), (15, 3), (15, 3), (15, 3), (16, 4), (16, 4), (16, 4), (16, 5), (16, 5), (16, 5), (16, 5), (16, 5), (13, 10), (13, 10), (13, 10), (13, 10), (13, 10), (13, 11), (13, 11), (13, 11), (13, 11), (14, 12), (14, 12), (14, 12), (14, 12), (15, 12), (15, 12), (15, 12), (15, 12), (16, 11), (16, 11), (16, 11), (16, 11), (16, 10), (16, 10), (16, 10), (16, 10)]],[[(10, 8), (10, 8), (11, 7), (12, 8), (11, 9), (11, 9), (20, 8), (20, 8), (20, 8), (21, 7), (22, 8), (22, 8), (21, 9), (15, 3), (15, 3), (14, 4), (14, 4), (14, 4), (15, 5), (15, 5), (16, 4), (16, 4), (5, 12), (5, 12), (5, 12), (6, 13), (7, 12), (6, 11), (21, 2), (20, 3), (21, 4), (22, 3), (22, 3), (16, 10), (16, 10), (16, 10), (15, 11), (16, 12), (16, 12), (17, 11), (21, 12), (21, 12), (21, 12), (21, 12), (22, 13), (22, 13), (22, 13), (23, 12), (22, 11), (22, 11), (22, 11), (5, 4), (6, 5), (7, 4), (7, 4), (6, 3)]], [[(19, 6), (19, 6), (19, 6), (19, 6), (19, 6), (19, 7), (19, 7), (19, 7), (18, 7), (18, 7), (18, 6), (18, 6), (22, 6), (22, 6), (22, 6), (22, 6), (22, 6), (22, 7), (22, 7), (22, 7), (23, 7), (23, 7), (23, 7), (23, 6), (23, 6), (23, 6), (19, 10), (18, 11), (18, 11), (19, 11), (18, 10), (18, 10), (18, 10), (22, 10), (22, 10), (22, 10), (22, 10), (22, 10), (22, 11), (22, 11), (22, 11), (23, 11), (23, 11), (23, 10), (23, 10), (23, 10), (17, 8), (17, 8), (16, 8), (16, 8), (16, 8), (16, 8), (16, 8), (16, 9), (16, 9), (16, 9), (17, 9), (20, 12), (20, 12), (20, 12), (20, 12), (20, 13), (20, 13), (21, 13), (21, 13), (21, 13), (21, 13), (21, 12), (21, 12), (21, 12), (24, 9), (24, 9), (24, 9), (24, 9), (25, 9), (25, 9), (25, 9), (25, 9), (25, 8), (25, 8), (24, 8), (21, 5), (21, 5), (21, 5), (20, 5), (20, 5), (20, 5), (20, 4), (20, 4), (20, 4), (20, 4), (21, 4), (21, 4), (21, 4)]], [[(19, 7), (19, 7), (19, 8), (19, 8), (20, 9), (20, 9), (21, 9), (22, 8), (22, 7), (21, 6), (21, 6), (20, 6), (23, 6), (23, 6), (24, 6), (25, 7), (25, 8), (25, 8), (24, 9), (24, 9), (23, 9), (23, 9), (22, 10), (22, 10), (22, 11), (22, 11), (21, 12), (21, 12), (20, 12), (20, 12), (19, 11), (19, 11), (19, 10), (19, 10), (19, 5), (19, 5), (19, 5), (19, 4), (19, 4), (19, 4), (19, 4), (20, 3), (21, 3), (21, 3), (21, 3), (21, 3), (22, 4), (22, 4), (22, 5), (22, 5), (18, 6), (18, 6), (17, 6), (17, 6), (17, 6), (16, 7), (16, 7), (16, 7), (16, 7), (16, 8), (16, 8), (16, 8), (16, 8), (17, 9), (17, 9), (17, 9), (17, 9), (18, 9), (18, 9), (18, 9), (18, 9), (18, 9), (8, 6), (8, 6), (8, 6), (8, 6), (8, 6), (8, 7), (8, 7), (8, 7), (9, 7), (9, 7), (9, 7), (9, 7), (9, 7), (9, 6), (9, 6), (9, 6), (8, 10), (8, 10), (8, 10), (8, 10), (8, 11), (8, 11), (8, 11), (8, 11), (9, 11), (9, 11), (9, 11), (9, 11), (9, 10), (9, 10), (9, 10), (9, 10), (10, 12), (10, 12), (10, 12), (10, 13), (10, 13), (10, 13), (10, 13), (11, 13), (11, 13), (11, 13), (11, 13), (11, 12), (11, 12), (11, 12), (10, 5), (10, 5), (10, 5), (10, 4), (10, 4), (10, 4), (11, 4), (11, 4), (11, 4), (11, 5), (11, 5), (11, 5)]], [[(21, 7), (20, 8), (20, 8), (20, 8), (20, 8), (21, 9), (21, 9), (21, 9), (22, 8), (22, 8), (22, 8), (18, 5), (18, 5), (18, 5), (18, 5), (18, 5), (18, 6), (18, 6), (18, 6), (18, 6), (18, 6), (19, 6), (19, 6), (19, 6), (19, 6), (19, 5), (19, 5), (18, 10), (18, 10), (18, 10), (18, 10), (18, 11), (18, 11), (19, 11), (19, 11), (19, 11), (19, 11), (19, 11), (19, 10), (19, 10), (19, 10), (19, 10), (16, 7), (16, 7), (16, 7), (15, 8), (15, 8), (15, 8), (16, 9), (16, 9), (16, 9), (17, 8), (17, 8), (17, 8), (17, 8), (23, 5), (23, 5), (23, 5), (23, 6), (23, 6), (23, 6), (23, 6), (24, 6), (24, 6), (24, 6), (24, 6), (24, 6), (24, 5), (24, 5), (24, 5), (23, 10), (23, 10), (23, 10), (23, 10), (23, 10), (23, 11), (23, 11), (23, 11), (23, 11), (24, 11), (24, 11), (24, 11), (24, 11), (24, 11), (24, 11), (24, 10), (24, 10), (24, 10), (24, 10)]], [[(6, 3), (6, 3), (6, 3), (6, 2), (7, 2), (8, 2), (7, 4), (7, 4), (7, 4), (7, 4), (12, 3), (12, 3), (12, 2), (12, 2), (13, 2), (13, 2), (13, 2), (13, 2), (14, 2), (14, 2), (14, 2), (13, 4), (13, 4), (13, 4), (18, 3), (18, 3), (18, 2), (18, 2), (19, 2), (19, 2), (19, 2), (20, 2), (20, 2), (20, 2), (19, 4), (19, 4), (19, 4), (10, 10), (10, 10), (10, 9), (10, 9), (10, 9), (11, 9), (12, 9), (11, 11), (11, 11)]]]
level = 0
pygame.init()
pygame.display.set_caption("CONWAY'S GAME OF LIFE")
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
fps = 60
mode = {"play":True, "pause":False, "start":False}
black = (255, 255, 255)
blue = (0, 0, 0)
blue1 = (255,255,255)
white = (255, 255, 255)
overdrive = False
scaler = 65
offset = 1
win = False
grid = Grid(width,height, scaler, offset, screen, stage[level])
grid.random2d_array()

pause = True
run = True
randcol = False
'''
screen.blit(pygame.image.load("sprite_0.png"), [0, 0, 960, 540])
pygame.display.update()
time.sleep(10)
'''
#===============main loop============
while run:
    if mode["play"]:
        clock.tick(fps)
        screen.fill(black)
        if grid.has_won():
            if not win: 
                pause = True
                level += 1
                if level == len(stage):
                    win = True
                
                
            grid = Grid(width,height, scaler, offset, screen, stage[level])
            grid.random2d_array()


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    run = False
                elif event.key == pygame.K_SPACE:
                    pause = not pause
                elif event.key == pygame.K_c:
                    grid.random2d_array()
                    pause = True
                elif event.key == pygame.K_r:
                    randcol  = not randcol
                elif event.key == pygame.K_o:
                    overdrive = not overdrive
        grid.Conway(off_color=blue, on_color=white, surface=screen, pause=pause, randcol = randcol, overdrive = overdrive)

        if pygame.mouse.get_pressed()[0]:
            mouseX, mouseY = pygame.mouse.get_pos()
            grid.HandleMouse(mouseX, mouseY)
        elif pygame.mouse.get_pressed()[2]:
            mouseX, mouseY = pygame.mouse.get_pos()
            grid.HandleMouse(mouseX, mouseY, True)
        if win == True:
            font = pygame.font.SysFont(None, 24)
            img = font.render('You Win', True, (255, 255, 255))
            screen.blit(img, (715, 195))
        

        pygame.display.update()

pygame.quit()
