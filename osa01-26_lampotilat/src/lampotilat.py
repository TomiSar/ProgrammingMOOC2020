# Kirjoita ratkaisu tähän
lampo_f = int(input("Anna lämpötila (F): "))
 
lampo_c = (lampo_f - 32) * 5/9
 
print(lampo_f, "fahrenheit-astetta on", lampo_c, "celsius-astetta") 
 
if lampo_c < 0:
    print("Paleltaa!")