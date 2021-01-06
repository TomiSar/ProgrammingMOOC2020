def palindromi(sana):
    kaannetty = ''
    pituus = len(sana) - 1
    while pituus >= 0:
        kaannetty += sana[pituus]
        pituus -= 1
    return sana == kaannetty
        
# huomaa, että tällä kertaa pääohjelmaa ei tule kirjoittaa lohkon
while True:
    sana = input("Anna sana: ")
    if palindromi(sana):
        print(f'{sana} on palindromi!')
        break
    print('ei ollut palindromi')

#The slice statement means start at string length, end at position 0, move with the step -1 (or one step backward).
# str="Python" # initial string
# stringlength=len(str) # calculate length of the list
# slicedString=str[stringlength::-1] # slicing 
# print (slicedString) # print the reversed string