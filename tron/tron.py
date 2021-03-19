import pygame
import time
import random
import os
import sys
 
# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
LIGHTBLUE = (4, 229, 225)
ORANGE = (249, 141, 0)
BLUE = (0, 73, 209)
 
pygame.init()
 
# Set the width and height of the screen [width, height]
size = (500, 500)
screen = pygame.display.set_mode(size)
 
pygame.display.set_caption("T R O N")
 
# Loop until the user clicks the close button.
done = False

#start music
kill_sound = pygame.mixer.Sound("mcp_blip.wav")
try:
    pygame.mixer.music.stop()
    pygame.mixer.music.load('io_tower_music.wav')
    pygame.mixer.music.play(-1)
except Exception:
    nothing = "nothing"

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

#setup
trailX = [46]
trailY = [50]
robotrailX = [250]
robotrailY = [254]
animationtrailX = [434]
animationtrailY = [450]
animationcolor = [ORANGE]
playerX = 50
playerY = 50
roboY = 250
roboX = 250
animationX = 430
animationY = 450
playerX_speed = 1
playerY_speed = 0
roboX_speed = 0
roboY_speed = -1
animationX_speed = -1
animationY_speed = 0
death = False
win = False
speed = 2
Continue = False
end = False
turning = False

#game setup loop
while not Continue:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            mode = "human"
            done = True
            end = True
            Continue = True


    #logic
    pos = pygame.mouse.get_pos()
    mouseX = pos[0]
    mouseY = pos[1]
    pressed1, pressed2, pressed3 = pygame.mouse.get_pressed()
    if pressed1 and (mouseX>=160) and (mouseX<=340) and (mouseY >= 360) and (mouseY <= 400):
        mode = "human"
        done = True
        end = True
        Continue = True
    elif pressed1 and (mouseX <=250):
        mode = "human"
        Continue = True
    elif pressed1 and (mouseX > 250):
        mode = "computer"
        Continue = True

    """animation control code"""
    if (animationX >= 470) and (animationX_speed == 1):
        animationX_speed = 0
        animationY_speed = 1
    elif (animationX <= 30) and (animationX_speed == -1):
        animationX_speed = 0
        animationY_speed = -1
    elif (animationY >= 470) and (animationY_speed == 1):
        animationX_speed = -1
        animationY_speed = 0
    elif (animationY <= 30) and (animationY_speed == -1):
        animationX_speed = 1
        animationY_speed = 0

    if len(animationtrailX)>200:
        del animationtrailX[0]
        del animationtrailY[0]
        del animationcolor[0]
    animationtrailX.append(animationX)
    animationtrailY.append(animationY)
    if (animationX >= 250):
        animationcolor.append(LIGHTBLUE)
    elif (animationX < 250):
        animationcolor.append(ORANGE)
        

    animationX += animationX_speed*speed
    animationY += animationY_speed*speed
    
    #display
    screen.fill(BLACK)
    pygame.draw.rect(screen,LIGHTBLUE,[0,0,500,500], 10)
    for i in range(len(animationtrailX)):
        pygame.draw.rect(screen,animationcolor[i],[animationtrailX[i],animationtrailY[i],4,4])
    pygame.draw.rect(screen,WHITE,[animationX,animationY,4,4])
    pygame.draw.line(screen, BLUE, [70, 170], [430, 170], 5)

    pygame.draw.line(screen, ORANGE, [250, 497], [500, 497], 5)
    pygame.draw.line(screen, ORANGE, [497, 0], [497, 500], 5)
    pygame.draw.line(screen, ORANGE, [250, 2], [500, 2], 6)
    pygame.draw.line(screen, ORANGE, [250, 0], [250, 80], 5)
    pygame.draw.line(screen, ORANGE, [248, 78], [440, 78], 5)
    pygame.draw.line(screen, ORANGE, [440, 76], [440, 215], 5)
    pygame.draw.line(screen, ORANGE, [442, 218], [250, 218], 5)
    pygame.draw.line(screen, ORANGE, [252, 218], [252, 500], 5)
    
    pygame.draw.line(screen, LIGHTBLUE, [245, 0], [245, 80], 5)
    pygame.draw.line(screen, LIGHTBLUE, [247, 78], [60, 78], 5)
    pygame.draw.line(screen, LIGHTBLUE, [60, 76], [60, 215], 5)
    pygame.draw.line(screen, LIGHTBLUE, [58, 218], [249, 218], 5)
    pygame.draw.line(screen, LIGHTBLUE, [247, 218], [247, 500], 5)

    pygame.draw.line(screen, ORANGE, [250, 357], [330, 357], 5)
    pygame.draw.line(screen, ORANGE, [329, 355], [329, 404], 5)
    pygame.draw.line(screen, ORANGE, [329, 402], [250, 402], 5)

    pygame.draw.line(screen, LIGHTBLUE, [245, 357], [170, 357], 5)
    pygame.draw.line(screen, LIGHTBLUE, [171, 355], [171, 404], 5)
    pygame.draw.line(screen, LIGHTBLUE, [171, 402], [245, 402], 5)

    startfont = pygame.font.SysFont('Calibri', 25, True, False)
    humantext = startfont.render("Human v.s. Human",True,WHITE)
    screen.blit(humantext, [25, 240])
    robotext = startfont.render("Human v.s. Computer",True,WHITE)
    screen.blit(robotext, [260, 240])
    pygame.draw.rect(screen,BLACK,[190,360,120,40])
    robotext = startfont.render("Click a side to begin",True,BLUE)
    screen.blit(robotext, [140, 185])
    robotext = startfont.render("Close Program",True,WHITE)
    screen.blit(robotext, [175, 370])

    Titlefont = pygame.font.SysFont('Times New Roman', 100, True, False)
    Titletext = Titlefont.render("T R O N",True,BLUE)
    screen.blit(Titletext, [70, 70])
    
        #display to screen
    pygame.display.flip()

