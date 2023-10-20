hobby = 'Sport'

print(hobby.upper())
print(hobby.lower())
print(hobby.capitalize())
print(hobby.replace("r", "t"))
print(len(hobby))

first = 'Hello'
second = 'World!'
print(first + ' ' + second)
print(f'{first} {second}')

# Convertit le nombre entier 3 (int) en chaîne de caractère "3" (str)
str(3)
# Convertit la chaîne de caractères "3" (str) en nombre entier 3 (int)
int("3")
# Convertit la chaîne de caractères "5.6" (str) en nombre flottant 5.6 (float)
float("5.6")
# Convertit la chaîne de caractères "True" (str) en booléen True (bool)
bool("True")

a = input('Veuillez entrer un premier nombre : ')
b = input('Veuillez entrer un second nombre : ')
result = int(a) + int(b)
print(f'Le résultat de l\'addition est {result}')

points = 7
if points < 5:
    score = 0
elif points == 5:
    score = 10
elif 6 <= points <= 10:
    score = 50
else:
    score = 1000
    
age = 19
height = 1.68
if age >= 18 and height > 1.50:
    print('Chouette, vous avez accès au manège.')
else:
    print('Accès au manège refusé.')
    
# Boucle : While
i = 0
while i < 5:
    print(i)
    i = i + 1
    
# Boucle : For
for i in range(0, 100):
    if i > 5:
        print("Stop")
        break
    print(i)

# Boucle : For
for i in range(0, 5):
    if i == 3:
        # Saut de la valeur 3
        print("-")
        continue
    print(i)
    
cities = ['Paris', 'Lyon', 'Marseille']
print(cities[2])
for city in cities:
    print(city)
    
hobbies = ['Sport', 'Music']
# Ajouter un élément
# append() ajoute un élément en fin de liste.
hobbies.append('Movies')
# insert() ajoute un élément à l'index indiqué, ici 0.
hobbies.insert(0, 'Games')
# Rechercher un élément
# index() retourne l'index de l'élément indiqué.
hobbies.index('Music')
# Supprimer un élément
# del permet de supprimer un élément via l'index.
del hobbies[1]
# remove supprime l'élément via la valeur.
hobbies.remove('Movies')

hobbies = ['Sport', 'Music']
# Concaténation de listes
# extend() étend la liste.
hobbies.extend(['Travel', 'Writing'])
# Concaténation en créant une nouvelle liste.
new_hobbies = hobbies + ['Movies']
# Condition avec les listes
if 'Sport' in hobbies:
    input('Ah génial, quel sport pratiques-tu ?')
# Segment de liste
# Retourne une sous-liste entre l'index 1 et l'index 2.
hobbies[1:3]

marks = [6, 18, 12, 15.5, 9]
# Tri de liste
# sort() ordonne les éléments de la liste, cette méthode retourne None.
marks.sort()
# reverse() inverse l'ordre des éléments de la liste, cette méthode retourne None.
marks.reverse()
# sorted(...) génère une nouvelle liste avec les éléments ordonnés.
result = sorted(marks)
# Fonction applicable sur une liste
# Retourne la taille de la liste
result = len(marks)
# Retourne le plus petit élément de la liste
result = min(marks)
# Retourne le plus grand élément de la liste
result = max(marks)
# Retourne la somme des éléments de la liste
result = sum(marks)

# Chaîne de caractères --> Liste
# split(sep) sépare la chaîne de caractères via un séparateur.
email = 'john.doe@yahoo.fr'
result = email.split('.')
# Liste --> Chaîne de caractères
# join(list) joint les éléments de la liste via un caractère.
cities = ['Paris', 'Monaco', 'Limoges']
result = '-'.join(cities)

# Tuple
fruits = ('banana', 'peach', 'apple')
print(type(fruits))
# Unpacking
mass, speed = (3, 12.7)
print(mass)
print(speed)

# Dictionnaire
user = {
    "last_name": "Doe",
    "first_name": "John",
    "age": 20
}
# Ajout d'une paire clef/valeur
user["email"] = "john.doe@xyz.fr"
user.update({ "email": "john.doe@xyz.fr" })
# Modification d'une valeur
user["age"] = 22
user.update({ "age": 22 })
# Suppression d'une paire clef/valeur
del user["first_name"]

# Retourne la liste des clefs du dictionnaire
list(user)
# Retourne un objet dict_keys
# (Liste) des clefs du dictionnaire
user.keys()
# Retourne un objet dict_values
# (Liste) des valeurs du dictionnaire
user.values()
# Retourne un objet dict_items
# (Liste) de tuples (clef, valeur) du dictionnaire
user.items()

# Boucle, en ayant accès aux clefs
for key in user.keys():
    print(key)
# Boucle, en ayant accès aux valeurs
for value in user.values():
    print(value)
# Boucle, en ayant accès aux clefs/valeurs
for key, value in user.items():
    print(f'{key} - {value}')
    
user = {
    "last_name": "Doe",
    "first_name": "John"
}

if 'age' not in user.keys():
    user['age'] = int(input('Entrer votre âge : '))