from grafo import Grafo
from lista import Lista

dioses = Grafo(dirigido=False)

dioses.insertar_vertice('Urano', data='Acercamiento a la mitología griega')
dioses.insertar_vertice('Gaia', data='diosa del misterio')

dioses.insertar_vertice('Themis', data='diosa del misterio')
dioses.insertar_vertice('Mnemosyne', data='diosa del misterio')
dioses.insertar_vertice('Hyperomn', data='diosa del misterio')
dioses.insertar_vertice('Theia', data='diosa del misterio')
dioses.insertar_vertice('Krios', data='diosa del misterio')
dioses.insertar_vertice('Kronos', data='diosa del misterio')
dioses.insertar_vertice('Rhea', data='diosa del misterio')
dioses.insertar_vertice('Kdios', data='diosa del misterio')
dioses.insertar_vertice('Phobe', data='diosa del misterio')
dioses.insertar_vertice('Iapetos', data='diosa del misterio')
dioses.insertar_vertice('Okeanos', data='diosa del misterio')
dioses.insertar_vertice('Tethys', data='diosa del misterio')
dioses.insertar_vertice('Helios', data='diosa del misterio')
dioses.insertar_vertice('Selene', data='diosa del misterio')
dioses.insertar_vertice('Eos', data='diosa del misterio')
dioses.insertar_vertice('Prometheus', data='diosa del misterio')
dioses.insertar_vertice('Epimetheus', data='diosa del misterio')
dioses.insertar_vertice('Atlas', data='diosa del misterio')
dioses.insertar_vertice('Pleone', data='diosa del misterio')
dioses.insertar_vertice('Poseidon', data='diosa del misterio')


dioses.insertar_vertice('Hestia', data='diosa del misterio')
dioses.insertar_vertice('Hera', data='diosa del misterio')
dioses.insertar_vertice('Zeus', data='el dios del cielo')
dioses.insertar_vertice('Leto', data='diosa del misterio')
dioses.insertar_vertice('Semele', data='diosa del misterio')
dioses.insertar_vertice('Maia', data='diosa del misterio')

dioses.insertar_vertice('Persephone', data='diosa del misterio')
dioses.insertar_vertice('Aphrodite', data='diosa del misterio')
dioses.insertar_vertice('Ares', data='dissa del misterio')
dioses.insertar_vertice('Hephaistos', data='diossa del misterio')
dioses.insertar_vertice('Athena', data='diosa del misterio')
dioses.insertar_vertice('Apollo', data='protector de la musica y de la medicina')
dioses.insertar_vertice('Ardemis', data='diosa del misterio')
dioses.insertar_vertice('Dionysos', data='diosa del misterio')
dioses.insertar_vertice('Hermes', data='diosa del misterio')
dioses.insertar_vertice('Penelopeia', data='diosa del misterio')
dioses.insertar_vertice('Deiomos', data='diosa del misterio')


dioses.insertar_vertice('Phobos', data='diosa del misterio')
dioses.insertar_vertice('Deimos', data='diosa del misterio')
dioses.insertar_vertice('Eros', data='diosa del misterio')
dioses.insertar_vertice('Himeros', data='diosa del misterio')
dioses.insertar_vertice('Pan', data='diosa del misterio')
dioses.insertar_vertice('Hades', data='diosa del misterio')
dioses.insertar_vertice('Demeter', data='diosa del misterio')
dioses.insertar_vertice('Hermaphrodite', data='diosa del misterio')
dioses.insertar_vertice('Hermes', data='diosa del misterio')

dioses.insertar_arista(1, 'Urano', 'Gaia', data={'relacion': ['esposos']})

