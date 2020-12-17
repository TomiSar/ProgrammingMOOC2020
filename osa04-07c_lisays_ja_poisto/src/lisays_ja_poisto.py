# Kirjoita ratkaisu tähän
lista = []
i = 1

print(f"Lista on nyt {lista}")
while True:
    valinta = input("(l)isää, (p)oista vai e(x)it: ")
    if valinta == 'x':
        break
    if valinta == 'l':
        lista.append(i)
        i += 1
    if valinta == 'p':
        i -= 1
        lista.remove(i)
    print(f"Lista on nyt {lista}")

print('Moi!')