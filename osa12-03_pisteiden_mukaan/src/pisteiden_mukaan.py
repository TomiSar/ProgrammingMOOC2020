# Tee funktio jarjesta_pisteiden_mukaan(alkiot: list). Funktio saa parametrina listan sanakirjoja, 
# jotka edustavat yksittäisiä TV-sarjoja, ja järjestää ne pisteiden mukaiseen laskevaan järjestykseen. 
# Funktio ei muuta parametrina olevaa listaa, vaan palauttaa uuden listan.
def jarjesta_pisteiden_mukaan(alkiot: list):
    def pistejarjestys(alkio):
        return alkio["pisteet"]
    return sorted(alkiot, key=pistejarjestys, reverse=True)

#main
if __name__ == "__main__":
    sarjat = [{ "nimi": "Dexter", "pisteet" : 8.6, "kausia":9 }, { "nimi": "Friends", "pisteet" : 8.9, "kausia":10 },  { "nimi": "Simpsons", "pisteet" : 8.7, "kausia":32 }  ]
    print("IMDB:n mukainen pistemäärä")
    for sarja in jarjesta_pisteiden_mukaan(sarjat):
        print(f"{sarja['nimi']} {sarja['pisteet']}")