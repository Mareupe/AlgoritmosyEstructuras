
class Lista(object):
    """crea un objeto de tipo lista"""

    def __init__(self):
        self.__elementos= []
    
    def __criterio(self, dato, criterio):
        if(criterio == None):
            return dato
        else:
            return dato[criterio]


    def insertar(self, dato, criterio=None):#! tener en cuenta que la insercion es ordenada
        if(len(self.__elementos) == 0):
            self.__elementos.append(dato)
        elif(self.__criterio(dato, criterio)< self.__criterio(self.__elementos[0], criterio)):
            self.__elementos.insert(0, dato)
        else:
            pos = 0
            while(pos < len(self.__elementos) and self.__criterio(dato, criterio)>=self.__criterio(self.__elementos[pos], criterio)):
                pos +=1 
            self.__elementos.insert(pos, dato)
    
    def eliminar(self, dato):
        if(dato in self.__elementos):
            self.__elementos.remove(dato)
            return dato
        else:
            return None
    
    def modificar_elemento(self, pos, nuevo_valor):
        self.__elementos.pop(pos)
        self.insertar(nuevo_valor)
    
    def busqueda(self, buscado, criterio=None, clave=None, criterio_clave=None):
        pos = -1
        primero = 0
        ultimo = len(self.__elementos) -1
        while(primero<= ultimo and pos == -1):
            medio = (primero + ultimo) // 2
            if(self.__criterio(self.__elementos[medio], criterio) == buscado):
                pos = medio
            elif(self.__criterio(self.__elementos[medio], criterio)> buscado):
                ultimo = medio -1
            else:
                primero = medio +1
        if(pos != -1 and clave is not None and self.__elementos[pos][criterio_clave] != clave):
            while(self.__criterio(self.__elementos[pos], criterio) == self.__criterio(self.__elementos[pos-1], criterio)):
                pos -= 1
            while(self.__elementos[pos][criterio_clave] != clave and 
                self.__criterio(self.__elementos[pos], criterio) == self.__criterio(self.__elementos[pos+1], criterio)):
                pos += 1
            if(self.__elementos[pos][criterio_clave] != clave):
                pos = -1

        return pos
 
    def obtener_elemento(self, pos):
        if(pos >= 0):
            return self.__elementos[pos]
        else:
            return None
    #def modificar_elementos(self, pos, nuevo_valor):
      #  self.__elementos

    def lista_vacia(self):
        return len(self.__elementos) == 0
    
    def tamanio(self):
        return len(self.__elementos)

    def barrido(self):
        for elemento in self.__elementos:
            print(elemento)

    def barrido_eliminado(self, datos_eliminar):
        for elemento in self.__elementos:
            if(elemento in datos_eliminar):
                self.__elementos.remove(elemento)

    def ordenar(self, criterio):
        pass

from random import randint
lista_vocales = Lista()
lista_num = Lista()
lista_par = Lista()
lista_impar = Lista()
lista_personas = Lista()
lista_uno = Lista()
lista_dos = Lista()

for i in range(5):
    lista_uno.insertar(i)
    lista_dos.insertar(randint(1,10))

print('lista uno')
lista_uno.barrido()
print()
print('lista dos')
lista_dos.barrido()
print()

for i in range(lista_dos.tamanio()):
    num = lista_dos.obtener_elemento(i)
    if(lista_uno.busqueda(num) == -1):
        lista_uno.insertar(num)

lista_uno.barrido()