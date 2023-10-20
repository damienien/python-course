numbers_dict = {
    "0": "Zero",
    "1": "One",
    "2": "Two",
    "3": "Three",
    "4": "Four",
    "5": "Five",
    "6": "Six",
    "7": "Seven",
    "8": "Eight",
    "9": "Nine"
}

number = input("Entrez un numéro de téléphone : ")
result = []

for i in number:
    for key, value in numbers_dict.items():
        if(i in key):
            result.append(value)
            
print(' '.join(result))

#ou
result2 = ""
for digit in number:
    result2 += numbers_dict.get(digit, "[Character not mapped]") + ' '
    
print(result2)