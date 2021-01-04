# Tehtäväpohjassa on valmiina funktio sulut_tasapainossa, joka tarkastaa, onko sen parametrina olevassa 
# merkkijonossa sulut tasapainossa, eli onko jokaista "aukeavaa" sulkumerkkiä ( kohti on oma "sulkeutuva" sulkumerkki ), 
# ja että sulut eivät mene ristiin.
# Laajenna funktiota siten, että se jättää huomiotta kaikki muut kuin sulkumerkit, ja että se osaa kaarisulkujen 
# lisäksi myös hakasulut. Haka- ja kaarisulut eivät saa mennä ristiin!
def sulut_tasapainossa(merkkijono: str):
        # merkkijono tyhjä, eli se on kunnossa
    if len(merkkijono) == 0:
        return True
 
    # jos ensimmäinen merkki ei ole mikään sulku syödään se pois
    if not merkkijono[0] in "()[]":
        return sulut_tasapainossa(merkkijono[1:])
 
    # jos viimeinen merkki ei ole mikään sulku syödään se pois
    if not merkkijono[-1] in "()[]":
        return sulut_tasapainossa(merkkijono[:-1])
    
    # nyt tiedetään että ensimmäinen ja viimeinen ovat sulkuja --> tarkistetaan ovatko ne vastinpari
    if merkkijono[0]=="(" and merkkijono[-1]==")":
        return sulut_tasapainossa(merkkijono[1:-1])
    if merkkijono[0]=="[" and merkkijono[-1]=="]":
        return sulut_tasapainossa(merkkijono[1:-1])

    # eivät olleet, joten merkkijono ei ollut kunnossa
    return False
    # poistetaan ensimmäinen ja viimeinen merkki

#main
if __name__ == "__main__":
    ok = sulut_tasapainossa("([([])])")
    print(ok)

    ok = sulut_tasapainossa("(python versio [3.7]) käytä tätä!")
    print(ok)
    
    # ei kelpaa sillä virheellinen loppusulku
    ok = sulut_tasapainossa("(()]")
    print(ok)

    # ei kelpaa sillä erityyppiset sulut menevät ristiin
    ok = sulut_tasapainossa("([huono)]")
    print(ok)
