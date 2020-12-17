# tee ratkaisu tänne
def pisin(lista):
    pisinmj = lista[0]
    for merkkijono in lista:
        if len(pisinmj) < len(merkkijono):
            pisinmj = merkkijono
    
    return pisinmj

if __name__ == "__main__":
    jonot = ["moi", "moikka", "heip", "hellurei", "terve"]
    print(pisin(jonot))