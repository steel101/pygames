######### IMPORTS ###################################################


import random, math, pygame
from pygame.locals import *


counter = 0
snakelist1 = [[300,400],[280,400],[260,400]]
snakelist2 = [[300,400],[280,400],[260,400],[240,400],[220,400],[200,400]]
snakelist3 = [[300,400],[280,400],[260,400],[240,400],[220,400],[200,400],[180,400],[160,400]]
snakelist4 = [[300,400],[280,400],[260,400],[240,400],[220,400],[200,400],[180,400],[160,400],[140,400]]
snakelist5 = [[300,400],[280,400],[260,400],[240,400],[220,400],[200,400],[180,400],[160,400],[140,400],[120,400],[100,400]]
snakelist6 = [[300,400],[280,400],[260,400],[240,400],[220,400],[200,400],[180,400],[160,400],[140,400],[120,400],[100,400],[80,400],[60,400]]
snakelist7 = [[300,400],[280,400],[260,400],[240,400],[220,400],[200,400],[180,400],[160,400],[140,400],[120,400],[100,400],[80,400],[60,400],[40,400],[20,400]]
snakelist8 = [[300,400],[280,400],[260,400],[240,400],[220,400],[200,400],[180,400],[160,400],[140,400],[120,400],[100,400],[80,400],[60,400],[40,400],[20,400],[0,400]]
snakelist = snakelist1 

from tkinter import *
from tkinter import ttk
root=Tk()
mainframe = ttk.Frame(root,padding="1 1 12 12")
root.geometry('525x100')
root.title("snake settings enter on numbers and then click start game button")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
mainframe.columnconfigure(0, weight=1)
mainframe.rowconfigure(0, weight=1)


variable1=StringVar() # Value saved here
variable1.set("5")
variable2=StringVar() # Value saved here
variable2.set("1")
variable3=StringVar() # Value saved here
variable3.set("1")
variable4=StringVar() # Value saved here
variable4.set("1")
variable5=StringVar() # Value saved here
variable5.set("3")

def search():
  #print(variable1.get())
  root.destroy()
  return ''

ttk.Entry(mainframe, width=7, textvariable=variable1).grid(column=2, row=1)
ttk.Entry(mainframe, width=7, textvariable=variable2).grid(column=4, row=1)
ttk.Entry(mainframe, width=7, textvariable=variable3).grid(column=2, row=2)
ttk.Entry(mainframe, width=7, textvariable=variable4).grid(column=4, row=2)
ttk.Entry(mainframe, width=7, textvariable=variable5).grid(column=2, row=3)

ttk.Label(mainframe, text="speed 1-10").grid(column=1, row=1)
ttk.Label(mainframe, text="grow 1-5").grid(column=3, row=1)
ttk.Label(mainframe, text="start video 1=on 0=off").grid(column=1, row=2)
ttk.Label(mainframe, text="score add 1-5").grid(column=3, row=2)
ttk.Label(mainframe, text="snake start length 3-10").grid(column=1, row=3)
ttk.Button(mainframe, text="StartGame", command=search).grid(column=10, row=13)
root.mainloop()
###################################################################################
#get user input for speed of snake 1 to 10 and set back to 10 if user enter anything #above 10 we go into if loop and anything below 1 we go into the elif loop

print("Enter a number for the speed of snake between 1(real fast) and 10(real slow): ", end="")
gameregulatorvalue = int(variable1.get())
print("\nYou've entered:", gameregulatorvalue)
if gameregulatorvalue > 10:
	gameregulatorvalue = 10 
	print("\nYou've entered a number above 10 so we set it to 10 for you:")
elif gameregulatorvalue < 1:
	gameregulatorvalue = 1
	print("\nYou've entered a number below 1 so we set it to 1 for you:")
###################################################################################
#get user input for snake lenght and set back to 10 if user enter anything #above 10 we go into if loop and anything below 3 we go into the elif loop

