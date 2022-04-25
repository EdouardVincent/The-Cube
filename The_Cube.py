import pygame
from pygame.locals import*
import sys
import random
import time
from tkinter import *
from tkinter import ttk
from turtle import*

#variables#

start = 0
length_blocks = 2
loop=21
nb_movements = 0
level = 0
total_time = 0.0
show_score = 0
tutorial = 0
menu = 1
game = 0
a=0
moove = ''
lose = 0

coordonees_block = {}
corner_coordonees_cube_x = 0
corner_coordonees_cube_y = 0

movement = []

#variables#

pygame.init()

fond = pygame.font.Font('freesansbold.ttf',30)

TextSurf = fond.render('Choose your square', True, (255, 255, 255))
PressStartSurf = fond.render('Press ESPACE to start', True, (255, 255, 255))

#Images#

red_cube = pygame.image.load('Images\\red_cube.jpg')
blue_cube = pygame.image.load('Images\\blue_cube.jpg')
green_cube =  pygame.image.load('Images\\green_cube.jpg')
purple_cube = pygame.image.load('Images\\purple_cube.png')
square =  pygame.image.load('Images\\square.png')
background =  pygame.image.load('Images\\bg.png')
menu_image = pygame.image.load('Images\\Menu.png')
button_leave_image = pygame.image.load('Images\\button_leave.png')
button_play_image = pygame.image.load('Images\\button_play.png')
button_tutorial_image = pygame.image.load('Images\\button_tutorial.png')
tutorial_image = pygame.image.load('Images\\Tutorial.png')
Lost_animation = pygame.image.load('Images\\Lost_animation.png')
yes_button_image = pygame.image.load('Images\\yes_button.png')
no_button_image = pygame.image.load('Images\\no_button.png')

#Images

class cube () :
    def __init__ (self) :
        self.x = 642
        self.y = 324
        self.image = red_cube
        self.velocity = 30

    def display(self) :
        window.blit(self.image,(self.x,self.y))

    def moove_left(self) :
        self.x-=self.velocity

    def moove_right(self) :
        self.x+=self.velocity

    def moove_up(self) :
        self.y-=self.velocity

def generate_random_map (crd,lgth_blocks,loop) :
    x = 642
    y = 618
    last_moove = 'up'
    for i in range(loop) :
        random_number = random.randint(0,2)

        
        for j in range(lgth_blocks) :
        
            if random_number == 0 and last_moove == 'up' or last_moove == 'right' : #add a block on the right
                x+=30
                last_moove = 'right'

            if random_number == 1 and last_moove == 'up' or last_moove == 'left' : #add a block on the left
                x-=30
                last_moove = 'left'

            if random_number == 2 : #add a block up
                if last_moove == 'right' :
                    x-=30

                if last_moove == 'left' :
                    x+=30
                    
                y-=30
                last_moove = 'up'

            movement.append(last_moove)

            crd[i,j] = ((x,y))
            
#Turtle Sequence#

ht()
color('red')
speed(5000)

for x in range (200) :
	forward(x)
	left(x)
	
penup()
left(90)
forward(170)
pendown()
write("Made by Edouard Vincent")
time.sleep(5)
bye()

#Turtle Sequence#

window = pygame.display.set_mode((1284, 648))
pygame.display.set_icon(red_cube)
pygame.display.set_caption('The Cube')

button_leave_rect = button_leave_image.get_rect(topleft = (500,500))
button_play_rect = button_play_image.get_rect(topleft = (500,300))
button_tutorial_rect = button_tutorial_image.get_rect(topleft = (500,400))
        
while menu :
    for event in pygame.event.get() :

        mouse_position = pygame.mouse.get_pos() 

        if event.type == QUIT :
            pygame.quit()
            sys.exit()

        if event.type == MOUSEBUTTONDOWN :
            if button_leave_rect.collidepoint(mouse_position) :
                pygame.quit()
                sys.exit()

            if button_tutorial_rect.collidepoint(mouse_position) :
                tutorial = 1
                menu = 0

            if button_play_rect.collidepoint(mouse_position) :
                choose_square = 1
                menu = 0
            
    window.blit(menu_image,(0,0))
    window.blit(button_leave_image,(500,500))
    window.blit(button_tutorial_image,(500,400))
    window.blit(button_play_image,(500,300))
    
    pygame.display.flip()