dioses.insertar_arista(1, 'Urano', 'Themis', data={'relacion': ['padre', 'hijo']})
dioses.insertar_arista(1, 'Urano', 'Mnemosyne', data={'relacion': ['padre', 'hijo']})
dioses.insertar_arista(1, 'Urano', 'Theia', data={'relacion': ['padre','hijo']})
dioses.insertar_arista(1, 'Urano', 'Hyperomn', data={'relacion': ['padre', 'hijo']})
dioses.insertar_arista(1, 'Urano', 'Krios', data={'relacion': ['padre', 'hijo']})
dioses.insertar_arista(1, 'Urano', 'Kronos', data={'relacion': ['padre', 'hijo']})
dioses.insertar_arista(1, 'Urano', 'Rhea', data={'relacion': ['padre', 'hijo']})
dioses.insertar_arista(1, 'Urano', 'Kdios', data={'relacion': ['padre', 'hijo']})
dioses.insertar_arista(1, 'Urano', 'Phobe', data={'relacion': ['padre', 'hijo']})
dioses.insertar_arista(1, 'Urano', 'Iapetos', data={'relacion': ['padre', 'hijo']})
dioses.insertar_arista(1, 'Urano', 'Okeanos', data={'relacion': ['padre', 'hijo']})
dioses.insertar_arista(1, 'Urano', 'Tethys', data={'relacion': ['padre', 'hijo']})

dioses.insertar_arista(1, 'Gaia', 'Gaia', data={'relacion': ['Marido','Mujer']})

dioses.insertar_arista(1, 'Gaia', 'Themis', data={'relacion': ['madre', 'hijo']})
dioses.insertar_arista(1, 'Gaia', 'Mnemosyne', data={'relacion': ['madre', 'hijo']})
dioses.insertar_arista(1, 'Gaia', 'Hyperomn', data={'relacion': ['madre', 'hijo']})
dioses.insertar_arista(1, 'Gaia', 'Theia', data={'relacion': ['madre', 'hijo']})
dioses.insertar_arista(1, 'Gaia', 'Krios', data={'relacion': ['madre', 'hijo']})
dioses.insertar_arista(1, 'Gaia', 'Kronos', data={'relacion': ['madre', 'hijo']})
dioses.insertar_arista(1, 'Gaia', 'Rhea', data={'relacion': ['madre', 'hijo']})
dioses.insertar_arista(1, 'Gaia', 'Kdios', data={'relacion': ['madre', 'hijo']})
dioses.insertar_arista(1, 'Gaia', 'Phobe', data={'relacion': ['madre', 'hijo']})
dioses.insertar_arista(1, 'Gaia', 'Iapetos', data={'relacion': ['madre', 'hijo']})
dioses.insertar_arista(1, 'Gaia', 'Okeanos', data={'relacion': ['madre', 'hijo']})
dioses.insertar_arista(1, 'Gaia', 'Tethys', data={'relacion': ['madre', 'hijo']})


dioses.insertar_arista(1, 'Themis', 'Mnemosyne', data={'relacion': ['hermano']})
dioses.insertar_arista(1, 'Themis', 'Hyperomn', data={'relacion': ['hermano']})
dioses.insertar_arista(1, 'Themis', 'Theia', data={'relacion': ['hermano']})
dioses.insertar_arista(1, 'Themis', 'Krios', data={'relacion': ['hermano']})
dioses.insertar_arista(1, 'Themis', 'Kronos', data={'relacion': ['hermano']})
dioses.insertar_arista(1, 'Themis', 'Rhea', data={'relacion': ['hermano']})
dioses.insertar_arista(1, 'Themis', 'Kdios', data={'relacion': ['hermano']})
dioses.insertar_arista(1, 'Themis', 'Phobe', data={'relacion': ['hermano']})
dioses.insertar_arista(1, 'Themis', 'Iapetos', data={'relacion': ['hermano']})
dioses.insertar_arista(1, 'Themis', 'Okeanos', data={'relacion': ['hermano']})
dioses.insertar_arista(1, 'Themis', 'Tethys', data={'relacion': ['hermano']})

dioses.insertar_arista(1, 'Mnemosyne', 'Hyperomn', data={'relacion': ['hermano']})
dioses.insertar_arista(1, 'Mnemosyne', 'Theia', data={'relacion': ['hermano']})
dioses.insertar_arista(1, 'Mnemosyne', 'Krios', data={'relacion': ['hermano']})
dioses.insertar_arista(1, 'Mnemosyne', 'Kronos', data={'relacion': ['hermano']})
dioses.insertar_arista(1, 'Mnemosyne', 'Rhea', data={'relacion': ['hermano']})
dioses.insertar_arista(1, 'Mnemosyne', 'Kdios', data={'relacion': ['hermano']})
dioses.insertar_arista(1, 'Mnemosyne', 'Phobe', data={'relacion': ['hermano']})
dioses.insertar_arista(1, 'Mnemosyne', 'Iapetos', data={'relacion': ['hermano']})
dioses.insertar_arista(1, 'Mnemosyne', 'Okeanos', data={'relacion': ['hermano']})
dioses.insertar_arista(1, 'Mnemosyne', 'Tethys', data={'relacion': ['hermano']})

