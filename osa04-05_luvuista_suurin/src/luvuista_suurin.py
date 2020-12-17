# tee ratkaisu tänne
def luvuista_suurin(luku1, luku2, luku3):
    if luku2 < luku1 > luku3:
        return luku1
    elif luku2 > luku3:
        return luku2  
    else:
        return luku3

# funktiota kannattaa testata kutsumalla sitä täällä seuraavasti
if __name__ == "__main__":
    suurin = luvuista_suurin(11, 4, 8)
    print(suurin)
