# tee ratkaisu tänne,
from datetime import datetime, timedelta
 
def ruutuaika():
    if True:
        tuloste_tiedosto = input("Tiedosto: ")
        aloitus_paiva = input("Aloituspäivä: ")   
        kpl_paivia = int(input("Montako päivää: "))
    else: 
        tuloste_tiedosto = "kesakuun_loppu.txt"
        aloitus_paiva ="24.6.2020"
        kpl_paivia = 2
 
    aika = datetime.strptime(aloitus_paiva, "%d.%m.%Y") 
 
    print("Anna ruutuajat kunakin päivänä minuutteina (TV tietokone mobiililaite):")
    i = 0
    lista_ajoista = []
    while i < kpl_paivia:
        paiva = (aika + timedelta(days=i)).strftime("%d.%m.%Y")
        ruutuaika = input(f'Ruutuaika {paiva}: ')
        lista_ajoista.append((paiva, ruutuaika))
        i += 1
    
    eka_paiviva = aika.strftime("%d.%m.%Y")
    viimeinen_paiva = paiva = (aika + timedelta(days=kpl_paivia - 1)).strftime("%d.%m.%Y")
    aika_yhteensa = 0
    for a in lista_ajoista:
        for b in a[1].split(" "):
            aika_yhteensa += int(b)
 
    aika_keskimaarin = aika_yhteensa / kpl_paivia
 
    open(tuloste_tiedosto, "w").close()
    with open(tuloste_tiedosto, "a") as output:
        output.write(f'Ajanjakso: {eka_paiviva}-{viimeinen_paiva}\n')
        output.write(f'Yhteensä minuutteja: {aika_yhteensa}\n')
        output.write(f'Keskimäärin minuutteja päivässä: {aika_keskimaarin}\n')
 
        for i in lista_ajoista:
            j = i[1].split(" ")
            output.write(f'{i[0]}: {j[0]}/{j[1]}/{j[2]}\n')
 
    print(f'Tiedot tallennettu tiedostoon {tuloste_tiedosto}')
 


if __name__ == "__main__":
    ruutuaika()