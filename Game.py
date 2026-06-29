import pygame,sys,time
import pygame.locals as GAMES_GLOBALS
import pygame.event as GAME_EVENTS
from tkinter.messagebox import showinfo
pygame.init()

width,height = 800,600
window = pygame.display.set_mode((width,height))
pygame.display.set_caption("Ping Pong")

# /// Variables \\\
ball = pygame.Rect(width//2-15,height//2-15,30,30)
ball_SY = 4
ball_SX = 4
player1 = pygame.Rect(20,height//2-70,10,140)#LEFT
player2 = pygame.Rect(width-30,height//2-70,10,140)#RIGHT
player1_score = 0
player2_score = 0
font_score = pygame.font.Font(None,30)
speed_ball = 97
# \\\ Variables ///

while True:
    for event in GAME_EVENTS.get():
        if event.type == GAMES_GLOBALS.QUIT:
            pygame.quit()
            sys.exit()

    ball.x+=ball_SX
    ball.y+=ball_SY

    if ball.top<=0 or ball.bottom>=height:
        ball_SY *= -1

    keys = pygame.key.get_pressed()

    if keys[pygame.K_w] and player1.top>0:
        player1.y -= 5
    if keys[pygame.K_s] and player1.bottom<height:
        player1.y += 5
    if keys[pygame.K_UP] and player2.top>0:
        player2.y -= 5
    if keys[pygame.K_DOWN] and player2.bottom<height:
        player2.y += 5

    if ball.colliderect(player1) or ball.colliderect(player2):
        ball_SX *= -1

    if ball.left <= 0:
        player2_score += 1
        ball.x = width//2-15
        ball.y = height//2-15
        ball_SX *= -1
    if ball.right >= width:
        player1_score += 1
        ball.x = width//2-15
        ball.y = height//2-15
        ball_SX *= -1

    if player1_score == 10:
        time.sleep(0.3)
        showinfo("Winner !", "Red player is the winner")
        pygame.quit()
        sys.exit()
    if player2_score == 10:
        time.sleep(0.5)
        showinfo("Winner !", "Blue player is the winner")
        pygame.quit()
        sys.exit()

    if player1_score >= 5 or player2_score >= 5:
        speed_ball = 135

    window.fill((0,190,0))
    pygame.draw.aaline(window,(255,255,255),(width//2,0),(width//2,height))
    text1 = font_score.render('Red player score : ' + str(player1_score),True,(255,0,0))
    text2 = font_score.render('Blue player score : ' + str(player2_score),True,(0,0,255))
    pygame.draw.ellipse(window,(255,255,255),ball)
    pygame.draw.rect(window,(255,0,0),player1)
    pygame.draw.rect(window,(0,0,255),player2)
    window.blit(text2,(width*3//4-20,20))
    window.blit(text1,(width//4-20,20))

    pygame.display.update()
    pygame.time.Clock().tick(speed_ball)
