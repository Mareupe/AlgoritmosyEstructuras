from lista import Lista
from random import randint
# lista_num = Lista()

# datos = [
#     {'name' : 'juan', 'edad': 34, 'provincia': 'misiones'}

# ]

# for persona in datos:
#     lista_personas.insertar(persona)
# #    lista_num.insertar(randint(0, 100))

# lista_num.barrido()
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

# from random import randit
# lista_vocales = Lista()
# lista_personas = Lista()

# for i in range(50):
#     vocal = chr(randit(65, 90))
#     lista_vocales.insertar(vocal)
# lista_vocales.barrido()

"""Ejercicio 6"""

# lista_SuperHeroes = Lista()

# SuperHeroes = [
#                         {'nombre' : "Iron Man",'anio' : 1963,'casa' : "Marvel",'biografia' : "Anthony Edward Stark conocido como Tony Stark, un multimillonario magnate empresarial estadounidense, playboy e ingenioso científico, quien sufrió una grave lesión en el pecho durante un secuestro. Cuando sus captores intentan forzarlo a construir un arma de destrucción masiva crea, en cambio, una armadura para salvar su vida y escapar del cautiverio."},
#                         {'nombre' : "Linterna Verde",'anio' : 1940,'casa' : "DC",'biografia' : "Cada Linterna Verde posee un anillo de poder y una batería (en forma de linterna) que garantiza a su portador la posibilidad de manifestar una gran variedad de poderes."},
#                         {'nombre' : "Hulk",'anio' : 1969,'casa' : "Marvel",'biografia' : "El Doctor Robert Bruce Banner es un científico de renombre y miembro fundador de los Vengadores. Él era un experto en la bioquímica, la física nuclear y la radiación gamma, por lo que el General Thaddeus Ross lo reclutó para recrear el Suero del Súper Soldado, pero esto resultó en un experimento fallido de radiación gamma, que convirtió a Banner en un monstruo verde llamado Hulk. Debido a lo peligroso que era, Banner abandonó a Elizabeth Ross para buscar una cura mientras era perseguido por Thaddeus Ross. Con el tiempo, Banner se reunió con Samuel Sterns y Elizabeth Ross para fabricar un antídoto, sin embargo, cuando Emil Blonsky se convirtió en la Abominación, Banner se vio forzado a utilizar a Hulk para vencerlo."},
#                         {'nombre' : "Wolverine",'anio' : 1974,'casa' : "Marvel",'biografia' : "Wolverine, cuyo nombre de nacimiento es James Howlett (también conocido como James Logan o simplemente Logan)4​ es un superhéroe ficticio que aparece en los cómics estadounidenses publicado por Marvel Comics, principalmente en asociación con los X-Men. Es un mutante que posee sentidos afinados a los animales, capacidades físicas mejoradas, poderosa capacidad de regeneración conocida como un factor de curación, y tres garras retráctiles en cada mano. Wolverine ha sido representado de diversas formas como miembro de los X-Men, Alpha Flight, Fuerza-X y Los Vengadores."},
#                         {'nombre' : "Dr.Strange",'anio' : 2016,'casa' : "DC",'biografia' : "El Doctor Stephen Strange, un neurocirujano muy reconocido, pierde el uso de sus manos en un terrible accidente de auto, quedando éstas aplastadas hasta el antebrazo. Strange sobrevive apenas. Su examante y compañera de trabajo Christine Palmer trata de ayudarlo a seguir adelante, pero en lugar de eso, el arrogante Strange quiere sanar rápidamente sus heridas."},
#                         {'nombre' : "Capitana Marvel",'anio' : 1962,'casa' : "Marvel",'biografia' : "1995, en el planeta Hala, capital del Imperio Kree, la guerrera y miembro de la Fuerza Estelar Vers sufre de pesadillas recurrentes que involucran a una mujer mayor. Yon-Rogg, su mentor y comandante, le advierte mientras entrenan que controle sus habilidades, y a su vez la Inteligencia Suprema, una inteligencia artificial orgánica que actúa como gobernante Kree, la insta a mantener sus emociones bajo control."},
#                         {'nombre' : "Mujer Maravilla",'anio' : 1941,'casa' : "DC",'biografia' : "El Traje de Mujer Maravilla ha variado con el tiempo, a pesar de que casi la totalidad de sus apariencias en sus encarnaciones han conservado una cierta forma de armadura, la tiara, los brazaletes y sus símbolos de estrella en su diseño.151​ Aunque el diseño de su traje se ha basado originalmente en el simbolismo de Estados Unidos y su iconografía, que permitió explicar más arraigada las raíces amazónicas. Durante una escena en retrospectiva en el volumen 3 de Wonder Woman,152​ Hipólita ordena la emisión de tener una prenda creada para Diana, que fue inspirada en el cielo nocturno en la noche en que Diana nació; una luna roja cazadora y en un campo de estrellas de azul profundo y el pectoral el águila, que es un símbolo de las representaciones antropomórficas de Atenea."},
#                         {'nombre' : "Flash",'anio' : 1959,'casa' : "DC",'biografia' : "Bartholomew Henry Barry Allen es un científico asistente de la División de Ciencia Criminal y Forense del Departamento de Policía de Ciudad Central en 1956, conocido por ser lento y llegar siempre tarde a su trabajo, lo cual enojaba a su prometida Iris West. Una noche, le cayó un rayo , un rayo cayó en su laboratorio lleno de químicos que bañaron a Allen, creando un accidente que le otorgaría una súper velocidad e increíbles reflejos (también la capacidad de viajar en el tiempo y entre dimensiones). Con un traje rojo y el símbolo de un rayo (que recuerda al original Capitán Maravilla de Fawcett Comics), su novia lo nombró Flash, (ya que cuando era niño algo veloz mató a su madre y Barry dijo que fue como un flash) empezando así a combatir el crimen en Ciudad Central."},
#                         {'nombre' : "Star-Lord",'anio' : 1976,'casa' : "Marvel",'biografia' : "supongamos que este tiene armadura, Cuando por accidente la nave de J'son cae en la Tierra, él es rescatado por Meredith Quill. Los dos forman una relación, mientras J'son hace reparaciones a su nave. Eventualmente, J'son se ve obligado a salir para regresar a casa y luchar en una guerra. Se va, sin saber que Meredith está embarazada de Peter Quill. 10 años más tarde, Meredith es asesinada cuando es atacada por dos soldados Badoon que han venido a matar a Peter y terminar la línea de sangre de J'son. Peter los mata con una pistola, encuentra la pistola de su padre por accidente, y escapa de su casa antes de que sea destruida por la nave Badoon. Los Badoon presumen que Peter es asesinado y se va. Peter es colocado en un orfanato y finalmente se une a la NASA. Finalmente se explicó que fue criado por su madre Lisa Chang, que era comandante de la NASA."},
#                         ]

