import pygame
import sys

pygame.init()

WIDTH=800
HEIGHT=600

RED=(255,0,0)
GREEN=(0,255,0)
BACKGROUND_COLOR=(0,0,0)

player_pos=[400,520]
player_size=50

screen=pygame.display.set_mode((WIDTH, HEIGHT))

game_over=False

while not game_over:

    for event in pygame.event.get():

        if event.type==pygame.QUIT:
            pygame.display.quit()
            sys.exit()
            
        if event.type==pygame.KEYDOWN:
            
            x=player_pos[0]
            y=player_pos[1]

            if event.key==pygame.K_LEFT:
                x-=30
            elif event.key==pygame.K_RIGHT:
                x+=30

            player_pos=[x,y]

    screen.fill((BACKGROUND_COLOR))            
    pygame.draw.rect(screen,GREEN,(player_pos[0],player_pos[1],player_size,player_size))

    pygame.display.update()
