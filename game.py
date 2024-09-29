import pygame
import random
import time
pygame.init()
screen = pygame.display.set_mode((650, 500))
pygame.display.set_caption("Snakes and Ladder")

#background
bckimg=pygame.image.load("./images/bckimg.jpg")
stg=pygame.image.load("./images/white.jpg")
arrow=pygame.image.load("./images/arrow.png")
bx=150
by=5

#players
r1=pygame.image.load("./images/redpin.png")
b1=pygame.image.load("./images/greenpin.png")

rx=100
ry=251

b1x=100
b1y=362

button=pygame.Rect(10,50,40,40)

font1=pygame.font.SysFont("comicsansms", 25)
font2=pygame.font.SysFont("comicsansms", 20)

def bck() :
    screen.blit(stg, (0,0))
    screen.blit(bckimg, (bx,by))
    screen.blit(arrow, (10,50))

def rplayer(x,y) :
    screen.blit(r1, (x,y))
def bplayer(x,y) :
    screen.blit(b1, (x,y))

def pickNumber():
    diceroll=random.randint(1,6)
    if diceroll==1:
        dice=pygame.image.load("./images/arrow.png")
    elif diceroll==2:
        dice=pygame.image.load("./images/arrow.png")
    elif diceroll==3:
        dice=pygame.image.load("./images/arrow.png")
    elif diceroll==4:
        dice=pygame.image.load("./images/d1.png")
    elif diceroll==5:
        dice=pygame.image.load("./images/d1.png")
    elif diceroll==6:
        dice=pygame.image.load("./images/dice.jpg")
    
    return(dice, diceroll)

def players():
    msg1=font1.render("Player 1", True, (255, 0, 0))
    screen.blit(msg1, [5, 251])
    msg2=font1.render("Player 2", True, (0, 0, 255))
    screen.blit(msg2, [5, 362])

def rollr():
    msg3=font2.render("Your Turn", True,(0,0,0))
    screen.blit(msg3, [25, 290])
def rollb():
    msg4=font2.render("Your Turn", True,(0,0,0))
    screen.blit(msg4, [25, 400])

#game loop
running=True
dice = None
diceroll = None
turn='red'
while running:
    screen.fill((0,255,195))
    bck()
    players()
    if turn=="red":
        rollr()
    else:
        rollb()

    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
        elif event.type==pygame.MOUSEBUTTONDOWN:
            mouse_pos=pygame.mouse.get_pos()
            if button.collidepoint(mouse_pos):
                pickNumber()
                dice,diceroll=pickNumber()
                screen.blit(dice, (10,40))
                print(diceroll)
            
            #player 1
            if pickNumber() and turn=='red':
                turn='blue'
                if diceroll==6 and rx == 100 and ry==251:
                    rx=152
                    ry=427
                    turn='red'

            elif pickNumber() and turn=='blue':
                turn='blue'
                if diceroll==6 and rx == 100 and ry==362:
                    b1x=162
                    b1y=450
                    turn='blue'
                
    rplayer(rx, ry)
    bplayer(b1x, b1y)
    pygame.display.update()
    time.sleep(1.3)
pygame.quit()
quit()


