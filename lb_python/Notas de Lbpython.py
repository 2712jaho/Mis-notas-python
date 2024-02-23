import this

print("Hello world")
# Hello dog

s = "El resultado de la operacion de (a + b)* c es:"
a, b, c = 16, 14.9, 2
result = (a + b) * c
var_bool = True

#if var_bool :
#    print(s, result)
# import keyword
# print(keyword.kwlist)
i = 3
'''for i in range (3):
    print (i )
'''
# lista_1: list[int] = [1,2,'pepa',4,5] NO TIENE SENTIDO LO DE ESTA LINEA
lista_1 = [1,2,'pepa',4,5]
print(len(lista_1))
# Ejercicio 1:Quiero que me imprimas una secuencia de numeros que va desde 7 a 10
for indice in range (10):
    if indice >= 6 :
        print(indice+1)
#otra forma
var = 7

#Fin de ejercicio 1
#Ejercicio 2 Imprimir los elementos de una lista
lista = [23, 'seis', 23.9, "pedro", 50]
long = len(lista)
for i in range (long):
    print(lista[i])
#Otra forma de hacerlo, otra manera de imprimir una lista
for element in lista :
    print(element)
#Fin de ejercicio 2
#Como crear una lista usando la palabra reservada list
a = list("Palabra")
print(a)
b  = 23900 #Me creo una variable int y para que pueda ser cargada en una lista necesito convertirla a string
print( list(str(b)))
#Hablemos de tuplas
mi_tupla = (1, 2, 'tres', 4.0)
# Acceder a elementos de una tupla
#Una tupla es una lista inmodificable ya que no se puede agregar ningun elemento mas una ves creada
# y no se puede modificar ningun elemento es decir "mi_tupla[2] = 89" daria error
primer_elemento = mi_tupla[0]
tercer_elemento = mi_tupla[2]
# Slicing en una tupla
sub_tupla = mi_tupla[1:4:2]
print( sub_tupla)
A = 1; B = 1
B = B + 10
A = (A * 6) + 4
if (A is B) == False :
    print("No son iguales")
else:
    print("Son iguales")
#-----------------Forma no optima de ver si un element esta en una lista
a=3
lista_1=[1, 2, 3, 4, 5]
def estaContenido(a, lista1):
    Bol = False
    for l in lista1:
        if a==l:
            Bol =  True
    return Bol

print(estaContenido(a, lista_1))
#-----------------Forma Optima de ver si un element esta en una lista
print(a in lista_1)
indice = 4
for indice in range(4):
    print(indice)
pepa = list("el pepe")
print(pepa)
#--------------Otra forma de usar "==" para comparar un valor booleano
mi_variable = True
if mi_variable is True:
    print("La variable tiene un valor asignado Bool de True")
else:
    print("La variable tiene un valor asignado Bool de False")
#fin
#Uso de continue en bucles este lo que hace es cortar la ejecucion hasta la sgte iteracion ya sea de
#un while o un for
for i in range(3):
    if i == 1:
        print("Corteeeee")
        continue
    print(i)
    print("EL PEPE")
#fin
#Ejercicio para contar cuantas veces llamo a una funcion
n = 0
def funcion_bb ():
    letras = list("pepe")
    this.n = 'pepe'
    global n
    n += 1
    return letras[n-1]
print(funcion_bb())
print(funcion_bb())
print(funcion_bb())
print(funcion_bb())
print('Usted llamo a la funcion la cantidad de:',n,'veces')
#fin
#ejemplo de usos de yield en generadores
def generador():
    n = 1
    yield 1

    n = n + 10
    yield 2

    n = n - 11
    yield 3

for i in generador():
    print(i)
#Fin
#Clases
class Ropa:
    def __init__(self, marca, costo):
        self.marca = marca
        self.costo = costo
    def get_datos(self):
        print("la marca de ropa es:", self.marca, "el costo es de:", self.costo)
remera = Ropa("gucci", 250)
#fin de clases
#Entendiendo Iteradores:
#---Iterando un objeto iterable tipo string
mi_string = "Pablito Picasso"
iter_de_mi_string = iter(mi_string)
for i in range(len(mi_string)):
    print(next(iter_de_mi_string))
#---Iterando un objeto iterable tipo lista
mi_lista = [2,3,4,5,6]
iter_de_mi_lista = iter(mi_lista)
for i in range(len(mi_lista)):
    print(next(iter_de_mi_lista))
#fin
#Prueba Para ver si dos variables apuntan a la misma direccion de memoria
marina = True
Felipe = None
Pablo = None
print(Felipe is Pablo)
#Notese que no necesariamente va ser asi ya que puede ser que python almacene distintos Trues
#en la memoria y se puede dar el caso de que felipe y pablo no apunten a la misma direccion de memoria
#fin
#Uso del try exception
x = "a"
valor = None
try:
    valor = int(x)
except Exception as e:
    print("Hubo un error:", e)
finally:
    print("El valor es", valor)
