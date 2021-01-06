def rivi_oikein(sudoku: list, rivi: int):
    luvut = []
    for luku in sudoku[rivi]:
        if luku > 0 and luku in luvut:
            return False
        luvut.append(luku)
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