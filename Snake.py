import pygame
import time
import random

##initialization
pygame.init()
##usually return (6,0),if you "print" it which means 6 successes and 0 failure

##Colors and Fills
white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
green = (0,155,0)

display_width = 800
display_height = 600 

##pygame.display.set_mode: display screen set
gameDisplay = pygame.display.set_mode((display_width,display_height))

##pygame.display.update(): update the whole surface(if no parameter)
##alternative method: pygame.display.flip(): upgrade the whole surface like a flipbook
pygame.display.set_caption('Slither')

#set icon
icon = pygame.image.load('Apple.png')
pygame.display.set_icon(icon)

pygame.display.update()

img = pygame.image.load('Snakehead2.png')
appleimg = pygame.image.load('Apple.png')

AppleThickness = 30
block_size = 20

FPS = 15
direction = "right"

def game_intro():
    intro = True

    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    intro = False

                if event.key == pygame.K_q:
                    quit()
        gameDisplay.fill(white)
        message_to_screen("Welcome to Slither",
                          green,
                          -100,
                          "large")

        message_to_screen("The object of the game is to eat red apples",
                          black,
                          -30)
        
        message_to_screen("The more apples you eat, the longer you get",
                          black,
                          10)

        message_to_screen("If you run into yourself, or the edges, you die",
                          black,
                          50)

        message_to_screen("Press C to play or Q to quit",
                          black,
                          180)
        pygame.display.update()
        clock.tick(15)
        

# generate a snake
# snakehead point direction
def snake(block_size, snakelist):


    if direction == "right":
        head = pygame.transform.rotate(img, 270)

    if direction == "left":
        head = pygame.transform.rotate(img, 90)
        
    if direction == "up":
        head = img
        
    if direction == "down":
        head = pygame.transform.rotate(img, 180)     
    
    gameDisplay.blit(head, (snakelist[-1][0],snakelist[-1][1]))
    for XnY in snakelist[:-1]:
        pygame.draw.rect(gameDisplay, green, [XnY[0], XnY[1], block_size, block_size])


#random apple generator
def randAppleGen():
    randAppleX = round(random.randrange(0, display_width-AppleThickness))#/10.0)*10.0
    randAppleY = round(random.randrange(0, display_height-AppleThickness))#/10.0)*10.0

    return randAppleX, randAppleY





    
#pygame.font: Create a Font object from the system fonts
smallfont = pygame.font.SysFont("comicsansms", 25)
medfont = pygame.font.SysFont("comicsansms", 50)
largefont = pygame.font.SysFont("comicsansms", 80)



#define text object (center all text)
def text_objects(text,color,size):
    if size == "small":
        textSurface = smallfont.render(text,True,color)
    elif size == "medium":
        textSurface = medfont.render(text,True,color)
    elif size == "large":
        textSurface = largefont.render(text,True,color)
    return textSurface, textSurface.get_rect()
    
#score
def score(score):
    text = smallfont.render("Score: "+str(score), True, black)
    gameDisplay.blit(text,[0,0])


#Add text (centered )
def message_to_screen(msg,color, y_displace=0, size="small"):
    textSurf, textRect = text_objects(msg,color,size)    
    textRect.center = (display_width/2), (display_height/2)+y_displace
    gameDisplay.blit(textSurf, textRect)





#return a pygame clock object
clock = pygame.time.Clock()

