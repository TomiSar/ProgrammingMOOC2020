# Tee Ratkaisu tänne
def vanhin(henkilot: list):
    vanhin = []
    for i in henkilot:
        vanhin.append(i[1])
    
    hakusana = min(vanhin)
    for i in henkilot:
        if hakusana == i[1]:
            return i[0]

if __name__ == "__main__":
    h1 = ("Arto", 1977)
    h2 = ("Einari", 1985)
    h3 = ("Maija", 1953)
    h4 = ("Essi", 1997)
    henkilot = [h1, h2, h3, h4 ]
    print(vanhin(henkilot))