print("Enter a number for the start size of snake): ", end="")
snakelistuserinput = int(variable5.get())
print("\nYou've entered:", snakelistuserinput)
if snakelistuserinput > 10:
	snakelist = snakelist8 
	print("\nYou've entered a number above 10 so we set it to 10 for you:")
elif snakelistuserinput < 3:
	snakelist = snakelist1
	print("\nYou've entered a number below 1 so we set it to 1 for you:")
elif snakelistuserinput == 3:
        snakelist = snakelist2
elif snakelistuserinput == 4:
        snakelist = snakelist3
elif snakelistuserinput == 5:
        snakelist = snakelist4
elif snakelistuserinput == 6:
        snakelist = snakelist5
elif snakelistuserinput == 7:
        snakelist = snakelist6
elif snakelistuserinput == 8:
        snakelist = snakelist7
elif snakelistuserinput == 9:
        snakelist = snakelist8
elif snakelistuserinput == 10:
        snakelist = snakelist8
####################################################################################
#get user input for how much the snake grows each time if users input is above 5 we #go into if loop if user input is less then 2 we go into elif loop 
###################################################################################
print("Enter a number for how much the snakes grows each time you eat 2 to 5: ", end="")
snakegrowuserinput = int(variable2.get())
print("\nYou've entered:", snakegrowuserinput)
if snakegrowuserinput > 5:
	snakegrowuserinput = 5 
	print("\nYou've entered a number above 5 so we set it to 5 for you:")
elif snakegrowuserinput  < 2:
	snakegrowuserinput = 2
	print("\nYou've entered a number below 2 so we set it to 2 for you:")
	print(snakegrowuserinput)

###################################################################################
#get user input for how much the score goes up each time you eat if users input is #more then 10 we go into if loop and if users input is less then 1 we go into elif #loop
###################################################################################
print("Enter a number for how much the score goes up each time you eat 1 to 10: ", end="")
scoreuserinput = int(variable4.get())
print("\nYou've entered:", scoreuserinput)
if scoreuserinput > 10:
	scoreuserinput = 10 
	print("\nYou've entered a number above 10 so we set it to 10 for you:")
elif scoreuserinput < 1:
	scoreuserinput = 1
	print("\nYou've entered a number below 1 so we set it to 1 for you:")
###################################################################################   
#start amtaion on or off user enter 1 for on 0 for off
print("do you want start video on or off 1 for on and 0 for off: ", end="")
startuserinput = int(variable3.get())
print("\nYou've entered:", startuserinput)
if startuserinput > 1:
	startuserinput = 1 
	print("\nyou enter a number above 1 so we turned the start video on for you:")

######### MAIN #####################################################