# for SuperHeroe in SuperHeroes:
#     lista_SuperHeroes.insertar(SuperHeroe, 'nombre')
# pos = lista_SuperHeroes.busqueda('Linterna Verde', 'nombre')
# print(lista_SuperHeroes.obtener_elemento(pos))
# print('')

# print('a: Linterna verde se ha eliminado')
# lista_SuperHeroes.eliminar('Linterna Verde', 'nombre')
# pos = lista_SuperHeroes.busqueda('Linterna Verde', 'nombre')
# print(lista_SuperHeroes.obtener_elemento(pos))

# print('')
# print('b: Año de aparicion de Wolverine')
# pos = lista_SuperHeroes.busqueda('Wolverine', 'nombre')
# personaje = lista_SuperHeroes.obtener_elemento(pos)
# print(personaje['anio'])

# print('')
# print('c: La nueva casa de Dr. Strange')
# pos = lista_SuperHeroes.busqueda('Dr.Strange', 'nombre')
# personaje = lista_SuperHeroes.obtener_elemento(pos)
# personaje['casa'] = 'Marvel'
# lista_SuperHeroes.modificar_elemento(pos, personaje, 'nombre')
# pos = lista_SuperHeroes.busqueda('Dr.Strange', 'nombre')
# print(lista_SuperHeroes.obtener_elemento(pos))

