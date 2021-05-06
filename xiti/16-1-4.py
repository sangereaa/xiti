import pygame
import sys
pygame.init()
screen = pygame.display.set_mode([640, 480])
screen.fill([255, 255, 255])
my_miao = pygame.image.load("miao.jpg")
x = 50
y = 50
screen.blit(my_miao, [x, y])
pygame.display.flip()
for looper in range(1, 85):
    pygame.time.delay(20)
    pygame.draw.rect(screen, [255, 255, 255], [x, y, 150, 160], 0)
    x = x + 5
    screen.blit(my_miao, [x, y])
    pygame.display.flip()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
pygame.quit()
