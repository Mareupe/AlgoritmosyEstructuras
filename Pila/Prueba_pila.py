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


"""Ejercicio 22"""
