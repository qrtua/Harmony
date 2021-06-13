import random
from typing import Tuple

import pygame
import os
from pygame.locals import *
import pyautogui #modul z oknami dialogowymi, wymaga instalacji, uzywany do NotatkiZwycięstwa
                # uruchom, cmd, jako admin i w konsole wpisać " python -m pip install pyautogui"

WIDTH, HEIGHT = 480, 480
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Gra studia HARMONY®")
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
SIZE_3 = int(WIDTH/3)
SIZE_FOUR = int(WIDTH/4)
notatka_powitalna = "Celem gry jest odtworzenie właściwego układu obrazka, zrób to a dowiesz się czegoś nowego na temat mieszkańcow dżungli. \n Używaj klawiatury lub myszki \n (naciśnij [h] na klawiaturze jeśli poziom trudności będzie za wysoki) \n Czy chcesz zagrać?"

pygame.init()

typ_fa = pygame.font.Font('Adca.ttf', 80)

FPS = 60

BORD_2 = pygame.Rect(0, 0, 480, 480)




def draw_window(pictures, line, side = 3):
    pygame.draw.rect(WIN, BLACK, BORD_2)
    for x in range(side):
        for y in range(side):
            WIN.blit(pictures[x][y], (x*line, y*line))
    pygame.display.update()


def key_movement(grid, empty_space, n = 1):
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
    elif get_key[pygame.K_h]:
        if n == 1:
            main_three(5, 1)
        else:
            main_four(5, 1)
    """elif get_key[pygame.K_l]:
        for i in range(10):
            fake_key_movement(grid,empty_space)"""


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

