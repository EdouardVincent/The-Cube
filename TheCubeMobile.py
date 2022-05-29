#The Cube Mobile
#Author : Edouard Vincent

import pygame
from pygame.locals import*
import sys
import random
import time
from turtle import*
import ctypes
import math

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
leave = 0

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
arrow_right_image = pygame.image.load('Images//arrow_right.png')
arrow_left_image = pygame.image.load('Images//arrow_left.png')
exit_image = pygame.image.load('Images//Exit.png')

PURPLE  = (205, 65, 119)

#Images

class Sprite () :
    def __init__ (self) :
        self.x = 642
        self.y = 324
        self.image = red_cube
        self.color = (0,0,0)
        self.velocity = 30

    def scale_image (self, image) :
        user32 = ctypes.windll.user32
        screensize = user32.GetSystemMetrics(78), user32.GetSystemMetrics(79)

        width = image.get_width()
        height = image.get_height()

        new_w = (screensize[0]/1284)*width
        new_h = (screensize[1]/648)*height

        size = (math.trunc(new_w), math.trunc(new_h))
                                   
        return size

    def New_coords (self, x, y) :
        user32 = ctypes.windll.user32
        screensize = user32.GetSystemMetrics(78), user32.GetSystemMetrics(79)

        new_x = (screensize[0]/1284)*x
        new_y = (screensize[1]/648)*y
        new_coords = (math.trunc(new_x), math.trunc(new_y))
                                   
        return new_coords

    def assign_size_coords(self) :
        self.image = pygame.transform.scale(self.image,(Sprite.scale_image(self, self.image)))
        self.x = Sprite.New_coords(self, self.x, self.y)[0]
        self.y = Sprite.New_coords(self, self.x, self.y)[1]

    def display(self) :
        window.blit(self.image,(self.x, self.y))

    def display_surface(self) :
        pygame.draw.rect(window, self.color, pygame.Rect(self.x, self.y, 30, 30))

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

user32 = ctypes.windll.user32
screensize = user32.GetSystemMetrics(78), user32.GetSystemMetrics(79)

window = pygame.display.set_mode((screensize))
pygame.display.set_icon(red_cube)
pygame.display.set_caption('The Cube')


Menu = Sprite()
button_leave = Sprite()
button_tutorial = Sprite()
button_play = Sprite()

Menu.x = 0
Menu.y = 0
Menu.image = menu_image
Menu.assign_size_coords()


button_leave.x = 500
button_leave.y = 500
button_leave.image = button_leave_image
button_leave.assign_size_coords()

button_tutorial.x = 500
button_tutorial.y = 400
button_tutorial.image = button_tutorial_image
button_tutorial.assign_size_coords()

button_play.x = 500
button_play.y = 300
button_play.image = button_play_image
button_play.assign_size_coords()


button_leave_rect = button_leave.image.get_rect(topleft = (button_leave.x, button_leave.y))
button_tutorial_rect = button_tutorial.image.get_rect(topleft = (button_tutorial.x, button_tutorial.y))
button_play_rect = button_play.image.get_rect(topleft = (button_play.x, button_play.y))
      
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

    Menu.display()
    button_play.display()
    button_tutorial.display()
    button_leave.display()
    
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

Cube = Sprite()

Cube1 = Sprite()
Cube2 = Sprite()
Cube3 = Sprite()

Text = Sprite()

Cube1.x = 642
Cube1.y = 324
Cube1.image = red_cube
Cube1.assign_size_coords()

Cube2.x = 602
Cube2.y = 324
Cube2.image = blue_cube
Cube2.assign_size_coords()

Cube3.x = 682
Cube3.y = 324
Cube3.image = green_cube
Cube3.assign_size_coords()

Text.x = 512
Text.y = 284
Text.image = TextSurf
Text.assign_size_coords()


