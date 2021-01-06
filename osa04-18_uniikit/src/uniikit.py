def uniikit(lista):
    uniikit = []
    for alkio in lista:
        if alkio not in uniikit:
            uniikit.append(alkio)

    return sorted(uniikit)

if __name__ == "__main__":
    lista = [3, 2, 2, 1, 3, 3, 1]
    print(uniikit(lista)) # [1, 2, 3]