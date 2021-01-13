class  Lukutilasto:
    def __init__(self):
        self.luvut = []
    
    #lisää uuden luvun tilastoon
    def lisaa_luku(self, luku:int):
        self.luvut.append(luku)

    #kertoo lisättyjen lukujen määrän
    def lukujen_maara(self):
        return len(self.luvut)

    #kertoo lisättyjen lukujen summan (tyhjän lukutilaston summa on 0)
    def summa(self):
        return sum(self.luvut)

    #kertoo lisättyjen lukujen keskiarvon (tyhjän lukutilaston keskiarvo on 0)
    def keskiarvo(self):
        if not self.luvut:
            return 0.0
        else:
            return self.summa() /len(self.luvut)


tilasto = Lukutilasto()
parilliset = Lukutilasto()
parittomat = Lukutilasto()
print("Anna lukuja: ")
while True:
    luku = int(input("")) 
    if luku == -1:
        break
    
    tilasto.lisaa_luku(luku)
    if luku % 2 == 0:
        parilliset.lisaa_luku(luku)
    else:
        parittomat.lisaa_luku(luku)

print("Summa:", tilasto.summa())         
print("Keskiarvo:", tilasto.keskiarvo())
print("Parillisten summa:", parilliset.summa())
print("Parittomien summa:", parittomat.summa()) 

# tilasto.lisaa_luku(3)
# tilasto.lisaa_luku(5)
# tilasto.lisaa_luku(1)
# tilasto.lisaa_luku(2)
# print("Lukujen määrä:", tilasto.lukujen_maara()) #Määrä: 4
# print("Summa:", tilasto.summa())                 #Summa: 11
# print("Keskiarvo:", tilasto.keskiarvo())         #Keskiarvo: 2.75

# tilasto = Lukutilasto()
# tilasto.lisaa_luku(3)
# tilasto.lisaa_luku(5)
# tilasto.lisaa_luku(1)
# tilasto.lisaa_luku(2)
# print("Lukujen määrä:", tilasto.lukujen_maara()) #Lukujen määrä: 4