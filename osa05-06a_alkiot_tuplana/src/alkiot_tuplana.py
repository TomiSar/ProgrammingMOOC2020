# tee ratkaisu tänne
def tuplaa_alkiot(luvut):
    tuplana = []
    for luku in luvut:
        tuplana.append(luku * 2)
    
    return tuplana


if __name__ == "__main__":
    luvut = [2, 4, 5, 3, 11, -4]
    tuplaluvut = tuplaa_alkiot(luvut)
    print(tuplaluvut)