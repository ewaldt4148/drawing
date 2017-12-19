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
    
# Colors
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
ORANGE = (255, 125 , 0)
BROWN = (122, 48, 8)
CARPET = (86, 64, 32)
WALL = (255, 244, 198)

clrs_list = [RED, WHITE, BLUE]

# Game loop
done = False

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    screen.fill(WALL)
    '''carpet'''
    pygame.draw.rect(screen, CARPET, [0, 400, 800, 200])
    '''chimney'''
    pygame.draw.rect(screen, RED, [700, 0, 100, 400])
    for x in range(700, 800, 10):
        for y in range(0, 400, 10):
            brick = x, y, 15, 10
            pygame.draw.rect(screen, WHITE, brick, 1)

    '''rug'''
    pygame.draw.ellipse(screen, RED, [250, 500, 300, 100])
    pygame.draw.ellipse(screen, BLUE, [300, 500, 200, 100])
    pygame.draw.ellipse(screen, WHITE, [350, 500, 100, 100])
    '''door'''
    pygame.draw.rect(screen, BLACK, [100, 150, 150, 250])
    '''tree'''
    pygame.draw.polygon(screen, GREEN, [[400, 100], [500, 500], [300, 500]])
    pygame.draw.rect(screen, BROWN, [360, 500, 80, 50])
    for s in dec:
        pygame.draw.ellipse(screen, clrs_list[random.randint(0,2)], s)
        
    pygame.draw.polygon(screen, WALL, [[400, 100], [500, 500], [300, 500]])


    










    pygame.display.flip()
    clock.tick(refresh_rate)




pygame.quit()


    
