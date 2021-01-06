def keskiarvo(lista):
    return sum(lista) / len(lista)

# funktiota kannattaa testata kutsumalla sitä täällä seuraavasti
if __name__ == "__main__":
    lista = [1, 2, 3, 4, 5]
    vastaus = keskiarvo(lista)
    print("vastaus", vastaus)
