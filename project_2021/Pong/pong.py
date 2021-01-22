#!/usr/bin/python3
#Ella Adam
#10/28/2020


'''This is a multiplayer pong game'''

#Import Section
import pygame
from paddles import Paddle

pygame.init()


# --- Define some colors ----
BLACK = (0,0,0)
WHITE = (255,255,255)

# --- Creating a new Window Screen ------

size = (700, 500)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Pong")

paddleA = Paddle(WHITE, 10, 100)
paddleA.rect.x = 20
paddleA.rect.y = 200
 
paddleB = Paddle(WHITE, 10, 100)
paddleB.rect.x = 670
paddleB.rect.y = 200

#This list will contain all sprites we intend to use
all_sprites_list = pygame.sprite.Group()

# Add the paddles to the list of sprites
all_sprites_list.add(paddleA)
all_sprites_list.add(paddleB)


# ---- Game loop untill user closes program ----
carryOn = True

# ---Clock for screen updates ----
clock = pygame.time.Clock()


# -------- Main Program Loop -----------
while carryOn:
    # --- Main Event Loop ---------
    for event in pygame.event.get(): #If the user did something
        if event.type == pygame.QUIT: #If the user closes the app
            carryOn = False #Stops the program
        elif event.type==pygame.KEYDOWN:
            if event.key==pygame.K_ESCAPE: #Pressing the ESC Key will quit the game
                carryOn=False        
    
    
    #Moving the paddles when the user uses the arrow keys (player A) or "W/S" keys (player B) 
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            paddleA.moveUp(6)
        if keys[pygame.K_s]:
            paddleA.moveDown(6)
        if keys[pygame.K_UP]:
            paddleB.moveUp(6)
        if keys[pygame.K_DOWN]:
            paddleB.moveDown(6)    
    
    # --- Game logic should go here --------
    all_sprites_list.update()
    
    # --- Drawing Code -----
    screen.fill(BLACK)
    #Drawing the Net
    pygame.draw.line(screen, WHITE, [349,0], [349, 500], 5)
    #Draw the sprites
    all_sprites_list.draw(screen) 
    
    
    # ---- Updating the Screen with the drawings ----
    pygame.display.flip()
    
    # --- Frames per Second -----
    clock.tick(60)

pygame.quit()