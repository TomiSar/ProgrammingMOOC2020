# Tee ohjelma, joka piirtää robotin jokaiseen ikkunan neljään nurkkaan.
import pygame

pygame.init()
pygame.display.set_caption("Neljä robottia")
leveys, korkeus = 640, 480
naytto = pygame.display.set_mode((leveys, korkeus))

robotimage = pygame.image.load("robo.png")

oikea_x = leveys - robotimage.get_width()
ala_y = korkeus - robotimage.get_height()

# Piirretään robotit: vasen yläkulma, oikea yläkulma, vasen alakulma, oikea alakulma
naytto.fill((0,0,0))
naytto.blit(robotimage, (0, 0))
naytto.blit(robotimage, (oikea_x, 0))
naytto.blit(robotimage, (0, ala_y))
naytto.blit(robotimage, (oikea_x, ala_y))
pygame.display.flip()

while True:
    for tapahtuma in pygame.event.get():
        if tapahtuma.type == pygame.QUIT:
            exit()