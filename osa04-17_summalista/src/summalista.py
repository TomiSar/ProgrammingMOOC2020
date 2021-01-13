def summa(lista1, lista2):
    summalista = []
    for i in range(len(lista1)):
        summalista.append(lista1[i] + lista2[i])

    return summalista


if __name__ == "__main__":
    a = [1, 2, 3]
    b = [7, 8, 9]
    print(summa(a, b)) # [8, 10, 12]a = [1, 2, 3]
    b = [7, 8, 9]
    print(summa(a, b)) # [8, 10, 12]