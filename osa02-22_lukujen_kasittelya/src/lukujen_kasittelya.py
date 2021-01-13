print("Syötä kokonaislukuja, 0 lopettaa:")
luvut = 0
summa = 0
positiiviset = 0

while True:
    luku = int(input("Luku: "))
    if luku == 0:
        break
    
    luvut += 1
    summa += luku
    if luku > 0:
        positiiviset += 1
        
print(f"Lukuja yhteensä {luvut}") 
print(f"Lukujen summa {summa}")
print(f"Lukujen keskiarvo {summa / luvut}")
print(f"Positiivisia {positiiviset}")
print(f"Negatiivisia {luvut - positiiviset}")