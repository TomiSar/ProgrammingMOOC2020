def shakkilauta(koko):
    i = 0
    while i < koko:
        if i % 2 == 0:
            rivi = "10" * koko  #parilliset rivit tulostetaan "pari" 10
        else:
            rivi = "01" * koko  #parittomat rivit tulostetaan "pari" 01 *
        # poistetaan rivin lopusta ylimääräiset merkit
        print(rivi[0:koko])
        i += 1

# kokeillaan funktiota kutsumalla sitä täällä seuraavasti
if __name__ == "__main__":
    shakkilauta(5)