#fin
#Contador de instancias de una clase
class Prueba :
    #Podemos crear un atributo global en una clase en python que nos puede ayudar
    #a cuantas veces creamos una instancia de la misma clase
    #Y para hacer referencia a esa variable simplemente usamos el nombre de la clase "." y el nombre de la variable
    pepe = 0
    def __init__(self):
        Prueba.pepe += 1
    def Cont_Inst(self):
        return Prueba.pepe
ins1 = Prueba()
ins2 = Prueba()
ins3 = Prueba()
ins4 = Prueba()
print(str(ins1.Cont_Inst()))
#fin
#Funciones anidadas y uso de las variables global y nonlocal
def funcion_a():
    x = 10
    def funcion_b():
        nonlocal x
        x = 20
        print("funcion_b", x)

    funcion_b()
    print("funcion_a", x)
funcion_a()
#fin
#Llamadas desde el exterior sobre una funcion que se encuentra dentro de otra
'''Sin embargo, hay una excepción conocida como el "retorno de funciones anidadas". 
Puedes hacer que la función externa devuelva la función interna, y luego puedes llamar 
a la función interna desde fuera de la función externa. Aquí tienes un ejemplo:
'''
def funcion_externa():
    print("Esta es la función externa.")

    def funcion_interna():
        print("Esta es la función interna.")

    # Devolver la función interna
    return funcion_interna

# Obtener la función interna
funcion_anidada = funcion_externa()

# Llamar a la función interna desde fuera de la función externa
funcion_anidada()
#MIERDA PAPAAAA -------------------- aca vemos como una funcion puede retornar otra funcion que se
# encuentre dentro de ella
#Fin-------------------------------------------------------
#Aprendiendo sobre atributos globales dentro de una clase y atributos propios de una instancia
class learn:
    a = 0 #Atributo global para todas las instancias
    def __iter__(self):
        self.a = 1
        return self
    def llamada_a_instancia(self):
        learn.a += 1
    def contador(self):
        return learn.a
aprender = learn()
#aprender.__iter__()
#print(aprender.a) Comentario sobre que ocurre caundo tengo dos atributos igualnombre
# de una clase global y local y que pasa cuando lo llamo siendo que tienen el mismo nombre
aprender.llamada_a_instancia()
aprender.llamada_a_instancia()
aprender.llamada_a_instancia()
print("las instancias totales creadas son:", aprender.contador())
#Fin------------------
#"in" para ver si un elemento forma parte de un objeto iterable ya sea string, lista, tupla, diccionario, etc
nombre = "Pablo"
print( "P" in nombre) # print True
for i in nombre:
    print(i)
lista_2 = ['A', 'b', 'c']
print('a' in lista_2) # Print False
for i in lista_2:
    print(i)
#Fin----------------
#leyendo archivos en python
with open("C:/Users/josealejandro/Documents/Iteracion en python.txt") as fichero: # La palabra "with" Permite cerrar un archivo una ves
                                                                                  # que el codigo ya no este indentado
#fichero = open(r"C:\Users\josealejandro\Documents\Iteracion en python.txt")---Otra forma de abrir un archivo
    print(fichero.read())
#----------------------Leyendo caracter por caracter un archivo
fichero_1 = open(r"C:\Users\josealejandro\Documents\Iteracion en python.txt")
car = fichero_1.readline(2) # este "2" significa que yo leere solon un caracter
while car != " d":
    print(car)
    car = fichero_1.readline(2)
#-------------------Almacenando cada linea de mi archivo como un elemento de una lista
fichero_2 = open(r"C:\Users\josealejandro\Documents\Iteracion en python.txt")
lista_fichero = fichero_2.readlines() #Al usar "readlines" yo creo una lista donde cada element es una linea del fichero
fichero_2.close()
#print(lista_fichero[0])
cont = 0
for i in lista_fichero:
    cont += 1
    print(i.strip()) #"strip" permite al iterador "i" leer cada elemento de la lista pero borrando los espacios en blancos entre ellos
print("La cantidad de lineas de tu archivo txt son de", cont)
#Fin--------------
#Escribir contenido dentro de un fichero ya existente usando append 'a'
with open(r"C:\Users\josealejandro\Documents\Lista de compras.txt", 'a') as Lista_Compras:
    Lista_Compras.write(" es sinonimo de platano\n")
#--------------
#Escribir contenido en un nuevo archivo con 'x'
try:
    with open(r"C:\Users\josealejandro\Documents\Nuevo archivo 3.txt", 'x') as Arch_new:
        for i in range(6):
            Arch_new.write(f"Este es la linea {i} de texto de mi nuevo archivo\n")
except Exception as error:
    print("El nombre del archivo ya existe, no se puede reescribir sobre el")
