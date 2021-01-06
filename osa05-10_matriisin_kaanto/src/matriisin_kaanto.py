def transponoi(matriisi: list):
    kopio = [[matriisi[j][i] for j in range(len(matriisi))] for i in range(len(matriisi[0]))]
    for i in range(len(matriisi)):
        for j in range(len(matriisi[0])):
            matriisi[i][j] = kopio[i][j]

if __name__ == "__main__":
    #transponoi([[1,2],[4,5]])
    transponoi([[1,2, 3],[4,5,6],[7,8,9]])