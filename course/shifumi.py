import random

dict_choice = {
    1: "Pierre",
    2: "Feuille",
    3: "Ciseaux"
}

for key, value in dict_choice.items():
    print(f'{key}: {value}')
    
print('')
choice = int(input('Quelle est votre choix ?: '))
result = random.randint(1, 3)

def game(choice, result):
    for k, v in dict_choice.items():
        if(int(choice) == k):
            print(f'Choix du joueur: {v}')
        elif(int(result) == k):
            print(f'Choix de l\'ordinateur: {v}')
        
    match(choice, result):
        case 1, 1:
            print('Égalité !')
            
game(choice, result)