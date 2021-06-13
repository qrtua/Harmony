import random
import pygame
import os
from pygame.locals import *
import pyautogui  # modul z oknami dialogowymi, wymaga instalacji, uzywany do NotatkiZwycięstwa
# uruchom, cmd, jako admin i w konsole wpisać " python -m pip install pyautogui"

COUNTER = 0

WIDTH, HEIGHT = 450, 450
WIN = pygame.display.set_mode((WIDTH, HEIGHT))

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
SIZE = (150, 150)

notatka_powitalna = "Celem gry jest odtworzenie właściwego układu obrazka, zrób to a dowiesz się czegoś nowego na temat mieszkańcow dżungli. \n Używaj klawiatury lub myszki \n (naciśnij [h] na klawiaturze jeśli poziom trudności będzie za wysoki) \n Czy chcesz zagrać?"

pygame.init()

typ_fa = pygame.font.Font('Adca.ttf', 100)

FPS = 60
# BORD = pygame.image.load(os.path.join('Assets', 'outerbox.png'))
# BORD = pygame.transform.scale(BORD, (450, 450))
BORD_2 = pygame.Rect(0, 0, 460, 460)

Kwadrat = pygame.Rect(0, 0, 150, 150)


def draw_window(pictures):
    WIN.fill(WHITE)
    pygame.draw.rect(WIN, BLACK, BORD_2)
    for x in range(3):
        for y in range(3):
            WIN.blit(pictures[x][y], (x*150, y*150))
    pygame.display.update()


def key_movement(grid, empty_space):
    global COUNTER
    COUNTER = COUNTER + 1
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
        main(random.randint(50,100),1)
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
    global COUNTER
    COUNTER = COUNTER + 1
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


def make_tresc_notatki(f, n):
    tresc_notatki = f.read().replace('\n', '')
    tresc_notatki = ('Gratulacje!\n Liczba wykonanych ruchów: ' + str(n) + '.\n' + tresc_notatki +
                     '\nCzy chcesz rozwiązać kolejną zagadkę?')
    return tresc_notatki


def main(n,m):
    global COUNTER
    COUNTER = 0


    wylosowany_temat = random.choice(os.listdir("Assets/jungle_photos"))[:-4]


    picture_0 = pygame.transform.scale(pygame.image.load(os.path.join("Assets", "outerbox.png")), (SIZE))


    obrazek = pygame.image.load(os.path.join("Assets\jungle_photos",wylosowany_temat+".jpg")) #obrazek musi znaajdować się w assetach i mieć określoną w tej linijce nazwę
    obrazek = pygame.transform.smoothscale(obrazek, (WIDTH, HEIGHT))

    picture_1 = obrazek.subsurface(0,0,150,150)
    picture_2 = obrazek.subsurface(150,0,150,150)
    picture_3 = obrazek.subsurface(300,0,150,150)
    picture_4 = obrazek.subsurface(0,150,150,150)
    picture_5 = obrazek.subsurface(150,150,150,150)
    picture_6 = obrazek.subsurface(300,150,150,150)
    picture_7 = obrazek.subsurface(0,300,150,150)
    picture_8 = obrazek.subsurface(150,300,150,150)

    #
    if m == 1:
        picture_1.blit(typ_fa.render('1',2,(0,0,0)), (75,75))
        picture_2.blit(typ_fa.render('2',2,(0,0,0)), (75,75))
        picture_3.blit(typ_fa.render('3',2,(0,0,0)), (75,75))
        picture_4.blit(typ_fa.render('4',2,(0,0,0)), (75,75))
        picture_5.blit(typ_fa.render('5',2,(0,0,0)), (75,75))
        picture_6.blit(typ_fa.render('6',2,(0,0,0)), (75,75))
        picture_7.blit(typ_fa.render('7',2,(0,0,0)), (75,75))
        picture_8.blit(typ_fa.render('8',2,(0,0,0)), (75,75))

    #

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

    for i in range(n):    #pętla, ilość iteracji odpowiada trudności układanki
        fake_key_movement(pictures, picture_0) #wykonuje się 5 fałszywego ruchu

    clock = pygame.time.Clock()
    run = True
    draw_window(pictures) #rysuje obrazek przed jakimkolwiek wydarzeniem
    while run:
        clock.tick(FPS)

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                run = False
            if event.type == KEYDOWN:
                key_movement(pictures, picture_0)
                draw_window(pictures) #należało to tu wstawić by wykonał sie ostatni ruch

                if pictures == poprawny_uklad:
                    with open("Assets/interesting_facts/" + wylosowany_temat + str(random.randint(1, 3)) + ".txt", "r",
                              encoding="utf-8") as f:
                        tresc_notatki = make_tresc_notatki(f, COUNTER)
                    if pyautogui.confirm(tresc_notatki,"Zwycięstwo!",['Kolejna gra','Dość!']) == 'Kolejna gra':
                        x = pyautogui.confirm("Wybierz poziom trudności",'Menu',['Banalny','Łatwy','Trudny'])
                        if x == 'Banalny':
                            main(5,1)
                        elif x == 'Łatwy':
                            main(30,1)
                        else:
                            main(100,0)
                    else:
                        run = False

            if event.type == MOUSEBUTTONDOWN:
                x, y = event.pos
                mouse_movement(x, y, pictures, picture_0, 150, 150)
                draw_window(pictures) #należało to tu wstawić by wykonał sie ostatni ruch, podobnie jak wyzej

                if pictures == poprawny_uklad:
                    pass
                    with open("Assets/interesting_facts/" + wylosowany_temat + str(random.randint(1, 3)) + ".txt", "r",
                              encoding="utf-8") as f:
                        tresc_notatki = make_tresc_notatki(f, COUNTER)
                    if pyautogui.confirm(tresc_notatki,"Zwycięstwo!",['Kolejna gra','Dość!']) == 'Kolejna gra':
                        x = pyautogui.confirm("Wybierz poziom trudności",'Menu',['Banalny','Łatwy','Trudny'])
                        if x == 'Banalny':
                            main(5,1)
                        elif x == 'Łatwy':
                            main(30,1)
                        else:
                            main(100,0)
                    else:
                            run = False

        #draw_window() #chyba nieporzebnie sie to nieustannie wykonuje, no moze do czasu wstawienia animacji...


    pygame.quit()


if __name__ == "__main__":
    if pyautogui.confirm(notatka_powitalna,"Gra studia HARMONY®",['Tak!','Nie, chyba nie to kliknąłem']) == 'Tak!':
        main(random.randint(0,40),0)
