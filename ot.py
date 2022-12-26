import pygame
import random

pygame.init()
size = [300,300]
screen = pygame.display.set_mode(size)
a = 50
b = 50
screen.fill(('white'))
pygame.draw.line(screen, (0, 0, 0), (100, 0), (100,300), 5)
pygame.draw.line(screen, (0, 0, 0), (200, 0), (200,300), 5)
pygame.draw.line(screen, (0, 0, 0), (0, 100), (300,100), 5)
pygame.draw.line(screen, (0, 0, 0), (0, 200), (300,200), 5)
pygame.draw.line(screen, ('red'), (0, 100), (100,100), 5)
pygame.draw.line(screen, ('red'), (100, 200), (200,200), 5)
pygame.draw.line(screen, ('red'), (0, 100), (100,100), 5)
pygame.draw.line(screen, ('red'), (0, 0), (0,300), 5)
pygame.draw.line(screen, ('red'), (200, 100), (200,200), 5)
pygame.draw.line(screen, ('red'), (0, 0), (300,0), 5)
pygame.draw.line(screen, ('red'), (300, 0), (300,300), 5)
pygame.draw.line(screen, ('red'), (0, 300), (300,300), 5)
pygame.draw.rect(screen, ('pink'), (200, 200, 100, 100))
pygame.draw.circle (screen, ('green'),(50,50), (20))
while True:
    for event in pygame.event.get():
        print ('Event:', event.type)
        if event.type == 200:
            if event.key == pygame.K_RIGHT:
                circle.move_ip(50,0)
            if event.key == pygame.K_LEFT:
                circle.move_ip(-50.0)
            if event.type == pygame.QUIT:
                running = False
    pygame.display.flip()



