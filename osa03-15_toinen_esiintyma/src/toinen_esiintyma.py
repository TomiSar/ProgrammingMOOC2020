jono = input("Anna merkkijono: ")
osajono = input("Anna osajono: ")

eka = jono.find(osajono) #eka esiintymä
jono = jono[eka + 1:]   #kasvatetaan eka esiintyminen indeksiä yhdellä ja jatketaan hakua
toka = jono.find(osajono) #katsotaan löytyykö merkkijonosta toista esiintymää
if toka != -1:
    print("Osajonon toinen esiintymä on kohdassa " + str(eka + toka + 1) + ".")
else:
    print("Osajono ei esiinny merkkijonossa kahdesti.")