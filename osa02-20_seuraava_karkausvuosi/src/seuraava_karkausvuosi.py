aloitusvuosi = int(input("Vuosi: "))
vuosi = aloitusvuosi + 1

while True:
    if vuosi % 4 == 0 and vuosi % 100 != 0 or vuosi % 400 == 0:
        break
    vuosi += 1

print(f"Vuotta {aloitusvuosi} seuraava karkausvuosi on {vuosi}")