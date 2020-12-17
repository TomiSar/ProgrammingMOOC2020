# Kirjoita ratkaisu tähän
ika = int(input("Kerro ikäsi? "))
if ika < 0:
    print("Taitaa olla virhe")
elif ika < 5:
    print("En usko, että osaat kirjoittaa...")
else:
    print("Ok, olet siis " + str(ika) + "-vuotias")