#Fin-------------
#Hacer un programa que pida dos numeros al usuario y que devuelva la suma de ellos
# con 3 intentos como maximo...
bandera = True
contador = 0
print("Programa que devuelve la suma dos numeros con 3 intentos como maximo")
while ((bandera)and(contador < 3)):
    try:
        num1 = int(input("Ingrese el primer numero "))
        num2 = int(input("Ingrese el segundo numero "))
        resultado = num1 + num2
        print(f"La suma de {num1} + {num2} da como resultado {resultado}", end='\n')#Por defecto end tiene como valor '\n' saltos de linea
        bandera = False
    except Exception as error:
        contador+= 1
        print(f"Error intento numero {contador} ,quedan {3 - contador} intentos")
        if(contador == 3):
            print("Se acabaron los intentos gil!!")
input("Press para finalizar")
#Fin----------
#Concepto de duck typing
#En resumen trata de que vs podes hacer funciones que reciven como parametro un objeto "x" de cualquier
# clase para luego con ese objeto poder llamar a metodos "x.hablar" y si la clase del objeto ingresado
# tiene la funcion hablar entonces la ejecutara, caso contrario saldra un error
class Perro:
    def hablar(self):
        print("¡Guau, Guau!")

class Gato:
    def hablar(self):
        print("¡Miau, Miau!")

class Vaca:
    def hablar(self):
        print("¡Muuu, Muuu!")
def LLamar_hablar(x):
    x.hablar()
#puca = Perro()
michi = Gato()
lola = Vaca()
LLamar_hablar(Perro())#Python crea una instancia de la clase perro que nosotros no vemos y espera que dicha
                      # instancia tenga el metodo hablar, pero en resumen si crea una instancia de la clase
LLamar_hablar(michi)
LLamar_hablar(lola)
#-----------paron
lista_3 = ['pedro', 23, True, 23.45]
for i in lista_3:
    print( i == 'pedro')
    print( i == 23.45)  #En estos ejemplos notamos que el iterador "i" va cambiando de tipo int, str..segun
                        #sea corresponda con el elemento de la lista a iterar
    print(i)
#-----------fin de paron
#Para pensar sobre duck typing:
'''Otra forma de verlo, es iterando una lista con diferentes animales, donde animal va tomando los 
valores de cada objeto animal. Todo un ejemplo del duck typing y del tipado dinámico en Python.'''

lista = [Perro(), Gato(), Vaca()]
for animal in lista:
    animal.hablar()

# ¡Guau, Guau!
# ¡Miau, Miau!
# ¡Muuu, Muuu!
#Fin de para pensar
#Entendiendo el duck typing y como la funcion len() es un claro ejemplo de ello
#Aprendiendo tambien que las listas, tuplas, cadenas de car son objetos de clases
class pedr0():
    def __len__(self):
        return 23
instancia = pedr0()
#print(len(instancia))
print(instancia.__len__())
vector = [1,2,3,4,5]
print(vector.__len__())
#Fin----------------
#Con type podemos ver la clase a la que pertenece la variable
palabra = "pedro"
print(type(palabra))
#Fin------------
# Unpacking en python como almacenar en variables distintas los elementos de una lista, tupla, etc
lista = [1, 2, 3, 4, 5]
a, b, *resto = lista #Usando * y un nombre podemos almacenar los elementos que quedan de una lista en otra
print(a, b, resto)
print(f"la longuitud de mi lista 'resto' es de {len(resto)}")
print(f"mi lista resto tiene los sgtes element:", resto)
#Fin de Unpacking
#Viendo que pasa cuando leo un fichero donde dejo una linea completamente en blanco
print("Abriendo archivo pepe")
with open(r"C:\Users\josealejandro\Documents\pepe.py", 'r') as archivo_pepe :
    lista_pepe = archivo_pepe.readlines()
    print(f"longitud de archivo pepe es", len(lista_pepe), "lineas")
    print("Longitud de una linea vacia sin texto de un fichero:",len(lista_pepe[1]))#Una linea en blanco en
    #un fichero tiene una longitud de 1 recordemos que todas tienen el salto de linea incorporado "\n" q1 vale 1    
    iterador = iter(lista_pepe)
    print(next(iterador).strip())
    print(next(iterador).strip())
    print(next(iterador).strip())
with open(r"C:\Users\josealejandro\Documents\pepe.py", 'r') as archivo_pepe_1 :
    print(len(archivo_pepe_1.readline()))
    print(len(archivo_pepe_1.readline()))
    print(len(archivo_pepe_1.readline()))
#Fin-----------------------------
#Abriendo un archivo txt introducido por el ususario para leero por completo con read
name_file = input("Ingrese el nombre del archivo.txt ")
ruta = fr"C:\Users\josealejandro\Documents\{name_file}"
print(ruta)
try:
    with open(ruta, 'r') as archivo:
        print(archivo.read())
except Exception as e:
    print(e)
#Fin------------------------
#---------------------------------Bucle For---------------
#Ejemplo de for iterados para leer una matriz(lista dentro de otra lista)
lista = [[56, 34, 1],
         [12, 4, 5],
         [9, 4, 3]]
for i in lista:
    for j in i :
        print(j)
#fin de ejemplo
#Iterando una cadena al reves 
texto = "Python"
for i in texto[::-1]:# texto[::-1] lo que hace es invertir la cadena y luego recien el bucle for itera
    print(i)         # sobre la cadena inversa directamente
