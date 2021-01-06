lampotila = int(input("Lämpötila: "))
sade = input("Sataako (kyllä/ei): ")
print("Pue housut ja t-paita")
if lampotila < 21:
    print("Ota myös pitkähihainen paita")
if lampotila < 11:
    print("Pue päälle takki")
if lampotila < 6:
    print("Suosittelen lämmintä takkia")
    print("Kannattaa ottaa myös hanskat")
if sade == "kyllä":
    print("Muista sateenvarjo!")