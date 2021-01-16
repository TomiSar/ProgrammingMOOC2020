# Tee animaatio, jossa taivaalta tippuu satunnaisesti robotteja. Kun robotti laskeutuu maahan, 
# se lähtee joko vasemmalle tai oikealle ja katoaa lopuksi ruudulta.
import pygame
from random import randint

pygame.init()
pygame.display.set_caption("Robotti-invaasio")
leveys, korkeus = 640, 480
naytto = pygame.display.set_mode((leveys, korkeus))

robotimage = pygame.image.load("robo.png")

# robottien määrä (samoja robotteja kierrätetään)
maara = 20
 
robot = []
for i in range(maara):
    # aiheuttaa että alkupaikka arvotaan heti
    robot.append([-1000,korkeus])
 
kello = pygame.time.Clock()
 
while True:
    for tapahtuma in pygame.event.get():
        if tapahtuma.type == pygame.QUIT:
            exit()
 
    for i in range(maara):
        if robot[i][1]+robotimage.get_height() < korkeus:
            # robotti putoaa alaspäin
            robot[i][1] += 1
        else:
            if robot[i][0] < -robotimage.get_width() or robot[i][0] > leveys:
                # arvotaan uusi alkupaikka
                robot[i][0] = randint(0,leveys-robotimage.get_width())
                robot[i][1] = -randint(100,1000)
            elif robot[i][0]+robotimage.get_width()/2 < leveys/2:
                # robotti liikkuu vasemmalle
                robot[i][0] -= 1
            else:
                # robotti liikkuu oikealle
                robot[i][0] += 1
 
    naytto.fill((0, 0, 0))
    for i in range(maara):
        naytto.blit(robotimage, (robot[i][0], robot[i][1]))
    pygame.display.flip()
 
    kello.tick(60)