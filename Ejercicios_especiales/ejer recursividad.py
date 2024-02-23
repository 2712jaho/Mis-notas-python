#------------------RECURSIVIDAD--------------
#Hacer la serie de fibonacci recursiva 
# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34 secuencia fibo
# 1  2  3  4  5  6  7  8   9   10 indice de la secuencia
def fibo (indice):# indice es la posicion de cada elemento de la secuencia    
    if indice == 1:
        return 0
    elif indice == 2:
        return 1
    else:
        return fibo(indice - 1) + fibo(indice - 2)
while True:    
    print(f"El numero de la secuencia de fibo en esa posicion es: {fibo(int(input("Ingrese un indice de fibo ")))}")
    if input("Presione 1 para salir o otro numero para continuar") == '1':
        break
#---------
#Factorial 
def fact (n):
    if n == 2:
        return n
    else:
        return n * fact(n-1)    
while True:    
    print(f"El factorial de ese numero es: {fact(int(input("Ingrese un numero ")))}")
    if input("Presione 1 para salir o otro numero para continuar") == '1':
        break
#------------
#Crear una funcion que me sume desde 1 hasta n numeros
def suma_recursiva (n):
    if n == 1:
        return n
    else:
        return n + suma_recursiva(n-1)
    
while True:    
    print(f"La suma desde 1 hasta n es {suma_recursiva(int(input("Ingrese un numero n ")))}")
    if input("Presione 1 para salir o otro numero para continuar") == '1':
        break
#------------
#Escribí una función recursiva cant_digitos(n) que reciba un número positivo, n, y devuelva la 
# cantidad de dígitos que tiene.
def cant_dig (n):
    if len(str(n)) == 1:
        return 1
    else:
        return 1 + cant_dig(n//10)
    
while True:    
    print(f"La cantidad de dig de n es {cant_dig(int(input("Ingrese un numero n ")))}")
    if input("Presione 1 para salir o otro numero para continuar") == '1':
        break
#----------------






