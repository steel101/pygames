import pygame, sys, os
from pygame.locals import *

# Game Initialization
pygame.mixer.pre_init(frequency=22050, size=-16, channels=2, buffer=4096)
pygame.init()

# Center the Game Application
os.environ['SDL_VIDEO_CENTERED']='1'


# Game Resolution
screen_width=800
screen_height=600
screen=pygame.display.set_mode((screen_width, screen_height))

# Initialize Sound Files
sound=pygame.mixer.Sound('sounds/sound.wav')
sound.set_volume(.5)

# Color
black=(0, 0, 0)
white=(255, 255, 255)
blue=(0, 0, 255)

# Fonts
font="font/Arcade Future.otf"

# Framerate
clock=pygame.time.Clock()
fps=200

# Initial Variables
lineWidth=10
paddleSize=50
paddleOffset=20


# Text Renderer
def text_format(text, textFont, textSize, textColor):
    font=pygame.font.Font(textFont, textSize)
    newText=font.render(text, 0, textColor)
    return newText


def BackgroundGameplay():
    screen.fill(black)
    pygame.draw.line(screen, white, ((screen_width / 2), 0), ((screen_width / 2), screen_height), 2)
    pygame.draw.rect(screen, blue, ((0, 0), (screen_width, screen_height)), lineWidth)

def Paddle(paddle):
    if paddle.bottom > screen_height - lineWidth:
        paddle.bottom = screen_height - lineWidth
    elif paddle.top < lineWidth:
        paddle.top = lineWidth

    pygame.draw.rect(screen, white, paddle)

def Ball(ball):
    pygame.draw.rect(screen, white, ball)

def BallMovement(ball, ballDirX, ballDirY):
    ball.x += ballDirX
    ball.y += ballDirY
    return ball

def WallCollision(ball, ballDirX, ballDirY):
    if ball.top == (lineWidth) or ball.bottom == (screen_height - lineWidth):
        ballDirY = ballDirY * -1
    if ball.left == (lineWidth) or ball.right == (screen_width - lineWidth):
        ballDirX = ballDirX * -1

    return ballDirX, ballDirY

def BallCollision(ball, paddle1, paddle2, ballDirX):
    if ballDirX == -1 and paddle1.right == ball.left and paddle1.top < ball.top and paddle1.bottom > ball.bottom:
        return -1
    elif ballDirX == 1 and paddle2.left == ball.right and paddle2.top < ball.top and paddle2.bottom > ball.bottom:
        return -1
    else:
        return 1

def UpdateScore(paddle1, ball, score, ballDirX):
    if ball.left == lineWidth:
        return 0
    elif ballDirX == -1 and paddle1.right == ball.left and paddle1.top < ball.top and paddle1.bottom > ball.bottom:
        score += 1
        return score
    elif ball.right == screen_width - lineWidth:
        score=0
        return score
    else:
        return score

def ScoreHandler(score):
    text=text_format("Score: %s" % (score), font, 24, white)
    textRect=text.get_rect()
    textRect.topleft=(50, 25)
    screen.blit(text, textRect)


def EnemyMovement(ball, ballDirX, paddle2):
    if ballDirX == -1:
        if paddle2.centery < (screen_height / 2):
            paddle2.y += 1
        elif paddle2.centery > (screen_height / 2):
            paddle2.y -= 1
            # if ball moving towards bat, track its movement.
    elif ballDirX == 1:
        if paddle2.centery < ball.centery:
            paddle2.y += 1
        else:
            paddle2.y -= 1
    return paddle2


def main():

    ballPosX=screen_width/2 - lineWidth/2
    ballPosY=screen_height/2 - lineWidth/2

    playerPos=(screen_height-paddleSize)/2
    enemyPos=(screen_height-paddleSize)/2
    score=0

    ballDirX = -1
    ballDirY = -1

    paddle1=pygame.Rect(paddleOffset, playerPos, lineWidth, paddleSize)
    paddle2 = pygame.Rect(screen_width - paddleOffset - lineWidth, enemyPos, lineWidth, paddleSize)
    ball=pygame.Rect(ballPosX, ballPosY, lineWidth, lineWidth)

    BackgroundGameplay()
    Paddle(paddle1)
    Paddle(paddle2)
    Ball(ball)
    pygame.mouse.set_visible(0)

    sound.play(loops=-1)

    while True:
        for event in pygame.event.get():
            if event.type==QUIT:
                pygame.quit()
                sys.exit()
            elif event.type==MOUSEMOTION:
                mousex, mousey=event.pos
                paddle1.y=mousey

        BackgroundGameplay()
        Paddle(paddle1)
        Paddle(paddle2)
        Ball(ball)

        ball=BallMovement(ball, ballDirX, ballDirY)
        ballDirX, ballDirY=WallCollision(ball, ballDirX, ballDirY)
        score=UpdateScore(paddle1, ball, score, ballDirX)
        ballDirX = ballDirX * BallCollision(ball, paddle1, paddle2, ballDirX)
        paddle2=EnemyMovement(ball, ballDirX, paddle2)
        ScoreHandler(score)
        pygame.display.set_caption('Python - Pygame Simple Arcade Game')
        pygame.display.update()
        clock.tick(fps)




if __name__=='__main__':
    main()