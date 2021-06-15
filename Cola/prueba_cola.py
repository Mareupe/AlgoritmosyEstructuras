from cola import Cola
from random import randint

cola_datos = Cola()
cola_aux = Cola()

# for i in range(0, 10):
#     num = randint(0, 100)
#     cola_datos.arribo(num)
#     print(num)
# print()
# while(not cola_datos.cola_vacia()):
#     dato = cola_datos.atencion()
#     cola_aux.arribo(dato)
#     print(dato)


"""Ejercicio 11"""
# cola_Star = Cola()
# cola_auxS = Cola()

# StarWars = [['Luke', 'Alderaan'],['Han Solo', 'Endor'],['Yoda', 'Tatooine'],['Jar Jar Binks', 'Anoat'], ['Chewbacca', 'Tatooine']]
# #A,B
# for element in StarWars:
#     cola_Star.arribo(element)

# while not cola_Star.cola_vacia():
#     aux = cola_Star.atencion()
#     if (aux[1] in ['Alderaan', 'Endor' , 'Tatooine']):
#         print('El personaje', aux[0], 'es del planeta', aux[1])
#     if (aux[0] in ['Luke', 'Han Solo']):
#         print('El planeta natal de', aux[0], 'es:', aux[1])
#         print(' ')
#     cola_auxS.arribo(aux)

# print(' ')

# #C,D
# while not cola_auxS.cola_vacia():
#     aux = cola_auxS.atencion()
#     if (aux[0] == 'Yoda'):
#         cola_Star.arribo(['Obi-wan Kenobi', ' Endor'])
#     elif(aux[0] == 'Jar Jar Binks'):
#         cola_auxS.atencion()
#     cola_Star.arribo(aux)

# while(not cola_Star.cola_vacia()):
#     dato = cola_Star.atencion()
#     print(dato)
# print()

"""Ejercicio 12"""

# cola_1 = Cola()
# cola_2 = Cola()
# cola_3 = Cola()

# cola1 = [1, 2, 3, 4]
# cola2 = [5, 6, 7, 8]

# for element in cola1 and cola2:
#     cola_1.arribo()
#     cola_2.arribo()

# while not cola_1.cola_vacia() and not cola_2.cola_vacia():
    

"""Ejercicio 22"""

# cola_MCU = Cola()
# cola_auxM = Cola()

# Marvel = [['Tony Stark', 'Iron Man', 'M'],['Steve Rogers', 'Capitán América', 'M'], ['Natasha Romanoff','Black Widow', 'F'],['Carol Danvers', 'Capitana Marvel', 'F'],['Scott Lang','Ant-Man', 'M']]

# for element in Marvel:
#     cola_MCU.arribo(element)

# #A
# while not cola_MCU.cola_vacia():
#     aux = cola_MCU.atencion()
#     if (aux[1] in ['Capitana Marvel']):
#         print('El nombre del personaje de la supehéroe', aux[1],'es', aux[0])
#     cola_auxM.arribo(aux)

# print(' ')

# #B,C
# while not cola_auxM.cola_vacia():
#     aux = cola_auxM.atencion()
#     if(aux[2] in ['F']):
#         print('Superhéroes Femeninos', aux[1])
#     else:
#         print('Superhéroes Masculinos', aux[1])
#     cola_MCU.arribo(aux)

# print(' ')

# #D
# while not cola_MCU.cola_vacia():
#     aux = cola_MCU.atencion()
#     if(aux[0] in ['Scott Lang']):
#         print('El nombre del personaje de', aux[0],'es', aux[1])
#     cola_auxM.arribo(aux)

# print(' ')

# #E
# while not cola_auxM.cola_vacia():
#     aux = cola_auxM.atencion()
#     if(aux[0][0] in ['S']):
#         print('Los personajes o Superhéroes que comienza con S son:', aux[0])
#     cola_MCU.arribo(aux)

# print('')

# #F
# while not cola_MCU.cola_vacia():
#     aux = cola_MCU.atencion()
#     if (aux[0] in ['Carol Danvers']):
#         print(aux[0],'se encuentra en la cola, y su superhéroe se llama', aux[1])
#     cola_auxM.arribo(aux)