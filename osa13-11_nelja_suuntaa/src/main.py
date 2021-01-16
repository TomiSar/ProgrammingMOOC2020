# Tee ohjelma, jossa pelaaja pystyy ohjaamaan robottia neljään suuntaan nuolinäppäimillä.
import pygame

pygame.init()
pygame.display.set_caption("Neljä suuntaa")
leveys, korkeus = 640, 480
naytto = pygame.display.set_mode((640, 480))

robotimage = pygame.image.load("robo.png")
x = leveys/2 - robotimage.get_width()/2
y = korkeus/2 - robotimage.get_height()/2 

oikea = False
vasen = False
ylos = False
alas = False 

kello = pygame.time.Clock()
while True:
    for tapahtuma in pygame.event.get():
        if tapahtuma.type == pygame.KEYDOWN:
            if tapahtuma.key ==  pygame.K_RIGHT:
                oikea = True
            if tapahtuma.key ==  pygame.K_LEFT:
                vasen = True
            if tapahtuma.key ==  pygame.K_UP:
                ylos = True
            if tapahtuma.key ==  pygame.K_DOWN:
                alas = True

        if tapahtuma.type == pygame.KEYUP:
            if tapahtuma.key == pygame.K_RIGHT:
                oikea = False
            if tapahtuma.key == pygame.K_LEFT:
                vasen = False
            if tapahtuma.key == pygame.K_UP:
                ylos = False
            if tapahtuma.key == pygame.K_DOWN:
                alas = False

        if tapahtuma.type == pygame.QUIT:
            exit()
    
    if oikea:
        x += 2
    if vasen:
        x -= 2
    if ylos:
        y -= 2
    if alas:
        y += 2

    naytto.fill((0, 0, 0))
    naytto.blit(robotimage,(x, y))
    pygame.display.flip()

    kello.tick(60)