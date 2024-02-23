#-------------------------------
'''Ejercicio 1'''
#Escribir un programa que pregunte el nombre del usuario en la consola y un número entero e 
# imprima por pantalla en líneas distintas el nombre del usuario tantas veces como el número introducido.
nombre_1 = input("Ingrese su nombre: ")
num_1 = int(input("Ingrese un numero: "))
for i in range(num_1):
    print(nombre_1)
#------------------------NOTA IMPORTANTE: podemos repetir un string en consola tantas veces que queramos con
#                        el sgte codigpo: "print( ("juan domingo peron \n")* 3 )"                        
'''Fin de ejercicio 1'''
#-------------------------------
'''Ejercicio 2'''
print()
#Escribir un programa que pregunte el nombre completo del usuario en la consola y después muestre 
# por pantalla el nombre completo del usuario tres veces, una con todas las letras minúsculas, otra 
# con todas las letras mayúsculas y otra solo con la primera letra del nombre y de los apellidos en 
# mayúscula. El usuario puede introducir su nombre combinando mayúsculas y minúsculas como quiera.
'''#Como lo hace un Senior DIOS MIO
name = input("¿Cómo te llamas? ")
print(name.lower())
print(name.upper())
print(name.title())
'''
nombre = input("Ingrese un nombre: ")
nombre_minus = nombre.lower()
print(nombre_minus)
nombre_mayus = nombre.upper()
print(nombre_mayus)
nombre_lista = nombre_minus.split(' ')#Nota: en vez de hacer toda esta mierda de convertir en lista, luego usar
for i in range(len(nombre_lista)):    # ".split" para cada palabra sea mayus su primer letra y toda esa mierda
    nombre_lista[i] =  nombre_lista[i].capitalize() # podemos usar ".title" con mi cadena y me convierte cada
print(' '.join(nombre_lista))                       # primera letra de cada palabra en mayuscula
'''Fin de ejercicio 2'''
#-------------------------------
'''Ejercicio 3'''
print()
#Escribir un programa que pregunte el nombre del usuario en la consola y después de que el usuario lo 
# introduzca muestre por pantalla <NOMBRE> tiene <n> letras, donde <NOMBRE> es el nombre de usuario en 
# mayúsculas y <n> es el número de letras que tienen el nombre.
nombre_3 = input("Ingrese un nombre: ")
print(f"{nombre_3.upper()} tiene {len(nombre_3)} letras")
'''Fin de ejercicio 3'''
#-------------------------------
'''Ejercicio 4'''
print()
#Los teléfonos de una empresa tienen el siguiente formato prefijo-número-extension donde el prefijo es 
# el código del país +34, y la extensión tiene dos dígitos (por ejemplo +34-913724710-56). 
# Escribir un programa que pregunte por un número de teléfono con este formato y muestre por pantalla el 
# número de teléfono sin el prefijo y la extensión.
num_4 = input("Ingrese un numero con el sgte formaton +00-000000000-00 : ")
#--------Forma 1
print(num_4[4:13]) # Medio mal esta forma he pero bue 
#--------Forma 2
lista_4 = num_4.split('-')
print(lista_4[1])
'''Fin de ejercicio 4'''
#-------------------------------
'''Ejercicio 5'''
print()
#Escribir un programa que pida al usuario que introduzca una frase en la consola y muestre por 
# pantalla la frase invertida.
frase = input("Introduzca una frase: ")
#-------Forma 1
lista_5 = list(frase)
lista_5.reverse() #NOTA al usar reverse lo que hace es que modifica mi lista original y la invierte a diferencia
result_5 = ''.join(lista_5) # de reversed(mi_lista) que me devuelve un objeto iterable y luego lo tengo que
print(result_5)             # convertir a lista con "list(objeto_iterable"
#-------Forma 2 de Senior
'''Forma de senioorrrrrrrrrrrrrrr: '''
frase_invertida_5 = frase[::-1]
print(frase_invertida_5)
'''Fin de forma de seniorrrrrrrrrr'''
#-------Forma 3 
lista_5 = list(frase)
lista_revers = lista_5[::-1]
result_5 = ''.join(lista_revers)
print(result_5)
'''Fin de ejercicio 5'''
#-------------------------------
'''Ejercicio 6'''
print()
#Escribir un programa que pida al usuario que introduzca una frase en la consola y una vocal, y
# después muestre por pantalla la misma frase pero con la vocal introducida en mayúscula.
'''#Forma de un senior usando la funcion ".replace(cadena_antigua, cadena_nueva)"
frase = input("Introduce una frase: ")
vocal = input("Introduce una vocal en minúscula:  ")
print(frase.replace(vocal, vocal.upper()))
'''
#forma mia
frase_6 =  input("Ingrese una frase: ")
vocal_6 =  input("Ingrese una vocal: ")
lista_6 = list(frase_6)
for i in range(len(lista_6)):
    if (lista_6[i] == vocal_6) :
        lista_6[i] = lista_6[i].upper()
