# Tee ohjelma, jossa robotti on satunnaisessa paikassa ikkunassa. Kun pelaaja painaa hiirellä robotista, se siirtyy aina uuteen paikkaan.
import pygame
from random import randint
 
pygame.init()
pygame.display.set_caption("Robottin paikka")
leveys, korkeus = 640, 480
naytto = pygame.display.set_mode((leveys, korkeus))

roboimage = pygame.image.load("robo.png")
 
x = randint(0, leveys-roboimage.get_width())
y = randint(0, korkeus-roboimage.get_height())
 
while True:
    for tapahtuma in pygame.event.get():
        if tapahtuma.type == pygame.MOUSEBUTTONDOWN:
            hiiri_x = tapahtuma.pos[0]
            hiiri_y = tapahtuma.pos[1]
 
            osuma_x = hiiri_x >= x and hiiri_x <= x+roboimage.get_width()
            osuma_y = hiiri_y >= y and hiiri_y <= y+roboimage.get_height()
 
            if osuma_x and osuma_y:
                x = randint(0, leveys-roboimage.get_width())
                y = randint(0, korkeus-roboimage.get_height())
 
        if tapahtuma.type == pygame.QUIT:
            exit()
 
        naytto.fill((0, 0, 0))
        naytto.blit(roboimage, (x, y))
        pygame.display.flip()