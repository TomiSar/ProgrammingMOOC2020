# Kirjoita ratkaisu tähän
sanat = []
while True:
    sana = input("sana: ")
    if sana in sanat:
        break
    sanat.append(sana)
print("Annoit",len(sanat),"eri sanaa")