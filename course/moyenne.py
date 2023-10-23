table = []
def moyenne():
    global table
    
    note = input('Entrer un nombre positif: ')
    try:
        note = int(note)
    except ValueError:
        print('Ceci n\'est pas un nombre...')
        return moyenne()
    else:
        while note >= 0:
            table.append(note)
            return moyenne()
        if note < 0 and len(table) > 0:
            average = sum(table)/len(table)
            print(f'La moyenne des {len(table)} notes est de: {average:.2f}')
        elif note < 0:
            print(f'Il y\'a : {len(table)} note(s)')
            raise ZeroDivisionError('Vous n\'avez pas saisi de notes')      
    
moyenne()