#Fin de iterando cadena al reves
#------------------------------Generadores una forma de lista que usa yield y ahorra memoria 
'''Estudiar todo sobre generadores 
resultado = (f"{i} es mayor que 10" if i > 10 else f"{i} no es mayor que 10" for i in range(15))
for mensaje in resultado:
    print(mensaje)    
'''
#Hay que investigar mucho sobre este tema ES MUY COMPLEJO
#-------------------------
#Uso de List comprehensions para crear listas en una sola linea usando ciclo for

#sintaxis para crear list comprehensions solo con for:
                # lista = [expresión for elemento in iterable]
#sintaxis para crear list comprehensions con for y ademas si se cumple una condicion:
                # lista = [expresión for elemento in iterable if condición]
                
# Cargando una lista usando un for con RANGO
lista_de_prueba = [f"Elemento numero {i+1}" for i in range(10)]
for i in lista_de_prueba :
    print(i)
    
# Cargando una lista usando un for con UN ITERABLE
lista_de_prueba = [i for i in "PALABRA"]
for i in lista_de_prueba :
    print(i)    
    
#Cargando una lista usando for y un condicional 
lista_num = [i for i in range(1,16)]
print(lista_num)
lista_num_pares = [ i for i in lista_num if i % 2 == 0]
print(f"Lista num pares {lista_num_pares}")
#fin---------------
#fin de BUCLE FOR---------------------
#--------------------------------------SETS que son similares a las listas
#Ejercicio con SETS, dado un conjunto crear otro conjunto cuyos elementos sean el cuadrado del primer conjunto
conjunto_inicial = {i for i in range(1,6)} #me genera los numeros del "1".."5"
print(conjunto_inicial)
conjunto_r = { i**2 for i in conjunto_inicial }
print(conjunto_r)
#fin de ejercicio
#Unir dos conjuntos sin usar la funcion intersection "SETS"
conjunto_A = { i for i in range(1,5)}
print(conjunto_A)
conjunto_B = { i for i in range(3,7)}
print(conjunto_B)
conjunto_interseccion = { i for i in conjunto_A if i in conjunto_B}
print(conjunto_interseccion)
#fin de ejercicio
#-----------------------------------------------Entendiendo la funcion ENUMERATE
# Nos devuelve dos datos una el indice de la posisicion del elemento en la lista y dos el elemento
# de esa posicion pero si por casualidad el elemento vendria a ser otra lista, o tupla como en mi ejemplo
# si yo solo le pongo un parametro en vez de dos (elemento_de_mi_lista) lo que me retornaria seria la tupla
# q es un elemento de mi lista, pero si le ingreso variables iguales a la cantidad de elementos de mi tupla
# como en este ejemplo me retornara en cada varaible cada elemento de mi tupla
nombre_edad = [('alejandro', 12), ('matias',32), ('enzo', 13)]

for indice, (nombre,edad) in enumerate(nombre_edad):
    print(f"Índice: {indice}, Nombre: {(nombre).ljust(10)} Edad: {edad}")
# Fin
#-----------El range se puede usar con list para crear una lista
print(list(range(1,11))) # lista de numeros del 1 al 10 [1,2,3....,10]
#---------Se puede usar como condicion de un while una lista que mientras no este vacia se ejecutara el bloque
lista_while = [1,2,3,4]
while lista_while :
    lista_while.pop(0)
    print(lista_while)
#Fin
#-----------------USO DE DECORADORES PARA FUNCIONES CON CANTIDAD PREDEFINIDA DE PARAMETROS-------
#----------------Creando mi primer decorador
def mi_decorador (una_funcion_con_2_parametros):
    def nueva_funcion_decorada (parametro1, parametro2):
        print("Estamos dentro de mi funcion decorada ")
        una_funcion_con_2_parametros(parametro1, parametro2)
        print("Estamos saliendo de mi funcion decorada")
    return nueva_funcion_decorada


def funcion_multiplicacion (a,b):
    print("Dentro de mi funcion multiplicacion")
    print(f"El resultado de {a} * {b} es { int(a) * int(b)}")
    
    
def funcion_division (a,b):
    while ( b == 0):
        b = int(input("Error no se puede dividir por cero!!, ingrese otro valor: "))
    print(f"El resultado de dividir {a}/{b} es { a/b}")
        

a = int(input(f"Ingrese el valor de a "))
b = int(input(f"Ingrese el valor de b "))
# funcion_multiplicacion = mi_decorador(funcion_multiplicacion)
# funcion_multiplicacion(a,b)

funcion_division = mi_decorador(funcion_division)
funcion_division(a,b)
#Fin----
#---ARGUMENTOS POSICIONALES Y DE PALABRAS CLAVE(QUE ES COLOCAR DIRECTAMENTE EL NOMBRE DEL PARAMETR0 = "VALOR")

#* me empaquetan en una tupla y ** en un diccionario

#----posicional(importa el orden)
def suma(a, b):
    return a + b

