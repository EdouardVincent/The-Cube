#The Cube Mobile
#Author : Edouard Vincent

import pygame
from pygame.locals import*
import sys
import random
import time
from turtle import*

#variables#

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
time_limit = 30
lose_with_time = 0
best_score = 0

coordonees_block = {}
corner_coordonees_cube_x = 0
corner_coordonees_cube_y = 0

movement = []

#variables#

pygame.init()

fond = pygame.font.Font('freesansbold.ttf',30)

TextSurf = fond.render('Choose your square', True, (255, 255, 255))

#Images#

red_cube = pygame.image.load('Images//red_cube.jpg')
blue_cube = pygame.image.load('Images//blue_cube.jpg')
green_cube =  pygame.image.load('Images//green_cube.jpg')
purple_cube = pygame.image.load('Images//purple_cube.png')
square =  pygame.image.load('Images//square.png')
background =  pygame.image.load('Images//bg.png')
menu_image = pygame.image.load('Images//Menu.png')
button_leave_image = pygame.image.load('Images//button_leave.png')
button_play_image = pygame.image.load('Images//button_play.png')
button_tutorial_image = pygame.image.load('Images//button_tutorial.png')
tutorial_image = pygame.image.load('Images//Tutorial.png')
Lost_animation = pygame.image.load('Images//Lost_Animation.png')
yes_button_image = pygame.image.load('Images//yes_button.png')
no_button_image = pygame.image.load('Images//no_button.png')
arrow_up = pygame.image.load('Images//arrow_up.png')
arrow_right = pygame.image.load('Images//arrow_right.png')
arrow_left = pygame.image.load('Images//arrow_left.png')
exit_image = pygame.image.load('Images//Exit.png')

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

            Cube.image = red_cube
            choose_square = 0
            game = 1
            
        if blue_cube_rect.collidepoint(mouse_position) :
            window.blit(square,(Cube2.x-2.5, Cube2.y-2.5))
            
            Cube.image = blue_cube
            choose_square = 0
            game = 1
                
        if green_cube_rect.collidepoint(mouse_position) :
            window.blit(square,(Cube3.x-2.5, Cube3.y-2.5))
            
            Cube.image = green_cube
            choose_square = 0
            game = 1
        
        window.blit(TextSurf,(512, 284))         
        Cube1.display()
        Cube2.display()
        Cube3.display()
        pygame.display.flip()

    except pygame.error :
        break

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

blocks = [cube() for i in range(43)]

button_no_rect = no_button_image.get_rect(topleft = (755, 300))
button_yes_rect = yes_button_image.get_rect(topleft = (370, 300))

arrow_up_left_rect = arrow_up.get_rect(topleft = (70,254))
arrow_up_right_rect = arrow_up.get_rect(topleft = (1144,254))
arrow_right_rect = arrow_left.get_rect(topleft = (1214,324))
arrow_left_rect = arrow_right.get_rect(topleft = (0,324))

exit_rect = exit_image.get_rect(topleft = (0,0))

for x in range(len(blocks)) :
    blocks[x].image = purple_cube

