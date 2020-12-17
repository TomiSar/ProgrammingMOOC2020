# tee ratkaisu tänne
def tallenna_henkilo(henkilo: tuple):
   with open("henkilot.csv", "a") as h:
      h.write(f'{henkilo[0]};{str(henkilo[1])};{str(henkilo[2])}\n')
 
if __name__ == '__main__':
   tallenna_henkilo(("Kimmo Kimmonen", 37, 175.5))
   #tallenna_henkilo("Maija-Pirkko Virtanen-Lahtinen", 65, 155.5)
