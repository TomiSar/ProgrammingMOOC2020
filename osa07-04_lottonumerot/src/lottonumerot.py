from random import randint

def lottonumerot(maara: int, alaraja: int, ylaraja: int):
    lista = []
    i = 1
    while (i <= maara):
        numero = randint(alaraja, ylaraja)
        if numero not in lista:
            lista.append(numero)
        i += 1
        
    return sorted(lista)


if __name__ == "__main__":
    for numero in lottonumerot(3, 2, 22):
        print(numero)