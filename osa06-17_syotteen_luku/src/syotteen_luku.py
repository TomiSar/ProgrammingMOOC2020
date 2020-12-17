# tee ratkaisu tänne
def lue(syote, min: int, max: int):
    while True:
        try:
            syote = input("syötä luku: ")
            luku = int(syote)
            if luku >= min and luku <= max:
                return luku
            else:
                print("Syötteen on oltava kokonaisluku väliltä 5...10")    
        except ValueError:
            print("Syötteen on oltava kokonaisluku väliltä 5...10")


# if __name__ == "__main__":
#     luku = lue("syötä luku: ", 5, 10)
#     print("syötit luvun:", luku)
