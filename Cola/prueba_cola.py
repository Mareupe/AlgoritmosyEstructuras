from cola import Cola
from random import randint

cola_datos = Cola()
cola_aux = Cola()

for i in range(0, 10):
    num = randint(0, 100)
    cola_datos.arribo(num)
    print(num)
print()
while(not cola_datos.cola_vacia()):
    dato = cola_datos.atencion()
    cola_aux.arribo(dato)
    print(dato)
    
