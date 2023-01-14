import pygame
from sys import exit
from random import randint


def display_score():
    current_time = int(pygame.time.get_ticks()/1000) - start_time
    score_surf = test_font.render(f'Score: {current_time}', False, (64,64,64))
    score_rect = score_surf.get_rect(center = (400,50))
    screen.blit(score_surf, score_rect)
    return current_time

def obstacle_movement(obstacle_list):
    if obstacle_list:
        for obstacle_rect in obstacle_list:
            obstacle_rect.x -= 5
            if obstacle_rect.bottom == 300: screen.blit(snail_surf,obstacle_rect)
            else:
                screen.blit(fly_surf,obstacle_rect)
        obstacle_list = [obstacle for obstacle in obstacle_list if obstacle.x > -100]
        return obstacle_list
    else: return []

def collisions(player,obstacles):
    if obstacles:
        for obstacle_rect in obstacles:
            if player.colliderect(obstacle_rect): return False
    return True

pygame.init()

screen = pygame.display.set_mode((800,400))
pygame.display.set_caption("Test Game Wahoo Yipee!")
clock = pygame.time.Clock()
test_font = pygame.font.Font("1st Pygame/font/Pixeltype.ttf",50)
game_active = False
start_time = 0
score = 0

sky_surface = pygame.image.load('1st Pygame/graphics/Sky.png').convert()
ground_surface = pygame.image.load('1st Pygame/graphics/ground.png').convert()


#Obstacles
snail_surf = pygame.image.load('1st Pygame/graphics/snail/snail1.png').convert_alpha()
fly_surf = pygame.image.load('1st Pygame/graphics/Fly/Fly1.png').convert_alpha()

obstacle_rect_list = []

player_surf = pygame.image.load('1st Pygame/graphics/Player/player_walk_1.png').convert_alpha()
player_rect = player_surf.get_rect(midbottom = (80,300))
player_gravity = 0

#Intro Screen
player_stand = pygame.image.load('1st Pygame/graphics/Player/player_stand.png').convert_alpha()
player_stand = pygame.transform.rotozoom(player_stand,0,2)
player_stand_rect = player_stand .get_rect(center = (400,200))


#Timer Section :)
#Add plus one to each event to avoid reserved events
obstacle_timer = pygame.USEREVENT + 1
pygame.time.set_timer(obstacle_timer,900)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        #Allows for both clicking on the player and hitting the spacebar to jump!
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if player_rect.bottom == 300:
                    player_gravity = -20
                if game_active == False:
                    game_active = True
                    start_time = int(pygame.time.get_ticks()/1000)

        if event.type == pygame.MOUSEBUTTONDOWN:
            if player_rect.collidepoint(event.pos):
                player_gravity = -20

        #When the timer finishes, a new snail will spawn!
        if event.type == obstacle_timer and game_active == True:
            if randint(0,2):
                obstacle_rect_list.append(snail_surf.get_rect(midbottom = (randint(900,1300),300)))
            else:
                obstacle_rect_list.append(fly_surf.get_rect(midbottom = (randint(900,1300),210)))

    if game_active:
        screen.blit(sky_surface,(0,0))
        screen.blit(ground_surface,(0,300))
        score = display_score()

        #Player
        #Remember that y-inputs are reversed, so a positive value drags you down
        #Why? Who knows...
        player_gravity += 1
        player_rect.y += player_gravity
        #Hey, are you lower on the screen than 300? No sweat, we'll just pop you up to 300!
        if player_rect.bottom >= 300: player_rect.bottom = 300
        screen.blit(player_surf,player_rect)

        #Obstacle Movement
        obstacle_rect_list = obstacle_movement(obstacle_rect_list)

        #Collision
        game_active = collisions(player_rect,obstacle_rect_list)
    else:   
        screen.fill((94,129,162))
        #Empties the list to prevent telefraging on restart :)
        obstacle_rect_list.clear()
        player_rect.midbottom = 300
        player_gravity = 0
        post_surf = test_font.render(f'Your Score Was: {score}!',False,"Black")
        post_rect = post_surf.get_rect(center = (400,320))
        mess_surf = test_font.render("Press Space to Play!",False,"Black")
        mess_rect = mess_surf.get_rect(center = (400,350))
        screen.blit(player_stand,player_stand_rect)

        if score > 0:
            screen.blit(post_surf,post_rect)
        else:
            screen.blit(mess_surf,mess_rect)


    pygame.display.update()
    clock.tick(60)
