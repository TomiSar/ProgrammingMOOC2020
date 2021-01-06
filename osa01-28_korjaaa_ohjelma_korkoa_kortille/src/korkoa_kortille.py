alkupisteet = int(input("Kuinka paljon pisteitä? "))
if alkupisteet < 100:
    pisteet = 1.1 * alkupisteet
    print("Sait 10 % bonusta")
if alkupisteet >= 100:
    pisteet = 1.15 * alkupisteet
    print("Sait 15 % bonusta")
print("Pisteitä on nyt", pisteet)
