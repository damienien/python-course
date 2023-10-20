import re

text = "Two roads diverged in a yellow wood, And sorry I could not travel both And be one traveler, long I stood And looked down one as far as I could To where it bent in the undergrowth."

dictionnary = {}
liste = []
text = text.upper()
for i in text:
    if(re.match('[^!.? ]+', i)):
        liste.append(i)

for i in liste:
    if i not in dictionnary.keys():
        dictionnary[i] = liste.count(i)
print(dictionnary)
    