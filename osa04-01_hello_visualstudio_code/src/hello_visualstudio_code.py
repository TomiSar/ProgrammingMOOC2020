while True:
    editori = input("Editori: ").lower()
    if editori == "visual studio code":
        break
    if editori == "word" or editori == "notepad":
        print('surkea')
    else:
        print('ei ole hyvä')

print('loistava valinta!')

# Another possible solution 
# while True:
#     editori = input("Editori: ").lower()
#     if editori == "visual studio code":
#         break
#     if editori == "word" or editori == "notepad":
#         print('surkea')
#     else:
#         print('ei ole hyvä')
# print('loistava valinta!')