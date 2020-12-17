def tulosta_monesti(merkkijono, kertaa):
    while kertaa > 0:
        print(merkkijono)
        kertaa -= 1

# funktiota kannattaa testata kutsumalla sitä täällä seuraavasti
if __name__ == "__main__":
    merkkijono = input("Merkkijono: ")
    kertaa = int(input("Tulostuksia: "))
    tulosta_monesti(merkkijono, kertaa)