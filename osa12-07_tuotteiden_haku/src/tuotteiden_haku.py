# Tässä tehtävässä käsitellään tupleina esitettäviä tuotteita, jotka on esimerkeissä alustettu muuttujaan tuotteet seuraavasti:
# tuotteet = [("banaani", 5.95, 12), ("omena", 3.95, 3), ("appelsiini", 4.50, 2), ("vesimeloni", 4.95, 22), ("Kaali", 0.99, 1)]
# Toteuta funktio hae(tuotteet: list, kriteeri: callable), missä toisena parametrina on funktio, joka saa parametriksi yhden 
# tuotetta edustavan tuplen ja palauttaa totuusarvon. Funktio palauttaa listassa parametrina annetuista tuotteista ne, jotka toteuttavat kriteerin.
def hae(tuotteet: list, kriteeri: callable):
    return [tuote for tuote in tuotteet if kriteeri(tuote)]

#main
# if __name__ == "__main__":
#     for tuote in hae(tuotteet, lambda t: t[2]>10):
#         print(tuote)