if tutorial == 1 :
    button_play_rect = button_play_image.get_rect(topleft = (200,200))
    while tutorial :
        for event in pygame.event.get() :

            mouse_position = pygame.mouse.get_pos()   

            if event.type == QUIT :
                pygame.quit()
                sys.exit()

            if event.type == MOUSEBUTTONDOWN :
                if button_play_rect.collidepoint(mouse_position) :
                    tutorial = 0
                    choose_square = 1

            window.blit(tutorial_image,(0,0))
            window.blit(button_play_image,(200,200))
            pygame.display.flip()

Cube = cube()

Cube1 = cube()
Cube2 = cube()
Cube3 = cube()

Cube2.x = 602
Cube2.image = blue_cube

Cube3.x = 682
Cube3.image = green_cube

red_cube_rect = red_cube.get_rect(topleft = (Cube1.x, Cube1.y))
blue_cube_rect = blue_cube.get_rect(topleft = (Cube2.x, Cube2.y))
green_cube_rect  = green_cube.get_rect(topleft = (Cube3.x, Cube3.y))

while choose_square :

    for event in pygame.event.get () :

        mouse_position = pygame.mouse.get_pos()   
        
        if event.type == QUIT :
            pygame.quit()
            sys.exit()

        

    try :
        window.blit(background,(0,0))
        
        if red_cube_rect.collidepoint(mouse_position) :
            window.blit(square,(Cube1.x-2.5, Cube1.y-2.5))
            if event.type == MOUSEBUTTONDOWN :
                Cube.image = red_cube
                choose_square = 0
                game = 1
                pygame.quit()
            
        if blue_cube_rect.collidepoint(mouse_position) :
            window.blit(square,(Cube2.x-2.5, Cube2.y-2.5))
            if event.type == MOUSEBUTTONDOWN :
                Cube.image = blue_cube
                choose_square = 0
                game = 1
                pygame.quit()
                
        if green_cube_rect.collidepoint(mouse_position) :
            window.blit(square,(Cube3.x-2.5, Cube3.y-2.5))
            if event.type == MOUSEBUTTONDOWN :
                Cube.image = green_cube
                choose_square = 0
                game = 1
                pygame.quit()
                
        
        window.blit(TextSurf,(512, 284))         
        Cube1.display()
        Cube2.display()
        Cube3.display()
        pygame.display.flip()

    except pygame.error :
        break
    
window = pygame.display.set_mode((1286, 648))
pygame.display.set_icon(red_cube)
pygame.display.set_caption('The Cube')

#instances#

block0 = cube()
block1 = cube()
block2 = cube()
block3 = cube()
block4 = cube()
block5 = cube()
block6 = cube()
block7 = cube()
block8 = cube()
block9 = cube()
block10 = cube()
block11 = cube()
block12 = cube()
block13 = cube()
block14 = cube()
block15 = cube()
block16 = cube()
block17 = cube()
block18 = cube()
block19 = cube()
block20 = cube()
block21 = cube()
block22 = cube()
block23 = cube()
block24 = cube()
block25 = cube()
block26 = cube()
block27 = cube()
block28 = cube()
block29 = cube()
block30 = cube()
block31 = cube()
block32 = cube()
block33 = cube()
block34 = cube()
block35 = cube()
block36 = cube()
block37 = cube()
block38 = cube()
block39 = cube()
block40 = cube()
block41 = cube()
block42 = cube()

#instances# Sorry for that ...

blocks = [block0,
    block1,
    block2,
    block3,
    block4,
    block5,
    block6,
    block7,
    block8,
    block9,
    block10,
    block11,
    block12,
    block13,
    block14,
    block15,
    block16,
    block17,
    block18,
    block19,
    block20,
    block21,
    block22,
    block23,
    block24,
    block25,
    block26,
    block27,
    block28,
    block29,
    block30,
    block31,
    block32,
    block33,
    block34,
    block35,
    block36,
    block37,
    block38,
    block39,
    block40,
    block41,
    block42]

