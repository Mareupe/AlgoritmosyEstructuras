from arbol_binario import Arbol
from random import randint

arbol = Arbol()

# for i in range(20):
#     numero = randint(1, 10)
#     arbol.insertar_nodo(numero)

# print('inorden')
# arbol.inorden()
# print()

# # print('cantidad de ocurrencias', arbol.contar_ocurrencias(int(input('ingrese el valor '))))

# print('cantidad de pares impares', arbol.contar_pares_impares())


# pos = arbol.busqueda(int(input('ingrese el numero a buscar ')))
# if(pos is not None):
#     print('el valor esta', pos.info)
# else:
#     print('el valor no esta')

# arbol.eliminar_nodo(int(input('ingrese el numero a buscar ')))


# print('postorden')
# arbol.postorden()
# print()
# print('preorden')
# arbol.preorden()
# print()


"""Ejercicio 5"""
# datos = [
#     {'nombre':'Iron Man', 'heroe': True},
#     {'nombre':'Thanos', 'heroe': False},
#     {'nombre':'Kang', 'heroe': False},
#     {'nombre':'Captain Marvel', 'heroe': True},
#     {'nombre':'Agatha Harkness', 'heroe': False},
#     {'nombre':'Captain America', 'heroe': True},
#     {'nombre':'Taneleer Tivan', 'heroe': False},
#     {'nombre':'Black Widow', 'heroe': True},
#     {'nombre':'Doctor Strnge', 'heroe': True},
#     {'nombre':'Scarlet Witch', 'heroe': True}
# ]

# print('A')
# for elemento in datos:
#     arbol = arbol.insertar_nodo(elemento['nombre'],elemento)

# print('B: Lista de villanos ordenados alfabéticamente')
# arbol.inorden()
# print('')

# print('C: Superheroes que comienzan con C')

# arbol.inorden_nombreC()
# print('')

# print('D')

# print('En el árbol hay:',arbol.contar_heroes(True), 'Superheroes')
# print('')

# print('E: Modificar el nombre de un Superheroe')

# buscado = input('ingrese a quien buscar:')
# arbol.busqueda_proximidad(buscado)
# buscado = input('ingrese a quien quiere cambiar el nombre:')
# buscado2 = input('ingrese nuevo nombre:')
# clave, dato = arbol.eliminar_nodo(buscado)
# dato['nombre'] = buscado2
# arbol = arbol.insertar_nodo(buscado2,dato)
# arbol.inorden()
# print('')

# print('F: Listado de Superheroes de manera descendente')
# arbol.postorden()
# print('')

# print('G')

# arbolV = Arbol()
# arbolH = Arbol()

# arbolH = arbol.separar_arbol_Heroe_Villano(arbolH, True)
# arbolV = arbol.separar_arbol_Heroe_Villano(arbolV, False)

# print('El Arbol de Superheroes tiene:',arbolH.contar_heroes(True),'Nodos')
# arbolH.inorden()
# print('')
# print('El Arbol de Villanos tiene:',arbolV.contar_heroes(False),'Nodos')
# arbolV.inorden()

"""Ejercicio 16"""

# tabla = [['Despejado', 0.22], ['Nublado', 0.15], ['Lluvia', 0.03],['Baja', 0.26],['Alta', 0.14], ['1', 0.05], ['2', 0.01], ['3', 0.035], ['5', 0.06], ['7', 0.02], ['8', 0.025]]

# dic = {}


# def como_comparo(arbol):
#     return arbol.datos


# bosque = []

# for info, frecuencia in tabla:
#     arbol = Arbol(info, frecuencia)
#     bosque.append(arbol)


# bosque.sort(key=como_comparo)
# # for arbol in bosque:
# #     print(arbol.info, arbol.frecuencia)

# while(len(bosque) > 1):
#     arbol1 = bosque.pop(0)
#     arbol2 = bosque.pop(0)
#     nuevo_arbol = Arbol(datos=arbol1.datos+arbol2.datos)
#     nuevo_arbol.izq = arbol1
#     nuevo_arbol.der = arbol2
#     bosque.append(nuevo_arbol)
#     bosque.sort(key=como_comparo)

