from datetime import datetime, timedelta

paiva = int(input("Päivä: "))
kuukausi = int(input("Kuukausi: "))
vuosi = int(input("Vuosi: "))

syntymavuosi = datetime(vuosi, kuukausi, paiva)
vuosituhat = datetime(1999, 12, 31)
if syntymavuosi > vuosituhat:
    print('Et ollut syntynyt, kun vuosituhat vaihtui.')
else:
    aika = vuosituhat - syntymavuosi
    print(f"Olit {aika.days} päivää vanha, kun vuosituhat vaihtui.")