# print('')
# print('d: Todos los heroes con traje o armadura')
# for i in range(0, lista_SuperHeroes.tamanio()):
#     personaje = lista_SuperHeroes.obtener_elemento(i)
#     if (personaje['biografia'].find('armadura')!= -1) or (personaje['biografia'].find('traje')!= -1):
#         print('el superheroe es:', personaje['nombre'])

# print('')
# print('e: Heroes con fecha de aparicion 1963')
# for i in range(0, lista_SuperHeroes.tamanio()):
#     personaje = lista_SuperHeroes.obtener_elemento(i)
#     if (personaje['anio']< 1963):
#         print('el superheroe es:', personaje['nombre'], personaje['casa'])

# print('')
# print('f: Casa de Capitana Marvel y Mujer Maravilla')
# pos = lista_SuperHeroes.busqueda('Capitana Marvel', 'nombre')
# personaje = lista_SuperHeroes.obtener_elemento(pos)
# print(personaje['nombre'],' ', personaje['casa'])

# pos = lista_SuperHeroes.busqueda('Mujer Maravilla', 'nombre')
# personaje = lista_SuperHeroes.obtener_elemento(pos)
# print(personaje['nombre'],' ', personaje['casa'])

# print('')
# print('g: Toda la informacion de Star-Lord')
# pos = lista_SuperHeroes.busqueda('Star-Lord', 'nombre')
# personaje = lista_SuperHeroes.obtener_elemento(pos)
# print(personaje)
# print('')
# print('Toda la informacion de Flash')
# pos = lista_SuperHeroes.busqueda('Flash', 'nombre')
# personaje = lista_SuperHeroes.obtener_elemento(pos)
# print(personaje)

# print('')
# print('h: SuperHeroes que su nombre comience con B, S, M')
# for i in range(0, lista_SuperHeroes.tamanio()):
#     personaje = lista_SuperHeroes.obtener_elemento(i)
#     if (personaje['nombre'][0] in ['B', 'S', 'M']):
#         print(personaje['nombre'])

# print('')
# print('i: Cuantos SuperHeroes tiene cada casa de comic ')
# contM=0
# contDc=0
# for i in range(0, lista_SuperHeroes.tamanio()):
#     personaje = lista_SuperHeroes.obtener_elemento(i)
#     if (personaje['casa'] == 'Marvel'):
#         contM += 1
#     else:
#         contDc += 1
# print('Marvel tiene', contM, 'personajes')
# print('DC tiene', contDc, 'personajes')

"""Ejercicio 7 """

# lista1 = Lista()
# lista2 = Lista()
# lista3 = Lista()
# lista_concate = Lista()

# for i in range (10):
#     lista1.insertar(randint(0,20))
#     lista2.insertar(randint(0,20))

# lista1.barrido()
# print()
# lista2.barrido()
# print()

# for i in range(lista1.tamanio()):
#     lista_concate.insertar(lista1.obtener_elemento(i))
# for i in range(lista2.tamanio()):
#     lista_concate.insertar(lista2.obtener_elemento(i))

# print('a: Lista concatenada')
# lista_concate.barrido()
# print()

# for i in range(lista1.tamanio()):
#     elemento = lista1.obtener_elemento(i)
#     pos = lista3.busqueda(elemento)
#     if (pos == -1):
#         lista3.insertar(elemento)


# for i in range(lista2.tamanio()):
#     elemento = lista2.obtener_elemento(i)
#     pos = lista3.busqueda(elemento)
#     if (pos == -1):
#         lista3.insertar(elemento)

# print('b: Lista concatenada, ordenada y sin repetidos')
# lista3.barrido()
# print()  

# cont = 0

# for i in range(lista1.tamanio()):
#     elemento = lista1.obtener_elemento(i)
#     pos = lista2.busqueda(elemento)
#     if (pos != -1):
#         cont += 1

# print('C: Contador repetidos', cont)
# print()

# while 0 < lista1.tamanio():
#     elemento = lista1.obtener_elemento(0)
#     print('C: Elemento eliminado' ,lista1.eliminar(elemento))



"""Ejercicio 15"""

