from math import sqrt

while True:
    luku = float(input("Syötä luku: "))
    if luku == 0:
        break
    
    if (luku > 0):
        print(sqrt(luku)) 
    else:
        print("Epäkelpo luku")    

print("Lopetetaan...")