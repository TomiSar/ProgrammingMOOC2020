# tee ratkaisu tänne
def samat(merkkijono, indeksi1, indeksi2):
    if indeksi1 >= len(merkkijono) or indeksi2 >= len(merkkijono):
        return False
    return merkkijono[indeksi1] == merkkijono[indeksi2]

# funktiota kannattaa testata kutsumalla sitä täällä seuraavasti
if __name__ == "__main__":
    print(samat("koodari", 1, 2))
