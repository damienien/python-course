array = [8, 7, 11, 7, 2, 10, 5, 8]

array2 = sorted(array)
result = list(dict.fromkeys(array2))
print(result)

#ou

result2 = []

for number in array:
    if number not in result2:
        result2.append(number)
print(result2)

def multiply():
    number = int(input("Quelle table voulez vous afficher ?: "))
    table = []
    
    for i in range(1, 11):
        result = i * number
        if(result%3 == 0):
            table.append(f'{result}*')
        else:
            table.append(result)
        
    print(table)
    
multiply()