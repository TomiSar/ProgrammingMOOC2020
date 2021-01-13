# Tee animaatio, jossa kaksi robottia kulkee näytöllä vuorotellen oikealle ja vasemmalle.
import pygame

pygame.init()
pygame.display.set_caption("Kaksi robottia")
leveys, korkeus = 640, 480
naytto = pygame.display.set_mode((640, 480))

robotimage = pygame.image.load("robo.png")

x1 = 0
x2 = 0
nopeus1 = 1
nopeus2 = 2
kello = pygame.time.Clock()

while True:
    for tapahtuma in pygame.event.get():
        if tapahtuma.type == pygame.QUIT:
            exit()

    x1 += nopeus1   #ylempi robotti
    if x1 == 0 or x1 + robotimage.get_width() == leveys:
        nopeus1 = -nopeus1
    x2 += nopeus2   #alempi robotti
    if x2 == 0 or x2 + robotimage.get_width() == leveys:
        nopeus2 = -nopeus2
    
    naytto.fill((0, 0, 0))
    naytto.blit(robotimage, (x1, 50))
    naytto.blit(robotimage, (x2, 200))
    pygame.display.flip()

    kello.tick(60)