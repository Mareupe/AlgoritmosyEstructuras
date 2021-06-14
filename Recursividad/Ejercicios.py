
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

def binario(numero):
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
        if (binario(numero[0]) < binario(numero[1])):
            return (binario(numero[1]) - binario(numero[0])) + binario(numero[2:] )
        else:
            return (binario(numero[0]) + binario(numero[1:]))

def invertir_cadena(cad):
    """Ejercicio 6: invierte la cadena"""
    if(len(cad) == 0):
        return ""
    else:
        return cad[-1] + invertir_cadena(cad[0:-1])

def calcular_serie(num): #7
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

def invertir_numero(numero):
    """Invertir un número."""
    if(numero < 10):
        return numero
    else:
        return ((numero % 10) * 10 ** len(str(numero//10))) + invertir_numero(numero // 10)



def usar_fuerza(mochila, pos):#22
    if(pos< len(mochila)):
        if(mochila[pos] == 'Sable de luz'):
            return pos
        else:
            return usar_fuerza(mochila, pos+1)
    else:
        return -1



