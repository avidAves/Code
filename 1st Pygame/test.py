import pygame
from sys import exit

pygame.init()

screen = pygame.display.set_mode((800,400))
pygame.display.set_caption("Test Game Wahoo Yipee!")
clock = pygame.time.Clock()
test_font = pygame.font.Font("1st Pygame/font/Pixeltype.ttf",50)

sky_surface = pygame.image.load('1st Pygame/graphics/Sky.png').convert()
ground_surface = pygame.image.load('1st Pygame/graphics/ground.png').convert()

score_surf = test_font.render("My game", False, "Black")
score_rect = score_surf.get_rect(center = (400,50))

snail_surf = pygame.image.load('1st Pygame/graphics/snail/snail1.png').convert_alpha()
snail_rect = snail_surf.get_rect(midbottom = (600,300))

player_surf = pygame.image.load('1st Pygame/graphics/Player/player_walk_1.png').convert_alpha()
player_rect = player_surf.get_rect(midbottom = (80,300))
player_gravity = 0

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        #Allows for both clicking on the player and hitting the spacebar to jump!
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if player_rect.bottom == 300:
                    player_gravity = -20
        if event.type == pygame.MOUSEBUTTONDOWN:
            if player_rect.collidepoint(event.pos):
                player_gravity = -20

    screen.blit(sky_surface,(0,0))
    screen.blit(ground_surface,(0,300))
    pygame.draw.rect(screen,"Pink",score_rect,0,6)
    screen.blit(score_surf,score_rect)

    #Player
    #Remember that y-inputs are reversed, so a positive value drags you down
    #Why? Who knows...
    player_gravity += 1
    player_rect.y += player_gravity
    #Hey, are you lower on the screen than 300? No sweat, we'll just pop you up to 300!
    if player_rect.bottom >= 300: player_rect.bottom = 300
    screen.blit(player_surf,player_rect)

    #Snail
    if snail_rect.right < 0: snail_rect.left = 800
    snail_rect.x -= 4
    screen.blit(snail_surf,snail_rect)

    pygame.display.update()
    clock.tick(60)
