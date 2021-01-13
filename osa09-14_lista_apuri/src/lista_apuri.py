# Kirjoita luokka ListaApuri, jossa on kaksi luokkametodia.
class ListaApuri:

    # Metodi palauttaa alkion, jota esiintyy annetussa listassa eniten
    @classmethod
    def suurin_frekvenssi(cls, lista: list):
        # Jos listalla ei ole alkoita ollenkaan, palautetaan None
        if lista is None:
            return None

        max_frekvenssi = 0
        max_alkio = None
        for alkio in lista:
            frekvenssi = lista.count(alkio)
            if not max_alkio or frekvenssi > max_frekvenssi:
                max_frekvenssi = frekvenssi
                max_alkio = alkio
        return max_alkio

    # Metodi palauttaa sellaisten alkioden lukumäärän, jotka esiintyvät listassa vähintään kahdesti
    @classmethod
    def tuplia(cls, lista: list):
        maarat = {}
        for alkio in lista:
            maarat[alkio] = lista.count(alkio)
        
        tuplat = 0
        for arvo in maarat.values():
            if arvo > 1:
                tuplat += 1
        return tuplat


# main
if __name__ == "__main__":
    luvut = [1, 1, 2, 1, 3, 3, 4, 5, 5, 5, 6, 5, 5, 5]
    print("Taulukon suurin frekvessi:",ListaApuri.suurin_frekvenssi(luvut)) #Taulukon suurin frekvessi: 5
    print("Taulukon sisältää tupla-arvoja:",ListaApuri.tuplia(luvut))       #Taulukon sisältää tupla-arvoja: 3