start_ticks_total_time = pygame.time.get_ticks()
    
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
    start_ticks_level = pygame.time.get_ticks()

    for i in range(loop) :
        for j in range(length_blocks) :
            window.blit(purple_cube,(coordonees_block[i,j])) 
            pygame.display.flip()
            a+= 1
            blocks[a].x = coordonees_block[i,j][0]
            blocks[a].y = coordonees_block[i,j][1]
    
    a=0
    start_level = 1
            
    while start_level :
        total_time = (pygame.time.get_ticks()-start_ticks_total_time)/1000
        seconds_level = (pygame.time.get_ticks()-start_ticks_level)/1000
        
        for event in pygame.event.get() :
            if event.type == QUIT :
                pygame.quit()
                sys.exit()

            mouse_position = pygame.mouse.get_pos()   

            if event.type == MOUSEBUTTONDOWN:
            	if exit_rect.collidepoint(mouse_position):
            	    start_level = 0
            	    game = 0
            	    show_score = 1

            if button_no_rect.collidepoint(mouse_position) :
                if lose == 1 or lose_with_time == 1 :
                    if show_score == 0 :
                        start_level = 0
                        game = 0
                        pygame.quit()
                        sys.exit()

            if button_yes_rect.collidepoint(mouse_position) :
                if lose == 1 or lose_with_time == 1 :
                    if show_score == 0 :
                        level = 0
                        lose = 0
                        lose_with_time = 0
                        start_level = 0  
                        start_ticks_total_time = pygame.time.get_ticks()
             
            if event.type == MOUSEBUTTONDOWN :
                if arrow_left_rect.collidepoint(mouse_position) and lose == 0:
                    nb_movements = 0
                    for x in range(len(movement)) :
                        if movement[x] == 'left' :
                            nb_movements+=1 

                        if movement[x] != 'left' :
                            break

                    if nb_movements > 0 :
                        moove = 'left'

                    if moove == 'up' or moove == 'right' or movement[0] != 'left' :
                        lose = 1
                        show_score = 1

                if arrow_right_rect.collidepoint(mouse_position) and lose == 0 :
                    nb_movements = 0
                    for x in range(len(movement)) :
                        if movement[x] == 'right' :
                            nb_movements+=1      
                            
                        if movement[x] != 'right' :
                            break

                    if nb_movements > 0 :
                        moove = 'right'

                    if moove == 'up' or moove == 'left' or movement[0] != 'right':
                        lose = 1
                        show_score = 1
                
                if arrow_up_left_rect.collidepoint(mouse_position) or arrow_up_right_rect.collidepoint(mouse_position) and lose == 0 :
                    nb_movements = 0
                    for x in range(len(movement)) :
                        if movement[x] == 'up' :
                            nb_movements+=1

                        if movement[x] != 'up' :
                            break

                    if nb_movements > 0 :
                        moove = 'up'
                    
                    if moove == 'right' or moove == 'left' or movement[0] != 'up' :
                        lose = 1
                        show_score = 1
                        
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
            level+=1
            break

        window.blit(background,(200,0))

        window.blit(purple_cube,(642,618))

        for x in range(len(blocks)) :
            if x != 0 :
                blocks[x].display()

        if level == 0 :
            time_limit = 30

        if level == 1 :
            time_limit = 25

        if level == 2 :
            time_limit = 20

        if level == 3 :
            time_limit = 15

        if level == 4 :
            time_limit = 10

        if level >= 5 :
            
            time_limit = 9

        Cube.display()
        
        window.blit(arrow_up,(70,254))
        window.blit(arrow_up,(1144,254))
        window.blit(arrow_right,(1214,324))
        window.blit(arrow_left,(0,324))
        window.blit(exit_image,(0,0))
        #RED = (255, 0, 0)
        time_left = time_limit - seconds_level
        time_left = round(time_left, 2)
        
        ScoreSurf = fond.render('Levels Done : %s' %level, True, (255, 255, 255))
        if time_left - 5 <= 0 :
            TimeLimitSurf = fond.render('Time left : %s' %time_left, True, (255, 0, 0))

        else :
            TimeLimitSurf = fond.render('Time left : %s' %time_left, True, (255, 255, 255))

        if time_left <= 0 :
            lose = 1
            show_score = 1
            
        window.blit(ScoreSurf,(110,0))
        window.blit(TimeLimitSurf,(110,40))
        if lose == 1 and show_score == 0 :
            window.blit(background,(0,0))
            window.blit(Lost_animation,(350,200))
            window.blit(yes_button_image,(370,300))
            window.blit(no_button_image,(755,300))

        pygame.display.flip()

        if show_score == 1 :
            with open("TheCubeMobileScore.txt","r") as file :
                file = file.read()
                file = int(file)
                
            if level > file :
                with open("TheCubeMobileScore.txt","w") as file :
                    file.write(str(level))

                CongratsSurf = fond.render('Congrats ! You beat your score !', True, (255, 255, 255))
                best_score = 1

            with open("TheCubeMobileScore.txt","r") as file :
                file = file.read()
                file = int(file)
    
            BestScoreSurf = fond.render('Max Score : %s' %file, True, (255, 255, 255))
            ScoreSurf = fond.render('Levels Done : %s' %level, True, (255, 255, 255))
            TimeSurf = fond.render('Total Time : %s' %total_time, True, (255, 255, 255))
            window.blit(background,(0,0))
            if best_score == 1 :
                window.blit(CongratsSurf,(455, 0))
                
            window.blit(BestScoreSurf,(550, 280))
            window.blit(ScoreSurf, (550, 320))
            window.blit(TimeSurf, (550, 360))
            pygame.display.flip()
            time.sleep(4)
            show_score = 0
            best_score = 0
            
