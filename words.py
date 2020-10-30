from pattern.en import parse
from pattern.en import pprint

print('I drove my car to the hospital yesterday')
pprint(parse('I drove my car to the hospital yesterday', relations=True, lemmata=True))
#Separamos en lista
words = parse('I drove my car to the hospital yesterday', relations=True, lemmata=True).split()
text='I drove my car to the hospital yesterday'

def Convert(string): 
    li = list(string.split(" ")) 
    return li 

listText=Convert(text)
tam = len(listText)
print(tam)


print (words[0][0][0])
print (words[0][0][1])

print("----------")
palabras = []
verbos = []
for elemento in words:
    for x in range(tam):
        #print(elemento[x][0])
        palabras.append(elemento[x][0])
        #print(elemento[x][1])
        verbos.append(elemento[x][1])

print("Palabras:")
for elemento in palabras:
    print(elemento)
print("Verbos:")
for elemento in verbos:
    print(elemento)