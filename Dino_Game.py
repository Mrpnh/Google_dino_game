#importing pygame

import pygame
import time
import random

# Initialising pygame

pygame.init()
pygame.mixer.init()
pygame.mixer.music.load("point.mp3")

# Screen variables

screenW=1200
screenH=300

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
bg=pygame.transform.scale(bg,(screenW,screenH))
cactus=[pygame.image.load("cactus_1.png"),pygame.image.load("cactus_2.png")]
dino=[pygame.image.load("dino_1.png"),pygame.image.load("dino_3.png"),pygame.image.load("dino_2.png"),pygame.image.load("dino_4.png")]
bird=[pygame.image.load("bird_2.png"),pygame.image.load("bird_3.png")]

for i in range(2):
    bird[i]=pygame.transform.scale(bird[i],(64,64))

for i in range(4):
    dino[i]=pygame.transform.scale(dino[i],(80,80))


# regame loop

def regame(bgfinal,dino_x,dino_y,cactus_x,cactus_y,dino_index,current_cactus):
    restart=False
    while not restart:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
            if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_SPACE:
                        restart=True
        gameWindow.blit(bg,(bgfinal,0))
        gameWindow.blit(dino[dino_index%4],(dino_x,dino_y))
        gameWindow.blit(current_cactus,(cactus_x,cactus_y))
        pygame.display.update()
        clock.tick(100)
    gameloop()

#gameloop

def gameloop():
    #Gaming variables
    bgfinal=0
    bird_x=1300
    bird_y=0     
    bird_index=0
    cactus_x=1300
    cactus_y=140 
    current_cactus=random.choice(cactus)
    dino_x=90
    dino_y=160
    dino_index=0
    score=0
    reset=0
    jumpCount=10
    isJump=False
    neg=1
    exit_game=False   
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
        bgfinal-=7
        gameWindow.blit(bg,(bgfinal-bg.get_width(),0))
        
        # cactus running
        
        gameWindow.blit(current_cactus,(cactus_x,cactus_y))
        cactus_x-=7 # cactus speed

        # cactus random choice

        if cactus_x<0:
            current_cactus=random.choice(cactus)
            cactus_x=1300

        # Text on window 

        textRender("Score:"+str(score),(0,0,0),20,30,32)
        
        # score

        reset+=1
        if reset==100:
            score+=1
            reset=0
        
        # bird running

        bird_index+=1
        bird_x-=7

        # dino jumping

        if isJump:
            if jumpCount >=-10:
                neg=1
                if jumpCount<0:
                    neg=-1
                dino_y-= (jumpCount**2)*0.7*neg
                jumpCount-=1
                dino_x+=4
            else:
                isJump=False
                jumpCount=10
                dino_x=90

        # cactus crash
            
        if dino_x==cactus_x-6:
            break
        
        # bird crash

        if dino_y==bird_y and dino_x==bird_x-6:
           break

        # bird show
        if score>10:
            gameWindow.blit(bird[bird_index%2],(bird_x,bird_y))
        
        gameWindow.blit(dino[dino_index%4],(dino_x,dino_y))
        dino_index+=1
    
        if score%random.choice([10,20,100,40,80,50,60])==0:
            if bird_x<0:
                bird_x=1300
                bird_y=random.choice([160,60])
        
        pygame.display.update()
        clock.tick(100)

    regame(bgfinal,dino_x,dino_y,cactus_x,cactus_y,dino_index,current_cactus)

# main function

if __name__ == '__main__':
    gameloop()
    pygame.quit()
    quit()
