from lista import Lista
from random import randint
lista_num = Lista()

datos = [
    {'name' : 'juan', 'edad': 34, 'provincia': 'misiones'}

]

for persona in datos:
    lista_personas.insertar(persona)
#    lista_num.insertar(randint(0, 100))

lista_num.barrido()
#print()
#numero = int(input('ingrese valor a eliminar '))
#numero = int(input('ingrese valor a buscar '))
#print(lista_num.busqueda(numero))

#lista_num.modificar_elemento(pos, 43)
#print()
#lista_num.barrido()
#print(lista_num.eliminar(numero))
#print()
#lista_num.barrido()

#ejercicio2

from random import randit
lista_vocales = Lista()
lista_personas = Lista()

for i in range(50):
    vocal = chr(randit(65, 90))
    lista_vocales.insertar(vocal)
lista_vocales.barrido()