resultado = suma(3, 5)
#----palabra clave(no importa el orden de los argummentos ya que los asigno por el nombre del parametro)
def saludar(nombre, edad):
    print(f"Hola, {nombre}. Tienes {edad} años.")

saludar(edad=25, nombre="Juan")
#Uso de * y doble ** para empaquetar o desempaquetar un iterable!!!
#Desempaquetando un iterable de tipo string y asignandolo a parametros de la funcion popo
def popo (letra1,letra2,letra3,letra4):
    print(f"h = {letra1}\no = {letra2}\nl = {letra3}\na = {letra4}\n")    
popo(*("HOLA"))
#empaquetando un numero finito de enteros en una tupla que es un parametro de la funcion caca
# para luego con un for ir iterando esa tupla de numeros para imprimirlos
def caca(*args):
    for i in args:
        print(i)
caca(1,2,3,4,5)
#Fin de ARGUMENTOS POSICIONALE Y PALABRAS CLAVE Y UNPACKING (*,**)
#----------------Programacion funcional funciones "map", "filter","sorted" y "reduce del modulo functools"
#map recive como parametro una funcion y una lista, tupla, etc donde con cada elemento de la secuencia
#se evalua a la funcion y se almacena en un iterable que luego puedes convertir a lista, tupla, o set(conjunto)
def cuadrado (x):
    return x **2
lista_num = [1,2,3,4,5,6]
for i in (map(lambda x:x**2, lista_num)):# o tambien puedes hacer correrlo en un for 
    print(i)
#filter recive como parametro una funcion y un iterable y con cada elemento de ese iterable llama a la funcion
# de tal manera que si retorna true recien lo almacena en un iterable que puede ser lista, tupla, etc
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10,1,2,3,4,5,6,7,8,9,10]
impares = filter(lambda x: x % 2 != 0, numeros)
impares_lista = tuple(impares)
print(impares_lista)  # Salida: (1, 3, 5, 7, 9)
#Fin
#Funcion que mide el tiempo de ejecucion de otra funcion 
#Aqui vemos decoradores, la funcion time del modulo time, argumentos genericos de una funcion *tupla **diccionario
def usa_if(decimal):
    if decimal == '0':
        return "000"
    elif decimal == '1':
        return "001"
    elif decimal == '2':
        return "010"
    elif decimal == '3':
        return "011"
    elif decimal == '4':
        return "100"
    elif decimal == '5':
        return "101"
    elif decimal == '6':
        return "110"
    elif decimal == '7':
        return "111"
    else:
        return "NA"

import time
def mide_tiempo(funcion):
    def funcion_medida(*args, **kwargs):#convierte en tupla los argumentos pasados a "funcion"
        inicio = time.time()
        c = funcion(*args, **kwargs)# los 2 argumentos estan en tupla (una_funcion, entrada)
        print(f"Entrada: {args[1]}. Tiempo: {time.time() - inicio}")#Por eso cuando llama args[1] esta llamando
        return c                                                    #al elemento de la posi 1 de mi tupla que 
    return funcion_medida                                           #almacena la entrada de "una_funcion"

@mide_tiempo
def repite_funcion(funcion, entrada):
    return [funcion(entrada) for i in range(10000000)]
    # return list(map(funcion, [entrada for i in range(10000000)]))
    
for i in range(8):
    print(len(repite_funcion(usa_if, str(i))))
#Fin------
#Uso del break con bucles FOR Y WHILE
import random
print("No sales del juego hasta adivinar el numero!!")
while True :
    aleatorio = random.randint(1,10)
    if aleatorio == int(input("Intenta adivinar el numero ")):
        break
    print(f"Fallaste era el {aleatorio}, no puedes salir")
print("Fin del juego")
#fin-------
#------------USO DE ZIP PARA UNIR N LISTAS/OBEJTOS ITERABLES EN UNA TUPLA
numeros = [1, 2]
espanol = ["Uno", "Dos"]
ingles = ["One", "Two"]
frances = ["Un", "Deux"]
c = zip(numeros, espanol, ingles, frances)
print(list(c))
for n, e, i, f in zip([1,2], ['uno', 'dos'],["One", "Two"] ,["Un", "Deux"] ):
    print(n, e, i, f)
#Usando zip con DICCIONARIOS-----
esp = {'1': 'Uno', '2': 'Dos', '3': 'Tres'}
eng = {'1': 'One', '2': 'Two', '3': 'Three'}
print(list(zip(esp,eng))) #Cuando usamos zip con diccionarios este almacenara en tupla solo las KEYS de los diccionarios
for a, b in zip(esp, eng):#Entonces si iteramos las tuplas 'a' y 'b' solo imprimiran las Keys, pero si queremos
    print(esp[a], eng[b]) # que imprima sus valores podemos hacer "diccionario_1[a]"  y "diccionario_2[b]"    
