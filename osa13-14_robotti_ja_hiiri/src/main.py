# Tee ohjelma, jossa robotti seuraa hiirtä niin, että robotin keskikohta on aina hiiren kohdalla.
import pygame
 
pygame.init()
pygame.display.set_caption("Robotti ja hiiri")
leveys, korkeus = 640, 480
naytto = pygame.display.set_mode((leveys, korkeus))
 
roboimage = pygame.image.load("robo.png")
 
while True:
    for tapahtuma in pygame.event.get():
        if tapahtuma.type == pygame.MOUSEMOTION:
            x = tapahtuma.pos[0]-roboimage.get_width()/2
            y = tapahtuma.pos[1]-roboimage.get_height()/2
 
            naytto.fill((0, 0, 0))
            naytto.blit(roboimage, (x, y))
            pygame.display.flip()
 
        if tapahtuma.type == pygame.QUIT:
            exit()