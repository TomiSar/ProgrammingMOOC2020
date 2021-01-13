n = int(input("Kerrokset: "))
aakkoset = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
 
vasen = ""    # alaspäin menevä osa
oikea = ""    # ylöspäin menevä osa
k = n-1       # seuraavan merkin kohta aakkosissa
m = 2*n-1     # väliin tulevien merkkien määrä
while k >= 1:
    vasen = vasen+aakkoset[k]
    oikea = aakkoset[k]+oikea
    m -= 2
    print(vasen+aakkoset[k]*m+oikea)
    k -= 1
while k <= n-1:
    print(vasen+aakkoset[k]*m+oikea)
    vasen = vasen[:-1]
    oikea = oikea[1:]
    m += 2
    k += 1

