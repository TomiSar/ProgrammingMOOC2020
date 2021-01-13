import string

def jaa_merkkeihin(lause):
    osat = ["","",""]
    for merkki in lause:
        if string.ascii_letters.find(merkki) != -1:
            osat[0] += merkki
        elif string.punctuation.find(merkki) != -1:
            osat[1] += merkki
        else:
            osat[2] += merkki
            
    return (osat[0], osat[1], osat[2])

 
if __name__ == "__main__":
    osat = jaa_merkkeihin("Tämä on testi!!! Toimiiko, mitä?")
    print(osat[0])
    print(osat[1])
    print(osat[2])

