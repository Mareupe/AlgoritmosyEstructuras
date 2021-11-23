from grafo import Grafo

grafo = Grafo(dirigido=False)

grafo.insertar_vertice('Atenas' ,data={'Latitud' : '21º 46 52 S', 'Longitud': '66º 13 17'})
grafo.insertar_vertice('Zeus' ,data={'Latitud' : ' 28º 23 67', 'Longitud': '66º 12 87'})
grafo.insertar_vertice('Hera',data={'Latitud' : ' 27º 713 11', 'Longitud': '615º 83 87'})
grafo.insertar_vertice('Apolo', data={'Latitud' : ' 71º 2 10', 'Longitud': '102º 1 87'})
grafo.insertar_vertice('Poseidon',data={'Latitud' : ' 38º 91 09', 'Longitud': '59º 92 87'})
grafo.insertar_vertice('Artemisa', data={'Latitud' : ' 11º 10 12', 'Longitud': '16º 1 91'})
grafo.insertar_vertice('Teatro de Dionisio', data={'Latitud' : ' 99º 13 1', 'Longitud': '62º 1 64'})

grafo.insertar_arista(120, 'Atenas', 'Zeus')
grafo.insertar_arista(120, 'Atenas', 'Hera')
grafo.insertar_arista(10, 'Atenas', 'Apolo')
grafo.insertar_arista(121, 'Atenas', 'Poseidon')
grafo.insertar_arista(23, 'Atenas', 'Artemisa')
grafo.insertar_arista(54, 'Atenas', 'Teatro de Dionisio')
grafo.insertar_arista(64, 'Zeus', 'Hera')
grafo.insertar_arista(12, 'Zeus', 'Apolo')
grafo.insertar_arista(67, 'Zeus', 'Poseidon')
grafo.insertar_arista(10, 'Zeus', 'Artemisa')
grafo.insertar_arista(15, 'Zeus', 'Teatro de Dionisio')
grafo.insertar_arista(23, 'Hera', 'Apolo')
grafo.insertar_arista(93, 'Hera', 'Poseidon')
grafo.insertar_arista(8, 'Hera', 'Artemisa')
grafo.insertar_arista(6, 'Hera', 'Teatro de Dionisio')
grafo.insertar_arista(21, 'Apolo', 'Poseidon')
grafo.insertar_arista(461, 'Apolo', 'Artemisa')
grafo.insertar_arista(741, 'Apolo', 'Teatro de Dionisio')
grafo.insertar_arista(211, 'Poseidon', 'Artemisa')
grafo.insertar_arista(61, 'Poseidon', 'Teatro de Dionisio')
grafo.insertar_arista(14, 'Artemisa', 'Teatro de Dionisio')

#C
exp_mini = grafo.prim()
peso = 0
print('Árbol de expansión mínimo:')
for elemento in exp_mini:
    print(elemento[1])
    peso += elemento[0]
print('El costo total es', peso, 'km.')
print()

#D
ver_origen = grafo.buscar_vertice('Atenas')
ver_destino = grafo.buscar_vertice('Apolo')

pila_camino = grafo.dijkstra(ver_origen, ver_destino)
costo = None
destino = 'Apolo'
while(not pila_camino.pila_vacia()):
    dato = pila_camino.desapilar()
    if(dato[1][0] == destino):
        if(costo is None):
            costo = dato[0]
        print(dato[1][0])
        destino = dato[1][1]

print('El costo total del camino es', costo)


