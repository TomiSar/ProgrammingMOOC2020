#Solution
def pelaa_siirto(lauta: list, x: int, y: int, nappula: str):
    if x < 0 or y < 0 or x > 2 or y > 2:
        return False
    
    #Notify that y-coordinate is given first
    if lauta[y][x] == "":
        lauta[y][x] = nappula
        return True
    
    return False

if __name__ == "__main__":
    lauta = [["", "", ""], ["", "", ""], ["", "", ""]]
    print(pelaa_siirto(lauta,  0, 1, "X"))
    print(lauta)

