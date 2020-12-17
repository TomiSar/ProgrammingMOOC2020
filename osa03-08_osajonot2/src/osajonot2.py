# Kirjoita ratkaisu tähän
mjono = input("Anna merkkijono: ")
pituus = len(mjono) -1

while pituus >= 0:
    print(mjono[pituus:])
    pituus -= 1