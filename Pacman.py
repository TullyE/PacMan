import pygame
from pygame import display
import os
pygame.init()

myFrame = display.set_mode((540, 600))
display.set_caption("PacMan")
clock = pygame.time.Clock()

blue = (0,255,255)

name = "pacManBoard.png"
print(os.getcwd() + "/Images/" + name)
myFrame.fill(blue)
image = pygame.image.load(os.getcwd() + "/Images/" + name)
myFrame.blit(image, (0,0))



pmx = 190
pmy = 178
x1_change = 0
y1_change = 0


def wallDir(x, y):
    if x <= 10 and (y < 258 or y >= 278 ):
        return "left" 
    elif x >= 490 and (y < 258 or y >= 278 ):
        return "right" 
    return None

while True:
    barrier = wallDir(pmx, pmy)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                if barrier == "left":
                    x1_change = 0
                else:
                    x1_change = -5
                    y1_change = 0
            elif event.key == pygame.K_RIGHT:
                if barrier == "right":
                    x1_change = 0
                else:
                    x1_change = 5
                    y1_change = 0
            elif event.key == pygame.K_UP:
                x1_change = 0
                y1_change = -5
            elif event.key == pygame.K_DOWN:
                x1_change = 0
                y1_change = 5
            elif event.key == pygame.K_SPACE:
                print(pmx)
    
    myFrame.fill(blue)
    if pmx < -38:
        pmx = 540
    if pmx > 540:
        pmx = -38
    if barrier == "left" and x1_change == -5:
        print("works ez")
        x1_change = 0
    if barrier == "right" and x1_change == 5:
        x1_change = 0
    image = pygame.image.load(os.getcwd() + "/Images/" + "pacManBoard.png")
    myFrame.blit(image, (0,0))
    image = pygame.image.load(os.getcwd() + "/Images/" + "pacman.png")
    pmx += x1_change
    pmy += y1_change
    myFrame.blit(image, (pmx, pmy))
    clock.tick(30)
    barrier = None
    display.update()