#importing pygame

import pygame
import time
import random

# Initialising pygame

pygame.init()
pygame.mixer.init()
pygame.mixer.music.load("point.mp3")
#Game variables

screenW=1000
screenH=400
exit_game=False

# Rendering Text

def textRender(text,color,x,y,text_size):
     font=pygame.font.SysFont(None,text_size)
     screenText=font.render(text,True,color)
     gameWindow.blit(screenText,(x,y))

#Window Initialisation

gameWindow=pygame.display.set_mode((screenW,screenH))
pygame.display.set_caption("Dino Run")
clock=pygame.time.Clock()

#Loading Images

bg=pygame.image.load("Dino_run.jpg").convert()
bg=pygame.transform.scale(bg,(800,500))
cactus=[pygame.image.load("cactus_1.png"),pygame.image.load("cactus_2.png")]
dino=[pygame.image.load("dino_1.png"),pygame.image.load("dino_3.png"),pygame.image.load("dino_2.png"),pygame.image.load("dino_4.png")]
bird=[pygame.image.load("bird_2.png"),pygame.image.load("bird_3.png")]

for i in range(2):
    cactus[i]=pygame.transform.scale(cactus[i],(50,110))

for i in range(2):
    bird[i]=pygame.transform.scale(bird[i],(64,64))

for i in range(4):
    dino[i]=pygame.transform.scale(dino[i],(80,80))

#Gaming variables
bgfinal=0
cactus_x=900
bird_x=900
bird_y=0     
current_cactus=random.choice(cactus)
score=0
reset=0
bird_index=0
dino_index=0
dino_y=320
jumpCount=13
isJump=False
neg=1
#gameloop

while not exit_game:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            exit_game=True
            break
        if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_SPACE:
                    isJump=True
                    pygame.mixer.music.play()

    # background running
    
    bgfinal=bgfinal%bg.get_width()
    gameWindow.blit(bg,(bgfinal,0))
    bgfinal-=5
    gameWindow.blit(bg,(bgfinal-bg.get_width(),0))
    
    # cactus running
    
    gameWindow.blit(current_cactus,(cactus_x,290))
    cactus_x-=5

    if cactus_x<0:
        current_cactus=random.choice(cactus)
        cactus_x=900

    # Text on window 
    textRender("Score:"+str(score),(0,0,0),20,30,32)
    
    reset+=1
    if reset==100:
        score+=1
        reset=0
    
    bird_index+=1
    bird_x-=6

    if isJump:
        if jumpCount >=-13:
            neg=1
            if jumpCount<0:
                neg=-1
            dino_y-= (jumpCount**2)*0.4*neg
            jumpCount-=1
        else:
            isJump=False
            jumpCount=13
        


    if score>5:
        gameWindow.blit(bird[bird_index%2],(bird_x,bird_y))
    
    gameWindow.blit(dino[dino_index%4],(40,dino_y))
    dino_index+=1
   
    if score%random.choice([10,20,100,40,80,50,60])==0:
        if bird_x<0:
            bird_x=900
            bird_y=random.choice([160,300])
    
    pygame.display.update()
    clock.tick(80)

pygame.quit()
