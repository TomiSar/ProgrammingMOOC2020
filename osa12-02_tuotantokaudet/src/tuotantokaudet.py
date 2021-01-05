# Tee funktio jarjesta_tuotantokausien_mukaan(alkiot: list). Funktio saa parametrina listan sanakirjoja, 
# jotka edustavat yksittäisiä TV-sarjoja, ja järjestää ne tuotantokausien lukumäärän mukaiseen kasvavaan 
# järjestykseen. Funktio ei muuta parametrina olevaa listaa, vaan palauttaa uuden listan.
def jarjesta_tuotantokausien_mukaan(alkiot: list):
    def kausijarjestys(alkio):
        return alkio["kausia"]
    return sorted(alkiot, key=kausijarjestys)

#main
if __name__ == "__main__":
    sarjat = [{ "nimi": "Dexter", "pisteet" : 8.6, "kausia":9 }, { "nimi": "Friends", "pisteet" : 8.9, "kausia":10 },  { "nimi": "Simpsons", "pisteet" : 8.7, "kausia":32 }  ]
    for sarja in jarjesta_tuotantokausien_mukaan(sarjat):
        print(f"{sarja['nimi']} {sarja['kausia']} tuotantokautta")