def anagrammi(mjono1, mjono2):
    return sorted(mjono1) == sorted(mjono2)

if __name__ == "__main__":
    print(anagrammi("talo", "tola")) # True
    print(anagrammi("talo", "lato")) # True
    print(anagrammi("python", "java")) # False