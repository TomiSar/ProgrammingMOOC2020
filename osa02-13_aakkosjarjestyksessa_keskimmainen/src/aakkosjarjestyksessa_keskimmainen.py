kirjain1 = input("Anna 1. kirjain: ")
kirjain2 = input("Anna 2. kirjain: ")
kirjain3 = input("Anna 3. kirjain: ")

if kirjain2 > kirjain1 > kirjain3 or kirjain2 < kirjain1 < kirjain3:
    keski = kirjain1
elif kirjain1 > kirjain2 > kirjain3 or kirjain1 < kirjain2 < kirjain3:
    keski = kirjain2
elif kirjain1 > kirjain3 > kirjain2 or kirjain1 < kirjain3 < kirjain2:
    keski = kirjain3
    
print("Keskimmäinen kirjain on " + keski)