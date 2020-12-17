# Kirjoita ratkaisu tähän
yritykset = 1

while True:
    pin = input("PIN-koodi: ")
    if pin == "4321":
         break
    print("Väärin")
    yritykset += 1

if yritykset == 1:
    print("Oikein, tarvitsit vain yhden yrityksen!")
else:
    print("Oikein, tarvitsit",yritykset,"yritystä")