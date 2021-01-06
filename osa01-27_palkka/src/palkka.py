tuntipalkka = float(input("Tuntipalkka: "))
tunnit = int(input("Työtunnit: "))
paiva = input("Viikonpäivä :")

palkka = tuntipalkka * tunnit
if paiva == "sunnuntai":
    palkka *= 2
print("Palkka",palkka,"euroa")