dioses.insertar_arista(1, 'Hyperomn', 'Theia', data={'relacion': ['hermano']})
dioses.insertar_arista(1, 'Hyperomn', 'Krios', data={'relacion': ['hermano']})
dioses.insertar_arista(1, 'Hyperomn', 'Kronos', data={'relacion': ['hermano']})
dioses.insertar_arista(1, 'Hyperomn', 'Rhea', data={'relacion': ['hermano']})
dioses.insertar_arista(1, 'Hyperomn', 'Kdios', data={'relacion': ['hermano']})
dioses.insertar_arista(1, 'Hyperomn', 'Phobe', data={'relacion': ['hermano']})
dioses.insertar_arista(1, 'Hyperomn', 'Iapetos', data={'relacion': ['hermano']})
dioses.insertar_arista(1, 'Hyperomn', 'Okeanos', data={'relacion': ['hermano']})
dioses.insertar_arista(1, 'Hyperomn', 'Tethys', data={'relacion': ['hermano']})

dioses.insertar_arista(1, 'Theia', 'Krios', data={'relacion': ['hermano']})
dioses.insertar_arista(1, 'Theia', 'Kronos', data={'relacion': ['hermano']})
dioses.insertar_arista(1, 'Theia', 'Rhea', data={'relacion': ['hermano']})
dioses.insertar_arista(1, 'Theia', 'Kdios', data={'relacion': ['hermano']})
dioses.insertar_arista(1, 'Theia', 'Phobe', data={'relacion': ['hermano']})
dioses.insertar_arista(1, 'Theia', 'Iapetos', data={'relacion': ['hermano']})
dioses.insertar_arista(1, 'Theia', 'Okeanos', data={'relacion': ['hermano']})
dioses.insertar_arista(1, 'Theia', 'Tethys', data={'relacion': ['hermano']})

dioses.insertar_arista(1, 'Krios', 'Kronos', data={'relacion': ['hermano']})
dioses.insertar_arista(1, 'Krios', 'Rhea', data={'relacion': ['hermano']})
dioses.insertar_arista(1, 'Krios', 'Kdios', data={'relacion': ['hermano']})
dioses.insertar_arista(1, 'Krios', 'Phobe', data={'relacion': ['hermano']})
dioses.insertar_arista(1, 'Krios', 'Iapetos', data={'relacion': ['hermano']})
dioses.insertar_arista(1, 'Krios', 'Okeanos', data={'relacion': ['hermano']})
dioses.insertar_arista(1, 'Krios', 'Tethys', data={'relacion': ['hermano']})

dioses.insertar_arista(1, 'Kronos', 'Rhea', data={'relacion': ['hermano']})
dioses.insertar_arista(1, 'Kronos', 'Kdios', data={'relacion': ['hermano']})
dioses.insertar_arista(1, 'Kronos', 'Phobe', data={'relacion': ['hermano']})
dioses.insertar_arista(1, 'Kronos', 'Iapetos', data={'relacion': ['hermano']})
dioses.insertar_arista(1, 'Kronos', 'Okeanos', data={'relacion': ['hermano']})
dioses.insertar_arista(1, 'Kronos', 'Tethys', data={'relacion': ['hermano']})



dioses.insertar_arista(1, 'Rhea', 'Phobe', data={'relacion': ['hermano']})
dioses.insertar_arista(1, 'Rhea', 'Kdios', data={'relacion': ['hermano']})
dioses.insertar_arista(1, 'Rhea', 'Iapetos', data={'relacion': ['hermano']})
dioses.insertar_arista(1, 'Rhea', 'Okeanos', data={'relacion': ['hermano']})
dioses.insertar_arista(1, 'Rhea', 'Tethys', data={'relacion': ['hermano']})

