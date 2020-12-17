import random
import string

# tee ratkaisu tänne
def luo_salasana(pituus: int):
    merkit = string.ascii_lowercase
    salasana = ''.join(random.choice(merkit) for i in range(pituus))
    return salasana

if __name__ == "__main__":
    for i in range(10):
        print(luo_salasana(8))
