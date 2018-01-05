#
import pygame
import random
import math

#start game engine
pygame.init()

#Window
SIZE = (800, 600)
TITLE = "First Drawnig"
screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption(TITLE)

# Timer
clock = pygame.time.Clock()
refresh_rate = 60


dec = []
for i in range(50):
    x = random.randrange(300, 500)
    y = random.randrange(100, 500)
    r = random.randrange(5, 10)
    s = [x, y, r, r]
    dec.append(s)

snow = []
for i in range(11):
    x = random.randrange(500, 590)
    y = random.randrange(120, 250)
    r = random.randrange(5, 10)
    f = [x, y, r, r]
    snow.append(f)

# Colors
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
ORANGE = (255, 125 , 0)
BROWN = (122, 48, 8)
CARPET = (39, 26, 12)
WALL = (255, 244, 198)
DOOR = (77, 51, 25)
SKY = (153, 204, 255)
STAR = (255,215,0)
clrs_list = [RED, WHITE, BLUE, ORANGE, WHITE]


#doll house
def star(x,y):
   pygame.draw.polygon(screen, STAR, [[x, y], [x+20, y], [x+10, y-20],[x+10, y],[x+20, y-20]]) 

# Game loop
done = False
def lights(x):
    pygame.draw.arc(screen, ORANGE, [x, -25, 70, 50], math.pi, 2*math.pi, 4)
    
        
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    for x in range(1,800,70):
        pygame.draw.arc(screen, ORANGE, [x, -25, 70, 50], math.pi, 2*math.pi, 4)

    
    screen.fill(WALL)
    '''carpet'''
    pygame.draw.rect(screen, CARPET, [0, 400, 800, 200])
    '''chimney'''
    pygame.draw.rect(screen, RED, [700, 0, 100, 400])
    for x in range(700, 800, 5):
        for y in range(0, 400, 10):
            brick = x, y, 15, 10
            pygame.draw.rect(screen, WHITE, brick, 1)

    '''rug'''
    pygame.draw.ellipse(screen, RED, [250, 500, 300, 100])
    pygame.draw.ellipse(screen, BLUE, [300, 500, 200, 100])
    pygame.draw.ellipse(screen, WHITE, [350, 500, 100, 100])


    '''door'''
    pygame.draw.rect(screen, DOOR, [100, 150, 150, 250])
    pygame.draw.rect(screen, WHITE, [100, 150, 150, 250],10)
    '''tree'''
    pygame.draw.polygon(screen, GREEN, [[400, 100], [500, 500], [300, 500]])
    pygame.draw.rect(screen, BROWN, [360, 500, 80, 50])
    for s in dec:
        pygame.draw.ellipse(screen, clrs_list[random.randint(0,2)], s)
        
    pygame.draw.polygon(screen, WALL, [[280, 100], [400, 100], [325, 400],[280,400]])
    pygame.draw.polygon(screen, WALL, [[600, 100], [400, 100], [476, 400],[600,400]])
    pygame.draw.polygon(screen, CARPET, [[500, 500], [476, 400], [600,400], [600, 500]])
    pygame.draw.polygon(screen, CARPET, [[325, 400], [300, 400], [280,400], [300, 500]])

    '''window'''
    pygame.draw.rect(screen, SKY, [500, 120, 100, 150])
    pygame.draw.rect(screen, BLACK, [495, 120, 100, 150],10)
    for f in snow:
        pygame.draw.ellipse(screen, WHITE, f)
    for y in snow:
        y[1] += 1

        if y[1] > 250:
            y[0] = random.randrange(500, 590)
            y[1] = random.randrange(100, 180)
    '''lights'''
    for x in range(1,800,70):
        pygame.draw.arc(screen, BLACK, [x, -25, 70, 50], math.pi, 2*math.pi, 4)


    '''star'''
    star(390,100)





    pygame.display.flip()
    clock.tick(refresh_rate)




pygame.quit()




    

    
