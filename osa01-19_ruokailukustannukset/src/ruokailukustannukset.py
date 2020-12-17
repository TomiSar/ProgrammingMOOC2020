# Kirjoita ratkaisu tähän
kerrat = int(input("Montako kertaa viikossa syöt Unicafessa? "))
lounashinta = float(input("Unicafe-lounaan hinta? "))
vkruokaostokset = float(input("Unicafe-lounaan hinta? "))

viikossaruokaan = kerrat * lounashinta + vkruokaostokset
paivassaruokaan = viikossaruokaan / 7

print('\nKustannukset keskimäärin:')
print(f"Päivässä {paivassaruokaan} euroa")
print(f"Viikossa {viikossaruokaan} euroa")