import re

table = []

def menu():
    print('Menu : ')
    print('1- Chiffrer un message')
    print('2- Déchiffrer un message')
    question = input("Que voulez vous faire ? (1 ou 2) ")
    try:
        question = int(question)
        if question != 1 and question != 2:
            print('')
            raise ValueError()
    except ValueError:
        print('')
        print("Merci de choisir un nombre valide.")
        return menu()
    else:
        text = input('Quel est le texte a chiffrer ?: ')
        decalage = int(input('De combien est le décalage ?: '))
        match question:
            case 1:
                return caesar_cipher(text, decalage)
            case 2:
                return ceaser_dechiffre(text, decalage)

def ceaser_dechiffre(value: str, dec: int):
    global table
    table = []
    for i in value:
        if(re.match('[^.!? ]+', i)):
            x = ord(i) - dec
            table.append(chr(x))
        else:
            table.append(i)
    result = ''.join(table)
    print(result)

def caesar_cipher(value: str, dec: int):
    global table
    for i in value:
        if(re.match('[^.!? ]+', i)):
            if 'a' <= i <= 'z':
                x = (ord(i) - ord('a'))
                x = (x + dec) % 26
                x = chr(x + ord('a'))
                table.append(x)
                continue
            if 'A' <= i <= 'Z':
                x = (ord(i) - ord('A'))
                x = (x + dec) % 26
                x = chr(x + ord('A'))
                table.append(x)
                continue
        else:
            table.append(i)
    result = ''.join(table)
    print(result)
        
menu()
    