dioses.insertar_arista(1, 'Phobe', 'Kdios', data={'relacion': ['hermano']})
dioses.insertar_arista(1, 'Phobe', 'Iapetos', data={'relacion': ['hermano']})
dioses.insertar_arista(1, 'Phobe', 'Okeanos', data={'relacion': ['hermano']})
dioses.insertar_arista(1, 'Phobe', 'Tethys', data={'relacion': ['hermano']})

dioses.insertar_arista(1, 'Kdios', 'Iapetos', data={'relacion': ['hermano']})
dioses.insertar_arista(1, 'Kdios', 'Okeanos', data={'relacion': ['hermano']})
dioses.insertar_arista(1, 'Kdios', 'Tethys', data={'relacion': ['hermano']})



dioses.insertar_arista(1, 'Iapetos', 'Okeanos', data={'relacion': ['hermano']})
dioses.insertar_arista(1, 'Iapetos', 'Tethys', data={'relacion': ['hermano']})

dioses.insertar_arista(1, 'Okeanos', 'Tethys', data={'relacion': ['hermano']})


dioses.insertar_arista(1, 'Hyperomn', 'Theia', data={'relacion': ['marido', 'mujer']})
dioses.insertar_arista(1, 'Hyperomn', 'Helios', data={'relacion': ['padre', 'hijo']})
dioses.insertar_arista(1, 'Hyperomn', 'Eos', data={'relacion': ['padre', 'hijo']})
dioses.insertar_arista(1, 'Hyperomn', 'Selene', data={'relacion': ['padre', 'hijo']})

dioses.insertar_arista(1, 'Theia', 'Helios', data={'relacion': ['madre', 'hijo']})
dioses.insertar_arista(1, 'Theia', 'Eos', data={'relacion': ['madre', 'hijo']})
dioses.insertar_arista(1, 'Theia', 'Selene', data={'relacion': ['madre', 'hijo']})

dioses.insertar_arista(1, 'Helios', 'Eos', data={'relacion': ['hermano']})
dioses.insertar_arista(1, 'Helios', 'Selene', data={'relacion': ['hermano']})

dioses.insertar_arista(1, 'Eos', 'Selene', data={'relacion': ['hermano']})

dioses.insertar_arista(1, 'Iapetos', 'Prometheus', data={'relacion': ['padre', 'hijo']})
dioses.insertar_arista(1, 'Iapetos', 'Epimetheus', data={'relacion': ['padre', 'hijo']})
dioses.insertar_arista(1, 'Iapetos', 'Atlas', data={'relacion': ['padre', 'hijo']})
dioses.insertar_arista(1, 'Iapetos', 'Pleone', data={'relacion': ['padre', 'hijo']})

dioses.insertar_arista(1, 'Prometheus', 'Epimetheus', data={'relacion': ['hermano']})
dioses.insertar_arista(1, 'Prometheus', 'Atlas', data={'relacion': ['hermano']})
dioses.insertar_arista(1, 'Prometheus', 'Pleone', data={'relacion': ['hermano']})

dioses.insertar_arista(1, 'Epimetheus', 'Atlas', data={'relacion': ['hermano']})
dioses.insertar_arista(1, 'Epimetheus', 'Pleone', data={'relacion': ['hermano']})

dioses.insertar_arista(1, 'Atlas', 'Pleone', data={'relacion': ['hermano']})


dioses.insertar_arista(4,'Hestia', 'Rhea', data={'relacion': ['hijo', 'madre']})
dioses.insertar_arista(4,'Hestia', 'Kronos', data={'relacion': ['hijo', 'padre']})
dioses.insertar_arista(4,'Hestia', 'Zeus', data={'relacion': ['hermano']})
dioses.insertar_arista(4,'Hestia', 'Hera', data={'relacion': ['hermana']})

dioses.insertar_arista(4,'Hera', 'Rhea', data={'relacion': ['hijo', 'madre']})
dioses.insertar_arista(4,'Hera', 'Kronos', data={'relacion': ['hijo', 'padre']})
dioses.insertar_arista(4,'Hera', 'Zeus', data={'relacion': ['hermano']})
dioses.insertar_arista(4,'Hera', 'Zeus', data={'relacion': ['esposos']})
dioses.insertar_arista(5, 'Hera', 'Ares', data={'relacion': ['madre', 'hijo']})
dioses.insertar_arista(5, 'Hera', 'Hephaistos', data={'relacion': ['hijo', 'madre']})


