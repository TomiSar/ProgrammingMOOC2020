# tee ratkaisu tänne
def ilman_vokaaleja(mjono):
    vokaalit = 'aeiouyåäö'
    uusimjono = ''
    for kirjain in mjono:
        if kirjain not in vokaalit:
            uusimjono += kirjain

    return uusimjono

if __name__ == "__main__":
    mjono = "tämä on esimerkki"
    print(ilman_vokaaleja(mjono))