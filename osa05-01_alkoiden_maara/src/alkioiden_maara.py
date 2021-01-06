def laske_alkiot(lista, etsitty):
    loydetytalkiot = 0
    for rivi in lista:
        for alkio in rivi:
            if alkio == etsitty:
                loydetytalkiot += 1
    
    return loydetytalkiot


if __name__ == "__main__":
    m = [[1, 2, 1], [0, 3, 4], [1, 0, 0]]
    print(laske_alkiot(m, 1))