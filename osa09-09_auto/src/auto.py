# TEE RATKAISUSI TÄHÄN:
# Toteuta luokka Auto, jossa on kapseloituina attribuutteina tieto bensatankin sisällöstä
# (0-60 litraa) ja ajetuista kilometreista.
# Attribuutti bensaa ja ajettu ovat piilotetut bensan ja ajettujen kilometrien määrä on kapseloitava, 
# niihin ei tule pystyä vaikuttamaan muuten kuin auton metodeja kutsumalla.
class Auto:
    def __init__(self):
        self.__bensaa = 0
        self.__ajettu = 0

    # joka täyttää bensatankin täyteen 60
    def tankkaa(self):
        self.__bensaa = 60

    # Ajaa parametrina olevan kilometrimäärän tai niin pitkälle kuin bensaa riittää
    # Auto kuluttaa litran bensaa kilometrillä.
    def aja(self, km:int):
        if km > self.__bensaa:
            km = self.__bensaa
        self.__ajettu += km
        self.__bensaa -= km

    def __str__(self):
        return f"Auto: ajettu {self.__ajettu} km, bensaa {self.__bensaa} litraa"


#main
if __name__ == "__main__":
    auto = Auto()
    print(auto)     #Auto: ajettu 0 km, bensaa 0 litraa
    auto.tankkaa()  
    print(auto)     #Auto: ajettu 0 km, bensaa 60 litraa
    auto.aja(20)
    print(auto)     #Auto: ajettu 20 km, bensaa 40 litraa
    auto.aja(50)
    print(auto)     #Auto: ajettu 60 km, bensaa 0 litraa
    auto.aja(10)
    print(auto)     #Auto: ajettu 60 km, bensaa 0 litraa
    auto.tankkaa()
    auto.tankkaa()
    print(auto)     #Auto: ajettu 60 km, bensaa 60 litraa