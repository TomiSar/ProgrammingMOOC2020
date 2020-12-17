# Kirjoita ratkaisu tähän
pisteet = int(input("Anna pisteet [0-100]: "))
if pisteet < 0 or pisteet > 100:
    arvosana = "mahdotonta!"
elif pisteet <= 49:
    arvosana = "hylätty"
elif pisteet <= 59:
    arvosana = "1"
elif pisteet <= 69:
    arvosana = "2"
elif pisteet <= 79:
    arvosana = "3"
elif pisteet <= 89:
    arvosana = "4"
else:
    arvosana = "5"
print("Arvosana: " + arvosana)