def main_three(n,m):
    wylosowany_temat = random.choice(os.listdir("Assets/jungle_photos"))[:-4]


    picture_0 = pygame.transform.scale(pygame.image.load(os.path.join("Assets", "outerbox.png")), (SIZE_3,SIZE_3))


    with open("Assets/interesting_facts/"+wylosowany_temat+str(random.randint(1,3))+".txt", "r", encoding="utf-8") as f:
        tresc_notatki = f.read().replace('\n','')
    tresc_notatki = 'Gratulacje!\n'+tresc_notatki+'\nCzy chcesz rozwiązać kolejną zagadkę?'




    obrazek = pygame.image.load(os.path.join("Assets\jungle_photos",wylosowany_temat+".jpg")) #obrazek musi znaajdować się w assetach i mieć określoną w tej linijce nazwę
    obrazek = pygame.transform.smoothscale(obrazek, (WIDTH, HEIGHT))

    picture_1 = obrazek.subsurface(0,0, SIZE_3, SIZE_3)
    picture_2 = obrazek.subsurface(SIZE_3, 0, SIZE_3, SIZE_3)
    picture_3 = obrazek.subsurface(2*SIZE_3, 0, SIZE_3, SIZE_3)
    picture_4 = obrazek.subsurface(0, SIZE_3, SIZE_3, SIZE_3)
    picture_5 = obrazek.subsurface(SIZE_3, SIZE_3, SIZE_3, SIZE_3)
    picture_6 = obrazek.subsurface(2*SIZE_3, SIZE_3, SIZE_3, SIZE_3)
    picture_7 = obrazek.subsurface(0, 2*SIZE_3, SIZE_3, SIZE_3)
    picture_8 = obrazek.subsurface(SIZE_3, 2*SIZE_3, SIZE_3, SIZE_3)

    #
    if m == 1:
        picture_1.blit(typ_fa.render('1',2,(0,0,0)), (75, 75))
        picture_2.blit(typ_fa.render('2',2,(0,0,0)), (75, 75))
        picture_3.blit(typ_fa.render('3',2,(0,0,0)), (75, 75))
        picture_4.blit(typ_fa.render('4',2,(0,0,0)), (75, 75))
        picture_5.blit(typ_fa.render('5',2,(0,0,0)), (75, 75))
        picture_6.blit(typ_fa.render('6',2,(0,0,0)), (75, 75))
        picture_7.blit(typ_fa.render('7',2,(0,0,0)), (75, 75))
        picture_8.blit(typ_fa.render('8',2,(0,0,0)), (75, 75))

    #

    pygame.draw.rect( picture_1 , BLACK, pygame.Rect(0, 0, SIZE_3, SIZE_3),  3)
    pygame.draw.rect( picture_2 , BLACK, pygame.Rect(0, 0, SIZE_3, SIZE_3),  3)
    pygame.draw.rect( picture_3 , BLACK, pygame.Rect(0, 0, SIZE_3, SIZE_3),  3)
    pygame.draw.rect( picture_4 , BLACK, pygame.Rect(0, 0, SIZE_3, SIZE_3),  3)
    pygame.draw.rect( picture_5 , BLACK, pygame.Rect(0, 0, SIZE_3, SIZE_3),  3)
    pygame.draw.rect( picture_6 , BLACK, pygame.Rect(0, 0, SIZE_3, SIZE_3),  3)
    pygame.draw.rect( picture_7 , BLACK, pygame.Rect(0, 0, SIZE_3, SIZE_3),  3)
    pygame.draw.rect( picture_8 , BLACK, pygame.Rect(0, 0, SIZE_3, SIZE_3),  3)



    pictures = [[picture_1, picture_4, picture_7],
                [picture_2, picture_5, picture_8],
                [picture_3, picture_6, picture_0]]

    poprawny_uklad = [[picture_1, picture_4, picture_7],
                [picture_2, picture_5, picture_8],
                [picture_3, picture_6, picture_0]]

    for i in range(n):    #pętla, ilość iteracji odpowiada trudności układanki
        fake_key_movement(pictures, picture_0) #wykonuje się 5 fałszywego ruchu

    clock = pygame.time.Clock()
    run = True
    draw_window(pictures,SIZE_3) #rysuje obrazek przed jakimkolwiek wydarzeniem
    while run:
        clock.tick(FPS)

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                run = False
            if event.type == KEYDOWN:
                key_movement(pictures, picture_0)
                draw_window(pictures, SIZE_3) #należało to tu wstawić by wykonał sie ostatni ruch

                if pictures == poprawny_uklad:
                    pass
                    if pyautogui.confirm(tresc_notatki, "Zwycięstwo!",
                                         ['Kolejna gra 3x3', 'Kolejna gra 4x4', 'Dość!']) == 'Kolejna gra 3x3':
                        x = pyautogui.confirm("Wybierz poziom trudności", 'Menu', ['Banalny', 'Łatwy', 'Trudny'])
                        if x == 'Banalny':
                            main_three(5, 1)
                        elif x == 'Łatwy':
                            main_three(30, 1)
                        else:
                            main_three(100, 0)
                    elif pyautogui.confirm(tresc_notatki, "Zwycięstwo!",
                                           ['Kolejna gra 3x3', 'Kolejna gra 4x4', 'Dość!']) == 'Kolejna gra 4x4':
                        x = pyautogui.confirm("Wybierz poziom trudności", 'Menu', ['Banalny', 'Łatwy', 'Trudny'])
                        if x == 'Banalny':
                            main_four(20, 1)
                        elif x == 'Łatwy':
                            main_four(40, 1)
                        else:
                            main_four(100, 0)
                    else:
                        run = False

            if event.type == MOUSEBUTTONDOWN:
                x, y = event.pos
                mouse_movement(x, y, pictures, picture_0, SIZE_3, SIZE_3)
                draw_window(pictures, SIZE_3) #należało to tu wstawić by wykonał sie ostatni ruch, podobnie jak wyzej

                if pictures == poprawny_uklad:
                    pass
                    if pyautogui.confirm(tresc_notatki,"Zwycięstwo!",['Kolejna gra 3x3', 'Kolejna gra 4x4', 'Dość!']) == 'Kolejna gra 3x3':
                        x = pyautogui.confirm("Wybierz poziom trudności",'Menu',['Banalny','Łatwy','Trudny'])
                        if x == 'Banalny':
                            main_three(5, 1)
                        elif x == 'Łatwy':
                            main_three(30, 1)
                        else:
                            main_three(100, 0)

                    elif pyautogui.confirm(tresc_notatki,"Zwycięstwo!",['Kolejna gra 3x3', 'Kolejna gra 4x4', 'Dość!']) == 'Kolejna gra 4x4':
                        x = pyautogui.confirm("Wybierz poziom trudności",'Menu',['Banalny','Łatwy','Trudny'])
                        if x == 'Banalny':
                            main_four(20, 1)
                        elif x == 'Łatwy':
                            main_four(40, 1)
                        else:
                            main_four(100, 0)
                    else:
                            run = False

        #draw_window() #chyba nieporzebnie sie to nieustannie wykonuje, no moze do czasu wstawienia animacji...


    pygame.quit()