# Uso de la función items, podemos acceder al key y value de cada elemento.
esp = {'1': 'Uno', '2': 'Dos', '3': 'Tres'}
eng = {'1': 'One', '2': 'Two', '3': 'Three'}
print(list(zip(esp.items(), eng.items()))) #[(('1', 'Uno'), ('1', 'One')), (('2', 'Dos'), ('2', 'Two')), (('3', 'Tres'), ('3', 'Three'))]
for (k1, v1), (k2, v2) in zip(esp.items(), eng.items()):
    print(k1, v1, v2)
#-------------Fin------------
#--------------------USO DE "ENUMERATE" CON LISTAS, TUPLAS, SETS
lista_listas =[['carro', 'auto'],['moto','bicicleta'], ['avion','helicoptero']]
#Usando enumerate cunado mis elementos Tambien son listas----
for indice, elementos in enumerate(lista_listas):# aqui elemento es una lista
    print(indice , end= ' ')
    for element in elementos:#itero la lista llamda "elementos"
        print(element, end = ' ')
    print()
#OTRO USO DE "ENUMERATE" podemos crear iterables que contienen pares de tuplas con indice y elemento
lista = ["A", "B", "C"]
en = list(enumerate(lista)) # salida: [(0, 'A'), (1, 'B'), (2, 'C')]
print(en) #Podemos convertirlos en LISTAS, TUPLAS, Y SETS
#--------------LIST COMPREHESIONS
#sintaxis                                  lista = [expresión for elemento in iterable]
frase = "El perro de san roque no tiene rabo"
erres = [i for i in frase if i == 'r'] #podemos colocar como expresion a funciones, constantes y todo lo que queramos
#salida ['r', 'r', 'r', 'r']
#--------------DICTIONARY COMPREHESIONS
dic = {i:j for i,j in enumerate(['cero', 'uno', 'dos', 'tres', 'cuatro', 'cinco']) }
print(dic[5]) #para los diccionarios el iterable tiene que ser un par de elementos [(a,b)] o ((a,b))
#----------------------------
# Son mutables los siguientes tipos:

# Listas
# Bytearray
# Memoryview
# Diccionarios
# Sets
# Y clases definidas por el usuario

# Y son inmutables:

# Booleanos
# Complejos
# Enteros
# Float
# Frozenset
# Cadenas
# Tuplas
# Range
# Bytes

#---------PASO DE PARAMETROS POR VALOR Y REFERENCIA--------------
'''IMPORTANTE'''
#Las funciones que reciben como parametros variables de tipo mutables como listas, sets, diccionarios lo 
# que hacen es que dicha funcion recibe un paso de valores por referencia por ende lo que yo haga dentro de
# dicha funcion con esa lista, set, diccionario SE VERA MODIFICADO en la variable original ya que ambas
# apuntan a la misma direccion de memoria
# Ocurre lo contrario con los de tipo inmutables ya que ellos mandan a la funcion una copia de dicho valor
# en otro espacio de memoria por ende si modifico mi var tipo "int" dentro de la funcion esta no afectara
# a la de afuera
def paso_por_referencia(lista):
    lista[0] ='nuevo elemento bb'
    return lista
lista = [1,2,3,4,5]
print(id(lista), lista)
print(id(paso_por_referencia(lista)), lista)

def  paso_por_valor (num):
    num = num + 1
    print(id(num), num)
  
num = 29  
print(id(num), num)
num += 1
print(id(num), num)
#fin------
#--------------Como modificar una tupla usando slicing
tupla_padre = (1,2,3)
tupla_madre = (5,6,7)
tupla_hijo = (4,)
conct_tuplas = tupla_padre + tupla_hijo + tupla_madre #concatenamos las 3 tuplas, IMPORTA EL ORDEN!!
print(conct_tuplas)
#fin------
#Uso de r antes de un string 
print(r'Esta "r" antes de un string lo que hace es que todos los valores especiales como \n\t quedan INVALIDOS')
#Uso de \" para mostrar dobles comillas en un string
print("imprimeros dobles comillas (\")")
#Uso de "If" dentro de un print para que dado el cumplimiento de una condicion me imprima una cosa u otra
print('vamos bocaa' if 'boca' in 'Boca campeon mundial' else 'vamoo river')
#FIN------------
#-----------------------------VARIABLES GLOBALES DENTRO DE UNA FUNCION-----------
#para acceder a una variable global dentro de una funcion basta con escribir su nombre y ya, de esta forma podemos
#ver su valor, PERO SI QUISIERAMOS MODIFICARLA DENTRO DE LA FUNCION tendriamos que usar la palabra reservada
# "global nombre_var_global" y debajo de dicha sentencia "nombre_var_global = nuevo_valor" para asi poder
# modificar la var global dentro de la funcion
#--PEROOOO aunque debemos usar este concepto para reasignar un valor a una var global, lo que si podemos hacer
# dentro de una funcion es que TODOS LOS TIPOS DE OBJETOS MUTABLES PUEDEN SER MODIFICADOS como agregando elementos
# ,nuevos keys DENTRO DE LA FUNCION SIN NECESIDAD DE USAR LA WORD RESERV "GLOBLAL" EXPLICACION:
# Para tipos de datos mutables en Python, como listas, bytearray, memoryview, diccionarios y sets, puedes 
# modificar sus elementos directamente dentro de una función sin necesidad de utilizar la palabra clave global. 
# Esto se debe a que estos tipos de datos son mutables, lo que significa que sus valores pueden cambiar 
# sin necesidad de reasignar la variable a un nuevo objeto.
mi_lista = [1, 2, 3]
mi_diccionario = {'a': 1, 'b': 2, 'c': 3}

