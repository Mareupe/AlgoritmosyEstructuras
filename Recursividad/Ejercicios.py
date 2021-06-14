
def fibonacci_R(numero):
    """Ejercicio 1: Fibonacci"""
    if(numero == 0 or numero == 1):
        return numero
    else:
        return fibonacci_R(numero - 1) + fibonacci_R(numero - 2)

def suma(numero):
    """Ejercicio 2: suma"""
    if (numero == 0):
        return (0)
    else:
        return (numero + suma(numero-1))


def producto(numero1, numero2):
    """Ejercicio 3: producto entre dos numeros entreros"""
    if (numero1 == 1):
        return (numero1)
    else:
        return(numero1 + producto(numero1, numero2 - 1))

def potencia(b, e):
    """Ejercicio 4: calcula la potencia de dos numeros"""
    if (e == 0):
        return(b)
    else:
        return b * potencia(b, e - 1)

def romano_decimal(numero):
    """Ejercicio 5: convertir de romano a decimal"""
    if (numero == ""):
        return (0)
    elif (numero == "M"):
        return (1000)
    elif (numero == "D"):
        return (500)
    elif (numero == "C"):
        return (100)
    elif (numero == "L"):
        return (50)
    elif (numero == "X"):
        return (10)
    elif (numero == "V"):
        return (5)
    elif (numero == "I"):
        return (1)
    else:
        if (romano_decimal(numero[0]) < romano_decimal(numero[1])):
            return (romano_decimal(numero[1]) - romano_decimal(numero[0])) + romano_decimal(numero[2:] )
        else:
            return (romano_decimal(numero[0]) + romano_decimal(numero[1:]))

def invertir_cadena(cad):
    """Ejercicio 6: invierte la cadena"""
    if(len(cad) == 0):
        return ""
    else:
        return cad[-1] + invertir_cadena(cad[0:-1])

def invertir_numero(numero):
    """Ejercicio 6: Invertir un número."""
    if(numero < 10):
        return numero
    else:
        return ((numero % 10) * 10 ** len(str(numero//10))) + invertir_numero(numero // 10)


def calcular_serie(num):
    """Ejercicio 7: Calcular una serie"""
    if (num >= 1):
        return calcular_serie(num - 1) + 1/num
    else:
        return 0


def decimal_binario(numero):
    """Ejercicio 8: convertir """
    if (numero == 0):
        return ("")
    else:
        return decimal_binario(numero//2) + str(numero % 2)


def usar_fuerza(mochila, pos):
    """Ejercicio 22: La mochila Jedi"""
    if(pos< len(mochila)):
        if(mochila[pos] == 'Sable de luz'):
            return pos
        else:
            return usar_fuerza(mochila, pos+1)
    else:
        return -1


# def salida_laberinto(matriz, x, y, caminos=[]):
#     """Ejercicio 24: Salida del laberinto."""
#     if(x >= 0 and x <= len(matriz)-1) and (y >= 0 and y <= len(matriz[0])-1):
#         if(matriz[x][y] == 2):
#             caminos.append([x, y])
#             print("Saliste del laberinto")
#             print(caminos)
#             caminos.pop()
#         elif(matriz[x][y] == 1):
#             matriz[x][y] = 3
#             caminos.append([x, y])
#             print("mover este")
#             salida_laberinto(matriz, x, y+1, caminos)
#             print("mover oeste")
#             salida_laberinto(matriz, x, y-1, caminos)
#             print("mover norte")
#             salida_laberinto(matriz, x-1, y, caminos)
#             print("mover sur")
#             salida_laberinto(matriz, x+1, y, caminos)
#             caminos.pop()
#             matriz[x][y] = 1

# lab = [[1, 1, 1, 1, 1, 1, 1],
#        [0, 0, 0, 0, 1, 0, 1],
#        [1, 1, 1, 0, 1, 0, 1],
#        [1, 0, 1, 1, 1, 1, 1],
#        [1, 0, 0, 0, 0, 0, 0],
#        [1, 1, 1, 1, 1, 1, 2]]
    
# salida_laberinto(lab, 0, 0)





