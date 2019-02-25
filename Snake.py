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
pygame.display.update()

block_size = 10
FPS = 30

# generate a snake
def snake(block_size, snakeList):
    for XnY in snakeList:
        pygame.draw.rect(gameDisplay, green, [XnY[0], XnY[1], block_size, block_size])

    
    
#pygame.font: Create a Font object from the system fonts
font = pygame.font.SysFont(None, 25)


#Add text
def message_to_screen(msg,color):
    screen_text = font.render(msg, True, color)
    gameDisplay.blit(screen_text, [display_width/2, display_height/2])





#return a pygame clock object
clock = pygame.time.Clock()

# game loop
def gameLoop():
    gameExit = False
    gameOver = False
 
    lead_x = display_width/2
    lead_y = display_height/2
    
    lead_x_change = 0
    lead_y_change = 0

    snakeList = []
    snakeLength = 1
    # Random Location of apples
    randAppleX = round(random.randrange(0, display_width-block_size)/10.0)*10.0
    randAppleY = round(random.randrange(0, display_height-block_size)/10.0)*10.0
    
    while not gameExit:
        #game over functionality 
        while gameOver == True:
            gameDisplay.fill(white)
            message_to_screen("Game over, press C to play again or Q to quit", red)
            pygame.display.update()

            for event in pygame.event.get():
                #Quit or Retry
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        gameExit = True
                        gameOver = False
                    if event.key == pygame.K_c:
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
                elif event.key == pygame.K_RIGHT:
                    lead_x_change = block_size
                    lead_y_change = 0
                elif event.key == pygame.K_UP:
                    lead_y_change = -block_size
                    lead_x_change = 0
                elif event.key == pygame.K_DOWN:
                    lead_y_change = block_size
                    lead_x_change = 0

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
        pygame.draw.rect(gameDisplay, red, [randAppleX, randAppleY, block_size, block_size])


       
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
        
        #Restriction:clock.tick (*framerate): never run more than *framerate frames per sec
        pygame.display.update()

        #if cross over or say "apple be eaten"
        if lead_x == randAppleX and lead_y == randAppleY:
            #new random apple regenerated
            randAppleX = round(random.randrange(0, display_width-block_size)/10.0)*10.0
            randAppleY = round(random.randrange(0, display_height-block_size)/10.0)*10.0
            snakeLength += 1
            
            
        clock.tick(FPS)

    #### REMINDER: The first option of changing the speed of moving object is always lead_x_change and lead_y_change
    ####clock.tick() Second
        
    ##uninitialize game
    pygame.quit()


    ##quit the python window
    quit()

gameLoop()
