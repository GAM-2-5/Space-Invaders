import pygame
import sys
import time
import random

pygame.init()

WIDTH=800
HEIGHT=600

RED=(255,0,0)
GREEN=(0,255,0)
BACKGROUND_COLOR=(0,0,0)

fire_time=0.00
tick_time=0.00
enemy_down=0
enemy_left=0
enemy_right=20

playerImg=pygame.image.load('ship.png')
playerImgRect=playerImg.get_rect()
player_pos=[370,550]
left=False
right=False

enemyImg=pygame.image.load('enemy 1.png')
enemyImgRect=enemyImg.get_rect()
enemy_pos=[370,100]

bulletImg=pygame.image.load('bullet.png')
bulletImgRect=bulletImg.get_rect()

friendly_bullet=[]
enemy_bullet=[]
enemy=[]


pygame.display.set_caption("Space Invaders")
screen=pygame.display.set_mode((WIDTH, HEIGHT))

game_over=False
start=True

while not game_over:

    if time.time()-1/30>=tick_time:
        tick_time=time.time()

        if start:     
            player_pos=[370,550]
            start=False
            for i in range(4):
                for n in range(9):
                    enemy.append([170+50*n,50+56*i])

            enemy_down=0
            enemy_left=0
            enemy_right=100
            enemy_speed=1

        for event in pygame.event.get():
        

            if event.type==pygame.QUIT:
                pygame.display.quit()
                sys.exit()
            if event.type==pygame.KEYUP:
                if event.key==pygame.K_LEFT:
                    left=False
                elif event.key==pygame.K_RIGHT:
                    right=False
            if event.type==pygame.KEYDOWN:

                if event.key==pygame.K_SPACE and time.time()-0.5>fire_time:
                    friendly_bullet.append([player_pos[0]+16,player_pos[1]-10])
                    fire_time=time.time()

                if event.key==pygame.K_LEFT:
                    left=True
                elif event.key==pygame.K_RIGHT:
                    right=True

                                  
        if left and player_pos[0]>=10:
            player_pos[0]=player_pos[0]-4
        elif right and player_pos[0]<=760:
            player_pos[0]=player_pos[0]+4

        for i in range(len(friendly_bullet)):
            friendly_bullet[i][1]-=18
        for i in friendly_bullet:
            if i[1]<=0:
                friendly_bullet.remove(i)

        if enemy_down>0:
            enemy_down-=enemy_speed
            for i in range(len(enemy)):
                enemy[i][1]+=enemy_speed
            if enemy_down<=0:
                if direction:
                    enemy_right=200
                else:
                    enemy_left=200

        if enemy_right>0:
            enemy_right-=enemy_speed
            for i in range(len(enemy)):
                enemy[i][0]+=enemy_speed
            if enemy_right<=0:
                enemy_down=32
                direction=False
                
        if enemy_left>0:
            enemy_left-=enemy_speed
            for i in range(len(enemy)):
                enemy[i][0]-=enemy_speed
            if enemy_left<=0:
                enemy_down=32
                direction=True


        dead_enemy=[]
        dead_Fbullet=[]

        for i in range(len(friendly_bullet)):
            for n in range(len(enemy)):
                if friendly_bullet[i][1]>=enemy[n][1] and friendly_bullet[i][1]<=(enemy[n][1]+32) and ((friendly_bullet[i][0]>=enemy[n][0] and friendly_bullet[i][0]<=(enemy[n][0]+32))or(friendly_bullet[i][0]+5>=enemy[n][0] and friendly_bullet[i][0]+5<=(enemy[n][0]+32))):
                    dead_enemy.append(n)
                    dead_Fbullet.append(i)

        for i in range(len(dead_Fbullet)):
            friendly_bullet.pop(dead_Fbullet[i])

        for i in range(len(dead_enemy)):
            enemy.pop(dead_enemy[i])
                
        
               
        screen.fill((BACKGROUND_COLOR))
        screen.blit(playerImg,player_pos)
        for i in range(len(friendly_bullet)):
            screen.blit(bulletImg,friendly_bullet[i])
        for i in range(len(enemy)):
            screen.blit(enemyImg,enemy[i])
        pygame.display.update()
