# tee ratkaisu tänne
from random import sample
def sanat(n: int, alku: str):
    lista = []
    sanalista = ""
 
    with open("sanat.txt") as tiedosto:
    
        for rivi in tiedosto:
            rivi = rivi.replace("\n", "")            
            rivi = rivi.strip() 
            if rivi.startswith(alku):
                lista.append(rivi)
    
        sanalista = sample(lista, n)
        return sanalista
 
 
if __name__ == '__main__':
    lista = sanat(5, "ab")
    for sana in lista:
        print(sana)