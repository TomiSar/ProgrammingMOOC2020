# Tee ratkaisusi tähän:
class Sekuntikello:
    def __init__(self):
        self.sekunnit = 0
        self.minuutit = 0

    #Metodi tick vie siis kelloa sekunnin eteenpäin, ja sekä sekuntien että minuuttien arvo on 
    # suuruudeltaan korkeintaan 59. Lisäksi oliossa tulee olla metodi __str__, joka näyttää kellonajan yllä olevassa muodossa.
    def tick(self):
        self.sekunnit += 1
        if self.sekunnit == 60:
            self.sekunnit = 0
            self.minuutit += 1
            if self.minuutit == 60:
                self.minuutit = 0

    def __str__(self):
        return f"{self.minuutit:02}:{self.sekunnit:02}"


#main
if __name__ == "__main__":
    kello = Sekuntikello()
    for i in range(3600):
        print(kello)
        kello.tick()