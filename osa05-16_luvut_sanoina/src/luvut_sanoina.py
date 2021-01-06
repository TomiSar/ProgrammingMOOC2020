def lukukirja():
    # Apusanakirja
    ykkoset = {0:"nolla", 1:"yksi", 2:"kaksi", 3:"kolme", 4:"neljä", 5:"viisi", 6:"kuusi", 7:"seitsemän", 8:"kahdeksan", 9:"yhdeksän"}
    luvut = {}
 
    # 0 - 9
    for i in range(10):
        luvut[i] = ykkoset[i]
 
    # 10 on erikoistapaus
    luvut[10] = "kymmenen"
 
    # 11 - 19
    for i in range(1, 10):
        luvut[i + 10] = ykkoset[i] + "toista"
 
    # 20 - 99
    for i in range(2, 10):
        luvut[i * 10] = ykkoset[i] + "kymmentä"
        for j in range(1, 10):
            luvut[i * 10 + j] = ykkoset[i] + "kymmentä" + ykkoset[j]
 
    return luvut
 
if __name__ == "__main__":
    print(lukukirja())

# Another possible solution 
# def lukukirja():
#     luvut = {}
#     avaimet = []
#     sanat = []
#     for i in range(0, 100):
#         avaimet.append(i)
#     kirjaimet = ["nolla", "yksi", "kaksi", "kolme", "neljä", "viisi", "kuusi", "seitsemän", "kahdeksan", "yhdeksän", "kymmenen", "toista", "kymmentä"]
    
#     i = 0
#     while i <= 99:
#         while i <= 10:
#             sanat.append(kirjaimet[i])
#             i += 1 
#         while 11 <= i <= 19:
#             sanat.append(kirjaimet[i-10]+kirjaimet[11])
#             i += 1
#         while i == 20:
#             sanat.append(kirjaimet[2]+kirjaimet[12])
#             i += 1
#         while 21 <= i <= 29:
#             sanat.append(kirjaimet[2]+kirjaimet[12]+kirjaimet[i-20])
#             i += 1
#         while i == 30:
#             sanat.append(kirjaimet[3]+kirjaimet[12])
#             i += 1
#         while 31 <= i <= 39:
#             sanat.append(kirjaimet[3]+kirjaimet[12]+kirjaimet[i-30])
#             i += 1
#         while i == 40:
#             sanat.append(kirjaimet[4]+kirjaimet[12])
#             i += 1
#         while 41 <= i <= 49:
#             sanat.append(kirjaimet[4]+kirjaimet[12]+kirjaimet[i-40])
#             i += 1
#         while i == 50:
#             sanat.append(kirjaimet[5]+kirjaimet[12])
#             i += 1
#         while 51 <= i <= 59:
#             sanat.append(kirjaimet[5]+kirjaimet[12]+kirjaimet[i-50])
#             i += 1
#         while i == 60:
#             sanat.append(kirjaimet[6]+kirjaimet[12])
#             i += 1
#         while 61 <= i <= 69:
#             sanat.append(kirjaimet[6]+kirjaimet[12]+kirjaimet[i-60])
#             i += 1
#         while i == 70:
#             sanat.append(kirjaimet[7]+kirjaimet[12])
#             i += 1
#         while 71 <= i <= 79:
#             sanat.append(kirjaimet[7]+kirjaimet[12]+kirjaimet[i-70])
#             i += 1
#         while i == 80:
#             sanat.append(kirjaimet[8]+kirjaimet[12])
#             i += 1
#         while 81 <= i <= 89:
#             sanat.append(kirjaimet[8]+kirjaimet[12]+kirjaimet[i-80])
#             i += 1
#         while i == 90:
#             sanat.append(kirjaimet[9]+kirjaimet[12])
#             i += 1
#         while 91 <= i <= 99:
#             sanat.append(kirjaimet[9]+kirjaimet[12]+kirjaimet[i-90])
#             i += 1
#         i += 1

#     x = 0
#     while x < len(avaimet):
#         for i in avaimet:
#             luvut[i] = sanat[x]
#             x += 1
#     return luvut

# if __name__ == "__main__":
#     print(lukukirja()[2])
#     print(lukukirja()[11])
#     print(lukukirja()[45])
#     print(lukukirja()[99])
#     print(lukukirja()[0])