datosEntrenador = [
                    {'nombre': 'Ash', 'cantTorneosGanados' : 3, 'cantBatallasPerdidas': 30, 'cantBatallasGanadas': 180, 'pokemons': Lista()}, 
                    {'nombre': 'Serena', 'cantTorneosGanados' : 1, 'cantBatallasPerdidas': 64, 'cantBatallasGanadas': 300, 'pokemons': Lista()},
                    {'nombre': 'Misty', 'cantTorneosGanados' : 4, 'cantBatallasPerdidas': 33, 'cantBatallasGanadas': 50, 'pokemons': Lista()},
                    {'nombre': 'Brock', 'cantTorneosGanados' : 9, 'cantBatallasPerdidas': 150, 'cantBatallasGanadas': 20, 'pokemons': Lista()},
                    {'nombre': 'Clemo', 'cantTorneosGanados' : 0, 'cantBatallasPerdidas': 98, 'cantBatallasGanadas': 1, 'pokemons': Lista()},
                    ]

datosPokemnos1 = [{'nombre': 'Pikachu', 'nivel': 100, 'tipo' : 'Electrico', 'subtipo': 'ninguno'},
                 {'nombre': 'Raichu', 'nivel': 30, 'tipo' : 'Electrico', 'subtipo': 'Rayo'},
                 {'nombre': 'Pikachu', 'nivel': 100, 'tipo' : 'Electrico', 'subtipo': 'ninguno'},
                 {'nombre': 'Bulbasaur', 'nivel': 23, 'tipo' : 'Agua', 'subtipo': 'ninguno'},
                 {'nombre': 'Ivysaur', 'nivel': 12, 'tipo' : 'Fuego', 'subtipo': 'ninguno'},
                 ]

datosPokemnos2 = [{'nombre': 'Venusaur', 'nivel': 30, 'tipo' : 'Viento', 'subtipo': 'ninguno'},
                 {'nombre': 'Raichu', 'nivel': 50, 'tipo' : 'Electrico', 'subtipo': 'Rayo'},
                 {'nombre': 'Squirtle', 'nivel': 90, 'tipo' : 'Agua', 'subtipo': 'ninguno'},
                 ]

datosPokemnos3 = [{'nombre': 'Weedle', 'nivel': 90, 'tipo' : 'Yerba', 'subtipo': 'ninguno'},
                  {'nombre': 'Wigglytuff', 'nivel': 20, 'tipo' : 'Fuego', 'subtipo': 'Planta'},
                  {'nombre': 'Terrakion', 'nivel': 3, 'tipo' : 'Tierra', 'subtipo': 'Ninguno'},
                 ]

datosPokemnos4 = [{'nombre': 'Spearow', 'nivel': 12, 'tipo' : 'Magnetismo', 'subtipo': 'ninguno'},
                 {'nombre': 'Ekans', 'nivel': 30, 'tipo' : 'Hielo', 'subtipo': 'ninguno'},
                 {'nombre': 'Arbok', 'nivel': 2, 'tipo' : 'Hielo', 'subtipo': 'ninguno'},
                 {'nombre': 'Ivysaur', 'nivel': 1, 'tipo' : 'Fuego', 'subtipo': 'ninguno'},
                 ]

datosPokemnos5 = [{'nombre': 'Arbok', 'nivel': 100, 'tipo' : 'Hielo', 'subtipo': ''},
                 {'nombre': 'Nidoking', 'nivel': 100, 'tipo' : 'Ninguno', 'subtipo': 'ninguno'},
                 {'nombre': 'Arbok', 'nivel': 1, 'tipo' : 'Hielo', 'subtipo': ''},
                 ]

lista_entrenadores = Lista()

for datoEntrenador in datosEntrenador:
    lista_entrenadores.insertar(datoEntrenador, 'nombre')

for pokemon in datosPokemnos1:
        lista_entrenadores.obtener_elemento(0)['pokemons'].insertar(pokemon, 'nombre')
for pokemon in datosPokemnos2:
        lista_entrenadores.obtener_elemento(1)['pokemons'].insertar(pokemon, 'nombre')
for pokemon in datosPokemnos3:
        lista_entrenadores.obtener_elemento(2)['pokemons'].insertar(pokemon, 'nombre')
for pokemon in datosPokemnos4:
        lista_entrenadores.obtener_elemento(3)['pokemons'].insertar(pokemon, 'nombre')
