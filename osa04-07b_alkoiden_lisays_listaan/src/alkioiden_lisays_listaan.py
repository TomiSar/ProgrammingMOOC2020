# Kirjoita ratkaisu tähän
lista = []
luvut = int(input("Kuinka monta lukua: "))
i = 1
while i <= luvut:
    luku = int(input(f"Anna luku {i}: "))
    lista.append(luku)
    i += 1

print(lista)