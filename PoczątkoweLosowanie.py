#Dokonane zmiany widać pomiędzy liniami typu """powyższe x **** PoczątkowegoLosowania""" a """poniższe x **** PoczątkowegoLosowania"""
#kod powinien się uruchamiać, można go skopiować w celu dodania kolejnej funkcjonalności, polecam jednak wtedy pozbawić go klamr tej funkcjonalności i postawić nowe
import random
import pygame
import os
from pygame.locals import *

WIDTH, HEIGHT = 450, 450
WIN = pygame.display.set_mode((WIDTH, HEIGHT))

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
SIZE = (150, 150)

FPS = 60
# BORD = pygame.image.load(os.path.join('Assets', 'outerbox.png'))
# BORD = pygame.transform.scale(BORD, (450, 450))
BORD_2 = pygame.Rect(0, 0, 460, 460)

Kwadrat = pygame.Rect(0, 0, 150, 150)

picture_1 = pygame.transform.scale(pygame.image.load(os.path.join("Assets", "1.png")), (SIZE))
picture_2 = pygame.transform.scale(pygame.image.load(os.path.join("Assets", "2.png")), (SIZE))
picture_3 = pygame.transform.scale(pygame.image.load(os.path.join("Assets", "3.png")), (SIZE))
picture_4 = pygame.transform.scale(pygame.image.load(os.path.join("Assets", "4.png")), (SIZE))
picture_5 = pygame.transform.scale(pygame.image.load(os.path.join("Assets", "5.png")), (SIZE))
picture_6 = pygame.transform.scale(pygame.image.load(os.path.join("Assets", "6.png")), (SIZE))
picture_7 = pygame.transform.scale(pygame.image.load(os.path.join("Assets", "7.png")), (SIZE))
picture_8 = pygame.transform.scale(pygame.image.load(os.path.join("Assets", "8.png")), (SIZE))
picture_0 = pygame.transform.scale(pygame.image.load(os.path.join("Assets", "outerbox.png")), (SIZE))


pictures = [[picture_1, picture_4, picture_7],
            [picture_2, picture_5, picture_8],
            [picture_3, picture_6, picture_0]]


def draw_window():
    WIN.fill(WHITE)
    pygame.draw.rect(WIN, BLACK, BORD_2)
    for x in range(3):
        for y in range(3):
            WIN.blit(pictures[x][y], (x*150, y*150))
    pygame.display.update()


def key_movement(grid, empty_space):
    no_reps = False
    get_key = pygame.key.get_pressed()
    if get_key[pygame.K_UP]:
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == empty_space:
                    if j != 0 and not no_reps:
                        no_reps = True
                        temp = grid[i][j-1]
                        grid[i][j-1] = grid[i][j]
                        grid[i][j] = temp
                        break
    elif get_key[pygame.K_DOWN]:
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == empty_space:
                    if j != len(grid[i])-1 and not no_reps:
                        no_reps = True
                        temp = grid[i][j+1]
                        grid[i][j+1] = grid[i][j]
                        grid[i][j] = temp
                        break
    elif get_key[pygame.K_LEFT]:
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == empty_space:
                    if i != 0 and not no_reps:
                        no_reps = True
                        temp = grid[i-1][j]
                        grid[i-1][j] = grid[i][j]
                        grid[i][j] = temp
                        break
    elif get_key[pygame.K_RIGHT]:
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == empty_space:
                    if i != len(grid)-1 and not no_reps:
                        no_reps = True
                        temp = grid[i+1][j]
                        grid[i+1][j] = grid[i][j]
                        grid[i][j] = temp
                        break

"""Poniższą funkcję dodano na potrzebę PoczątkowegoLosowania"""
def fake_key_movement(grid, empty_space): #fałszywy ruch, polega na tym samym co prawdziwy ale losuje kierunek zamiast pobierać z klawiatury
    no_reps = False
    get_key = random.choice([1,2,3,4])
    if get_key == 1:
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == empty_space:
                    if j != 0 and not no_reps:
                        no_reps = True
                        temp = grid[i][j-1]
                        grid[i][j-1] = grid[i][j]
                        grid[i][j] = temp
                        break
    elif get_key==2:
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == empty_space:
                    if j != len(grid[i])-1 and not no_reps:
                        no_reps = True
                        temp = grid[i][j+1]
                        grid[i][j+1] = grid[i][j]
                        grid[i][j] = temp
                        break
    elif get_key==3:
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == empty_space:
                    if i != 0 and not no_reps:
                        no_reps = True
                        temp = grid[i-1][j]
                        grid[i-1][j] = grid[i][j]
                        grid[i][j] = temp
                        break
    elif get_key==4:
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == empty_space:
                    if i != len(grid)-1 and not no_reps:
                        no_reps = True
                        temp = grid[i+1][j]
                        grid[i+1][j] = grid[i][j]
                        grid[i][j] = temp
                        break
"""Powyższą funkcję dodano na potrzebę PoczątkowegoLosowania"""

def mouse_movement(x, y, grid, empty_space, pict_spread, pict_size, offset_x=0, offset_y=0):
    no_reps = False
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == empty_space:
                if j != 0 and not no_reps:
                    if (offset_x + pict_spread*i < x < offset_x + (pict_spread*i + pict_size) and
                            offset_y + pict_spread*(j - 1) < y < offset_y + (pict_spread*(j -1 ) + pict_size)):
                        no_reps = True
                        temp = grid[i][j - 1]
                        grid[i][j - 1] = grid[i][j]
                        grid[i][j] = temp
                        break
                if j != len(grid[i]) - 1 and not no_reps:
                    if (offset_x + pict_spread * i < x < offset_x + (pict_spread * i + pict_size) and
                            offset_y + pict_spread * (j + 1) < y < offset_y + (pict_spread * (j + 1) + pict_size)):
                        no_reps = True
                        temp = grid[i][j + 1]
                        grid[i][j + 1] = grid[i][j]
                        grid[i][j] = temp
                        break
                if i != 0 and not no_reps:
                    if (offset_x + pict_spread * (i - 1) < x < offset_x + (pict_spread * (i - 1) + pict_size) and
                            offset_y + pict_spread * j < y <  offset_y + (pict_spread * j + pict_size)):
                        no_reps = True
                        temp = grid[i - 1][j]
                        grid[i - 1][j] = grid[i][j]
                        grid[i][j] = temp
                        break
                if i != len(grid) - 1 and not no_reps:
                    if (offset_x + pict_spread * (i + 1) < x < offset_x + (pict_spread * (i + 1) + pict_size) and
                            offset_y + pict_spread * j < y < offset_y + (pict_spread * j + pict_size)):
                        no_reps = True
                        temp = grid[i + 1][j]
                        grid[i + 1][j] = grid[i][j]
                        grid[i][j] = temp
                        break

def main():

    """Poniższe odpowiada za wykonanie PoczątkowegoLosowania"""
    for i in range(150):    #pętla, ilość iteracji odpowiada trudności układanki
        fake_key_movement(pictures, picture_0) #wykonuje się 5 fałszywego ruchu
    """Powyższe odpowiada za wykonanie PoczątkowegoLosowania"""

    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == KEYDOWN:
                key_movement(pictures, picture_0)
            if event.type == MOUSEBUTTONDOWN:
                x, y = event.pos
                mouse_movement(x, y, pictures, picture_0, 150, 150)

        draw_window()


    pygame.quit()


if __name__ == "__main__":
    main()