button_no_rect = no_button_image.get_rect(topleft = (755, 300))
button_yes_rect = yes_button_image.get_rect(topleft = (370, 300))

for x in range(len(blocks)) :
    blocks[x].image = purple_cube
    
while game :

    movement = []

    try :
        window.blit(background,(0,0))
    except pygame.error :
        show_score = 1

    Cube.x = 642
    Cube.y = 618

    corner_coordonees_cube_x = Cube.x
    corner_coordonees_cube_y = Cube.y

    generate_random_map(coordonees_block, length_blocks, loop)
    

    for i in range(loop) :
        for j in range(length_blocks) :
            window.blit(purple_cube,(coordonees_block[i,j])) 
            pygame.display.flip()
            a+= 1
            blocks[a].x = coordonees_block[i,j][0]
            blocks[a].y = coordonees_block[i,j][1]
        
    seconds = 0
    a=0
    start_level = 1
            
    while start_level :

        for event in pygame.event.get() :
            if event.type == QUIT :
                pygame.quit()
                sys.exit()

            mouse_position = pygame.mouse.get_pos()   

            if event.type == MOUSEBUTTONDOWN and lose == 1 :

                if button_no_rect.collidepoint(mouse_position) :    
                    pygame.quit()
                    sys.exit()     

                if button_yes_rect.collidepoint(mouse_position):    
                    level = 0
                    start = 0
                    lose = 0
                    start_level = 0                            

            if event.type == KEYDOWN :
                if event.key == K_ESCAPE :
                    show_score = 1
                    break

                if event.key == K_SPACE :
                    start = 1

                if event.key == K_LEFT and start == 1 and lose == 0:
                    nb_movements = 0
                    for x in range(len(movement)) :
                        if movement[x] == 'left' :
                            nb_movements+=1 

                        if movement[x] != 'left' :
                            break

                    if nb_movements > 0 :
                        moove = 'left'

                    if moove == 'up' or moove == 'right' :
                        lose = 1


                if event.key == K_RIGHT and start == 1 and lose == 0 :
                    nb_movements = 0
                    for x in range(len(movement)) :
                        if movement[x] == 'right' :
                            nb_movements+=1      
                            
                        if movement[x] != 'right' :
                            break

                    if nb_movements > 0 :
                        moove = 'right'

                    if moove == 'up' or moove == 'left' :
                        lose = 1


                if event.key == K_UP and start == 1 and lose == 0 :

                    nb_movements = 0
                    for x in range(len(movement)) :
                        if movement[x] == 'up' :
                            nb_movements+=1

                        if movement[x] != 'up' :
                            break

                    if nb_movements > 0 :
                        moove = 'up'
                    
                    if moove == 'right' or moove == 'left' :
                        lose = 1
                        
        if moove == 'up' and nb_movements > 0 :
            nb_movements-=1
            movement.remove('up')
            Cube.moove_up()

        if moove == 'right' and nb_movements > 0 :
            nb_movements-=1
            movement.remove('right')
            Cube.moove_right()

        if moove == 'left' and nb_movements > 0 :
            nb_movements-=1
            movement.remove('left')
            Cube.moove_left()

        if movement == [] :
            total_time+=seconds*3
            level+=1
            break

        window.blit(background,(0,0))

        if start == 0 :
            window.blit(PressStartSurf,(0,0))

        window.blit(purple_cube,(642,618))

        for x in range(len(blocks)) :
            blocks[x].display()

        Cube.display()

        if lose == 1 :
            window.blit(background,(0,0))
            window.blit(Lost_animation,(350,200))
            window.blit(yes_button_image,(370,300))
            window.blit(no_button_image,(755,300))

        pygame.display.flip()

        if show_score == 1 :
            break

    if show_score == 1 :

        pygame.quit()
        fenetre_tk = Tk()

        fenetre_tk.title = 'Score'

        label = Label(fenetre_tk, text="Levels Done : %s" %level)
        label.pack()

        button=Button(fenetre_tk, text="Close", command=fenetre_tk.quit)
        button.pack()

        fenetre_tk.mainloop()
