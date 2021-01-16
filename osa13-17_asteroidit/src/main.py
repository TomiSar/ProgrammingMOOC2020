# Tee peli, jossa pelaaja ohjaa robottia vasemmalle ja oikealle ja tavoitteena on kerätä taivaalta putoavia asteroideja. 
# Pelaaja saa pisteen jokaisesta kerätystä asteroidista, ja pistemäärä näytetään ikkunan ylälaidassa. 
# Peli päättyy, kun pelaaja ei saa kiinni asteroidia.
import pygame
from random import randint
 
pygame.init()
leveys, korkeus = 640, 480
naytto = pygame.display.set_mode((leveys, korkeus))
 
pygame.display.set_caption("Asteroidit")
 
robot = pygame.image.load("robo.png")
x = 0
y = korkeus-robot.get_height()
 
kivi = pygame.image.load("kivi.png")
maara = 5
kohdat = []
for i in range(maara):
    kohdat.append([randint(0,leveys-kivi.get_width()),-randint(100,1000)])
 
oikealle = False
vasemmalle = False
pisteet = 0
 
kello = pygame.time.Clock()
 
fontti = pygame.font.SysFont("Arial", 24)
 
while True:
    for tapahtuma in pygame.event.get():
        if tapahtuma.type == pygame.KEYDOWN:
            if tapahtuma.key == pygame.K_LEFT:
                vasemmalle = True
            if tapahtuma.key == pygame.K_RIGHT:
                oikealle = True
 
        if tapahtuma.type == pygame.KEYUP:
            if tapahtuma.key == pygame.K_LEFT:
                vasemmalle = False
            if tapahtuma.key == pygame.K_RIGHT:
                oikealle = False
 
        if tapahtuma.type == pygame.QUIT:
            exit()
 
    if oikealle:
        x += 2
    if vasemmalle:
        x -= 2
 
    for i in range(maara):
        kohdat[i][1] += 1
        if kohdat[i][1]+kivi.get_height() >= korkeus:
            # peli päättyy
            exit()
        if kohdat[i][1]+kivi.get_height() >= y:
            robo_keski = x+robot.get_width()/2
            kivi_keski = kohdat[i][0]+kivi.get_width()/2
            if abs(robo_keski-kivi_keski) <= (robot.get_width()+kivi.get_width())/2:
                # robotti sai asteroidin kiinni
                kohdat[i][0] = randint(0,leveys-kivi.get_width())
                kohdat[i][1] = -randint(100,1000)
                pisteet += 1
 
    naytto.fill((0, 0, 0))
    naytto.blit(robot, (x, y))
    for i in range(maara):
        naytto.blit(kivi, (kohdat[i][0], kohdat[i][1]))
 
    teksti = fontti.render("Pisteet: "+str(pisteet), True, (255, 0, 0))
    naytto.blit(teksti, (leveys-150, 10))
 
    pygame.display.flip()
 
    kello.tick(60)