from fractions import Fraction
# tee ratkaisu tänne
def jaa_palasiksi(maara: int):
    i = 0
    lista = []
    while i < maara:
        lista.append(Fraction(1, maara))
        i += 1
    return lista


if __name__ == "__main__":
    for p in jaa_palasiksi(3):
        print(p)
    print()
    print(jaa_palasiksi(5))