def main_four(n,m):
    wylosowany_temat = random.choice(os.listdir("Assets/jungle_photos"))[:-4]


    picture_0 = pygame.transform.scale(pygame.image.load(os.path.join("Assets", "outerbox.png")), (SIZE_FOUR,SIZE_FOUR))


    with open("Assets/interesting_facts/"+wylosowany_temat+str(random.randint(1,3))+".txt", "r", encoding="utf-8") as f:
        tresc_notatki = f.read().replace('\n','')
    tresc_notatki = 'Gratulacje!\n'+tresc_notatki+'\nCzy chcesz rozwiązać kolejną zagadkę?'




    obrazek = pygame.image.load(os.path.join("Assets\jungle_photos",wylosowany_temat+".jpg")) #obrazek musi znaajdować się w assetach i mieć określoną w tej linijce nazwę
    obrazek = pygame.transform.smoothscale(obrazek, (WIDTH, HEIGHT))

    picture_1 = obrazek.subsurface(0, 0, SIZE_FOUR, SIZE_FOUR)
    picture_2 = obrazek.subsurface(SIZE_FOUR, 0, SIZE_FOUR, SIZE_FOUR)
    picture_3 = obrazek.subsurface(2*SIZE_FOUR, 0, SIZE_FOUR, SIZE_FOUR)
    picture_4 = obrazek.subsurface(3*SIZE_FOUR, 0, SIZE_FOUR, SIZE_FOUR)
    picture_5 = obrazek.subsurface(0, SIZE_FOUR, SIZE_FOUR, SIZE_FOUR)
    picture_6 = obrazek.subsurface(SIZE_FOUR, SIZE_FOUR, SIZE_FOUR, SIZE_FOUR)
    picture_7 = obrazek.subsurface(2*SIZE_FOUR, SIZE_FOUR, SIZE_FOUR, SIZE_FOUR)
    picture_8 = obrazek.subsurface(3*SIZE_FOUR, SIZE_FOUR, SIZE_FOUR, SIZE_FOUR)
    picture_9 = obrazek.subsurface(0, 2*SIZE_FOUR, SIZE_FOUR, SIZE_FOUR)
    picture_10 = obrazek.subsurface(SIZE_FOUR, 2*SIZE_FOUR, SIZE_FOUR, SIZE_FOUR)
    picture_11 = obrazek.subsurface(2*SIZE_FOUR, 2*SIZE_FOUR, SIZE_FOUR, SIZE_FOUR)
    picture_12 = obrazek.subsurface(3*SIZE_FOUR, 2*SIZE_FOUR, SIZE_FOUR, SIZE_FOUR)
    picture_13 = obrazek.subsurface(0, 3*SIZE_FOUR, SIZE_FOUR, SIZE_FOUR)
    picture_14 =obrazek.subsurface(SIZE_FOUR, 3*SIZE_FOUR, SIZE_FOUR, SIZE_FOUR)
    picture_15 =obrazek.subsurface(2*SIZE_FOUR, 3*SIZE_FOUR, SIZE_FOUR, SIZE_FOUR)
    #
    if m == 1:
        picture_1.blit(typ_fa.render('1',2,(0,0,0)), (60, 60))
        picture_2.blit(typ_fa.render('2',2,(0,0,0)), (60, 60))
        picture_3.blit(typ_fa.render('3',2,(0,0,0)), (60, 60))
        picture_4.blit(typ_fa.render('4',2,(0,0,0)), (60, 60))
        picture_5.blit(typ_fa.render('5',2,(0,0,0)), (60, 60))
        picture_6.blit(typ_fa.render('6',2,(0,0,0)), (60, 60))
        picture_7.blit(typ_fa.render('7',2,(0,0,0)), (60, 60))
        picture_8.blit(typ_fa.render('8',2,(0,0,0)), (60, 60))
        picture_9.blit(typ_fa.render('9', 2, (0, 0, 0)), (60, 60))
        picture_10.blit(typ_fa.render('10', 2, (0, 0, 0)), (60, 60))
        picture_11.blit(typ_fa.render('11', 2, (0, 0, 0)), (60, 60))
        picture_12.blit(typ_fa.render('12', 2, (0, 0, 0)), (60, 60))
        picture_13.blit(typ_fa.render('13', 2, (0, 0, 0)), (60, 60))
        picture_14.blit(typ_fa.render('14', 2, (0, 0, 0)), (60, 60))
        picture_15.blit(typ_fa.render('15', 2, (0, 0, 0)), (60, 60))


    #

    pygame.draw.rect(picture_1, BLACK, pygame.Rect(0, 0, SIZE_FOUR, SIZE_FOUR),  3)
    pygame.draw.rect(picture_2, BLACK, pygame.Rect(0, 0, SIZE_FOUR, SIZE_FOUR), 3)
    pygame.draw.rect(picture_3, BLACK, pygame.Rect(0, 0, SIZE_FOUR, SIZE_FOUR), 3)
    pygame.draw.rect(picture_4, BLACK, pygame.Rect(0, 0, SIZE_FOUR, SIZE_FOUR), 3)
    pygame.draw.rect(picture_5, BLACK, pygame.Rect(0, 0, SIZE_FOUR, SIZE_FOUR), 3)
    pygame.draw.rect(picture_6, BLACK, pygame.Rect(0, 0, SIZE_FOUR, SIZE_FOUR), 3)
    pygame.draw.rect(picture_7, BLACK, pygame.Rect(0, 0, SIZE_FOUR, SIZE_FOUR), 3)
    pygame.draw.rect(picture_8, BLACK, pygame.Rect(0, 0, SIZE_FOUR, SIZE_FOUR), 3)
    pygame.draw.rect(picture_9, BLACK, pygame.Rect(0, 0, SIZE_FOUR, SIZE_FOUR), 3)
    pygame.draw.rect(picture_10, BLACK, pygame.Rect(0, 0, SIZE_FOUR, SIZE_FOUR), 3)
    pygame.draw.rect(picture_11, BLACK, pygame.Rect(0, 0, SIZE_FOUR, SIZE_FOUR), 3)
    pygame.draw.rect(picture_12, BLACK, pygame.Rect(0, 0, SIZE_FOUR, SIZE_FOUR), 3)
    pygame.draw.rect(picture_13, BLACK, pygame.Rect(0, 0, SIZE_FOUR, SIZE_FOUR), 3)
    pygame.draw.rect(picture_14, BLACK, pygame.Rect(0, 0, SIZE_FOUR, SIZE_FOUR), 3)
    pygame.draw.rect(picture_15, BLACK, pygame.Rect(0, 0, SIZE_FOUR, SIZE_FOUR), 3)

    pictures = [[picture_1, picture_5, picture_9, picture_13],
                [picture_2, picture_6, picture_10, picture_14],
                [picture_3, picture_7, picture_11, picture_15],
                [picture_4, picture_8,picture_12, picture_0]]

    poprawny_uklad = [[picture_1, picture_5, picture_9, picture_13],
                    [picture_2, picture_6, picture_10, picture_14],
                    [picture_3, picture_7, picture_11, picture_15],
                    [picture_4, picture_8,picture_12, picture_0]]

    for i in range(n):    #pętla, ilość iteracji odpowiada trudności układanki
        fake_key_movement(pictures, picture_0,) #wykonuje się 5 fałszywego ruchu

    clock = pygame.time.Clock()
    run = True
    draw_window(pictures,SIZE_FOUR, 4) #rysuje obrazek przed jakimkolwiek wydarzeniem
    while run:
        clock.tick(FPS)

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                run = False
            if event.type == KEYDOWN:
                key_movement(pictures, picture_0, 2)
                draw_window(pictures, SIZE_FOUR, 4) #należało to tu wstawić by wykonał sie ostatni ruch

                if pictures == poprawny_uklad:
                    pass
                    if pyautogui.confirm(tresc_notatki, "Zwycięstwo!",
                                         ['Kolejna gra 3x3', 'Kolejna gra 4x4', 'Dość!']) == 'Kolejna gra 3x3':
                        x = pyautogui.confirm("Wybierz poziom trudności", 'Menu', ['Banalny', 'Łatwy', 'Trudny'])
                        if x == 'Banalny':
                            main_three(5, 1)
                        elif x == 'Łatwy':
                            main_three(30, 1)
                        else:
                            main_three(100, 0)
                    elif pyautogui.confirm(tresc_notatki, "Zwycięstwo!",
                                           ['Kolejna gra 3x3', 'Kolejna gra 4x4', 'Dość!']) == 'Kolejna gra 4x4':
                        x = pyautogui.confirm("Wybierz poziom trudności", 'Menu', ['Banalny', 'Łatwy', 'Trudny'])
                        if x == 'Banalny':
                            main_four(20, 1)
                        elif x == 'Łatwy':
                            main_four(40, 1)
                        else:
                            main_four(100, 0)
                    else:
                        run = False

            if event.type == MOUSEBUTTONDOWN:
                x, y = event.pos
                mouse_movement(x, y, pictures, picture_0, SIZE_FOUR, SIZE_FOUR)
                draw_window(pictures, SIZE_FOUR, 4) #należało to tu wstawić by wykonał sie ostatni ruch, podobnie jak wyzej

                if pictures == poprawny_uklad:
                    pass
                    if pyautogui.confirm(tresc_notatki, "Zwycięstwo!",
                                         ['Kolejna gra 3x3', 'Kolejna gra 4x4', 'Dość!']) == 'Kolejna gra 3x3':
                        x = pyautogui.confirm("Wybierz poziom trudności", 'Menu', ['Banalny', 'Łatwy', 'Trudny'])
                        if x == 'Banalny':
                            main_three(5, 1)
                        elif x == 'Łatwy':
                            main_three(30, 1)
                        else:
                            main_three(100, 0)
                    elif pyautogui.confirm(tresc_notatki, "Zwycięstwo!",
                                           ['Kolejna gra 3x3', 'Kolejna gra 4x4', 'Dość!']) == 'Kolejna gra 4x4':
                        x = pyautogui.confirm("Wybierz poziom trudności", 'Menu', ['Banalny', 'Łatwy', 'Trudny'])
                        if x == 'Banalny':
                            main_four(20, 1)
                        elif x == 'Łatwy':
                            main_four(40, 1)
                        else:
                            main_four(100, 0)
                    else:
                        run = False

        #draw_window() #chyba nieporzebnie sie to nieustannie wykonuje, no moze do czasu wstawienia animacji...


    pygame.quit()

if __name__ == "__main__":
    if pyautogui.confirm(notatka_powitalna, "Gra studia HARMONY®", ['Tak 3x3!', 'Tak 4x4!', 'Nie, chyba nie to kliknąłem']) == 'Tak 3x3!':
        main_three(random.randint(0, 40), 0)
    elif pyautogui.confirm(notatka_powitalna, "Gra studia HARMONY®", ['Tak 3x3!', 'Tak 4x4!', 'Nie, chyba nie to kliknąłem']) == 'Tak 4x4!':
        main_four(random.randint(0, 40), 0)