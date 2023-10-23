def simple():
    f = open('./data/poem.txt')
    poem = f.read()
    f.close()
    print(poem)
    
def withmethod():
    with open('./data/poem.txt') as f:
        poem = f.read()
    print(poem)

simple()
withmethod()