dioses.insertar_arista(4,'Zeus', 'Rhea', data={'relacion': ['hijo', 'madre']})
dioses.insertar_arista(4,'Zeus', 'Kronos', data={'relacion': ['hijo', 'padre']})
dioses.insertar_arista(4,'Zeus', 'Hera', data={'relacion': ['esposa']})
dioses.insertar_arista(4,'Zeus', 'Leto', data={'relacion': ['amante']})
dioses.insertar_arista(5, 'Zeus', 'Persephone', data={'relacion': ['padre', 'hijo']})
dioses.insertar_arista(5, 'Zeus', 'Hephaistos', data={'relacion': ['padre', 'hijo']})
dioses.insertar_arista(5, 'Zeus', 'Athena', data={'relacion': ['padre', 'hijo']})
dioses.insertar_arista(5, 'Zeus', 'Ardemis', data={'relacion': ['padre', 'hijo']})
dioses.insertar_arista(5, 'Zeus', 'Dionysos', data={'relacion': ['padre','hijo']})
dioses.insertar_arista(5, 'Zeus', 'Hermes', data={'relacion': ['padre','hijo']})
dioses.insertar_arista(5, 'Zeus', 'Apollo', data={'relacion': ['padre', 'hijo']})


dioses.insertar_arista(4,'Leto', 'Kdios', data={'relacion': ['hijo', 'padre']})
dioses.insertar_arista(4,'Leto', 'Phobe', data={'relacion': ['hijo', 'madre']})

dioses.insertar_arista(4,'Poseidon', 'Kronos', data={'relacion': ['hijo', 'padre']})
dioses.insertar_arista(4,'Demeter', 'Kronos', data={'relacion': ['hijo', 'padre']})
dioses.insertar_arista(4,'Hades', 'Kronos', data={'relacion': ['hijo', 'padre']})




dioses.insertar_arista(4,'Semele', 'Zeus', data={'relacion': ['amante']})


dioses.insertar_arista(4,'Maia', 'Atlas', data={'relacion': ['hijo', 'padre']})
dioses.insertar_arista(4,'Maia', 'Pleone', data={'relacion': ['hijo', 'madre']})
dioses.insertar_arista(4,'Maia', 'Zeus', data={'relacion': ['amante']})

dioses.insertar_arista(5, 'Persephone', 'Hades', data={'relacion': ['esposos']})
dioses.insertar_arista(5, 'Persephone', 'Demeter', data={'relacion': ['hijo','madre']})


dioses.insertar_arista(5, 'Aphrodite', 'Urano', data={'relacion': ['hijo', 'padre']})
dioses.insertar_arista(5, 'Aphrodite', 'Ares', data={'relacion': ['esposos']})
dioses.insertar_arista(5, 'Aphrodite', 'Hephaistos', data={'relacion': ['amante']})
dioses.insertar_arista(5, 'Aphrodite', 'Hermes', data={'relacion': ['amante']})
dioses.insertar_arista(6, 'Aphrodite', 'Himeros', data={'relacion': ['madre','hijo']})
dioses.insertar_arista(6, 'Aphrodite', 'Phobos', data={'relacion': ['madre','hijo']})
dioses.insertar_arista(6, 'Aphrodite', 'Eros', data={'relacion': ['madre','hijo']})
dioses.insertar_arista(6, 'Aphrodite', 'Deimos', data={'relacion': ['madre','hijo']})

dioses.insertar_arista(5, 'Ares', 'Hephaistos', data={'relacion': ['hermano']})

dioses.insertar_arista(6, 'Ares', 'Phobos', data={'relacion': ['padre','hijo']})
dioses.insertar_arista(6, 'Ares', 'Deimos', data={'relacion': ['padre','hijo']})
dioses.insertar_arista(6, 'Ares', 'Eros', data={'relacion': ['padre','hijo']})
dioses.insertar_arista(6, 'Ares', 'Himeros', data={'relacion': ['padre','hijo']})



dioses.insertar_arista(5, 'Apollo', 'Leto', data={'relacion': ['hijo', 'madre']})
dioses.insertar_arista(5, 'Apollo', 'Ardemis', data={'relacion': ['hermano']})

