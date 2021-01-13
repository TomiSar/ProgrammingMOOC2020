def poista_pienin(luvut):
    luvut.remove(min(luvut))


if __name__ == "__main__":
    luvut = [2, 4, 6, 1, 3, 5]
    poista_pienin(luvut)
    print(luvut)