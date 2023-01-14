import pygame
from sys import exit

pygame.init()

screen = pygame.display.set_mode((800,400))
pygame.display.set_caption("Test Game Wahoo Yipee!")
clock = pygame.time.Clock()
test_font = pygame.font.Font("1st Pygame/font/Pixeltype.ttf",50)

sky_surface = pygame.image.load('1st Pygame/graphics/Sky.png').convert()
ground_surface = pygame.image.load('1st Pygame/graphics/ground.png').convert()
text_surface = test_font.render("My game", False, "Black")


snail_surface = pygame.image.load('1st Pygame/graphics/snail/snail1.png').convert_alpha()
snail_rect = snail_surface.get_rect(midbottom = (600,300))

player_surf = pygame.image.load('1st Pygame/graphics/Player/player_walk_1.png').convert_alpha()
player_rect = player_surf.get_rect(midbottom = (80,300))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    
    screen.blit(sky_surface,(0,0))
    screen.blit(ground_surface,(0,300))
    screen.blit(text_surface,(300,50))
    screen.blit(player_surf,player_rect)

    if snail_rect.right < 0:
        snail_rect.left = 800
    snail_rect.left -= 4
    screen.blit(snail_surface,snail_rect)
    #Updates the screen at a max rate of 60fps

    pygame.display.update()
    clock.tick(60)
