import pygame
from sys import exit

pygame.init()
screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption('Runner')
clock = pygame.time.Clock()
test_font = pygame.font.Font('python/fonts/Stopbuck.ttf', 50)

sky_surface = pygame.image.load('python/graphics/sky1.jpeg').convert()
ground_surface = pygame.image.load('python/graphics/ground.png').convert_alpha()

text_surface = test_font.render('SCORE', False, 'Blue').convert()
text_rect = text_surface.get_rect(center = (400, 50))

snail_surf = pygame.image.load('python/graphics/snail/snail1.png')
snail_surface = pygame.transform.scale(snail_surf, (47, 34)).convert_alpha()
snail_rect = snail_surface.get_rect(midbottom = (600, 283))


player_surf = pygame.image.load('python/graphics/player/player1.png')
player_surface = pygame.transform.scale(player_surf, (60, 88)).convert_alpha()
player_rect = player_surface.get_rect(midbottom = (80, 284))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
##  if event.type == pygame.MOUSEMOTION:
##          if player_rect.collidepoint(event.pos): print("collllision.")
    
    screen.blit(sky_surface, (0,-150))
    screen.blit(ground_surface, (0, 260))
    screen.blit(text_surface, text_rect)

    pygame.draw.line(screen, "Black", (0, 0), (800, 400))

    screen.blit(player_surface, player_rect)
    snail_rect.x -= 4 
    if snail_rect.right < 0: snail_rect.left = 800

    screen.blit(snail_surface, snail_rect)

    mouse_pos = pygame.mouse.get_pos()

##    if (player_rect.collidepoint(mouse_pos)):
##        print("collision.") 

##    if (player_rect.colliderect(snail_rect)):
##        print("Collision.")

    

    pygame.display.update()
    clock.tick(60)