red_cube_rect = Cube1.image.get_rect(topleft = (Cube1.x, Cube1.y))
blue_cube_rect = Cube2.image.get_rect(topleft = (Cube2.x, Cube2.y))
green_cube_rect  = Cube3.image.get_rect(topleft = (Cube3.x, Cube3.y))

while choose_square :

    for event in pygame.event.get () :

        mouse_position = pygame.mouse.get_pos()   
        
        if event.type == QUIT :
            pygame.quit()
            sys.exit()

        

    try :
        window.fill((0,0,0))
        if event.type == MOUSEBUTTONDOWN :
            if red_cube_rect.collidepoint(mouse_position) :
                Cube.image = red_cube
                choose_square = 0
                game = 1
            
            if blue_cube_rect.collidepoint(mouse_position) :
                Cube.image = blue_cube
                choose_square = 0
                game = 1
                
            if green_cube_rect.collidepoint(mouse_position) :
                Cube.image = green_cube
                choose_square = 0
                game = 1
        
        Text.display()      
        Cube1.display()
        Cube2.display()
        Cube3.display()
        pygame.display.flip()

    except pygame.error :
        break

#instances# 

block = (Sprite() for i in range(43))

blocks = [Sprite() for i in range(43)]

arrow_up1 = Sprite()
arrow_up1.x = 70
arrow_up1.y = 254
arrow_up1.image = arrow_up
arrow_up1.assign_size_coords()

arrow_up2 = Sprite()
arrow_up2.x = 1144
arrow_up2.y = 254
arrow_up2.image = arrow_up
arrow_up2.assign_size_coords()

arrow_right = Sprite()
arrow_right.x = 1214
arrow_right.y = 324
arrow_right.image = arrow_right_image
arrow_right.assign_size_coords()

        
arrow_left = Sprite()
arrow_left.x = 0
arrow_left.y = 324
arrow_left.image = arrow_left_image
arrow_left.assign_size_coords()


exit_ = Sprite()
exit_.x = 0
exit_.y = 0
exit_.image = exit_image
exit_.assign_size_coords()

arrow_up_left_rect = arrow_up1.image.get_rect(topleft = (arrow_up1.x, arrow_up1.y))
arrow_up_right_rect = arrow_up2.image.get_rect(topleft = (arrow_up2.x, arrow_up2.y))
arrow_right_rect = arrow_right.image.get_rect(topleft = (arrow_right.x,arrow_right.y))
arrow_left_rect = arrow_left.image.get_rect(topleft = (arrow_left.x,arrow_left.y))

exit_rect = exit_.image.get_rect(topleft = (exit_.x, exit_.y))

#Some instances ...
Lost_animation_ = Sprite()
Lost_animation_.x = 350
Lost_animation_.y = 200
Lost_animation_.image = Lost_animation
Lost_animation_.assign_size_coords()

Yes_button = Sprite()
Yes_button.x = 370
Yes_button.y = 300
Yes_button.image = yes_button_image
Yes_button.assign_size_coords()

No_button = Sprite()
No_button.x = 755
No_button.y = 300
No_button.image = no_button_image
No_button.assign_size_coords()

button_no_rect = No_button.image.get_rect(topleft = (No_button.x, No_button.y))
button_yes_rect = Yes_button.image.get_rect(topleft = (Yes_button.x, Yes_button.y))

for x in range(len(blocks)) :
    blocks[x].image = purple_cube

start_ticks_total_time = pygame.time.get_ticks()

Cube.image = pygame.transform.scale(Cube.image,(Cube.scale_image(Cube.image)))
    
