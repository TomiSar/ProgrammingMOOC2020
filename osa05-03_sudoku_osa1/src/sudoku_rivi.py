# tee ratkaisu tänne
def rivi_oikein(sudoku: list, rivi: int):
    rivilista = []
    for i in sudoku[rivi]:
        if i > 0:
            rivilista.append(i)
            for numero in rivilista:
                if rivilista.count(numero) > 1:
                    return False
    return True            

# Tee funktio rivi_oikein(sudoku: list, rivi: int), joka saa parametriksi sudokuruudukkoa esittävän kaksiulotteisen 
# taulukon ja rivin numeron kertovan kokonaisluvun (rivit on numeroitu nollasta alkaen). Metodi palauttaa tiedon, 
# onko rivi oikein täytetty eli onko siinä kukin luvuista 1–9 korkeintaan kerran.
if __name__ == "__main__":
    sudoku = [
    [9, 0, 0, 0, 8, 0, 3, 0, 0],
    [2, 0, 0, 2, 5, 0, 7, 0, 0],
    [0, 2, 0, 3, 0, 0, 0, 0, 4],
    [2, 9, 4, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 7, 3, 0, 5, 6, 0],
    [7, 0, 5, 0, 6, 0, 4, 0, 0],
    [0, 0, 7, 8, 0, 3, 9, 0, 0],
    [0, 0, 1, 0, 0, 0, 0, 0, 3],
    [3, 0, 0, 0, 0, 0, 0, 0, 2]]
    print(rivi_oikein(sudoku, 0))
    print(rivi_oikein(sudoku, 1))
    #tulosta(sudoku)



    # def rivi_oikein(sudoku: list, rivi: int):
    # rivilista = []
    # for rivi in range(len(sudoku)):
    #     for i in sudoku[rivi]:
    #         if i in rivilista:
    #             return False
    #         elif i != 0:
    #             rivilista.append(i)
    # return True