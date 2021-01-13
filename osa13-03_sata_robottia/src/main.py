import pygame

pygame.init()
pygame.display.set_caption("Sata robottia")
leveys, korkeus = 640, 480
naytto = pygame.display.set_mode((leveys, korkeus))

robotimage = pygame.image.load("robo.png")

naytto.fill((0, 0, 0))
# # i = rivit ja j = robotit kpl
for i in range(10):
    for j in range(10):
        naytto.blit(robotimage, (20+10*i+40*j, 100+i*20))
pygame.display.flip()

while True:
    for tapahtuma in pygame.event.get():
        if tapahtuma.type == pygame.QUIT:
            exit()