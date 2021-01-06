luku = int(input("Anna luku: "))
kohta = 1

while kohta+1 <= luku:
    print(kohta+1)      #1.tulostus kohta+1 --> luvut[2] kohta luvuista
    print(kohta)        #2.tulostus kohta   --> eka kohta luvuista
    kohta += 2          #kasvatetaan kohta arvo kahdella

if kohta <= luku:       #parittomat luvut viimeinen kohta 
    print(kohta)