#----------------------------
'''Ejercicio 1'''
print()
# Escribir una función que muestre por pantalla el saludo ¡Hola amiga! cada vez que se la invoque.
def ejer_1():
    print("Hola amiga")
ejer_1()
ejer_1()
ejer_1()
'''Fin ejercicio 1'''
#----------------------------
'''Ejercicio 2'''
print()
#Escribir una función que reciba un número entero positivo y devuelva su factorial.
from math import factorial
def facto (num):
    print(f"El factorial de {num}! es {factorial(num)}")
facto(int(input("Ingrese un numero para sacar su factorial ")))

def facto_2(num):#---otra forma
    factorial_2 = 1
    for i in range(2,num + 1):
        factorial_2 = factorial_2 * i
    print(f"El factorial de {num}! es {factorial_2}")
facto_2(int(input("Ingrese un numero para sacar su factorial ")))
'''fin ejercicio 2'''
#----------------------------
'''Ejercicio 3'''
print()
#Escribir una función que calcule el total de una factura tras aplicarle el IVA. 
# La función debe recibir la cantidad sin IVA y el porcentaje de IVA a aplicar, y devolver el total 
# de la factura. Si se invoca la función sin pasarle el porcentaje de IVA, deberá aplicar un 21%.
def calc_iva (factura, iva = 21):
    return factura + factura * (iva/100)
print(calc_iva(45))
'''fin ejercicio 3'''
#-----------------
'''Ejercicio 4'''
print()
#Escribir una función que calcule el área de un círculo y otra que calcule el volumen de un cilindro 
# usando la primera función.
from math import pi
def area_cir (radio):
    return(pi * (radio**2))
def vol_cilind(radio, h):
    return area_cir(radio) * h
print(vol_cilind(3,5))
'''fin ejercicio 4'''
#-------------
'''Ejercicio 5'''
print()
#Escribir una función que reciba una muestra de números en una lista y devuelva su media.
def media (lista):
    return sum(lista)/len(lista)
print(media([1, 2, 3, 4, 5]))
print(media([2.3, 5.7, 6.8, 9.7, 12.1, 15.6]))
'''fin ejercicio 5'''
#--------------
'''Ejercicio 6'''
print()
#Escribir una función que reciba una muestra de números en una lista y devuelva otra lista con sus cuadrados.
def cuadrado_list (lista):
    return [i**2 for i in lista]
print(cuadrado_list([1,2,3,4,5]))
'''fin ejercicio 6'''
#--------------
'''Ejercicio 7'''
print()
#Escribir un programa que reciba una cadena de caracteres y devuelva un diccionario con cada palabra que 
# contiene y su frecuencia. Escribir otra función que reciba el diccionario generado con la función anterior 
# y devuelva una tupla con la palabra más repetida y su frecuencia.
def save_dic(frase):
    lista_frase = frase.split(' ')
    dic_pal = {}
    for i in set(lista_frase):
        dic_pal[i] = lista_frase.count(i)
    return dic_pal

def tuple_pal_frec(dic):
    frec_mayor = 0
    palabra_m = ""        
    for pal, frec in dic.items():
        if frec > frec_mayor:
            frec_mayor = frec
            palabra_m = pal
    return (palabra_m, dic[palabra_m])

dic = save_dic("tres tristes tigres trigaron tristes en tres trigales")
print(dic)
result = tuple_pal_frec(dic)
print(result)
'''fin ejercicio 7'''
#---------------
'''Ejercicio 8'''
#Escribir una funcion tal que me diga si los numeros son primos y los almacene en una lista
def verif_primo (num):
    lista = [i for i in range(1,num+1) if num % i == 0]
    return len(lista) == 2

lista = [ i for i in range(20) if verif_primo(i)]
print(lista)
'''fin ejercicio 8'''
#--------------










