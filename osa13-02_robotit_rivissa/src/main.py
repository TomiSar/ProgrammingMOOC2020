# Tee ohjelma, joka piirtää kymmenen robottia riviin.
import pygame

pygame.init()
pygame.display.set_caption("Robotit rivissä")
leveys, korkeus = 640, 480
naytto = pygame.display.set_mode((leveys, korkeus))

robotimage = pygame.image.load("robo.png")

naytto.fill((0, 0, 0))
# x-koordinaatin arvoa kasvatetaan robo.png (50px X 86px) leveyden verran jokaisella kierroksella, y-koordinaatti pysyy samana
for i in range(10):
    naytto.blit(robotimage, (50 + 50 * i, 100))
pygame.display.flip()

while True:
    for tapahtuma in pygame.event.get():
        if tapahtuma.type == pygame.QUIT:
            exit()