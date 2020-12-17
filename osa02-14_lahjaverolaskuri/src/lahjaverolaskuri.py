# Kirjoita ratkaisu tähän
#veromaara = VeroAlaraja + (suuruus - LahjaArvoMinRajalla) * VeroprosenttiYlimenevä
suuruus = int(input("Lahjan suuruus? "))

if (suuruus < 5000):
    veromaara = 0
elif (suuruus <= 25000):
    veromaara = 100 + (suuruus - 5000) * 0.08
elif (suuruus <= 55000):
    veromaara = 1700 + (suuruus - 25000) * 0.1
elif (suuruus <= 200000):
    veromaara = 4700 + (suuruus - 55000) * 0.12
elif (suuruus <= 1000000):
    veromaara = 22100 + (suuruus - 200000) * 0.15
else:
    veromaara = 142100 + (suuruus - 1000000) * 0.17    

if veromaara == 0:
    print("Ei veroa!")
else:
    print("Vero:" ,veromaara, "euroa")