for pokemon in datosPokemnos5:
        lista_entrenadores.obtener_elemento(4)['pokemons'].insertar(pokemon, 'nombre')

#A
pos = lista_entrenadores.busqueda("Misty", 'nombre')
elemento = lista_entrenadores.obtener_elemento(pos)
print('La cantidad de pokemons del entrenador es de :',elemento["pokemons"].tamanio())
print('')

#B
for i in range(lista_entrenadores.tamanio()):
    elemento = lista_entrenadores.obtener_elemento(i)
    if elemento['cantTorneosGanados'] >=3:
        print('Los entrenadores con mas de 3 torneos ganados son:',elemento['nombre'])
print('')

#C
entrenador_mayor_torneos_ganados = 0
entrenador = None

for i in range(lista_entrenadores.tamanio()):
    elemento = lista_entrenadores.obtener_elemento(i)
    if elemento['cantTorneosGanados'] > entrenador_mayor_torneos_ganados:
        entrenador_mayor_torneos_ganados = elemento['cantTorneosGanados']
        entrenador = elemento

print('Entrenador con mas torneos ganados:',entrenador)

pokemons_mayor_nivel = 0
pokemons = None

for i in range(entrenador['pokemons'].tamanio()):
    elemento = entrenador['pokemons'].obtener_elemento(i)
    if elemento['nivel'] > pokemons_mayor_nivel:
        pokemons_mayor_nivel = elemento['nivel']
        pokemons = elemento

print('El pokemons de mayor nivel:',pokemons)
print('')

#D
pos = lista_entrenadores.busqueda("Brock", 'nombre')
entrenador = lista_entrenadores.obtener_elemento(pos)
print('Datos del entrenador:',entrenador)


for i in range(entrenador['pokemons'].tamanio()):
    elemento = entrenador['pokemons'].obtener_elemento(i)
    print('Sus pokemons:',elemento)
print('')


#E
for i in range(lista_entrenadores.tamanio()):
    elemento = lista_entrenadores.obtener_elemento(i)
    if (elemento['cantBatallasGanadas']*100)/(elemento['cantBatallasGanadas']+ elemento['cantBatallasPerdidas'])>79:
        print('Entrenador con batallas ganadas mayor a 79% ',elemento)
print('')


#F
print('Los entrenadores que tengan Pokémons de tipo fuego y planta o agua/volador')
for i in range(lista_entrenadores.tamanio()):
    elemento = lista_entrenadores.obtener_elemento(i)
    for j in range(elemento['pokemons'].tamanio()):
        elemento2 = elemento['pokemons'].obtener_elemento(j)
        if (elemento2['tipo'] == 'Fuego' and elemento2['subtipo'] == 'Planta')or(elemento2['tipo'] == 'Agua' and elemento2['subtipo'] == 'Volador'):
            print(elemento)
print('')        

#G
pos = lista_entrenadores.busqueda("Ash", 'nombre')
entrenador = lista_entrenadores.obtener_elemento(pos)
acu = 0
cont = 0
for i in range(entrenador['pokemons'].tamanio()):
    elemento = entrenador['pokemons'].obtener_elemento(i)
    cont += 1
    acu += elemento['nivel']
print('El promedio de pokemons es:' ,acu/cont)
print('')

#H
cont = 0
for i in range(lista_entrenadores.tamanio()):
    elemento = lista_entrenadores.obtener_elemento(i)
    for j in range(elemento['pokemons'].tamanio()):
        elemento2 = elemento['pokemons'].obtener_elemento(j)
        if (elemento2['nombre'] == 'Arbok'):
            cont +=1
print('El pokemon Arbok lo tiene', cont, 'entrenadores')
print('')

#i
for i in range(lista_entrenadores.tamanio()):
    elemento = lista_entrenadores.obtener_elemento(i)
    for j in range(elemento['pokemons'].tamanio()):
        for k in range(elemento['pokemons'].tamanio()):
            elemento2 = elemento['pokemons'].obtener_elemento(j)
            elemento3 = elemento['pokemons'].obtener_elemento(k)
            if (elemento2['nombre'] == elemento3['nombre']):
                print('El pokemon', elemento2['nombre'], 'lo tiene repetido el entrenador', elemento)
print('')

