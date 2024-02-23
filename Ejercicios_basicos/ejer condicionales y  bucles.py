#-----------------
'''Ejercicio 1'''
#Escribir un programa que pregunte al usuario su edad y muestre por pantalla si es mayor de edad o no.
edad_1 = int(input("Ingrese su edad "))
print("es mayor de edad" if edad_1 > 17 else "no es mayor de edad")
'''Fin Ejercicio 1'''
#-----------------
'''Ejercicio 2'''
print()
#Escribir un programa que almacene la cadena de caracteres contraseña en una variable, 
# pregunte al usuario por la contraseña e imprima por pantalla si la contraseña introducida 
# por el usuario coincide con la guardada en la variable sin tener en cuenta mayúsculas y minúsculas.
contra = input("Introduzca la contraseña a guardar ")
verficacion_contra = input("Introduzca de nuevo la contraseña ")
print("la contraseña es la misma" if ((contra.lower()) == (verficacion_contra.lower())) else "la contraseña no es la misma" )
'''Fin Ejercicio 2'''
#-----------------
'''Ejercicio 3'''
print()
#Escribir un programa que pida al usuario dos números y muestre por pantalla su división. 
# Si el divisor es cero el programa debe mostrar un error.
a = int(input("Introduce el dividendom "))
b = int(input("Introduce el divisor "))
print( "Error" if not b else str(a/b))
'''Fin Ejercicio 3'''
#-----------------
'''Ejercicio 4'''
print()
#Escribir un programa que pida al usuario un número entero y muestre por pantalla si es par o impar.
num_3 = int(input("Ingrese un numero "))
print("Es par!!" if not num_3 % 2 else "Es impar!!")
'''Fin Ejercicio 4'''
#-----------------
'''Ejercicio 5'''
print()
#Los alumnos de un curso se han dividido en dos grupos A y B de acuerdo al sexo y el nombre. 
# El grupo A esta formado por las mujeres con un nombre anterior a la M y los hombres con un 
# nombre posterior a la N y el grupo B por el resto. Escribir un programa que pregunte al usuario 
# su nombre y sexo, y muestre por pantalla el grupo que le corresponde.
nombre = ((input("Introduza su nombre "))[0:1]).upper()
sexo = (input("Introduzca su sexo ")).upper()
print(f"el sexo es {sexo}")
if(( (nombre >= 'A' ) and ( nombre <= 'L') ) and ( sexo == "FEMENINO" ) ) or ( ( (nombre >= 'O' ) and ( nombre <= 'Z') ) and ( sexo == "MASCULINO" )  ):
    print("Grupo A ")
else:
    print("Grupo B ")  
'''Fin Ejercicio 5'''
#---------------------------------------------BUCLES-----------------------------------------------------------
'''Ejercicio 1'''
print()
#Escribir un programa que pida al usuario un número entero y muestre por pantalla un triángulo
# rectángulo como el de más abajo, de altura el número introducido.
num = int(input("Introduzca un numero "))
for i in range(num):
    print(('*') * (i + 1))
'''Fin ejercicio 1'''
#--------------------
'''Ejercicio 2'''
print()
#Escribir un programa que muestre por pantalla la tabla de multiplicar del 1 al 10.
for i in range(1,11):
    num = i
    for j in range(10):
        print(num, end='\t')
        num += i
    print()
'''Fin ejercicio 2'''
#--------------------
'''Ejercicio 3'''
#Escribir un programa que pida al usuario un número entero y muestre por pantalla un triángulo rectángulo 
# como el de más abajo.
numero = int(input("Ingrese un numero "))
cadena = ""
contador = 1
for i in range(numero):
    cadena = str(contador) + " " +cadena
    print(cadena)
    contador += 2
'''Fin ejercicio 3'''
#-------------------------------------------------EXTRA EJERCICIO ARBOL DE NAVIDAD
'''Ejercicio extra '''
print()
num = int(input("Introduzca un numero para la altura del arbol: "))
cont = -1
for i in range(1,num +1):
    cont += 2
    espace = ""
    for j in range(num - i):
        espace = espace + " "
    print( espace + (('*')* cont) )
'''Fin de ejercicio extra'''
#--------------------
'''Ejercicio 4'''
print()
#Escribir un programa que pida al usuario un número entero y muestre por pantalla si es un número primo o no.
num_4 =  int(input("Ingrese un numero positivo "))
if num_4 % 2 == 0 :
    if num_4 == 2 :
        print("Es primo")
    else:
        print("No es primo")
else:
    divisores = 0
    for i in range(1, num_4 +1):
        if num_4 % i == 0:
            divisores += 1
    if divisores == 2:
        print("Es primo")
    else:
        print("No es primo")                
'''Fin ejercicio 4'''
#--------------------
'''Ejercicio 5'''
print()
#Escribir un programa que pida al usuario una palabra y luego muestre por pantalla una a una las 
# letras de la palabra introducida empezando por la última.
'''#Forma Senior sin modificar la palabra
word = input("Introduce una palabra: ")
for i in range(len(word)-1, -1, -1):
    print(word[i])
'''
palabra = (input("Ingrese una palabra "))[::-1]
for i in palabra :
    print(i, end= ' ')
'''Fin ejercicio 5'''
#--------------------
'''Ejercicio 6'''
print()
#Escribir un programa en el que se pregunte al usuario por una frase y una letra, y muestre por 
# pantalla el número de veces que aparece la letra en la frase.
frase = input("Ingrese una frase de abuelo ")
vocal = input("Ingrese una vocal ")
print(f"La vocal {vocal} en la frase '{frase}' se repite {frase.count(vocal)}")
'''Fin ejercicio 6'''




