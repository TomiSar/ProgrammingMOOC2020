from math import *

def hypotenuusa(kateetti1: float, kateetti2: float):
    return sqrt(pow(kateetti1, 2) + pow(kateetti2, 2))


if __name__ == "__main__":
    print(hypotenuusa(3,4)) # 5.0
    print(hypotenuusa(5,12)) # 13.0
    print(hypotenuusa(1,1)) # 1.4142135623730951
