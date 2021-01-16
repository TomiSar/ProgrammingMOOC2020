# Tee animaatio, jossa pallo kimpoaa ikkunan reunoilta.
import pygame
import math
 
pygame.init()
pygame.display.set_caption("Pomppiva pallo")
leveys, korkeus = 640, 480
naytto = pygame.display.set_mode((leveys, korkeus))
 
pallo = pygame.image.load("pallo.png")
 
x = 0
y = 0
nopeus_x = 2
nopeus_y = 2
kello = pygame.time.Clock()
 
while True:
    for tapahtuma in pygame.event.get():
        if tapahtuma.type == pygame.QUIT:
            exit()
 
    x += nopeus_x
    y += nopeus_y
 
    if x == 0 or x+pallo.get_width() == leveys:
        nopeus_x = -nopeus_x
    if y == 0 or y+pallo.get_height() == korkeus:
        nopeus_y = -nopeus_y
 
    naytto.fill((0, 0, 0))
    naytto.blit(pallo, (x, y))
    pygame.display.flip()
 
    kello.tick(60)
