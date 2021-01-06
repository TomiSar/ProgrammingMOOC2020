def viiva(leveys: int, merkkijono: str):
    if merkkijono == "":
        merkkijono = "*"
    print(merkkijono[0] * leveys) 

# funktiota kannattaa testata kutsumalla sitä täällä seuraavasti
if __name__ == "__main__":
    viiva(5, "-")
    viiva(10, "LOL")
    viiva(7, "%")
    viiva(3, "")
