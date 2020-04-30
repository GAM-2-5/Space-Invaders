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
enemy_fire=0.0005
player_speed=4
fire_rate=0.5

player_lives=3
score=0

font=pygame.font.Font("freesansbold.ttf",32)
score_font=pygame.font.Font("freesansbold.ttf",20)
wave=1



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

EbulletImg=pygame.image.load('enemy bullet.png')
EbulletImgRect=EbulletImg.get_rect()

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
            text=font.render("wave "+str(wave),True,(255,255,255))
            textrect=text.get_rect()
            textrect.center=(400,300)
            screen.blit(text,textrect)
            pygame.display.update()
            pygame.mixer.music.load("next_level.wav")
            pygame.mixer.music.play(1)
            time.sleep(2)
            pygame.mixer.music.load("level_music.mp3")
            pygame.mixer.music.play(-1)
                        
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

                if event.key==pygame.K_SPACE and time.time()-fire_rate>fire_time:
                    friendly_bullet.append([player_pos[0]+16,player_pos[1]-10])
                    fire_time=time.time()

                if event.key==pygame.K_LEFT:
                    left=True
                elif event.key==pygame.K_RIGHT:
                    right=True

                                  
        if left and player_pos[0]>=10:
            player_pos[0]=player_pos[0]-player_speed
        elif right and player_pos[0]<=760:
            player_pos[0]=player_pos[0]+player_speed

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
                
        for i in range(len(enemy)):
            if random.random()<enemy_fire:
                enemy_bullet.append([enemy[i][0]+32,enemy[i][1]+16])
                
        for i in range(len(enemy_bullet)):
            enemy_bullet[i][1]+=8
        for i in enemy_bullet:
            if i[1]>=616:
                enemy_bullet.remove(i)

        dead_enemy=[]
        dead_Fbullet=[]
        dead_Ebullet=[]

        for i in range(len(friendly_bullet)):
            for n in range(len(enemy)):
                if friendly_bullet[i][1]>=enemy[n][1] and friendly_bullet[i][1]<=(enemy[n][1]+32) and ((friendly_bullet[i][0]>=enemy[n][0] and friendly_bullet[i][0]<=(enemy[n][0]+32))or(friendly_bullet[i][0]+5>=enemy[n][0] and friendly_bullet[i][0]+5<=(enemy[n][0]+32))):
                    dead_enemy.append(n)
                    dead_Fbullet.append(i)
                    score+=50

        for i in range(len(dead_Fbullet)):
            friendly_bullet.pop(dead_Fbullet[i])

        for i in range(len(dead_enemy)):
            enemy.pop(dead_enemy[i])

        if len(enemy)==0:
            start=True
            wave+=1
            enemy_speed*=1.20
            enemy_fire*=1.20
            fire_rate*=0.85
            player_speed*=1.20
            enemy_fire*=1.20
            


        for i in range(len(enemy_bullet)):
            if enemy_bullet[i][1]>=player_pos[1] and enemy_bullet[i][1]<=(player_pos[1]+32) and ((enemy_bullet[i][0]>=player_pos[0] and enemy_bullet[i][0]<=(player_pos[0]+32))or(enemy_bullet[i][0]+5>=player_pos[0] and enemy_bullet[i][0]+5<=(player_pos[0]+32))):
                player_lives-=1
                dead_Ebullet.append(i)
                if player_lives==0:
                    pygame.mixer.music.load("death_sound.mp3")
                    pygame.mixer.music.play(1)
                    time.sleep(1)
                    pygame.display.quit()
                    sys.exit()

        for i in range(len(dead_Ebullet)):
            enemy_bullet.pop(dead_Ebullet[i])
            
                
        
               
        screen.fill((BACKGROUND_COLOR))
        screen.blit(playerImg,player_pos)
        for i in range(len(friendly_bullet)):
            screen.blit(bulletImg,friendly_bullet[i])
        for i in range(len(enemy)):
            screen.blit(enemyImg,enemy[i])
        for i in range(len(enemy_bullet)):
            screen.blit(EbulletImg,enemy_bullet[i])
        text=score_font.render(str(score),True,(255,255,255))
        textRect=text.get_rect()
        textRect.center=(20,20)
        screen.blit(text,textRect)
        if player_lives>0:
            screen.blit(playerImg,(760,10))
        if player_lives>1:
            screen.blit(playerImg,(720,10))
        if player_lives>2:
            screen.blit(playerImg,(680,10))
        pygame.display.update()
