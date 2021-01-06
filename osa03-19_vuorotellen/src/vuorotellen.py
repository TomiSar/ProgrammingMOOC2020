luku = int(input("Anna luku: "))
vasen = 1
oikea = luku

while vasen < oikea:
    print(vasen)        #1.tulostus kohta 1
    print(oikea)         #2.tulostus kohta = luku
    vasen += 1
    oikea -= 1          #kasvatetaan kohta arvo kahdella

if vasen == oikea:       #parittomat luvut viimeinen kohta
    print(vasen)