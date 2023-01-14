import pygame
from sys import exit

pygame.init()

screen = pygame.display.set_mode((800,400))
pygame.display.set_caption("Test Game Wahoo Yipee!")
clock = pygame.time.Clock()
test_font = pygame.font.Font("1st Pygame/font/Pixeltype.ttf",50)

sky_surface = pygame.image.load('1st Pygame/graphics/Sky.png')
ground_surface = pygame.image.load('1st Pygame/graphics/ground.png')
text_surface = test_font.render("My game", False, "Black")

snail_surface = pygame.image.load('1st Pygame/graphics/snail/snail1.png')
#No need for a snail y position, since it doesn't move up and down
snail_x_pos = 600


while True:
    #Checks for pygame events, lets the user close the window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    
    #Displays the test surface
    screen.blit(sky_surface,(0,0))
    screen.blit(ground_surface,(0,300))
    screen.blit(text_surface,(300,50))
    #Makes snail move to the left
    snail_x_pos -= 6
    #If snail moves off screen, this teleports it back to the right side, slightly off screen
    if snail_x_pos <= -100:
        snail_x_pos = 900
    screen.blit(snail_surface,(snail_x_pos,250))
    #Updates the screen at a max rate of 60fps

    pygame.display.update()
    clock.tick(60)