def main():

    showstartscreen = startuserinput
    
    while 1:
        ######## CONSTANTS

        WINSIZE = [800,600]
        WHITE = [255,255,255]
        BLACK = [0,0,0]
        RED = [255,0,0]
        GREEN = [0,255,0]
        BLUE = [0,0,255]
        ORANGE = [255,165,0]
        BLOCKSIZE = [20,20]
        UP = 1
        DOWN = 3
        RIGHT = 2
        LEFT = 4
        MAXX = 760
        MINX = 20
        MAXY = 560
        MINY = 80
        SNAKESTEP = 20
        TRUE = 1
        FALSE = 0
        

        ######## VARIABLES

        direction = RIGHT # 1=up,2=right,3=down,4=left
        snakexy = [300,400]
        counter = 0
        score = 0
        appleonscreen = 0
        #applexy = [0,0]
        newdirection = RIGHT
        snakedead = FALSE
        gameregulator = gameregulatorvalue
        gamepaused = 0
        growsnake = 0  # added to grow tail by two each time 
        snakegrowunit = snakegrowuserinput # added to grow tail by two each time
        
        
        pygame.init()
        pygame.mixer.music.load('Ruined Planet.ogg')
        pygame.mixer.music.play(-1, 0.0)
        clock = pygame.time.Clock()
        screen = pygame.display.set_mode(WINSIZE)
        pygame.display.set_caption('SNAKE')
        screen.fill(BLACK)

        #### show initial start screen
        
        if showstartscreen == TRUE:
            showstartscreen = FALSE

            s = [[180,120],[180,100],[160,100],[140,100],[120,100],[100,100],[100,120],[100,140],[100,160],[120,160],[140,160],[160,160],[180,160],[180,180],[180,200],[180,220],[160,220],[140,220],[120,220],[100,220],[100,200]]
            apple = [100,200]
            
            pygame.draw.rect(screen,GREEN,Rect(apple,BLOCKSIZE))
            pygame.display.flip()
            clock.tick(8)
            
            for e in s:
                pygame.draw.rect(screen,BLUE,Rect(e,BLOCKSIZE))
                pygame.display.flip()
                clock.tick(8)
                
            font = pygame.font.SysFont("arial", 64)
            text_surface = font.render("NAKE", True, BLUE)
            screen.blit(text_surface, (220,180))
            font = pygame.font.SysFont("arial", 24)
            text_surface = font.render("Move the snake with the arrow keys to eat the apples", True, BLUE)
            screen.blit(text_surface, (50,300))
            text_surface = font.render("Avoid the walls and yourself !", True, BLUE)
            screen.blit(text_surface, (50,350))
            text_surface = font.render("Press s to start a new game - Press q to quit at any time", True, BLUE)
            screen.blit(text_surface, (50,400))
            text_surface = font.render("Press p to pause r to resume at any time", True, BLUE)
            screen.blit(text_surface, (50,450))

            pygame.display.flip()
            while 1:
                for event in pygame.event.get():
                    if event.type == QUIT:
                        exit()

                pressed_keys = pygame.key.get_pressed()
                if pressed_keys[K_q]: exit()
                if pressed_keys[K_s]: break

                clock.tick(10)


        while not snakedead:

            ###### get input events  ####

            for event in pygame.event.get():
                if event.type == QUIT:
                    exit()
                    
            pressed_keys = pygame.key.get_pressed()
            
            if pressed_keys[K_LEFT]: newdirection = LEFT
            if pressed_keys[K_RIGHT]: newdirection = RIGHT
            if pressed_keys[K_UP]: newdirection = UP
            if pressed_keys[K_DOWN]: newdirection = DOWN
            if pressed_keys[K_q]: snakedead = TRUE
            if pressed_keys[K_p]: gamepaused = 1

            ### wait here if p key is pressed until p key is pressed again
            
            while gamepaused == 1:
                pygame.mixer.music.stop()
                for event in pygame.event.get():
                    if event.type == QUIT:
                        exit()
                pressed_keys = pygame.key.get_pressed()
                if pressed_keys[K_r]:
                    gamepaused = 0
                    pygame.mixer.music.load('Ruined Planet.ogg')
                    pygame.mixer.music.play(-1, 0.0)
                    #pygame.mixer.music.stop() 
                clock.tick(10)


            ### added gameregulator because setting a very low clock ticks
            ### caused the keyboard input to be hit and miss.  So I up the
            ### gameticks and the input and screen refresh is at this rate
            ### but the snake moving and all other logic is at the slower
            ### "regulated" speed

            
            if gameregulator == gameregulatorvalue:

                ####### lets make sure we can't go back the reverse direction

                if newdirection == LEFT and not direction == RIGHT:
                    direction = newdirection

                elif newdirection == RIGHT and not direction == LEFT:
                    direction = newdirection

                elif newdirection == UP and not direction == DOWN:
                    direction = newdirection

                elif newdirection == DOWN and not direction == UP:
                    direction = newdirection
                    
                ##### now lets move the snake according to the direction
                ##### if we hit the wall the snake dies
                ##### need to make it less twitchy when you hit the walls
                    

                if direction == RIGHT:
                    snakexy[0] = snakexy[0] + SNAKESTEP
                    if snakexy[0] > MAXX:
                        snakedead = TRUE
                    
                elif direction == LEFT:
                    snakexy[0] = snakexy[0] - SNAKESTEP
                    if snakexy[0] < MINX:
                        snakedead = TRUE
                        
                elif direction == UP:
                    snakexy[1] = snakexy[1] - SNAKESTEP
                    if snakexy[1] < MINY:
                        snakedead = TRUE
                        
                elif direction == DOWN:
                    snakexy[1] = snakexy[1] + SNAKESTEP
                    if snakexy[1] > MAXY:
                        snakedead = TRUE

                ### is the snake crossing over itself
                ### had to put the > 1 test in there as I was
                ### initially matching on first pass otherwise - not sure why
                        
                if len(snakelist) > 3 and snakelist.count(snakexy) > 0: 
                    snakedead = TRUE
                

                        
                #### generate an apple at a random position if one is not on screen
                #### make sure apple never appears in snake position
                    
                if appleonscreen == 0:
                    good = FALSE
                    while good == FALSE:
                        x = random.randrange(1,39)
                        y = random.randrange(5,29)
                        applexy = [int(x*SNAKESTEP),int(y*SNAKESTEP)]
                        if snakelist.count(applexy) == 0:
                            good = TRUE
                    appleonscreen = 1

                #### add new position of snake head
                #### if we have eaten the apple don't pop the tail ( grow the snake )
                #### if we have not eaten an apple then pop the tail ( snake same size )

                snakelist.insert(0,list(snakexy))
                if snakexy[0] == applexy[0] and snakexy[1] == applexy[1]:
                    appleonscreen = 0
                    score = score + scoreuserinput
                    growsnake = growsnake + 1
                elif growsnake > 0:
                    growsnake = growsnake + 1
                    if growsnake == snakegrowunit:
                        growsnake = 0
                else:
                    snakelist.pop()
                    
                

                gameregulator = 0


            ###### RENDER THE SCREEN ###############
            
            ###### Clear the screen
            screen.fill(BLACK)
            
            ###### Draw the screen borders
            ### horizontals
            pygame.draw.line(screen,ORANGE,(0,9),(799,9),20)
            pygame.draw.line(screen,ORANGE,(0,590),(799,590),20)
            pygame.draw.line(screen,ORANGE,(0,69),(799,69),20)
            ### verticals
            pygame.draw.line(screen,ORANGE,(9,0),(9,599),20)
            pygame.draw.line(screen,ORANGE,(789,0),(789,599),20)
            
            ###### Print the score
            font = pygame.font.SysFont("arial", 38)
            text_surface = font.render("SNAKE!          Score: " + str(score), True, BLUE)
            screen.blit(text_surface, (50,18))

            ###### Output the array elements to the screen as rectangles ( the snake)
            for element in snakelist:
                pygame.draw.rect(screen,GREEN,Rect(element,BLOCKSIZE))

            ###### Draw the apple
            pygame.draw.rect(screen,RED,Rect(applexy,BLOCKSIZE))

            ###### Flip the screen to display everything we just changed
            pygame.display.flip()



            gameregulator = gameregulator + 1
            
            clock.tick(25)


        ##### if the snake is dead then it's game over
            
        if snakedead == TRUE:
            pygame.mixer.music.stop()
            screen.fill(BLACK)
            font = pygame.font.SysFont("arial", 48)
            text_surface = font.render("GAME OVER", True, BLUE)
            screen.blit(text_surface, (250,200))
            text_surface = font.render("Your Score: " + str (score), True, BLUE)
            screen.blit(text_surface, (250,300))
            font = pygame.font.SysFont("arial", 24)
            text_surface = font.render("Press q to quit", True, BLUE)
            screen.blit(text_surface, (300,400))
            text_surface = font.render("Press n to play again", True, BLUE)
            screen.blit(text_surface, (275,450))

            pygame.display.flip()
            while 1:
                for event in pygame.event.get():
                    if event.type == QUIT:
                        exit()

                pressed_keys = pygame.key.get_pressed()
                if pressed_keys[K_q]: exit()
                if pressed_keys[K_n]: break

                clock.tick(10)
    
if __name__ == '__main__':
    main()


