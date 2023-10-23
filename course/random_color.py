import random
from sty import fg

def color():
    return fg(random.randint(0,256))

print(color(), 'Hello')
print(color(), 'World !')