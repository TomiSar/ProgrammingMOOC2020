def eniten_kirjainta(mjono):
    yleisin = mjono[0]
    for kirjain in mjono:
        if mjono.count(yleisin) < mjono.count(kirjain):
            yleisin = kirjain

    return yleisin

if __name__ == "__main__":
    mjono = "abcbdbe"
    print(eniten_kirjainta(mjono))

    toinen_jono = "esimerkkimerkkijonokki"
    print(eniten_kirjainta(toinen_jono))