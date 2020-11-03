from pattern.en import parse
from pattern.en import pprint
import networkx as nx
import matplotlib.pyplot as plt


G = nx.DiGraph() 
print('I drove my car to the hospital yesterday')
pprint(parse('I drove my car to the hospital yesterday', relations=True, lemmata=True))
#Separamos en lista
words = parse('I drove my car to the hospital yesterday', relations=True, lemmata=True).split()
text='I drove my car to the hospital yesterday'
#print(parse('I drove my car to the hospital yesterday', relations=True, lemmata=True).split())
def Convert(string): 
    li = list(string.split(" ")) 
    return li 
#Obtenemos el tamaño de la lista
listText=Convert(text)
tam = len(listText)

print("----------")
#Declaramos las listas a usar
palabras = []
palabrasNodo = []
nodos = []
#Quizá podemos ahorrarnos estas listas, son para la creación de pares (palabra-tag)
tag = []
tag1 = []
tagg = []
partag = []
for elemento in words:
    for x in range(tam):
        #Creamos lista de palabras para nodos y pares
        palabras.append(elemento[x][0])
        palabrasNodo.append(elemento[x][0])
        #Asignamos a la lista los elementos en pares
        tag.append(elemento[x][1])
        tag1.append(elemento[x][1])
#sacamos el 1er elememto y hacemos un zip para que cree pares de las dos listas (I,Drove)...
palabrasNodo.pop(0)
nodos=zip(palabras, palabrasNodo)
#sacamos el 1er elememto y hacemos un zip para que cree pares de las dos listas de tags (BVD-PPP)...
tag1.pop(0)
tagg=zip(tag, tag1)
#Hacemos una lista nueva para que quede en forma de lista y no TUPLA, networkx pide en los label un str no tupla
for a,b in list(tagg):
    partag.append(a + "-" + b)
#Agregamos los nodos
for elemento in palabras:
    G.add_node(elemento)
#Agregamos los ejes con el valor del tag como valor del arista de cada uno de los tags de la lista anterior
for a,b in list(nodos):
    subtag = partag.pop(0)
    G.add_edge(a,b, label=subtag)


#Creamos el grafo
pos = nx.spring_layout(G)
nx.draw_networkx_nodes(G, pos, node_size = 2000)
nx.draw_networkx_labels(G, pos)
nx.draw_networkx_edges(G, pos, edge_color='r', arrows = True)
nx.draw_networkx_edge_labels(G, pos, edge_labels=None, label_pos=0.5, font_size=10, font_color='k', font_family='sans-serif', font_weight='normal', alpha=1.0, bbox=None, ax=None, rotate=True)

plt.show()