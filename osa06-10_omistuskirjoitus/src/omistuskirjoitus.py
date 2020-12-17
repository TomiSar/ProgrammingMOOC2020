# tee ratkaisu tänne
nimi = input("Kenelle teos omistetaan: ")
output = input("Mihin kirjoitetataan: ")

with open(output, "w") as tiedosto:
    tiedosto.write(f"Hei {nimi}, toivomme viihtyisiä hetkiä python-kurssimateriaalin parissa! Terveisin mooc.fi-tiimi")