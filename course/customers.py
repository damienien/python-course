clients = {
    "client_1": {
    "Nom": "Doe",
    "Prénom": "John",
    "Age": "21",
    "Email": "john.doe@xyz.fr",
    "Hobbies": ["Karaté", "Tennis"]
},
    "client_2" : {
    "Nom": "Stewart",
    "Prénom": "Jane",
    "Age": '26',
    "Email": '[Email non renseigné]',
    "Hobbies": ['danse', "peinture", "chant"]
},

"client_3" : {
    "Nom": "Tardieu",
    "Prénom": "Olivier",
    "Age": '32',
    "Email": 'olivier.tardieu@xyz.fr',
    "Hobbies": "[Hobbies non renseignés]"
}
    

}

for i, values in clients.items():
    print(f'{i}: {values}')