teksti = input("Write text: ")
 
with open("wordlist.txt") as tiedosto:
    sanalista = []
    for rivi in tiedosto:
        rivi = rivi.replace("\n", "")
        sanalista.append(rivi)
 
sanat = teksti.split(" ")
korjattu = []
for sana in sanat:
    if sana.lower() not in sanalista:
        korjattu.append(f"*{sana}*")
    else:
        korjattu.append(sana)

lause = ""
for sana in korjattu:
    lause += sana + " "

print(lause)
