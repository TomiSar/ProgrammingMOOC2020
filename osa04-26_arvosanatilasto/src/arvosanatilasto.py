# Kirjoita ratkaisu tähän
pisteet_taulukko = []

while True:
    mjono = input("Koepisteet ja harjoitusten määrä: ")
    if mjono == "":
        break
    luvut = mjono.split(" ")
    pisteet_taulukko.append(int(luvut[0]))       #koepisteet
    pisteet_taulukko.append(int(luvut[1]) // 10) #harjoituspisteet

#Tulostetaan tilasto annettujen pisteiden perusteella
#lasketaan yhteen kokeen pistemäärä ja tehtyjen harjoitusten määrä 
#Jos kokeen pistemäärä on alle 10, on arvosana kokonaispistemäärästä riippumatta 0 eli hylätty.
i = 0
tahdet = ["","","","","",""]
while True:
    if i >= len(pisteet_taulukko):
        break
    if pisteet_taulukko[i] >= 10:
        if  pisteet_taulukko[i] + pisteet_taulukko[i+1] >= 28:
            tahdet[0] +="*"
        elif pisteet_taulukko[i] + pisteet_taulukko[i+1] >= 24:
            tahdet[1] += "*"
        elif pisteet_taulukko[i] + pisteet_taulukko[i+1] >= 21:
            tahdet[2] += "*"
        elif pisteet_taulukko[i] + pisteet_taulukko[i+1] >= 18:
            tahdet[3] += "*"
        elif pisteet_taulukko[i] + pisteet_taulukko[i+1] >= 15:
            tahdet[4] += "*"
        else:
            tahdet[5] += "*"
    else:
        tahdet[5] += "*"
    i +=2

#Lasketaan keskiarvo ja hyväksymisprosentti
keskiarvo = f"{2*sum(pisteet_taulukko)/len(pisteet_taulukko):.1f}"
if sum(pisteet_taulukko) > 0:
    hyvaksymisprosentti = f"{100 * (1 - len(tahdet[5])/(len(tahdet[0]+tahdet[1]+tahdet[2]+tahdet[3]+tahdet[4]+tahdet[5] ))):.1f}"

print("Tilasto:")
print(f"Pisteiden keskiarvo: {keskiarvo}")
print(f"Hyväksymisprosentti: {hyvaksymisprosentti}")
print("Arvosanajakauma:")
print(f"  5: {tahdet[0]}")
print(f"  4: {tahdet[1]}")
print(f"  3: {tahdet[2]}")
print(f"  2: {tahdet[3]}")
print(f"  1: {tahdet[4]}")
print(f"  0: {tahdet[5]}")