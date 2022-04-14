import pygame
from pygame.locals import*
import sys
import random
import time

#variables#

start = 0
length_blocks = 2
loop=21
nb_movements = 0

coordonees_block = {}
corner_coordonees_cube_x = 0
corner_coordonees_cube_y = 0

movement = []

#variables#

pygame.init()

fond = pygame.font.Font('freesansbold.ttf',30)


TextSurf = fond.render('Choose your square', True, (255, 255, 255))
PressStartSurf = fond.render('Press ESPACE to start', True, (255, 255, 255))

red_cube = pygame.image.load('C:\\Users\\Isabelle\\Documents\\PYTHON\\The_cube\\Images\\red_cube.jpg')
blue_cube = pygame.image.load('C:\\Users\\Isabelle\\Documents\\PYTHON\\The_cube\\Images\\blue_cube.jpg')
green_cube =  pygame.image.load('C:\\Users\\Isabelle\\Documents\\PYTHON\\The_cube\\Images\\green_cube.jpg')
purple_cube = pygame.image.load('C:\\Users\\Isabelle\\Documents\\PYTHON\\The_cube\\Images\\purple_cube.png')
square =  pygame.image.load('C:\\Users\\Isabelle\\Documents\\PYTHON\\The_cube\\Images\\square.png')
background =  pygame.image.load('C:\\Users\\Isabelle\\Documents\\PYTHON\\The_cube\\Images\\bg.png')
hide_text =  pygame.image.load('C:\\Users\\Isabelle\\Documents\\PYTHON\\The_cube\\Images\\hide_text.png')
arrival_flag =  pygame.image.load('C:\\Users\\Isabelle\\Documents\\PYTHON\\The_cube\\Images\\flag_arrival.png')

window = pygame.display.set_mode((1284, 648))
pygame.display.set_icon(red_cube)
pygame.display.set_caption('The Cube')

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

            if random_number == 1 and last_moove == 'up' or last_moove == 'left': #add a block on the left
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

while True :

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
                pygame.quit()
            
        if blue_cube_rect.collidepoint(mouse_position) :
            window.blit(square,(Cube2.x-2.5, Cube2.y-2.5))
            if event.type == MOUSEBUTTONDOWN :
                Cube.image = blue_cube
                pygame.quit()
                
        if green_cube_rect.collidepoint(mouse_position) :
            window.blit(square,(Cube3.x-2.5, Cube3.y-2.5))
            if event.type == MOUSEBUTTONDOWN :
                Cube.image = green_cube
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

while True :
    window.blit(background,(0,0))
    Cube.x = 642
    Cube.y = 618

    generate_random_map(coordonees_block, length_blocks, loop)
    

    for i in range(loop) :
        for j in range(length_blocks) :
            window.blit(purple_cube,(coordonees_block[i,j])) 
            pygame.display.flip()

            

    seconds = 0
            
    while True :

        for event in pygame.event.get() :
            if event.type == QUIT :
                pygame.quit()
                sys.exit()

        

            if event.type == KEYDOWN :
                if event.key == K_SPACE :
                    start = 1

                if event.key == K_LEFT and start == 1 :
                    nb_movements = 0
                    for x in range(len(movement)) :
                        if movement[x] == 'left' :
                            nb_movements+=1 

                        if movement[x] != 'left' :
                            break

                    if nb_movements > 0 :
                        for v in range(nb_movements) :
                            Cube.moove_left()

                        for i in range(nb_movements) :
                            movement.remove('left')

                        window.blit(purple_cube,(corner_coordonees_cube_x, corner_coordonees_cube_y))
                        corner_coordonees_cube_x = Cube.x
                        corner_coordonees_cube_y = Cube.y


                if event.key == K_RIGHT and start == 1 :
                    nb_movements = 0
                    for x in range(len(movement)) :
                        if movement[x] == 'right' :
                            nb_movements+=1      
                            
                        if movement[x] != 'right' :
                            break

                    if nb_movements > 0 :
                        for v in range(nb_movements) :
                            Cube.moove_right()

                        for i in range(nb_movements) :
                            movement.remove('right')
                            
                        window.blit(purple_cube,(corner_coordonees_cube_x, corner_coordonees_cube_y))
                        corner_coordonees_cube_x = Cube.x
                        corner_coordonees_cube_y = Cube.y

                if event.key == K_UP and start == 1 :
                    nb_movements = 0
                    for x in range(len(movement)) :
                        if movement[x] == 'up' :
                            nb_movements+=1

                        if movement[x] != 'up' :
                            break

                    if nb_movements > 0 :
                        for v in range(nb_movements) :
                            Cube.moove_up()

                        for i in range(nb_movements) :
                            movement.remove('up')
                            
                        window.blit(purple_cube,(corner_coordonees_cube_x, corner_coordonees_cube_y))
                        corner_coordonees_cube_x = Cube.x
                        corner_coordonees_cube_y = Cube.y
                  

        if movement == [] :
            #str(seconds)
            #print("Votre temps est de",seconds*2.5,"secondes")
            break
       
        window.blit(PressStartSurf,(0,0))    
    
        if start == 1 :
            window.blit(hide_text,(0,0))
        
        Cube.display()
        pygame.display.flip()
        time.sleep(0.001)
        
        if start == 1 :
            seconds+=0.001
   

            
        