frase_6 = ''.join(lista_6)
print(frase_6)
'''Fin de ejercicio 6'''
#-------------------------------
'''Ejercicio 7'''
print()
#Escribir un programa que pregunte el correo electrónico del usuario en la consola y muestre 
# por pantalla otro correo electrónico con el mismo nombre (la parte delante de la arroba @) 
# pero con dominio ceu.es.
'''#Forma senior de hacerlo utilizando la funcion slicing para recortar la cadena hasta donde yo quiera
   #y luego concateno el texto "ceu.es"
email = input("Introduce tu correo electrónico: ")
print(email[:email.find('@')] + '@ceu.es')
'''
#Forma mia Como les da la cabeza para eso
correo_7 =  input("Ingrese un correo electronico: ")
lista_7 = list(correo_7)
posi_arroba = lista_7.index('@')#-----------------------METODO INDEX("CARACTER DE MI CADENA")
del lista_7[posi_arroba + 1: len(lista_7)]#     Lo que hace el metodo index es que dado el elementos
lista_agregada = list("ceu.es")               # que le colocamos como parametro me devuelve su indice de
lista_7.extend(lista_agregada)                # posicion en la cadena
result_7 = ''.join(lista_7)
print(result_7)
'''Fin de ejercicio 7'''
#-------------------------------
'''Ejercicio 8'''
print()
#Escribir un programa que pregunte por consola el precio de un producto en euros con dos decimales y 
# muestre por pantalla el número de euros y el número de céntimos del precio introducido.
monto_8 = input("Ingrese un monto con decimales separados por coma ")
print(f"Son {monto_8[: monto_8.index(',')]} euros y {monto_8[monto_8.index(',') + 1:len(monto_8)]} centimos")
'''Fin de ejercicio 8'''
#-------------------------------
'''Ejercicio 9'''
print()
#Escribir un programa que pregunte al usuario la fecha de su nacimiento en formato dd/mm/aaaa y 
# muestra por pantalla, el día, el mes y el año. Adaptar el programa anterior para que también funcione
# cuando el día o el mes se introduzcan con un solo carácter.
fecha =  input("Ingrese una fecha en formato dd/mm/aaaa ")
print(f"Dia {fecha[:fecha.index('/')]}")
sub_fecha = fecha[fecha.index('/') + 1:]
print(f"Mes {sub_fecha[:sub_fecha.index('/')]}")
print(f"Año {sub_fecha[sub_fecha.index('/') + 1 :]}")
'''Fin de ejercicio 9'''
#-------------------------------
'''Ejercicio 10'''
print()
#Escribir un programa que pregunte por consola por los productos de una cesta de la compra, 
# separados por comas, y muestre por pantalla cada uno de los productos en una línea distinta.
'''#Forma en la que lo hace un senior hdpppppppppppppppppppppppp
#Forma senior 1
cesta = input('Introduce los productos de la cesta de la compra separados por comas: ')
print(cesta.replace(',', '\n'))
#Forma senior 2
cesta = input('Introduce los productos de la cesta de la compra separados por comas: ')
print('\n'.join(cesta.split(',')))
'''
productos = input("Ingrese la lista de la compra separada por ',' ")
lista_productos = productos.split(',')
for i in lista_productos :
    print(i)
'''Fin de ejercicio 10'''
#-------------------------------
'''Ejercicio 11'''
print()
#Escribir un programa que pregunte el nombre el un producto, su precio y un número de unidades y 
# muestre por pantalla una cadena con el nombre del producto seguido de su precio unitario con 6 
# dígitos enteros y 2 decimales, el número de unidades con tres dígitos y el coste total con 8 dígitos 
# enteros y 2 decimales.






    
'''Fin de ejercicio 11'''








