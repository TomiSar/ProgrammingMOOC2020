def eka_sana(lause):
    sana = lause.split( )
    return sana[0]

def toka_sana(lause):
    sana = lause.split( )
    return sana[1]

def vika_sana(lause):
    sana = lause.split( )
    return sana[-1]

# funktiota kannattaa testata kutsumalla sitä täällä seuraavasti
if __name__ == "__main__":
    lause = "olipa kerran kauan sitten ohjelmoija"
    print(eka_sana(lause))
    print(toka_sana(lause))
    print(vika_sana(lause))
