#Jos sanan pituus on pariton, voit tulostaa sanan kumpaan tahansa mahdollisista keskikohdista.
sana = input("Sana: ")
alkuvali = (28 - len(sana)) // 2
loppuvali = alkuvali

#Sananpituus pariton lisätään loppuväliin 1 merkki jotta saadaan 30 merkin tulostus
if len(sana) % 2 != 0:
    loppuvali += 1

print(30 * "*")
print("*" + alkuvali * " " + sana + loppuvali * " " + "*")
print(30 * "*")