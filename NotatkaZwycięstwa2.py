#Dokonane zmiany widać pomiędzy liniami typu """powyższe x **** Notatka Zwyciestwa 2""" a """poniższe x **** Not Zwy 2"""
#kod powinien się uruchamiać, można go skopiować w celu dodania kolejnej funkcjonalności, polecam jednak wtedy pozbawić go klamr tej funkcjonalności i postawić nowe
#funkcjonalność została zaprojektowana zgodnie z innymi sztywnie wczesniej ustalonymi wymiarami, w razie decyzji projektowej o zmianie tychże tj: wielkość kafli, wielkość okna, marginesy, wymiary siatki itd, należy zedytować również PrzycinaniaObrazków
import random
import pygame
import os
from pygame.locals import *
import pyautogui #modul z oknami dialogowymi, wymaga instalacji, uzywany do NotatkiZwycięstwa
                # uruchom, cmd, jako admin i w konsole wpisać " python -m pip install pyautogui"

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


picture_0 = pygame.transform.scale(pygame.image.load(os.path.join("Assets", "outerbox.png")), (SIZE))

"""ponizsza zmienna jest ustalana na potrzebe NotatkiZwycięstwa"""
with open("ciekawostka_tukan_1.txt", "r", encoding="utf-8") as f:
    tresc_notatki = f.read().replace('\n','')
tresc_notatki = 'Gratulacje!\n'+tresc_notatki+'\nCzy chcesz rozwiązać kolejną zagadkę?'
"""powyższa zmienna jest ustalana na potrzebe NotatkiZwycięstwa"""


obrazek = pygame.image.load(os.path.join("Assets",'tucan.jpg')) #obrazek musi znaajdować się w assetach i mieć określoną w tej linijce nazwę
obrazek = pygame.transform.smoothscale(obrazek, (WIDTH, HEIGHT))

picture_1 = obrazek.subsurface(0,0,150,150)
picture_2 = obrazek.subsurface(150,0,150,150)
picture_3 = obrazek.subsurface(300,0,150,150)
picture_4 = obrazek.subsurface(0,150,150,150)
picture_5 = obrazek.subsurface(150,150,150,150)
picture_6 = obrazek.subsurface(300,150,150,150)
picture_7 = obrazek.subsurface(0,300,150,150)
picture_8 = obrazek.subsurface(150,300,150,150)

pygame.draw.rect( picture_1 , BLACK, pygame.Rect(0, 0, 150, 150),  3)
pygame.draw.rect( picture_2 , BLACK, pygame.Rect(0, 0, 150, 150),  3)
pygame.draw.rect( picture_3 , BLACK, pygame.Rect(0, 0, 150, 150),  3)
pygame.draw.rect( picture_4 , BLACK, pygame.Rect(0, 0, 150, 150),  3)
pygame.draw.rect( picture_5 , BLACK, pygame.Rect(0, 0, 150, 150),  3)
pygame.draw.rect( picture_6 , BLACK, pygame.Rect(0, 0, 150, 150),  3)
pygame.draw.rect( picture_7 , BLACK, pygame.Rect(0, 0, 150, 150),  3)
pygame.draw.rect( picture_8 , BLACK, pygame.Rect(0, 0, 150, 150),  3)



pictures = [[picture_1, picture_4, picture_7],
            [picture_2, picture_5, picture_8],
            [picture_3, picture_6, picture_0]]

poprawny_uklad = [[picture_1, picture_4, picture_7],
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

    for i in range(5):    #pętla, ilość iteracji odpowiada trudności układanki
        fake_key_movement(pictures, picture_0) #wykonuje się 5 fałszywego ruchu

    clock = pygame.time.Clock()
    run = True
    draw_window() #rysuje obrazek przed jakimkolwiek wydarzeniem
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == KEYDOWN:
                key_movement(pictures, picture_0)
                draw_window() #należało to tu wstawić by wykonał sie ostatni ruch

                if pictures == poprawny_uklad:
                    #print('zwycięstwo! 0') # to porzestaje być potrzebne
                    """poniższe realizuje notatke zwyciestwa2"""
                    if pyautogui.confirm(tresc_notatki,'Zwycięstwo!!!',['Kolejna gra','Dość']) == 'Dość':
                        run = False
                    elif pyautogui.confirm(tresc_notatki,'Zwycięstwo!!!',['Kolejna gra','Dość']) == 'Kolejna gra':
                        pass #narazie nie wiem, jakiś restart
                    """powyższe realizuje notatke zwyciestwa2"""

            if event.type == MOUSEBUTTONDOWN:
                x, y = event.pos
                mouse_movement(x, y, pictures, picture_0, 150, 150)
                draw_window() #należało to tu wstawić by wykonał sie ostatni ruch, podobnie jak wyzej

                if pictures == poprawny_uklad:
                    #print('zwycięstwo!') # to porzestaje być potrzebne, jak wyzej
                    """poniższe realizuje notatke zwyciestwa2"""
                    if pyautogui.confirm(tresc_notatki,'Zwycięstwo!!!',['Kolejna gra','Dość']) == 'Dość':
                        run = False
                    elif pyautogui.confirm(tresc_notatki,'Zwycięstwo!!!',['Kolejna gra','Dość']) == 'Kolejna gra':
                        pass #narazie nie wiem, jakiś restart
                    """powyższe realizuje notatke zwyciestwa2"""

        #draw_window() #chyba nieporzebnie sie to nieustannie wykonuje, no moze do czasu wstawienia animacji...


    pygame.quit()


if __name__ == "__main__":
    main()