def reasignar_datos():    
    mi_lista = [4, 5, 6]  # Crea una variable local llamada "mi_lista" 
    print("Lista dentro de la función:", mi_lista) # salida [4,5,6]
    # Para evitar el problema, se debe declarar la variable como global
    global mi_diccionario
    mi_diccionario = {'x': 10, 'y': 20, 'z': 30}

# Llamando a la función
reasignar_datos()

# Verificando cambios fuera de la función
print("Lista fuera de la función:", mi_lista)  # salida [1,2,3]
print("Diccionario modificado:", mi_diccionario)
#PARA PENSAR SOBRE LLAMADA A UNA VARIABLE GLOBAL Y MODIFICACION DE LA MISMA DENTRO DE UNA FUNCION
lista = [1,2,3,4,5]
def mutabilidad (lista_mutable):
    lista_mutable.append(2002)
    print(lista_mutable)
    lista_mutable = 23
    print(lista_mutable)
    global lista
    lista = 23    
    
mutabilidad(lista)
print(lista)
    
#-----------------------------------fin
#--------------------------------------SETS Y FROZENSETS 
#                           MIRAR LA LISTA DE TIPOS DE DATOS/ESTRUCTURAS MUTABLES E INMUTABLES
#Los sets son estructuras de datos MUTABLES ya que podemos agregar nuevos elementos, eliminar elementos existentes
# todo eso con ".add()" ".remove(elemento)" pero a su vez se dice que son en parte inmutables ya que no podemos
# modificar directamente sus elementos ya que los indices varian.
#Los FROZENsets sonestructuras INMUTABLES ya que no podemos agregar nuevos elementos, tampoco borrar los existentes
# y al igual que los sets tampoco podemos modificar un elemento gracias a su indice ya que igualmente varian
s1 = frozenset([1, 2,3,2,2,1,1,2,3])#tiene como argumento un iterable
s2 = frozenset([3, 4])
s3 = {s1, s2}
print(s3) 
#-------fin
#---------------Casting sinonimo de cambiar tipos de datos/ convertir un tipo de dato a otro
#-------------NOTA IMPORTANTE!!!!!! SOBRE LA MUTABILIDAD DE UNA TUPLA (RECORDANDO QUE UNA TUPLA ES INMUTABLE)
tupla = (1,2,3,4,5,6, [27,12,2002])#Cuando tenemos un elemento de una tupla que es un MUTABLE (lista, set, diccionario)
print(tupla)                       
tupla[6][0] = 31                   # nosotros podemos acceder y modificar dicho elemento del tipo mutable
print(tupla)                       # que se encuentra como elemento en mi lista
#mostramos un elemento de la lista
print(tupla[6][2])
#-----fin
#------------PARA PENSAR: FUNCION QUE ORDENA UN DICCIONARIO EN BASE A SUS VALORES
def ordenar_por_valor(**kwargs):#toma como parametros argumentos de palabras clave que luego convierte a diccionario
    return dict(sorted(kwargs.items(), key=lambda x: x[1])) 
#----fin
#------FUNCION "DICT()" recive un iterable de pares de elementos como parametro q luego convierte a diccionario
#----fin
#------FUNCION "SORTED(iterable a ordenar, key=argumento en el cual se basara el orden, reverse = false)" 
# cuando reverse = false esto ordenara el iterable en FORMA CRECIENTE, si reverse = true FORMA DECRECIENTE
#----fin
#------Uso de la funcion help(funcion_1) para mostrar el comentario '''comentario de ayuda''' de una funcion
# notemos que cuando la llamamos dentro de help no usamos "()" ya que sino help(funcion_1()) activariamos la 
# funcion, es decir la llamariamos como tal, pero si no usamos "()" pasamos la funcion como objeto a help()
lista = [i for i in range(11,21)]
print(dict(enumerate(lista)))

def eleva_cuadrado (num:int)-> int:
    '''MI funcion eleva un numero al cuadrado
    recive como parametro un numero y retorna 
    su cuadrado
    '''
    return num**2
help(eleva_cuadrado)
#----fin    
#-------------Function Annotations en Python
#Las anotaciones en python no son una imponenciacion obligatoria, es decir no es que limita los argumentos
# al tipo que yo elegi, sino que son una sugerencia o es lo que la funcion espera recibir de afuera
def funcion_con_argumentos_predefinidos (num1: int, num2: int ) -> int:
    return num1 + num2

#Haciendo uso de nombre_funcion.__annotations__ podemos acceder a todas las anotaciones de tipos que queremos 
# que sean nuestros argumentos 
def suma(a: int, b: int) -> int:
    return a + b