while game :

    movement = []

    try :
        window.blit(background,(0,0))
    except pygame.error :
        show_score = 1

    Cube.x = 642
    Cube.y = 618

    Cube.x = Cube.New_coords(Cube.x, Cube.y)[0]
    Cube.y = Cube.New_coords(Cube.x, Cube.y)[1]
    
    corner_coordonees_cube_x = Cube.x
    corner_coordonees_cube_y = Cube.y

    generate_random_map(coordonees_block, length_blocks, loop)
    start_ticks_level = pygame.time.get_ticks()

    for i in range(loop) :
        for j in range(length_blocks) :
            blocks[a].x = coordonees_block[i,j][0]
            blocks[a].y = coordonees_block[i,j][1]
            blocks[a].image = purple_cube
            blocks[a].assign_size_coords()
            blocks[a].display()
            pygame.display.flip()
            a+= 1
    
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
            	    leave = 1

            if button_no_rect.collidepoint(mouse_position) :
                if lose == 1 or lose_with_time == 1 :
                    if show_score == 0 :
                        start_level = 0
                        game = 0
                        pygame.quit()
                        sys.exit()

            if button_yes_rect.collidepoint(mouse_position) :
                if lose == 1 :
                    if show_score == 0 :
                        level = 0
                        lose = 0
                        start_ticks_total_time = pygame.time.get_ticks()
                        start_level = 0
                        start_ticks_level = pygame.time.get_ticks()
                        seconds_level = (pygame.time.get_ticks()-start_ticks_level)/1000
             
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
            Cube.velocity = Cube.scale_image(purple_cube)[1]
            Cube.moove_up()
            
        if moove == 'right' and nb_movements > 0 :     
            nb_movements-=1
            movement.remove('right')
            Cube.velocity = Cube.scale_image(purple_cube)[0]+1
            Cube.moove_right()

        if moove == 'left' and nb_movements > 0 :
            nb_movements-=1
            movement.remove('left')
            Cube.velocity = Cube.scale_image(purple_cube)[0]+1
            Cube.moove_left()

        if movement == [] :
            level+=1
            break

        window.fill((0,0,0))

        for f in range(len(blocks)) :
            if f != 0 :
                blocks[f].display()

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

        arrow_up1.display()
        arrow_up2.display()
        arrow_right.display()
        arrow_left.display()
        exit_.display()

        #RED = (255, 0, 0)
        time_left = time_limit - seconds_level
        time_left = round(time_left, 2)
        
        ScoreSurf = fond.render('Levels Done : %s' %level, True, (255, 255, 255))
        if time_left - 5 <= 0 :
            TimeLimitSurf = fond.render('Time left : %s' %time_left, True, (255, 0, 0))

        else :
            TimeLimitSurf = fond.render('Time left : %s' %time_left, True, (255, 255, 255))

        if time_left <= 0 and lose == 0 and show_score == 0 :
            lose = 1
            show_score = 1

        Score = Sprite()
        Time = Sprite()

        Score.x = 110
        Score.y = 0
        Score.image = ScoreSurf

        Time.x = 110
        Time.y = 40
        Time.image = TimeLimitSurf

        Score.assign_size_coords()
        Time.assign_size_coords()
        
        Score.display()
        Time.display()
        
        if lose == 1 and show_score == 0 :
            
            window.fill((0,0,0))

            Lost_animation_.display()
            Yes_button.display()
            No_button.display()

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

            Best_Score = Sprite()
            Best_Score.x = 550
            Best_Score.y = 280
            Best_Score.image = BestScoreSurf
            Best_Score.assign_size_coords()

            Score = Sprite()
            Score.x = 550
            Score.y = 320
            Score.image = ScoreSurf
            Score.assign_size_coords()

            Total_Time = Sprite()
            Total_Time.x = 550
            Total_Time.y = 360
            Total_Time.image = TimeSurf
            Total_Time.assign_size_coords()
            
            window.fill((0,0,0))
            if best_score == 1 :
                Congrats = Sprite()
                Congrats.x = 455
                Congrats.y = 0
                Congrats.image = CongratsSurf
                Congrats.assign_size_coords()
                Congrats.display()
                
            Best_Score.display()
            Score.display()
            Total_Time.display()
            pygame.display.flip()
            time.sleep(4)
            show_score = 0
            best_score = 0

        if leave == 1 :
            pygame.quit()
            sys.exit()
        
            
