# Tee funktio pituudet(listat: list) joka saa parametriksi listan, joka sisältää listoja, 
# jotka sisältävät kokonaislukuja. Funktio palauttaa listan, joka sisältää parametrina olevien listojen pituudet.
def pituudet(listat: list):
    return [len(lista) for lista in listat]

# main
if __name__ == "__main__":
    listat = [[1,2,3,4,5], [324, -1, 31, 7],[]]
    print(pituudet(listat))