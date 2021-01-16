# Tee ohjelma, joka näyttää graafisesti kellonajan.
import pygame
import math
from datetime import datetime

pygame.init()
leveys, korkeus = 640, 480
naytto = pygame.display.set_mode((640, 480))

def ympyra(vari: int, sade: int):
    pygame.draw.circle(naytto, vari, (keski_x, keski_y), sade)
 
def viisari(pituus: int, paksuus: int, osuus: float):
    kulma = 2*math.pi*osuus-math.pi/2
    loppu_x = keski_x+math.cos(kulma)*pituus
    loppu_y = keski_y+math.sin(kulma)*pituus
 
    pygame.draw.line(naytto, (0, 0, 255), (keski_x, keski_y), (loppu_x, loppu_y), paksuus)
 
while True:
    for tapahtuma in pygame.event.get():
        if tapahtuma.type == pygame.QUIT:
            exit()
 
    tunnit = datetime.now().hour%12
    minuutit = datetime.now().minute
    sekunnit = datetime.now().second
 
    pygame.display.set_caption(str(datetime.now().time())[:8])
 
    naytto.fill((0, 0, 0))
 
    keski_x = leveys/2
    keski_y = korkeus/2
 
    ympyra((255, 0, 0), 200)
    ympyra((0, 0, 0), 195)
    ympyra((255, 0, 0), 10)
 
    viisari(185, 1, sekunnit/60)
    viisari(180, 2, (minuutit+sekunnit/60)/60)
    viisari(150, 5, (tunnit+minuutit/60+sekunnit/3600)/12)
 
    pygame.display.flip()