print(suma.__annotations__)
# Salida: {'a': 'int','b': 'int','return': 'int'}
#---fin
#----------ANOTACIONES EN FUNCIONES "COMO VERIFICAR SI LOS ARGUMENTOS SON DEL TIPO DESEADO"
#Una forma de hacerlo pero en tiempo de ejecucion seria usando el metodo "__annotations__" 
# con la funcion, como se muestra a continuacion
def multiplicacion (num: int, multiplicando: int )->list:
    if (isinstance(num,multiplicacion.__annotations__['num'])) and (isinstance(multiplicando ,multiplicacion.__annotations__['multiplicando'])):
        print(num*multiplicando)    
    else:
        print("Argumentos de tipos incorretos", multiplicacion.__annotations__)
            
# print(multiplicacion.__annotations__) 
# Salida: {'num': <class 'int'>, 'multiplicando': <class 'int'>, 'return': <class 'list'>}
multiplicacion(3, False)
# ----fin
#--------USO DE "MYPY" para lograr hacer una verificacion estatica de los tipos de los argumentos, es decir
# hacer la verificacion sin necesidad de correr el programa, usando solo la terminal cmd de tu pc
# PASOS:
# Abre la terminal.
# Instala mypy
# $ pip install mypy
# Navega al directorio "proyecto_python" usando el comando cd:
# $ cd ruta/del/directorio/proyecto_python
# Asegúrate de reemplazar "ruta/del/directorio" con la ruta real hacia donde se encuentra tu directorio "proyecto_python".
# Después de haber cambiado al directorio correcto, puedes ejecutar los comandos mypy como se mencionó anteriormente:
# $ mypy suma_correcta.py
#---fin
#-------------------FUNCIONES GENERADORAS----
#Una funcion generadora es aquella que en vez de usar un "RETURN" usan "YIELD", gracias al yield nosotros
# podemos crear un iterador que cada vez que se llame con "next(iterador)" llamamos al yield de mas arriba
# y luego la funcion queda en pausa hasta el proximo "next(iterador)", donde se reanuda el codigo desde la 
# ultima llamada de yield
def generador_pares (lista:list):
    for num in lista:
        if num % 2 == 0:
            yield num
    yield 'Final de la funcion generadora'
#---NOTA IMPORTANTE una de las caracteristicas de los generadores es que sus variables, parametros
# una vez se llama a next, estas SE GUARDAN EN LA MEMORIA HASTA LA SGTE LLAMADA 
iter_par = generador_pares([1,2,3,4,5,6,7])                    
print(next(iter_par))
print(next(iter_par))
print(next(iter_par))
print(next(iter_par))
#Tambien podemos usar un ciclo for y como iterable a la funcion generadora, como en el sgte ejemplo:
def listas_paralelas (lista1, lista2):
    for elem1, elem2 in zip(lista1,lista2):
        yield elem1
        yield elem2

for i in listas_paralelas([1,3,5,7,9], [2,4,6,8,10]):
    print(i)
#-------fin
#------------------PARAMETROS DE FUNCIONES PREDEFINIDOS CON VALORES POR DEFECTO
#"la lista predeterminada se mantiene y se comparte entre todas las llamadas subsiguientes que no proporcionan 
# un argumento para lista" 
# EXACTO aca esta la logica a entender y si las llamadas subsiguientes tiene como 
# argumento una lista de afuera, todo lo que pase dentro de esa llamada afecta a la lista de afuera nada mas,
# luego la lista propia con valor predefinido se mantiene igual que antes con el valor 4 y se vuelve a usar  
# cuando llamemos a la funcion suma sin un argumento tipo lista
#------------TOD0 ESTO ES VALIDO SOLO CON VARIABLES MUTABLES COMO LISTA, DICCIONARIOS Y SETS
def suma (num, lista = []):
    lista.append(num)
    return sum(lista)

print(suma(4)) # salida 4
print(suma(10,[60])) # salida 70
print(suma(100)) # salida 104
#--Supongamos que creamos una funcion y queremos saber cuantas veces se la llamo, entonces usamos un contador tipo int
# que en teoria tendria que funcionar como las listas y pasar su valor a las sgtes llamadas en las que solo se le pase
# el argumento "num", PERO NO ES ASI, ya que los tipos inmutables como los int no tienen esa propiedad de que si en la
# llamada no le pasamos el argumento "cont" este usa cero la primera vez y ya la segunda va incrementado y ese valor se va 
# pasando de funcion en funcion eso no vale con los de tipo inmutables OJOOOO!!!!!!!!!!!
def elevar_cuadrado (num, cont = 0):
    cont += 1
    print(f"Llamada a la funcion numero: {cont}") #El contador siempre sera "1" ya que su valor no va pasando de funcion en funcion
    return num ** 2                               #No son como los de tipo Mutable

print(elevar_cuadrado(2)) # salida 4
print(elevar_cuadrado(5)) # salida 25
print(elevar_cuadrado(8)) # salida 64

    












    



















