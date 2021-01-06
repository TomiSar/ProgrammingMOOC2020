def risunelio(pituus):
    i = 1
    while i <= pituus:
        print(pituus * "#")
        i += 1

# funktiota kannattaa testata kutsumalla sitä täällä seuraavasti
if __name__ == "__main__":
    risunelio(5)