# game loop
def gameLoop():
    global direction
    gameExit = False
    gameOver = False
 
    lead_x = display_width/2
    lead_y = display_height/2
    
    lead_x_change = 10
    lead_y_change = 0

    snakeList = []
    snakeLength = 1
    # Random Location of apples
    randAppleX, randAppleY = randAppleGen()
    
    while not gameExit:
        #game over functionality 
        while gameOver == True:
            gameDisplay.fill(white)
            message_to_screen("Game over",
                              red,
                              -50,
                              size="large")
            
            message_to_screen("Press C to play again or Q  to quit",
                              black,
                              50,
                              size="medium")
            pygame.display.update()

            for event in pygame.event.get():
                
                #Quit or Retry
                if event.type == pygame.QUIT:
                    gameExit = True
                    gameOver = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        gameExit = True
                        gameOver = False
                    if event.key == pygame.K_c:
                        direction = 'right' 
                        gameLoop()


                        
        ##get event from the queue event
        '''
        QUIT             none
        ACTIVEEVENT      gain, state
        KEYDOWN          unicode, key, mod
        KEYUP            key, mod
        MOUSEMOTION      pos, rel, buttons
        MOUSEBUTTONUP    pos, button
        MOUSEBUTTONDOWN  pos, button
        JOYAXISMOTION    joy, axis, value
        JOYBALLMOTION    joy, ball, rel
        JOYHATMOTION     joy, hat, value
        JOYBUTTONUP      joy, button
        JOYBUTTONDOWN    joy, button
        VIDEORESIZE      size, w, h
        VIDEOEXPOSE      none
        USEREVENT        code
        '''
        
        
        for event in pygame.event.get():

            #quit handler
            if event.type == pygame.QUIT:
                gameExit = True

            #velocity and which direction
            #set 0 to the change variable to restrict only moving in four directions
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    lead_x_change = -block_size
                    lead_y_change = 0
                    direction = "left"
                elif event.key == pygame.K_RIGHT:
                    lead_x_change = block_size
                    lead_y_change = 0
                    direction = "right"
                elif event.key == pygame.K_UP:
                    lead_y_change = -block_size
                    lead_x_change = 0
                    direction = "up"
                elif event.key == pygame.K_DOWN:
                    lead_y_change = block_size
                    lead_x_change = 0
                    direction = "down"

            #Optional (KEYUP: Stop moving)
            '''
            
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    lead_x_change = 0
                if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    lead_y_change = 0
            '''
        #Boundaries
        #Touch the boundary == Game Over
        if lead_x >= display_width or lead_x < 0 or lead_y >= display_height or lead_y <0:
            gameOver = True

        #moving object            
        lead_x += lead_x_change
        lead_y += lead_y_change

        
        gameDisplay.fill(white)
         
    #Note:
    #game.Display can also be used to draw rectangle (ex:gameDisplay.fill(red,rect=[20,20,100,100]))
        

        #pygane.draw.rect(#screen, #color, #[coordinateX, coordianateY, width, length]
        #pygame.draw.rect(gameDisplay, red, [randAppleX, randAppleY, AppleThickness, AppleThickness])

        gameDisplay.blit(appleimg,(randAppleX, randAppleY))
       
        snakeHead = []
        snakeHead.append(lead_x)
        snakeHead.append(lead_y)
        snakeList.append(snakeHead)

        #without if statement below, the snake will continously get longer
        #"snakeLength" is a restriction variable how long the snake should be before eating a apple
        if len(snakeList) > snakeLength:
            del snakeList[0]

        #snake eat itself
        for eachSegament in snakeList[:-1]:
            if eachSegament == snakeHead:
                gameOver = True
        
        snake(block_size, snakeList)
        score(snakeLength-1)
        #Restriction:clock.tick (*framerate): never run more than *framerate frames per sec
        pygame.display.update()

        
        #Cross over
        #if cross over or say "apple be eaten"
        if lead_x > randAppleX and lead_x < randAppleX + AppleThickness or lead_x + block_size > randAppleX and lead_x + block_size <randAppleX + AppleThickness:
            if lead_y > randAppleY and lead_y <randAppleY + AppleThickness:
                randAppleX, randAppleY = randAppleGen()
                snakeLength += 1
            elif lead_y + block_size > randAppleY and lead_y + block_size < randAppleY + AppleThickness:
                randAppleX, randAppleY = randAppleGen()
                snakeLength += 1
            
        clock.tick(FPS)

    #### REMINDER: The first option of changing the speed of moving object is always lead_x_change and lead_y_change
    ####clock.tick() Second
        
    ##uninitialize game
    pygame.quit()


    ##quit the python window
    quit()
game_intro()
gameLoop()
