# Here is a game called "Escape Eskom"!
# You must escape Eskom otherwise you will be subject to stage 27 loadshedding!

import pygame
import random

pygame.init()

screen_width = 1024
screen_height = 677
screen = pygame.display.set_mode((screen_width,screen_height))

# Below are the images of the characters in the game:

player = pygame.image.load("eskomRunner.JPG")
enemy = pygame.image.load("eskomEnemy.JPG")   # I use the same picture for the "enemies" however they all have differet starting points and speeds at which they move
enemy2 = pygame.image.load("eskomEnemy2.JPG")
enemy3 = pygame.image.load("eskomEnemy3.JPG")
enemy4 = pygame.image.load("eskomEnemy4.JPG")
prize = pygame.image.load("eskomBulb.JPG")
background = pygame.image.load("eskomPlant.png").convert() #this is the background image of the game

# Collectiing the sizes of the images:

player_height = player.get_height()
player_width = player.get_width()
enemy_height = enemy.get_height()
enemy_width = enemy.get_width()
enemy2_height = enemy2.get_height()
enemy2_width = enemy2.get_width()
enemy3_height = enemy3.get_height()
enemy3_width = enemy3.get_width()
enemy4_height = enemy4.get_height()
enemy4_width = enemy4.get_width()
prize_height = prize.get_height()
prize_width = prize.get_width()

# Setting the starting points for all images on the screen:

playerXPosition = 50
playerYPosition = 50
enemyXPosition = screen_width                                     # Two of my enemies start somewhere randonly on the y-axis
enemyYPosition = random.randint(0, screen_height - enemy_height)  # The other enemies start in specific y-positions to "force" the user to move their character down
enemy2XPosition = screen_width                                    # This makes each game more unpredictable each time you play but still manages to "direct" the user
enemy2YPosition = random.randint(0, screen_height - enemy2_height)  
enemy3XPosition = screen_width                               
enemy3YPosition = 500
enemy4XPosition = screen_width                                      
enemy4YPosition = 200
prizeXPosition = screen_width - prize_width
prizeYPosition = screen_height - prize_height

# Set key booleans:

keyUp = False
keyDown = False
keyLeft = False
keyRight = False


# Now we set the game loop and call images onto the screen:

while 1:
    
    screen.blit(background, [0, 0])     # Background image here
    screen.blit(player, (playerXPosition, playerYPosition))
    screen.blit(enemy, (enemyXPosition, enemyYPosition))
    screen.blit(enemy2, (enemy2XPosition, enemy2YPosition))
    screen.blit(enemy3, (enemy3XPosition, enemy3YPosition))
    screen.blit(enemy4, (enemy4XPosition, enemy4YPosition))
    screen.blit(prize, (prizeXPosition, prizeYPosition))

    pygame.display.flip()

    for event in pygame.event.get():
    
        if event.type == pygame.QUIT:
            pygame.quit()
            break                        # I add "break" in here to stop an error message I get without it (Stack Overflow helped)
            
        if event.type == pygame.KEYDOWN: # This checks if a direction key was pressed and if it is the one we want
            if event.key == pygame.K_UP:
                keyUp = True
            if event.key == pygame.K_DOWN:
                keyDown = True
            if event.key == pygame.K_LEFT:  
                keyLeft = True              
            if event.key == pygame.K_RIGHT: 
                keyRight = True                 
            
        if event.type == pygame.KEYUP: # This does the same as above except checks whether a direction is not being pressed
            if event.key == pygame.K_UP:
                keyUp = False
            if event.key == pygame.K_DOWN:
                keyDown = False
            if event.key == pygame.K_LEFT:  
                keyLeft = False             
            if event.key == pygame.K_RIGHT: 
                keyRight = False
            
# Now the user can move the player around on the x/y-axis:

    if keyUp == True:
        if playerYPosition > 0:
            playerYPosition -= 1
    if keyDown == True:
        if playerYPosition < screen_height - player_height:
            playerYPosition += 1
    if keyLeft == True:                     
        if playerXPosition > 0:
            playerXPosition -= 1
    if keyRight == True:           
        if playerXPosition < screen_width - player_height:
            playerXPosition += 1


# This ensures that the object boxes stay with the characters when they move around:

    playerBox = pygame.Rect(player.get_rect())
    playerBox.top = playerYPosition
    playerBox.left = playerXPosition

    enemyBox = pygame.Rect(enemy.get_rect())
    enemyBox.top = enemyYPosition
    enemyBox.left = enemyXPosition

    enemy2Box = pygame.Rect(enemy2.get_rect()) 
    enemy2Box.top = enemy2YPosition
    enemy2Box.left = enemy2XPosition

    enemy3Box = pygame.Rect(enemy3.get_rect())  
    enemy3Box.top = enemy3YPosition
    enemy3Box.left = enemy3XPosition

    enemy4Box = pygame.Rect(enemy4.get_rect())  
    enemy4Box.top = enemy4YPosition
    enemy4Box.left = enemy4XPosition

    prizeBox = pygame.Rect(prize.get_rect())   
    prizeBox.top = prizeYPosition
    prizeBox.left = prizeXPosition

# Here we set the conditions for losing/winning the game:

    if playerBox.colliderect(enemyBox):
        print("You lose!")
        pygame.quit()
        break
    if playerBox.colliderect(enemy2Box):   
        print("You lose!")
        pygame.quit()
        break
    if playerBox.colliderect(enemy3Box):    
        print("You lose!")
        pygame.quit()
        break
    if playerBox.colliderect(enemy4Box):
        print("You lose")
        pygame.quit()
        break
    if playerBox.colliderect(prizeBox):    
        print("You did it! You have electricity!")
        pygame.quit()
        break

# The below ensures that if all the enemies make it off the screen, the hero wins even if he hasn't touched the prize:

    if enemyXPosition < 0 - enemy_width:
        if enemy2XPosition < 0 - enemy2_width:
            if enemy3XPosition < 0 - enemy3_width:
                if enemy4XPosition < 0 - enemy4_width:
                    print("You did it! You have electricity!")
                    pygame.quit()
                    break

# Lastly, the enemies all come at different speeds to make it more unpredictable! :D

    enemyXPosition -= 1.2
    enemy2XPosition -= 0.9
    enemy3XPosition -= 0.9
    enemy4XPosition -= 0.8
