def tallenna_henkilo(henkilo: tuple):
   # CSV nimi(string);ika(int);pituus(float) --> lisätään tiedostoon merkkijonona
   with open ("henkilot.csv", "a") as tiedosto:
      henkilotieto = henkilo[0] + ";" + str(henkilo[1]) + ";" + str(henkilo[2])
      tiedosto.write(henkilotieto + "\n")
 
#main
if __name__ == '__main__':
   tallenna_henkilo(("Kimmo Kimmonen", 37, 175.5))
   tallenna_henkilo(("Maija-Pirkko Virtanen-Lahtinen", 65, 162.0))
   tallenna_henkilo(("Timo Jutila", 50, 170))