dioses.insertar_arista(5, 'Ardemis', 'Leto', data={'relacion': ['hijo', 'madre']})
dioses.insertar_arista(5, 'Ardemis', 'Apollo', data={'relacion': ['hermano']})

dioses.insertar_arista(5, 'Dionysos', 'Semele', data={'relacion': ['hijo', 'madre']})

dioses.insertar_arista(5, 'Hermes', 'Maia', data={'relacion': ['hijo','madre']})

dioses.insertar_arista(5, 'Hermes', 'Penelopeia', data={'relacion': ['esposa']})
dioses.insertar_arista(5, 'Hermes', 'Pan', data={'relacion': ['padre','hijo']})

dioses.insertar_arista(6, 'Phobos', 'Deimos', data={'relacion': ['hermano']})
dioses.insertar_arista(6, 'Phobos', 'Eros', data={'relacion': ['hermano']})
dioses.insertar_arista(6, 'Phobos', 'Himeros', data={'relacion': ['hermano']})
dioses.insertar_arista(6, 'Phobos', 'Aphrodite', data={'relacion': ['hijo','madre']})
dioses.insertar_arista(6, 'Phobos', 'Ares', data={'relacion': ['hijo','padre']})

dioses.insertar_arista(6, 'Deiomos', 'Ares', data={'relacion': ['hijo','padre']})
dioses.insertar_arista(6, 'Deiomos', 'Aphrodite', data={'relacion': ['hijo','madre']})

dioses.insertar_arista(6, 'Eros', 'Ares', data={'relacion': ['hijo','padre']})
dioses.insertar_arista(6, 'Eros', 'Aphrodite', data={'relacion': ['hijo','madre']})

dioses.insertar_arista(6, 'Himeros', 'Ares', data={'relacion': ['hijo','padre']})
dioses.insertar_arista(6, 'Himeros', 'Aphrodite', data={'relacion': ['hijo','madre']})

dioses.insertar_arista(6, 'Hermaphrodite', 'Hermes', data={'relacion': ['hijo','padre']})
dioses.insertar_arista(6, 'Hermaphrodite', 'Aphrodite', data={'relacion': ['hijo','padre']})

dioses.insertar_arista(6, 'Pan', 'Hermes', data={'relacion': ['hijo','padre']})
dioses.insertar_arista(6, 'Pan', 'Penelopeia', data={'relacion': ['hijo','madre']})

#C
hijos = dioses.hijos('Urano')
print('Los hijos del Dios Urano son:')
for i in hijos:
    print(i)
print('')

#D
print('Urano')
padre, hijo, hermano = dioses.familia('Urano')
print('Padre:', padre,'Hijo/os:', hijo,'Hermano/os:', hermano)
print('')

#E
def directo(ver_origen, ver_destino):
    print('Tiene relacion directa:')
    pos = dioses.buscar_arista(ver_origen, ver_destino)
    if(pos != 1):
        pos_aux = dioses.buscar_vertice('Urano')
        print(dioses.inicio.obtener_elemento(pos_aux)['aristas'].obtener_elemento(pos))

directo('Urano', 'Themis')
print('')

#F
ver_origen = dioses.buscar_vertice('Urano')
ver_destino = dioses.buscar_vertice('Zeus')

pila_camino = dioses.dijkstra(ver_origen, ver_destino)
costo = None
destino = 'Zeus'
while(not pila_camino.pila_vacia()):
    dato = pila_camino.desapilar()
    if(dato[1][0] == destino):
        if(costo is None):
            costo = dato[0]
        print(dato[1][0])
        destino = dato[1][1]

print('El costo total del camino mas corto es:', costo)

print('')

# #G
print('Barrido en Profundidad de Grafo:')
dioses.barrido_profundidad(0)
print('')
dioses.marcar_no_visitado()
print('Barrido en Amplitud del Grafo:')
dioses.barrido_amplitud(0)
dioses.marcar_no_visitado()

print('')

#H
def relaciones(dios, relacion):
    origen = dioses.buscar_vertice(dios)
    if (origen != -1):
        dios = dioses.inicio.obtener_elemento(origen)
        for i in range(dios['aristas'].tamanio()):
            dio = dios['aristas'].obtener_elemento(i)
            if(relacion in dio['data']['relacion'][-1]):
                print(dio['destino'])       
    else:
        print('dios no encontrado')

