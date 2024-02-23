#----------------
'''Ejer 1'''
print()
# Escribir una función que aplique un descuento a un precio y otra que aplique el IVA a un precio.
# Escribir una tercera función que reciba un diccionario con los precios y porcentajes de una cesta de la 
# compra, y una de las funciones anteriores, y utilice la función pasada para aplicar los descuentos o el 
# IVA a los productos de la cesta y devolver el precio final de la cesta.
desc = lambda precio, desc: precio - (precio*(desc/100))
valor_agregd = lambda precio, iva: precio + (precio*(iva/100))
def ejer_1 (dic, funcion):
    return sum(list(map(funcion, dic.keys(), dic.values())))

cesta_compras = {1000:20, 500:10, 100:1}
print(f"total a pagar con descuento es de: {ejer_1(cesta_compras,desc)}")
print(f"total a pagar incluido iva es de: {ejer_1(cesta_compras,valor_agregd)}")
'''fin ejer 1'''
#----------------
'''Ejer 2'''
print()
# Escribir una función que simule una calculadora científica que permita calcular el seno, coseno, tangente,
# exponencial y logaritmo neperiano. La función preguntará al usuario el valor y la función a aplicar, y 
# mostrará por pantalla una tabla con los enteros de 1 al valor introducido y el resultado de aplicar la 
# función a esos enteros.
import math
seno = lambda num: math.sin(num)
coseno = lambda num: math.cos(num)
tangente =  lambda num: math.tan(num)
e = lambda num: math.exp(num)
log = lambda num: math.log10(num)
def calculadora ():   
    while(True) :
        indice = int(input("\n\t\tFunciones:\n\t\t1- Sen\n\t\t2- Cos\n\t\t3- Tang\n\t\t4- Exp\n\t\t5- Log\nSeleccione una opcion "))    
        num = float(input("\nIngrese un numero "))
        if indice == 1:
            for sub_indice, valor in enumerate(list(map(seno,[i for i in range(1, int(num)+1)]))):
                print(f"Sen({sub_indice + 1}) = {valor}")
        elif indice == 2:
            for sub_indice, valor in enumerate(list(map(coseno,[i for i in range(1, int(num)+1)]))):
                print(f"Cos({sub_indice + 1}) = {valor}")
        elif indice == 3:
            for sub_indice, valor in enumerate(list(map(tangente,[i for i in range(1, int(num)+1)]))):
                print(f"Tang({sub_indice + 1}) = {valor}")
        elif indice == 4:
            for sub_indice, valor in enumerate(list(map(e,[i for i in range(1, int(num)+1)]))):
                print(f"e^{sub_indice + 1} = {valor}")
        elif indice == 5:
            for sub_indice, valor in enumerate(list(map(log,[i for i in range(1, int(num)+1)]))):
                print(f"Log10({sub_indice + 1}) = {valor}")
        if (input("Presione Y/N si desea continuar ")).upper() == 'N':
            break
            
calculadora()        
'''Fin ejer 2'''
#--------------------
'''Ejercicio 3'''
print()
# Escribir una función que reciba otra función y una lista, y devuelva otra lista con el resultado de 
# aplicar la función dada a cada uno de los elementos de la lista. 
def funcion_de_funciones (funcion, lista: list)->list:
    print("LLamando forma 1")
    return list(map(funcion, lista))

def funcion_de_funciones_2(funcion, lista:list)->list:
    print("LLamando forma 2")
    return [ funcion(element) for element in lista]

cuadrado = lambda num: num**2
print(f"{funcion_de_funciones(cuadrado,[i for i in range(1,11)])}")
print(f"{funcion_de_funciones_2(cuadrado,[i for i in range(1,11)])}")
'''fin ejer 3'''
#--------------------
'''Ejercicio 4'''
print()
# Escribir una función que reciba otra función booleana y una lista, y devuelva otra lista con los elementos 
# de la lista que devuelvan True al aplicarles la función booleana.
def funcion_funciones_bool (funcion, lista):
    return [element for element in lista if funcion(element)]

