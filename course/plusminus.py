import random

essai = 0
result = 0


def menu():
    print('Facile - entre 0 et 10 (1)')
    print('Moyen - entre 0 et 100 (2)')
    print('Difficile - entre 0 et 1000 (3)')
    choose = input('Choisissez un niveau de diffculté: ')
    global result
    
    try:
        int(choose)
    except ValueError:
        print('Merci de choisir un nombre valide !')
        print('')
        return menu()
    else:
        new_choose = int(choose)
        if(new_choose != 1 and new_choose !=2 and new_choose !=3 ):
            print('Merci de choisir un niveau de difficulté valide : 1, 2 ou 3.')
            print('')
            return menu()
        else:
            match(new_choose):
                case 1:
                    result = random.randint(1, 10)
                    plusminus(1, 10, result)
                case 2:
                    result = random.randint(1, 100)
                    plusminus(1, 100, result)
                case 3:
                    result = random.randint(1, 1000)
                    plusminus(1, 1000, result)
                
    

def plusminus(val1, val2, result):
    t = input(f"Entrer un nombre entre {val1} et {val2} : ")
    global essai
    
    try:
        int(t)
    except ValueError:
        print('Ce n\'est pas un nombre')
        return plusminus(val1, val2, result)
    else:
        new_t = int(t)
        if(new_t > result):
            print(f'Le nombre est plus petit que {new_t}')
            essai += 1
            return plusminus(val1, val2, result)
        elif(new_t < result):
            print(f'Le nombre est plus grand que {new_t}')
            essai += 1
            return plusminus(val1, val2, result)
        else:
            print(f'Bravo, vous avez trouvé en {essai} essais')

menu()