# arbol_huffman = bosque[0]



# def generar_tabla(arbol, cadena='', dic=None):
#     if(arbol is not None):
#         if(arbol.izq is None):
#             dic[arbol.info] = cadena
#             # print(arbol.info, cadena)
#         else:
#             cadena += '0'
#             generar_tabla(arbol.izq, cadena, dic)
#             cadena = cadena[0:-1]
#             cadena += '1'
#             generar_tabla(arbol.der, cadena, dic)


# generar_tabla(arbol_huffman, dic=dic)


# def codificar(cadena, dic):
#     cadena_cod = ''
#     for caracter in cadena:
#         cadena_cod += dic[caracter]
#     return cadena_cod


# def decodificar(cadena_cod, arbol_huff):
#     cadena_deco = ''
#     arbol_aux = arbol_huff
#     pos = 0
#     while(pos < len(cadena_cod)):
#         if(cadena_cod[pos] == '0'):
#             arbol_aux = arbol_aux.izq
#         else:
#             arbol_aux = arbol_aux.der
#         pos += 1
#         if(arbol_aux.izq is None):
#             cadena_deco += arbol_aux.info
#             arbol_aux = arbol_huff
#         # cadena_deco
#     return cadena_deco


# cadena = ["Despejado", "Baja", '1', '5', '7']
# cadena_cod = codificar(cadena, dic)

# print(cadena_cod)
# print(decodificar(cadena_cod, arbol_huffman))

# from sys import getsizeof
# print(getsizeof(cadena_cod), getsizeof(b'0000011001101111010000000000000101100101101010101101000'))

"""Ejercicio 23"""

datos  = [
    { 'nombre' : 'Ceto' , 'capturada' : '' , 'descripcion' : '' },
    { 'nombre' : 'Cerda de Cromión' , 'capturada' : 'Teseo' , 'descripcion' : '' },
    { 'nombre' : 'Tifón' , 'capturada' : 'Zeus' , 'descripcion' : '' },
    { 'nombre' : 'Ortro' , 'capturada' : 'Heracles' , 'descripcion' : '' },
    { 'nombre' : 'Equidna' , 'capturada' : 'Argos Panoptes' , 'descripcion' : '' },
    { 'nombre' : 'Toro de Creta' , 'capturada' : 'Teseo' , 'descripcion' : '' },
    { 'nombre' : 'Dino' , 'capturada' : '' , 'descripcion' : '' },
    { 'nombre' : 'Jabalí de Calidón' , 'capturada' : 'Atalanta' , 'descripcion' : '' },
    { 'nombre' : 'Pefredo' , 'capturada' : '' , 'descripcion' : '' },
    { 'nombre' : 'Carcinos' , 'capturada' : '' , 'descripcion' : '' },
    { 'nombre' : 'Enio' , 'capturada' : '' , 'descripcion' : '' },
    { 'nombre' : 'Gerión' , 'capturada' : 'Heracles' , 'descripcion' : '' },
    { 'nombre' : 'Escila' , 'capturada' : '' , 'descripcion' : '' },
    { 'nombre' : 'Cloto' , 'capturada' : '' , 'descripcion' : '' },
    { 'nombre' : 'Caribdis' , 'capturada' : '' , 'descripcion' : '' },
    { 'nombre' : 'Laquesis' , 'capturada' : '' , 'descripcion' : '' },
    { 'nombre' : 'Euríale' , 'capturada' : '' , 'descripcion' : '' },
    { 'nombre' : 'Atropos' , 'capturada' : '' , 'descripcion' : '' },
    { 'nombre' : 'Esteno' , 'capturada' : '' , 'descripcion' : '' },
    { 'nombre' : 'Minotauro de Creta' , 'capturada' : 'Teseo' , 'descripcion' : '' },
    { 'nombre' : 'Medusa' , 'capturada' : 'Perseo' , 'descripcion' : '' },
    { 'nombre' : 'Harpías' , 'capturada' : '' , 'descripcion' : '' },
    { 'nombre' : 'Ladón' , 'capturada' : 'Heracles' , 'descripcion' : '' },
    { 'nombre' : 'Argos Panoptes' , 'capturada' : 'Hermes' , 'descripcion' : '' },
    { 'nombre' : 'Aguila del Cáucaso' , 'capturada' : '' , 'descripcion' : '' },
    { 'nombre' : 'Aves del Estínfalo' , 'capturada' : '' , 'descripcion' : '' },
    { 'nombre' : 'Quimera' , 'capturada' : 'Belerofonte' , 'descripcion' : '' },
    { 'nombre' : 'Talos' , 'capturada' : 'Medea' , 'descripcion' : '' },
    { 'nombre' : 'Hidra de Lerna' , 'capturada' : 'Heracles' , 'descripcion' : '' },
    { 'nombre' : 'Sirenas' , 'capturada' : '' , 'descripcion' : '' },
    { 'nombre' : 'León de Nemea' , 'capturada' : 'Heracles' , 'descripcion' : '' },
    { 'nombre' : 'Pitón' , 'capturada' : 'Apolo' , 'descripcion' : '' },
    { 'nombre' : 'Esfinge' , 'capturada' : 'Edipo' , 'descripcion' : '' },
    { 'nombre' : 'Cierva de Cerinea' , 'capturada' : '' , 'descripcion' : '' },
    { 'nombre' : 'Dragón de la Cólquida' , 'capturada' : '' , 'descripcion' : '' },
    { 'nombre' : 'Basilisco' , 'capturada' : '' , 'descripcion' : '' },
    { 'nombre' : 'Cerbero' , 'capturada' : '' , 'descripcion' : '' },
    { 'nombre' : 'Jabalí de Erimanto' , 'capturada' : '' , 'descripcion' : '' }
]

