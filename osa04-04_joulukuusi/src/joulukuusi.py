# tee ratkaisu tänne
def joulukuusi(korkeus):
    print('joulukuusi!')
    tahdet = "*"
    i = 1
    while i <= korkeus:
        print(" " * (korkeus - i) + tahdet)
        tahdet += "**"
        i += 1
    #Kuusen jalka
    print(" " * (korkeus - 1) + "*")

# funktiota kannattaa testata kutsumalla sitä täällä seuraavasti
if __name__ == "__main__":
    joulukuusi(5)