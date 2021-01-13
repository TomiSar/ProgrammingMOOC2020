sana = input("Anna sana: ")

if sana[1] == sana[len(sana)-2]:
    print(f"Toinen ja toiseksi viimeinen kirjain on {sana[1]}")
else:
    print("Toinen ja toiseksi viimeinen kirjain eroavat")