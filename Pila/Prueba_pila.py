from pila import Pila
from random import randint

pila_datos = Pila()
pila_aux = Pila()

# for i in range(0, 20): #1
#     num = randint(1, 20)
#     print(num)
#     pila_datos.apilar(num)

#cantidad = 0
#contar =int(input('ingrese el numero que desea contar'))

#while(not pila_datos.pila_vacia()):
#    x = pila_datos.desapilar()
#    if (x == contar):
#        cantidad += 1

#print('cantidad de numeros de ocurrencia', cantidad)


"""Ejercicio 14"""
# for i in range(0, 5): #14
#     elemento = int(input('ingrese el numero que desea apilar'))
#     if pila_datos.pila_vacia():
#         pila_datos.apilar(elemento)
#     else:
#         while (not pila_datos.pila_vacia()and (elemento < pila_datos.elemento_cima())):
#             aux = pila_datos.desapilar()
#             pila_aux.apilar(aux)
#         pila_datos.apilar(elemento)
#         while(not pila_aux.pila_vacia()):
#             aux = pila_aux.desapilar()
#             pila_datos.apilar(aux)

# while(not pila_datos.pila_vacia()):
#     x = pila_datos.desapilar()
#     print(x)



"""Ejercicio 16"""
# pila_EP_V = Pila()
# pila_EP_VII = Pila()
# pila_interseccion = Pila()
# pila_aux = Pila()

# Star_Wars_EP_V = ['Luke Skywalker', 'Han Solo', 'Darth Vader', 'Leia Organa', 'Yoda', 'Capitán Needan', 'Almirante Ozzel', 'Lando Calrissian']

# Star_Wars_EP_VII = ['Kylo Ren', 'Rey', 'Han Solo', 'Luke Skywalker', 'C3PO','Leia Organa', 'Chewbacca', '	Poe Dameron']

# for element in Star_Wars_EP_V:
#     pila_EP_V.apilar(element)
# for element in Star_Wars_EP_VII:
#     pila_EP_VII.apilar(element)

# while(not pila_EP_V.pila_vacia()):
#     aux1 = pila_EP_V.desapilar()
#     while(not pila_EP_VII.pila_vacia()): 
#         aux2 = pila_EP_VII.desapilar()
#         if aux1 == aux2:
#             pila_interseccion.apilar(aux1)
#         pila_aux.apilar(aux2)
#     while(not pila_aux.pila_vacia()):
#         pila_EP_VII.apilar(pila_aux.desapilar())

# while(not pila_interseccion.pila_vacia()):
#     x = pila_interseccion.desapilar()
#     print(x)


# """Ejercicio 22"""

# datos_Bobba_Fett = [["Alderan","Han Solo",300],["Tatoine","Luke",600]]

# datos_Din_Djarin = [["Tatoine","Leia Organa",400],["Alderan","Kylo Ren",700]]

# pila_Bobba_Fett = Pila()
# pila_Din_Djarin = Pila()
# pila_aux_B = Pila()
# pila_aux_D = Pila()

# for element in datos_Bobba_Fett:
#     pila_Bobba_Fett.apilar(element)
# for element in datos_Din_Djarin:
#     pila_Din_Djarin.apilar(element)

# #A
# while not pila_Bobba_Fett.pila_vacia():
#     pila_aux_B.apilar(pila_Bobba_Fett.desapilar())
# while not pila_Din_Djarin.pila_vacia():
#     pila_aux_D.apilar(pila_Din_Djarin.desapilar())

# print('Planeta Bobba')

# while not pila_aux_B.pila_vacia():
#     Bobba = pila_aux_B.desapilar()
#     print(Bobba[0])
#     pila_Bobba_Fett.apilar(Bobba)

# print('Planeta Din Djarin')

# while not pila_aux_D.pila_vacia():
#     Din = pila_aux_D.desapilar()
#     print(Din[0])
#     pila_Din_Djarin.apilar(Din)

# #B
# Bobba = 0
# Din = 0
# while not pila_Bobba_Fett.pila_vacia():
#     B = pila_Bobba_Fett.desapilar()
#     Bobba += B[2]
#     pila_aux_B.apilar(B)

# while not pila_Din_Djarin.pila_vacia():
#     D = pila_Din_Djarin.desapilar()
#     Din += D[2]
#     pila_aux_D.apilar(D)

# if (Bobba > Din):
#     print('Bobba Consiguio mas recompensa', Bobba)
# elif (Din > Bobba):
#     print('Din Consiguio mas recompensa', Din)
# else:
#     print('Consiguieron la misma cantidad de recompensa')

# #C
# Bpos = 0
# while not pila_aux_B.pila_vacia():
#     Bo = pila_aux_B.desapilar()
#     Bpos += 1
#     if Bo[1] == 'Han Solo':
#         print('Se atrapo a Han Solo en la mision', Bpos)
#     pila_Bobba_Fett.apilar(Bo)

# #D
# print('La cantidad de capturas de Bobba Fett es:', pila_Bobba_Fett.tamanio())
# print('La cantidad de capturas de Din Djarin es:', pila_aux_D.tamanio())


"""Ejercicio 23"""

Marvel = [['Rocket Raccoon', 2],['Groot', 1],['Black Widow', 6]]

pila_marvel = Pila()
pila_auxm = Pila()

for element in Marvel:
    pila_marvel.apilar(element)
#A
Rpos = 0
Gpos = 0

while not pila_marvel.pila_vacia():
    R = pila_marvel.desapilar()
    Rpos += 1
    Gpos += 1
    if R[0] == 'Rocket Raccoon':
        print('Rocket Raccoon se encuentra en la posicion:', Rpos)
    if R[0] == 'Groot':
        print('Groot se encuentra en la posicion:', Gpos)
    pila_auxm.apilar(R)

#B
while not pila_auxm.pila_vacia():
    X = pila_auxm.desapilar()
    if X[1] >= 5:
        print('El personaje:', X[0], 'aparece en:', X[1])
    pila_marvel.apilar(X)

#C
while not pila_marvel.pila_vacia():
    T = pila_marvel.desapilar()
    if T[0] == 'Black Widow':
        print('Black Widow participo en:', T[1])
    pila_auxm.apilar(T)

#D
while not pila_auxm.pila_vacia():
    T = pila_auxm.desapilar()
    if(T[0][0] in ['C', 'D', 'G']):
        print('Comienza con C, D, G:', T[0])
    pila_marvel.apilar(T)