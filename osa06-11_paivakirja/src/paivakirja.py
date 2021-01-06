while True:
    
    print("1 - lisää merkintä, 2 - lue merkinnät, 0 - lopeta")
    komento = int(input("Valinta: "))
    if komento == 0:
        print("Heippa!")
        break
    elif komento == 1:
        lause = input("Anna merkintä: ")
        print("Päiväkirja tallennettu")
        with open("paivakirja.txt", "a") as tiedosto:
            tiedosto.write(lause + "\n")
    elif komento == 2:
        print("Merkinnät:")
        with open("paivakirja.txt", "r") as tiedosto:
                print("Merkinnät: ")
                print(tiedosto.read())