#J
for i in range(lista_entrenadores.tamanio()):
    elemento = lista_entrenadores.obtener_elemento(i)
    for j in range(elemento['pokemons'].tamanio()):
        elemento2 = elemento['pokemons'].obtener_elemento(j)
        if (elemento2['nombre'] in ['Tyrantrum', 'Terrakion', 'Wingull']):
            print('El', elemento, 'tiene uno de estos tres pokemons Tyrantrum', 'Terrakion', 'Wingull')

print('')
#K
entrenador = input('Ingrese el nombre del entrenador')
pokemon = input('Ingrese el nombre del pokemon')
pos = lista_entrenadores.busqueda(entrenador, 'nombre')
if (pos != -1):
    entrenador2 = lista_entrenadores.obtener_elemento(pos)
    pos = entrenador2['pokemons'].busqueda(pokemon, 'nombre')
    if (pos != -1):
        pokemon2 = entrenador2['pokemons'].obtener_elemento(pos)
        print(entrenador2, pokemon2)

"""Ejercicio 22"""

# lista_jedis = Lista()
# lista_especie = Lista()

# file = open('jedis.txt', encoding="utf8")
# lineas = file.readlines()
# lineas.pop(0)
# for linea in lineas:
#     jedi = linea.split(';')
#     jedi_data = {}
#     jedi_data['name'] = jedi[0].title()
#     jedi_data['rank'] = jedi[1].title()
#     jedi_data['species'] = jedi[2]
#     jedi_data['master'] = jedi[3].title().split('/')
#     jedi_data['lightsaber_color'] = jedi[4].split('/')
#     jedi_data['homeworld'] = jedi[5].title()
#     jedi_data['birth_year'] = jedi[6]
#     jedi_data['height'] = float(jedi[7].split('\n')[0])
#     if len(jedi) > 8:
#         jedi_data['to_darkside'] = jedi[8]
#         jedi_data['come_lightside'] =jedi[9]
#     lista_jedis.insertar(jedi_data, 'name')
#     lista_especie.insertar(jedi_data, 'species')

# #A
# print('Listado ordenado por nombre')
# for i in range(lista_jedis.tamanio()):
#     jedi = lista_jedis.obtener_elemento(i)
#     print(jedi)
# print('')
# print('Listado ordenado por especie')
# for i in range(lista_especie.tamanio()):
#     especie = lista_especie.obtener_elemento(i)
#     print(especie)
# print('')

# #B
# pos = lista_jedis.busqueda('Ahsoka Tano', 'name')
# if (pos != -1):
#     jedi = lista_jedis.obtener_elemento(pos)
#     print(jedi)
# pos = lista_jedis.busqueda('Kit Fisto', 'name')
# if (pos != -1):
#     jedi = lista_jedis.obtener_elemento(pos)
#     print(jedi)

# #C
# for i in range(lista_jedis.tamanio()):
#     jedi = lista_jedis.obtener_elemento(i)
#     if ('Yoda' in jedi['master'] or 'Luke Skywalker' in jedi['master']):
#         print(jedi)

# print('')
# #D
# for i in range(lista_jedis.tamanio()):
#     jedi = lista_jedis.obtener_elemento(i)
#     if (jedi['species'] == "twi'lek" or jedi['species'] == 'human'):
#         print(jedi)

# print('')

# #E
# for i in range(lista_jedis.tamanio()):
#     jedi = lista_jedis.obtener_elemento(i)
#     if (jedi['name'][0] == "A"):
#         print(jedi)

# print('')

# #F
# for i in range(lista_jedis.tamanio()):
#     jedi = lista_jedis.obtener_elemento(i)
#     if (len(jedi['lightsaber_color']) > 1):
#         print(jedi)

# print('')

# #G
# for i in range(lista_jedis.tamanio()):
#     jedi = lista_jedis.obtener_elemento(i)
#     if ('yellow' in jedi['lightsaber_color'] or 'purple' in jedi['lightsaber_color']):
#         print(jedi)

# print('')

# #H
# for i in range(lista_jedis.tamanio()):
#     jedi = lista_jedis.obtener_elemento(i)
#     if ('Qui-Gon Jin' in jedi['master'] or 'Mace Windu' in jedi['master']):
#         print(jedi)