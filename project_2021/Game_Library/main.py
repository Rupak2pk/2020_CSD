#!/usr/bin/python3
#Ella Adam
#1/15/2021

import pygame
from pygame.locals import *
import os

# Game Initialization
pygame.init()

# Center the Game Application
os.environ['SDL_VIDEO_CENTERED'] = '1'

# Game Resolution
screen_width=800
screen_height=600
screen=pygame.display.set_mode((screen_width, screen_height))

#Music for game
pygame.mixer.music.load('8_Bit_March.mp3')
pygame.mixer.music.set_endevent(pygame.constants.USEREVENT)
pygame.mixer.music.play()

# Text Renderer
def text_format(message, textFont, textSize, textColor):
    newFont=pygame.font.Font(textFont, textSize)
    newText=newFont.render(message, 0, textColor)

    return newText


# Colors
white=(255, 255, 255)
black=(0, 0, 0)
gray=(50, 50, 50)
red=(255, 0, 0)
green=(0, 255, 0)
blue=(0, 0, 255)
yellow=(255, 255, 0)

# Game Fonts
font = "Retro.ttf"


# Game Framerate
clock = pygame.time.Clock()
FPS=30

# Main Menu
def main_menu():
    menu = True
    selected ="start"
    while menu:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
                #If quit is not hit, loop music
            elif event.type == pygame.constants.USEREVENT:
                pygame.mixer.music.load('8_Bit_March.mp3')
                pygame.mixer.music.play()
            
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_UP:
                    selected="start"
                elif event.key==pygame.K_DOWN:
                    selected="quit"
                    
                if event.key==pygame.K_RETURN:
                    if selected=="start":
                        game_library()
                    if selected=="quit":
                        pygame.quit()
                        quit()

        # Main Menu UI
        
        #Screen (AKA Background) 
        screen.fill(black)
        
        title=text_format("OddBall Gaming", font, 90, green)
        
        if selected=="start":
            text_start=text_format("START", font, 75, blue)
        else:
            text_start = text_format("START", font, 75, white)
            
        if selected=="quit":
            text_quit=text_format("QUIT", font, 75, blue)
        else:
            text_quit = text_format("QUIT", font, 75, white)

        title_rect=title.get_rect()
        start_rect=text_start.get_rect()
        quit_rect=text_quit.get_rect()

        # Main Menu Text
        screen.blit(title, (screen_width/2 - (title_rect[2]/2), 80))
        screen.blit(text_start, (screen_width/2 - (start_rect[2]/2), 300))
        screen.blit(text_quit, (screen_width/2 - (quit_rect[2]/2), 360))
        pygame.display.update()
        clock.tick(FPS)
        
        #Title
        pygame.display.set_caption("OddBall Gaming")





#Game Selecting Screen
def game_library():
    #print("I'm switching screens!!!")
    
    library = True
    selected ="return"
    while library:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
                #If quit is not hit, loop music
            elif event.type == pygame.constants.USEREVENT:
                pygame.mixer.music.load('8_Bit_March.mp3')
                pygame.mixer.music.play()
            
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_UP:
                    selected="return"
                elif event.key==pygame.K_DOWN:
                    selected="battleship"
                elif event.key==pygame.K_DOWN:
                    selected="pong"                
                '''
                elif event.key==pygame.K_DOWN:
                    selected="quit" '''
                    
                if event.key==pygame.K_RETURN:
                    if selected=="return":
                        main_menu()
                    if selected=="battleship":
                        print("Switching to Battleship")
                    if selected=="pong":
                        print("Switching to Pong")                    
                    '''
                    if selected=="quit":
                        pygame.quit()
                        quit() '''

        # Main Menu UI
        
        #Screen (AKA Background) 
        screen.fill(black)
        
        title=text_format("SELECT A GAME", font, 90, green)
        
        if selected=="return":
            text_start=text_format("RETURN", font, 75, blue)
        else:
            text_start = text_format("RETURN", font, 75, white)
        '''        
        if selected=="quit":
            text_quit=text_format("QUIT", font, 75, blue)
        else:
            text_quit = text_format("QUIT", font, 75, white)'''
                    

        title_rect=title.get_rect()
        start_rect=text_start.get_rect()
        #quit_rect=text_quit.get_rect()

        # Main Menu Text
        screen.blit(title, (screen_width/2 - (title_rect[2]/2), 80))
        screen.blit(text_start, (screen_width/2 - (start_rect[2]/2), 300))
        #screen.blit(text_quit, (screen_width/2 - (quit_rect[2]/2), 360))
        pygame.display.update()
        clock.tick(FPS)
        
        #Title
        pygame.display.set_caption("Game Library")    
    

#Initialize the Game
print("\"This is a arrow key based selector\"")
main_menu()

pygame.quit()
quit()