verif_par = lambda n: n%2==0

print(funcion_funciones_bool(verif_par, [i for i in range(1,11)]))
'''Fin ejer 4'''
#-------------
'''Ejercicio 5'''
print()
# Escribir una función que reciba una frase y devuelva un diccionario con las palabras que contiene 
# y su longitud.
def ejercicio_5 (frase:str)->dict: #FORMA 1
    result = {}
    for pal in frase.split(' '):
        result[pal] = len(pal)
    return result

print(f"{ejercicio_5('pepe comio paltas')}")

def ejercicio_5_2(frase:str)->dict:#FORMA 2
    return dict(map(lambda pal:(pal, len(pal)), frase.split(' ')))

print(f"{ejercicio_5_2('pepe come palta')}")
'''Fin ejer 5'''
#-------------
'''Ejercicio 6'''
print()
# Escribir una función reciba un diccionario con las asignaturas y las notas de un alumno y devuelva otro 
# diccionario con las asignaturas en mayúsculas y las calificaciones correspondientes a las notas.
def ejercicio_6(notas):
    def calificacion(nota):
        if nota < 5:
            return 'SS'
        elif nota < 7:
            return 'AP'
        elif nota < 9:
            return 'NT'
        elif nota < 10:
            return 'SB'
        else:
            return 'MH'
    return {materia.upper(): calificacion(nota) for materia, nota in notas.items()}

print(ejercicio_6({'Matemáticas':6.5, 'Física':5, 'Química':3.4, 'Economía':8.2, 'Historia':9.7, 'Programación':10}))
'''Fin ejer 6'''
#--------------
'''Ejercicio 7'''
print()
# Zona A: precio = (metros * 1000 + habitaciones * 5000 + garaje * 15000) * (1-antiguedad/100)
# Zona B: precio = (metros * 1000 + habitaciones * 5000 + garaje * 15000) * (1-antiguedad/100) * 1.5
# Construir una función que permita hacer búsqueda de inmuebles en función de un presupuesto dado. 
# La función recibirá como entrada la lista de inmuebles y un precio, y devolverá otra lista con los 
# inmuebles cuyo precio sea menor o igual que el dado. Los inmuebles de la lista que se devuelva deben
# incorporar un nuevo par a cada diccionario con el precio del inmueble, donde el precio de un inmueble 
# se calcula con las siguiente fórmula en función de la zona:
#FORMA MIA
def Ejercicio_7 (inmobiliaria: list, precio: float) -> list: 
    for casa in inmobiliaria:
        if casa['zona'] == 'A':
            casa['precio'] = float((casa['metros'] * 1000 + casa['habitaciones'] * 5000 + int(casa['garaje'])*15000) * (1 - (2020 - casa['año'])/100))
        else:
            casa['precio'] = float((casa['metros'] * 1000 + casa['habitaciones'] * 5000 + int(casa['garaje'])*15000) * (1 - (2020 - casa['año'])/100) * 1.5)
    return [ casa for casa in inmobiliaria if casa['precio'] <= precio]

casas = [{'año': 2000, 'metros': 100, 'habitaciones': 3, 'garaje': True, 'zona': 'A'}, {'año': 2012, 'metros': 60, 'habitaciones': 2, 'garaje': True, 'zona': 'B'}, {'año': 1980, 'metros': 120, 'habitaciones': 4, 'garaje': False, 'zona': 'A'}, {'año': 2005, 'metros': 75, 'habitaciones': 3, 'garaje': True, 'zona': 'B'}, {'año': 2015, 'metros': 90, 'habitaciones': 2, 'garaje': False, 'zona': 'A'}]
    
print(Ejercicio_7(casas,100000))


