from random import sample

def heita(noppa: str):
    nopat = {
        "A": [3, 3, 3, 3, 3, 6],
        "B": [2, 2, 2, 5, 5, 5],
        "C": [1, 4, 4, 4, 4, 4]
    }
    return sample(nopat[noppa], 1)[0]

def pelaa(noppa1: str, noppa2: str, kertaa: int):
    v1 = 0
    v2 = 0
    t = 0
    for i in range(kertaa):
        n1 = heita(noppa1)
        n2 = heita(noppa2)
        if n1 > n2:
            v1 += 1
        elif n1 < n2:
            v2 += 1
        else:
            t += 1
    return v1, v2, t

#main
if __name__ == "__main__":
    tulos = pelaa("A", "C", 1000)
    print(tulos)
    tulos = pelaa("B", "B", 1000)
    print(tulos)
    # for i in range(20):
    #     print(heita("A"), " ", end="")
    # print()
    # for i in range(20):
    #     print(heita("B"), " ", end="")
    # print()
    # for i in range(20):
    #     print(heita("C"), " ", end="")