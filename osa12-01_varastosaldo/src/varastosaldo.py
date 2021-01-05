# Tee funktio jarjesta_varastosaldon_mukaan(alkiot: list). Funktio saa parametrina listan tupleja, 
# joissa kolmantena alkiona on tuotteiden varastosaldo. Funktio järjestää parametrinaan saamat tuotteet 
# varastosaldojen mukaiseen kasvavaan järjestykseen. Funktio ei muuta parametrina olevaa listaa, vaan palauttaa uuden listan.
def jarjesta_varastosaldon_mukaan(alkiot: list):
    def saldojarjestys(alkio: tuple):
        return alkio[2]
    return sorted(alkiot, key=saldojarjestys) 

#main
if __name__ == "__main__":
    tuotteet = [("banaani", 5.95, 12), ("omena", 3.95, 3), ("appelsiini", 4.50, 2), ("vesimeloni", 4.95, 22)]
    for tuote in jarjesta_varastosaldon_mukaan(tuotteet):
        print(f"{tuote[0]} {tuote[2]} kpl")