# Tee animaatio, jossa robotti kiertää ympäri ikkunan reunaa.
import pygame

pygame.init()
pygame.display.set_caption("Reunan kierto")
leveys, korkeus = 640, 480
naytto = pygame.display.set_mode((640, 480))

robotimage = pygame.image.load("robo.png")

x = 0
y = 0
nopeus = 1
suunta = 1 # suunta 1 = oikea, 2 = alas, 3 = vasen, 4 = ylös
kello = pygame.time.Clock()

while True:
    for tapahtuma in pygame.event.get():
        if tapahtuma.type == pygame.QUIT:
            exit()

    naytto.fill((0, 0, 0))
    naytto.blit(robotimage, (x, y))
    pygame.display.flip()

    if suunta == 1:                                 # suunta oikea 
        x += nopeus
        if x + robotimage.get_width() == leveys:    # oikea seinä törmäys => suunta alas
            suunta = 2                              
    elif suunta == 2:                               # suunta alas
        y += nopeus
        if y + robotimage.get_height() == korkeus:  # alin seinä törmäys => suunta vasen
            suunta = 3                              
    elif suunta == 3:                               # suunta vasen 
        x -= nopeus
        if x == 0:                                  # vasen seinä törmäys => suunta ylös
            suunta = 4
    elif suunta == 4:                               # suunta ylös
        y -= nopeus
        if y == 0:                                  # ylin seinä törmäys => suunta oikea
            suunta = 1
    
    kello.tick(60)