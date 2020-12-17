# tee ratkaisu tänne
def summa():
    with open("matriisi.txt") as tiedosto:
        tulos=int()
        lista=[]
        for rivi in tiedosto:
            rivi = rivi.replace("\n", "")
            rivi = rivi.split(",")
            lista.append(rivi)
        for i in lista:
            for j in i:
                tulos+=int(j)
        return tulos
#summa()
 
def maksimi():
    with open("matriisi.txt") as tiedosto:
        tulos=int()
        lista=[]
        for rivi in tiedosto:
            rivi = rivi.replace("\n", "")
            rivi = rivi.split(",")
            lista.append(rivi)
        for i in lista:
            for j in i:
                if int(j) > tulos:
                    tulos = int(j)
        return tulos
#maksimi()
 
def rivisummat():
    with open("matriisi.txt") as tiedosto:
        lista=[]
        for rivi in tiedosto:
            rivi = rivi.replace("\n", "")
            rivi = rivi.split(",")
            lista.append(rivi)
        tulokset=[]
 
        while True:
            count=0
            alkio=int()
            x=0
            y=1
 
            while y <= len(lista):
                for i in lista[x:y]:
                    while count < len(lista):
                        for j in i:
                            alkio+=int(j)
                            count+=1
                tulokset.append(alkio)  
                alkio=0
                count=0        
                x+=1
                y+=1
            break
        return tulokset
       # return tulos
#rivisummat()

if __name__ == "__main__":
    summa()
    maksimi()
    rivisummat