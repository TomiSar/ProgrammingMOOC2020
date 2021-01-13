asti = int(input("Mihin asti? "))
luku = 1
summa = 1
luvutmjono = "1"
while summa < asti:
    luku += 1
    summa += luku
    luvutmjono += " + " + str(luku) 

print("Laskettiin",luvutmjono,"=",summa)  