pygame.mouse.set_visible(False)

try:
    pygame.mixer.music.stop()
    pygame.mixer.music.load('lightcycle.wav')
    pygame.mixer.music.play(-1)
except Exception:
    nothing = "nothing"
# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
            end = True
            
    # User pressed down on a key
        elif event.type == pygame.KEYDOWN:
        # Figure out if it was an arrow key. If so
        # adjust speed.
            if event.key == pygame.K_LEFT:
                if (playerX_speed == 0):
                    playerX_speed = -1
                    playerY_speed = 0
            elif event.key == pygame.K_RIGHT:
                if (playerX_speed == 0):
                    playerX_speed = 1
                    playerY_speed = 0
            elif event.key == pygame.K_UP:
                if (playerY_speed == 0):
                    playerY_speed = -1
                    playerX_speed = 0
            elif event.key == pygame.K_DOWN:
                if (playerY_speed == 0):
                    playerY_speed = 1
                    playerX_speed = 0

            if (mode == "human"):
                if event.key == pygame.K_w:
                    if (roboY_speed == 0):
                        roboY_speed = -1
                        roboX_speed = 0
                elif event.key == pygame.K_s:
                    if (roboY_speed == 0):
                        roboY_speed = 1
                        roboX_speed = 0
                elif event.key == pygame.K_d:
                    if (roboX_speed == 0):
                        roboX_speed = 1
                        roboY_speed = 0
                elif event.key == pygame.K_a:
                    if (roboX_speed == 0):
                        roboX_speed = -1
                        roboY_speed = 0
    # --- Game logic should go here
    """collision with line check(it happens before I add to the line because otherwise people wouild just run into the lines they make"""
    for i in range(len(trailX)):
        if (abs(playerX-trailX[i])<speed) and (abs(playerY-trailY[i])<speed):
            death = True
            kill_sound.play()
        elif (abs(playerX-robotrailX[i])<speed) and (abs(playerY-robotrailY[i])<speed):
            death = True
            kill_sound.play()
        if (turning == False):
            if (abs(roboX-robotrailX[i])<2) and (abs(roboY-robotrailY[i])<2):
                win = True
                kill_sound.play()
            elif (abs(roboX-trailX[i])<2) and (abs(roboY-trailY[i])<2):
                win = True
                kill_sound.play()

    turning = False

    """line drawing algorithm for both players"""
    trailX.append(playerX)
    trailY.append(playerY)
    robotrailX.append(roboX)
    robotrailY.append(roboY)

    """robot decision"""
    if (mode == "computer"):
        if (roboX < 440) and (roboX > 60) and (roboY > 60) and (roboY < 440):
            roboaction = random.randint(1,180)
            if (roboaction == 1):
                if (roboX_speed == 1) or (roboX_speed == -1):
                    roboY_speed = 1
                    roboX_speed = 0
                elif (roboY_speed == 1) or (roboY_speed == -1):
                    roboX_speed = 1
                    roboY_speed = 0
            if (roboaction == 2):
                if (roboX_speed == 1) or (roboX_speed == -1):
                    roboY_speed = -1
                    roboX_speed = 0
                elif (roboY_speed == 1) or (roboY_speed == -1):
                    roboX_speed = -1
                    roboY_speed = 0
            
        if (roboX > 480) or (roboX < 10) or (roboY > 480) or (roboY < 10):
            move = random.randint(1,2)
            if (roboX > 470) or (roboX < 20):
                turning = True
                roboX_speed = 0
                if (roboY > 450):
                    roboY_speed = -1
                elif (roboY < 50):
                    roboY_speed = 1
                else:
                    if (move == 1):
                        roboY_speed = -1
                    if (move == 2):
                        roboY_speed = 1
            if (roboY > 470) or (roboY < 20):
                roboY_speed = 0
                turning = True
                if (roboX > 450):
                    roboX_speed = -1
                elif (roboX < 50):
                    roboX_speed = 1
                else:
                    if (move == 1):
                        roboX_speed = -1
            
                    if (move == 2):
                        roboX_speed = 1

        roboaction = random.randint(1,2)
        for i in range(len(trailX)):
            if (abs((roboX+(roboX_speed*7))-trailX[i])<6) and (abs((roboY+(roboY_speed*7))-trailY[i])<6):
                if (roboX_speed != 0):
                    roboX_speed = 0
                    if (roboaction == 1):
                        roboY_speed = 1
                        for i in range(len(trailX)):
                            if (abs((roboX)-trailX[i])<4) and (abs((roboY+(roboY_speed*7))-trailY[i])<6):
                                roboY_speed = -1
                            if ((roboY + 5) >= 480):
                                roboY_speed = -1
                    if (roboaction == 2):
                        roboY_speed = -1
                        for i in range(len(trailX)):
                            if (abs((roboX)-trailX[i])<4) and (abs((roboY+(roboY_speed*7))-trailY[i])<6):
                                roboY_speed = 1
                            if ((roboY - 5) <= 10):
                                roboY_speed = 1
                elif (roboY_speed != 0):
                    roboY_speed = 0
                    if (roboaction == 1):
                        roboX_speed = 1
                        for i in range(len(robotrailX)):
                            if (abs((roboX+(roboX_speed*7))-trailX[i])<6) and (abs((roboY)-trailY[i])<4):
                                roboX_speed = -1
                            if ((roboX + 5) >= 480):
                                roboX_speed = -1
                    if (roboaction == 2):
                        roboX_speed = -1
                        for i in range(len(robotrailX)):
                            if (abs((roboX+(roboX_speed*7))-trailX[i])<6) and (abs((roboY)-trailY[i])<4):
                                roboX_speed = 1
                            if ((roboX - 5) <= 10):
                                roboX_speed = 1
        for i in range(len(robotrailX)):
            if (abs((roboX+(roboX_speed*7))-robotrailX[i])<6) and (abs((roboY+(roboY_speed*7))-robotrailY[i])<6):
                if (roboX_speed != 0):
                    roboX_speed = 0
                    if (roboaction == 1):
                        roboY_speed = 1
                        for i in range(len(robotrailX)):
                            if (abs((roboX)-robotrailX[i])<4) and (abs((roboY+(roboY_speed*7))-robotrailY[i])<6):
                                roboY_speed = -1
                            if ((roboY + 5) >= 480):
                                roboY_speed = -1
                    if (roboaction == 2):
                        roboY_speed = -1
                        for i in range(len(robotrailX)):
                            if (abs((roboX)-robotrailX[i])<4) and (abs((roboY+(roboY_speed*7))-robotrailY[i])<6):
                                roboY_speed = 1
                            if ((roboY - 5) <= 10):
                                roboY_speed = 1
                elif (roboY_speed != 0):
                    roboY_speed = 0
                    if (roboaction == 1):
                        roboX_speed = 1
                        for i in range(len(robotrailX)):
                            if (abs((roboX+(roboX_speed*7))-robotrailX[i])<6) and (abs((roboY)-robotrailY[i])<4):
                                roboX_speed = -1
                            if ((roboX + 5) >= 480):
                                roboX_speed = -1
                    if (roboaction == 2):
                        roboX_speed = -1
                        for i in range(len(robotrailX)):
                            if (abs((roboX+(roboX_speed*7))-robotrailX[i])<6) and (abs((roboY)-robotrailY[i])<4):
                                roboX_speed = 1
                            if ((roboX - 5) <= 10):
                                roboX_speed = 1
            
    
    """general movement"""
    playerX += playerX_speed*speed
    playerY += playerY_speed*speed
    roboX += roboX_speed*speed
    roboY += roboY_speed*speed
    
    if (playerX > 490) or (playerX < 5) or (playerY > 490) or (playerY < 5):
        death = True
    if (roboX > 490) or (roboX < 5) or (roboY > 490) or (roboY < 5):
        win = True

    # --- Screen-clearing code goes here
 
    # Here, we clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.
 
    # If you want a background image, replace this clear with blit'ing the
    # background image.
    screen.fill(BLACK)
 
    # --- Drawing code should go here
    for i in range(len(trailX)):
        pygame.draw.rect(screen, LIGHTBLUE, [trailX[i], trailY[i], 4, 4])
    for i in range(len(robotrailX)):
        pygame.draw.rect(screen, ORANGE, [robotrailX[i], robotrailY[i], 4, 4])
    pygame.draw.rect(screen, WHITE, [playerX, playerY, 4, 4])
    pygame.draw.rect(screen, WHITE, [roboX, roboY, 4, 4])
    pygame.draw.rect(screen, ORANGE, [0, 0, 500, 500], 5)
    font = pygame.font.SysFont('Calibri', 25, True, False)
    
    if (death == True):
        text = font.render("ORANGE has WON!",True,WHITE)
        screen.blit(text, [165, 220])
    if (win == True):
        text = font.render("BLUE has WON!",True,WHITE)
        screen.blit(text, [180, 220])
        
    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    #check death
    if (death == True) or (win == True):
        kill_sound.play()
        time.sleep(0.5)
        done = True
    # --- Limit to 60 frames per second
    clock.tick(60)
 
# Close the window and quit.
if end == False:
    os.execl(sys.executable, sys.executable, *sys.argv)
pygame.quit()