print('Dios y su Madre')
def barrido_madre():
    for i in range(dioses.tamanio()):
        dios = dioses.inicio.obtener_elemento(i)
        aux = dios['info']
        print('Madre de: ',aux)
        relaciones(aux, 'madre')

barrido_madre()
print('')

#I
def ancestro(vertice_nombre):
    origen = dioses.buscar_vertice(vertice_nombre)
    if(origen != -1):
        dios = dioses.inicio.obtener_elemento(origen)
        for i in range(dios['aristas'].tamanio()):
            nombre_dios = dios['aristas'].obtener_elemento(i)['destino']
            dios_aux = dios['aristas'].obtener_elemento(i)['data']
            if(len(dios_aux['relacion']) > 1):
                if(dios_aux['relacion'][1] == 'padre' or dios_aux['relacion'][1] == 'madre'):
                    print(nombre_dios, dios_aux['relacion'])
                    ancestro(nombre_dios)

print('Los ancestros de un Dios:')
ancestro('Zeus') 

print('')

#J
print('Los nietos de Cronos son:')
def nietos(dios, relacion = 'hijo'):
    origen = dioses.buscar_vertice(dios)
    if (origen != -1):
        dios = dioses.inicio.obtener_elemento(origen)
        for i in range(dios['aristas'].tamanio()):
            dio = dios['aristas'].obtener_elemento(i)
            if(relacion in dio['data']['relacion'][-1]):
                relaciones(dio['destino'], 'hijo')
    else:
        print('dios no encontrado')

nietos('Kronos')

print('')

#K
print('Los hijos de Tea son:')
hijos = dioses.hijos('Theia')
for i in hijos:
    print(i)
print('')


#HASTA ACA LOS EJERCICIOS A ENTREGAR











# for i in range(dioses.inicio.tamanio()):
#     dios = dioses.inicio.obtener_elemento(i)
#     print('aristas', dios['info'])
#     for j in range(dios['aristas'].tamanio()):
#         print(dios['aristas'].obtener_elemento(j))

#     print()

# origen = dioses.buscar_vertice('Cronos')
# dios = dioses.inicio.obtener_elemento(origen)
# print('aristas', dios['info'])
# for j in range(dios['aristas'].tamanio()):
#     arista = dios['aristas'].obtener_elemento(j)
#     if(len(arista['data']['relacion']) == 2):
#         if(arista['data']['relacion'][1] == 'hijo'):
#             print(arista)
# print()
# origen = dioses.buscar_vertice('Cronos')
# dios = dioses.inicio.obtener_elemento(origen)
# print('aristas', dios['info'])
# for j in range(dios['aristas'].tamanio()):
#     arista = dios['aristas'].obtener_elemento(j)
#     if(len(arista['data']['relacion']) == 2):
#         if(arista['data']['relacion'][1] == 'padre'):
#             print(arista)

# print()
# origen = dioses.buscar_vertice('Cronos')
# dios = dioses.inicio.obtener_elemento(origen)
# print('aristas', dios['info'])
# for j in range(dios['aristas'].tamanio()):
#     arista = dios['aristas'].obtener_elemento(j)
#     if(arista['data']['relacion'][0] == 'hermano'):
#         print(arista)

# print()
# origen = dioses.buscar_vertice('Cronos')
# dios = dioses.inicio.obtener_elemento(origen)
# print('aristas', dios['info'])
# for j in range(dios['aristas'].tamanio()):
#     arista = dios['aristas'].obtener_elemento(j)
#     if(arista['destino'] == 'Zeus'):
#         print(arista)


# vertice_origen = dioses.buscar_vertice('Urano')
# vertice_destino = dioses.buscar_vertice('Atenea')

# camino = dioses.dijkstra(vertice_origen, vertice_destino)

# destino = 'Atenea'
# costo = None
# while(not camino.pila_vacia()):
#     dato = camino.desapilar()
#     if(dato[1][0] == destino):
#         if(costo is None):
#             costo = dato[0]
#         print(dato[1][0])
#         destino = dato[1][1]
# print('el costo total del camino es:', costo)