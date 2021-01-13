def positiivisten_summa(lista):
    positiivisetsumma = 0
    for alkio in lista:
        if alkio > 0:
            positiivisetsumma += alkio
    return positiivisetsumma

if __name__ == "__main__":
    lista = [1, -2, 3, -4, 5]
    vastaus = positiivisten_summa(lista)
    print("vastaus", vastaus)