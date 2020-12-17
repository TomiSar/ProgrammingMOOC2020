# tee ratkaisu tänne
def tulosta(sudoku: list):
    r = 0
    for rivi in sudoku:
        s = 0
        for merkki in rivi:
            s += 1
            if merkki == 0:
                merkki = "_"
            m = f"{merkki} "
            if s%3 == 0 and s < 8:
                m += " "
            print(m, end="")
 
        print()
        r += 1
        if r%3 == 0 and r < 8:
            print()
 
def lisays(sudoku: list, rivi: int, sarake: int, luku: int):
    sudoku[rivi][sarake] = luku

if __name__ == "__main__":
    sudoku  = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0]]
    
    tulosta(sudoku)
    lisays(sudoku, 0, 0, 2)
    lisays(sudoku, 1, 2, 7)
    lisays(sudoku, 5, 7, 3)
    print()
    print("Kolme numeroa lisätty:")
    print()
    tulosta(sudoku)
    print()

# miten saan sinne välit 
# esim laittamalla mukaan laskurimuuttujat, jotka muistaa kuinka mones sareake/rivi tulostettiin
#sinne sopivat ifit sekaan, jotka kattoo tuleeko tulostaa ekstraväli/rivi

