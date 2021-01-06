def kumpi_voitti(pelilauta: list):
    pelaaja1 = 0
    pelaaja2 = 0

    for rivi in pelilauta:
        for ruutu in rivi:
            if ruutu == 1:
                pelaaja1 +=1
            elif ruutu == 2:
                pelaaja2 += 1

    if pelaaja1 > pelaaja2:
        return 1
    if pelaaja2 > pelaaja1:
        return 2
    else:
        return 0
    

#Funktio palauttaa arvon 1, jos pelaaja 1 on voittanut pelin, ja arvon 2, jos pelaaja 2 on voittanut pelin. 
# Jos molemmilla pelaajilla on yhtä paljon nappuloita laudalla, funktio palauttaa arvon 0.
if __name__ == "__main__":
    lauta = [ [1,2,1], [1,0,2], [0,2,2] ]
    print(kumpi_voitti(lauta))