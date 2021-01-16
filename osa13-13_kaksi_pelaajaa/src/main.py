# Tee ohjelma, jossa kaksi pelaajaa voi ohjata omia robottejaan. Toinen pelaaja käyttää nuolinäppäimiä ja toinen esimerkiksi w-s-a-d.
import pygame
 
pygame.init()
pygame.display.set_caption("Kaksi pelaajaa")
leveys, korkeus = 640, 480
naytto = pygame.display.set_mode((leveys, korkeus))
 
robotimage = pygame.image.load("robo.png")
 
# robottien kohdat
kohdat = [[0, 0],
          [leveys-robotimage.get_width(), korkeus-robotimage.get_height()]]
 
napit = []
# nappi, kumpi robotti liikkuu, vaakaliike, pystyliike
napit.append((pygame.K_LEFT, 0, -2, 0))
napit.append((pygame.K_RIGHT, 0, 2, 0))
napit.append((pygame.K_UP, 0, 0, -2))
napit.append((pygame.K_DOWN, 0, 0, 2))
napit.append((pygame.K_a, 1, -2, 0))
napit.append((pygame.K_d, 1, 2, 0))
napit.append((pygame.K_w, 1, 0, -2))
napit.append((pygame.K_s, 1, 0, 2))
 
kello = pygame.time.Clock()
 
painettu = {}
 
while True:
    for tapahtuma in pygame.event.get():
        if tapahtuma.type == pygame.KEYDOWN:
            painettu[tapahtuma.key] = True
 
        if tapahtuma.type == pygame.KEYUP:
            del painettu[tapahtuma.key]
 
        if tapahtuma.type == pygame.QUIT:
            exit()
 
    for nappi in napit:
        if nappi[0] in painettu:
            kohdat[nappi[1]][0] += nappi[2]
            kohdat[nappi[1]][1] += nappi[3]
 
    naytto.fill((0, 0, 0))
    for i in range(2):
        naytto.blit(robotimage, (kohdat[i][0], kohdat[i][1]))
    pygame.display.flip()
 
    kello.tick(60)