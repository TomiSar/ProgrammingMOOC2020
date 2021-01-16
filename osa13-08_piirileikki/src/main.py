# Tee animaatio, jossa on kymmenen robottia piirileikissä.
import pygame
import math

pygame.init()
pygame.display.set_caption("Piirileikki")
leveys, korkeus = 640, 480
naytto = pygame.display.set_mode((leveys, korkeus))

robotimage = pygame.image.load("robo.png")

kulma = 0
sade = 150
maara = 10
kello = pygame.time.Clock()

while True:
    for tapahtuma in pygame.event.get():
        if tapahtuma.type == pygame.QUIT:
            exit()

    naytto.fill((0, 0, 0))
    for i in range(maara):
        x = leveys/2+math.cos(kulma+2*math.pi*i/maara)*sade-robotimage.get_width()/2
        y = korkeus/2+math.sin(kulma+2*math.pi*i/maara)*sade-robotimage.get_height()/2
        naytto.blit(robotimage, (x, y))
    
    pygame.display.flip()

    kulma += 0.01
    kello.tick(60)