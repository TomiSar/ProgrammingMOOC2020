# Kirjoita ratkaisu tähän
opiskelijat = int(input("Montako opiskelijaa? "))
ryhmakoko = int(input("Ryhmän koko? "))

ryhmienmaara = (opiskelijat + ryhmakoko - 1) // ryhmakoko
print(f"Ryhmien määrä: {ryhmienmaara}")