#FORMA DE ALF
pisos = [{'año': 2000, 'metros': 100, 'habitaciones': 3, 'garaje': True, 'zona': 'A'}, {'año': 2012, 'metros': 60, 'habitaciones': 2, 'garaje': True, 'zona': 'B'}, {'año': 1980, 'metros': 120, 'habitaciones': 4, 'garaje': False, 'zona': 'A'}, {'año': 2005, 'metros': 75, 'habitaciones': 3, 'garaje': True, 'zona': 'B'}, {'año': 2015, 'metros': 90, 'habitaciones': 2, 'garaje': False, 'zona': 'A'}]

def añadir_precio(piso):
    precio = (piso['metros'] * 1000 + piso['habitaciones'] * 5000 + int(piso['garaje']) * 15000) * (1 - (2020 - piso['año']) / 100)
    if piso['zona'] == 'B':
        precio *= 1.5
    piso['precio'] = precio
    return piso

def busca_piso(pisos, presupuesto):
    def filtro(piso):
        return piso['precio'] <= presupuesto

    return list(filter(filtro,map(añadir_precio, pisos)))
'''Fin ejercicio 7'''
#---------------
'''Ejercicio 8'''
print()
# Escribir una función que tome una lista y devuelva una nueva lista eliminando los elementos duplicados.

def element_unicos (num, lista_auxi = []):
    respuesta = False
    if num not in lista_auxi:
        lista_auxi.append(num)
        respuesta = True
    return respuesta

print(list(filter(element_unicos,[1,2,3,1,3,12,3,2,4,6,2])))
'''Fin ejercicio 8'''
#---------------
'''Ejercicio 9'''
print()
#Palabras con longitud específica:
# Escribir una función que tome una lista de palabras y un número entero n, y devuelva una nueva 
# lista con las palabras que tienen una longitud igual a n.
def filtro_pal (lista, n):
    return list(filter(lambda pal: len(pal) == n, lista))

print(filtro_pal(['pepe', 'carlos', 'juan', 'mateo'], 4))
'''Fin ejercicio 9'''
#---------------
'''Ejercicio 10'''
print()
#Combinar Listas Únicas
#Escribe una función llamada combinar_listas_unicas que tome dos listas y devuelva una nueva lista que 
# contenga todos los elementos únicos de ambas listas. Utiliza las funciones map, filter, o cualquier 
# otra función de programación funcional que encuentres apropiada.
def comb_lista_unicas (list1, list2):    
    def element_unicos (num, lista_auxi = []):
        respuesta = False
        if num not in lista_auxi:
            lista_auxi.append(num)
            respuesta = True
        return respuesta
    return list(filter(element_unicos, list1 + list2))

print(comb_lista_unicas([1,2,3,4],[3,4,5,6]))
'''Fin ejercicio 10'''
#---------------
'''Ejercicio 11'''
print()
#Contar Palabras Únicas
#Escribe una función llamada contar_palabras_unicas que tome una lista de frases y devuelva un diccionario 
# donde las claves son palabras únicas y los valores son la cantidad de veces que aparecen en todas las frases. 
# Utiliza funciones como map, filter, reduce o cualquier otra función de programación funcional que encuentres 
# útil.
def cont_pal_unicas (lista_frases):
    lista_frases = ' '.join(lista_frases)
    lista_frases = lista_frases.split(' ')
    def pal_unicas (pal, lista_auxi = []):
        respuesta = False
        if pal not in lista_auxi:
            lista_auxi.append(pal)
            respuesta = True
        return respuesta
    lista_pal_unicas = list(filter(pal_unicas, lista_frases))
    cant_rep = list(map(lambda pal: ' '.join(lista_frases).count(pal), lista_pal_unicas))
    return {pal:cant for pal, cant in zip(lista_pal_unicas,cant_rep)}

frases = ["Hola mundo", "Python es genial", "Hola programación funcional", "Python es poderoso"]    
print(cont_pal_unicas(frases))
#{'Hola': 2, 'mundo': 1, 'Python': 2, 'es': 2, 'genial': 1, 'programación': 1, 'funcional': 1, 'poderoso': 1}
# {'Hola': 2, 'mundo': 1, 'Python': 2, 'es': 2, 'genial': 1, 'programación': 1, 'funcional': 1, 'poderoso': 1}






















