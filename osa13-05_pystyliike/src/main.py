# Tee animaatio, jossa robotti liikkuu vuorotellen ylös ja alas.
import pygame

pygame.init()
pygame.display.set_caption("Pystyliike")
leveys, korkeus = 640, 480
naytto = pygame.display.set_mode((640, 480))

robotimage = pygame.image.load("robo.png")

x = 0
y = 0
nopeus = 1
kello = pygame.time.Clock()

while True:
    for tapahtuma in pygame.event.get():
        if tapahtuma.type == pygame.QUIT:
            exit()

    naytto.fill((0, 0, 0))
    naytto.blit(robotimage, (x, y))
    pygame.display.flip()

    y += nopeus
    # robotti suunta muuttuu jos se törmää alaseinään
    if nopeus > 0 and y + robotimage.get_height() >= korkeus:
        nopeus = -nopeus
    # robotti suunta muuttuu jos se törmää yläseinään 
    if nopeus < 0 and y <= 0:
        nopeus = -nopeus
    
    kello.tick(60)