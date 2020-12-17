# tee ratkaisu tänne
#rivi oikein
def rivi_oikein(sudoku: list, rivi: int):
    luvut = []
    for luku in sudoku[rivi]:
        if luku > 0 and luku in luvut:
            return False
        luvut.append(luku)
    return True

#sarake oikein
def sarake_oikein(sudoku: list, sarake: int):
    luvut = []
    for rivi in sudoku:
        luku = rivi[sarake]
        if luku > 0 and luku in luvut:
            return False
        luvut.append(luku)
    return True

#neliö oikein
def nelio_oikein(sudoku: list, rivi: int, sarake: int):
    luvut = []
    for r in range(rivi, rivi+3):
        for s in range(sarake, sarake+3):
            luku = sudoku[r][s]
            if luku > 0 and luku in luvut:
                return False
            luvut.append(luku)
    return True

#sudoku oikein
def sudoku_oikein(sudoku: list):
    tulokset = []
    
    rivi = 0
    while rivi < 9:
        tulokset.append(rivi_oikein(sudoku, rivi))
        rivi += 1

    sarake = 0
    while sarake < 9:
        tulokset.append(sarake_oikein(sudoku, sarake))
        sarake += 1

    neliot = [[0, 0], [0, 3], [0, 6], [3, 0], [3, 3], [3, 6], [6, 0], [6, 3], [6, 6]]

    i = 0
    while i < 9:
        tulokset.append(nelio_oikein(sudoku, neliot[i][0], neliot[i][1]))
        i += 1
    print(tulokset)

    for tulos in tulokset:
        if tulos is False:
            return False
            
    return True

#kutsutaan pääohjelmaa
if __name__ == "__main__":
    sudoku1 = [
    [9, 0, 0, 0, 8, 0, 3, 0, 0],
    [2, 0, 0, 2, 5, 0, 7, 0, 0],
    [0, 2, 0, 3, 0, 0, 0, 0, 4],
    [2, 9, 4, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 7, 3, 0, 5, 6, 0],
    [7, 0, 5, 0, 6, 0, 4, 0, 0],
    [0, 0, 7, 8, 0, 3, 9, 0, 0],
    [0, 0, 1, 0, 0, 0, 0, 0, 3],
    [3, 0, 0, 0, 0, 0, 0, 0, 2]
    ]

    print(sudoku_oikein(sudoku1))

    sudoku2 = [
    [2, 6, 7, 8, 3, 9, 5, 0, 4],
    [9, 0, 3, 5, 1, 0, 6, 0, 0],
    [0, 5, 1, 6, 0, 0, 8, 3, 9],
    [5, 1, 9, 0, 4, 6, 3, 2, 8],
    [8, 0, 2, 1, 0, 5, 7, 0, 6],
    [6, 7, 4, 3, 2, 0, 0, 0, 5],
    [0, 0, 0, 4, 5, 7, 2, 6, 3],
    [3, 2, 0, 0, 8, 0, 0, 5, 7],
    [7, 4, 5, 0, 0, 3, 9, 0, 1]
    ]

    print(sudoku_oikein(sudoku2))