# Tee ohjelma, joka piirtää tuhat robottia satunnaisiin paikkoihin.
import pygame
from random import randint

pygame.init()
pygame.display.set_caption("Satunnaiset robotit")
leveys, korkeus = 640, 480
naytto = pygame.display.set_mode((640, 480))

robotimage = pygame.image.load("robo.png")

# Suoritetaan 1000 kierrosta, jokaiseisella kierroksella generoidaan x-koordinaatti ja y-koordinaatti 
# satunnaiseeen paikkaan ja piirretään koordinaatteihin uusi robotti.
naytto.fill((0, 0, 0))
for i in range(1000):
    x = randint(0, leveys-robotimage.get_width())
    y = randint(0, korkeus-robotimage.get_height())
    naytto.blit(robotimage, (x, y))
pygame.display.flip()

while True:
    for tapahtuma in pygame.event.get():
        if tapahtuma.type == pygame.QUIT:
            exit()