# Kirjoita ratkaisu tähän
# Kirjoita ratkaisu tähän
lista = []

while True:
    luku = int(input("Anna luku: "))
    if luku == 0:
        break
    lista.append(luku)
    print(f"Lista: {lista}")
    print(f"Järjestettynä: {sorted(lista)}")

print("Moi!")