arbol = Arbol()

for elemento in datos:
    arbol = arbol.insertar_nodo(elemento['nombre'],elemento)
print('Listado inorden de las criaturas:')
arbol.inorden()
print('')

print('C')
print('Toda la informacion de Talos:',arbol.busqueda_Talos('Talos'))
print('')

print('D: Los 3 heroes con mayor criaturas derrotadas')

dic = {}
def ordenar(elemento):
    return elemento[1]

arbol.conta_criaturas_derrotadas(dic)
lista = list(dic.items())
lista.sort(key=ordenar, reverse=True)

for i in range (3):
	print(lista[i])

print('')

print('E: Criaturas derrotadas por Heracles')
arbol.mostrar_criaturas_derrotadas('Heracles')
print('')

print('F: Criaturas que no han sido derrotadas')
arbol.mostrar_criaturas_derrotadas('')
print('')

print('H: Modifico los nodos para saber quien las atrapó') 
arbol.modificar_captura('Cerbero', 'Heracles')
arbol.modificar_captura('Toro de Creta', 'Heracles')
arbol.modificar_captura('Cierva de Cerinea', 'Heracles')
arbol.modificar_captura('Jabalí de Erimanto', 'Heracles')

arbol.inorden()
print('')

print('I:Busqueda por proximidad')

buscado = input('ingrese a quien buscar:')
arbol.busqueda_proximidad(buscado)
print('')

print('J: Se eliminan los nodos Basilisco y a las Sirenas')

arbol.eliminar_nodo('Basilisco')
arbol.eliminar_nodo('Sirenas')

arbol.inorden()
print('')

print('K: Se modifica el nodo Aves del Estínfalo y se agrega descripción')
arbol.modificar_descripcion('Aves del Estínfalo', 'Heracles derrotó varias')
arbol.inorden()
print('')

print('L: Se modifica el nombre de Ladón')
clave, dato = arbol.eliminar_nodo('Ladón')
dato['nombre'] = 'Dragón Ladón'
arbol = arbol.insertar_nodo('Dragón Ladón',dato)
arbol.inorden()
print('')

print('M: Se hace un listado por nivel')
arbol.barrido_por_nivel()
print('')

print('N: Criaturas capturadas por Heracles')
arbol.mostrar_criaturas_derrotadas('Heracles')