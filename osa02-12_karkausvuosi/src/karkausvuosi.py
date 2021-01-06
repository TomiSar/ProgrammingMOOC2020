# Vuosi on karkausvuosi, jos se on jaollinen 4:llä. Kuitenkin jos vuosi on jaollinen #100:lla, se on karkausvuosi vain silloin, kun se on jaollinen myös 400:lla.
vuosi = int(input("Anna vuosi: "))

if vuosi % 4 == 0 and (vuosi % 100 != 0 or vuosi % 400 == 0):
    print("Vuosi on karkausvuosi.")
else:
    print("Vuosi ei ole karkausvuosi.")

#Another possible solution
# karkausvuosi = False
# vuosi = int(input("Anna vuosi: "))

# if vuosi % 100 == 0:
#     if vuosi % 400 == 0:
#         karkausvuosi = True
# elif vuosi % 4 == 0:
#     karkausvuosi = True

# if karkausvuosi:
#     print("Vuosi on karkausvuosi.")
# else:
#     print("Vuosi ei ole karkausvuosi.")