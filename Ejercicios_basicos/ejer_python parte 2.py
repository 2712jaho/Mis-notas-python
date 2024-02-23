# Escribir una función mas_larga() que tome una lista de palabras y devuelva la mas larga.
frase = input("Ingrese una frase ")
def mas_larga(frase):
    pal_larga = ""
    car_largo = 0
    for pal in frase.split(' '):
        if len(pal) > car_largo :
            pal_larga = pal
            car_largo = len(pal)
    return pal_larga
print(mas_larga(frase))
# ------------------------------------------
# Escribir una función filtrar_palabras() que tome una lista de palabras y un entero n, y devuelva 
# las palabras que tengan mas de n caracteres.
lista_palabras = (input("Ingrese una frase ")).split(' ')
def filtrar_pal(lista_pal, n):
    return [ pal for pal in lista_pal if len(pal) > n ]
print(filtrar_pal(lista_palabras, 4))
# -----------------------------------------
# Escribir un programa que le diga al usuario que ingrese una cadena. 
# El programa tiene que evaluar la cadena y decir cuantas letras mayúsculas tiene.
cadena = input("Ingrese una cadena (palabra) ")
def cant_car_mayusc(cadena):
    return len([i for i in cadena if i == i.upper()])
print(cant_car_mayusc(cadena))
# -----------------------------------------
# Construir un pequeño programa que convierta números binarios en enteros.
def convert_bin_ent (num_bin):   
    return (sum([2**int(indice) for indice,element in enumerate((list(str(num_bin)))[::-1]) if element == '1']))
num_bin = int(input("Ingrese un numero binario "))
print(f"El numero {num_bin} convertido a base 10 es {convert_bin_ent(num_bin)}")
# -----------------------------------------
# Escribir un pequeño programa donde:
# - Se ingresa el año en curso.
# - Se ingresa el nombre y el año de nacimiento de tres personas.
# - Se calcula cuántos años cumplirán durante el año en curso.
# - Se imprime en pantalla.
año_actual = int(input("Ingrese el año actual "))
dicc_datos = {}
for i in range(3):
    lista_auxi = (input("Ingrese un nombre y el año de nacimiento ")).split(' ')
    dicc_datos[lista_auxi[0]] = int(lista_auxi[1])
for nombre, año_n in dicc_datos.items():
    print(f"{nombre} cumplira {año_actual - año_n} años de este año {año_actual}")
# ---------------------------------------------
# Definir una tupla con 10 edades de personas.
# Imprimir la cantidad de personas con edades superiores a 20.
# Puedes variar el ejercicio para que sea el usuario quien ingrese las edades.
edades = ()
lista_edades = []
for i in range(10):
    lista_edades.append(input(f"Ingrese la edad nro {i + 1} "))
edades = tuple(lista_edades)
for edad in edades:
    if int(edad) > 20:
        print(edad, end= ' ')
print()
# -----------------------------------------------
# Definir una lista con un conjunto de nombres, imprimir la cantidad de comienzan con la letra a.
# También se puede hacer elegir al usuario la letra a buscar
def cant_nombre_con_letra (list_nombre, letra):
    return [nombre for nombre in list_nombre if (nombre[0]).upper() == letra.upper()]    
nombres = []
for i in range(int(input("Ingrese la cantidad de nombres "))):
    nombres.append(input(f"Ingrese el nombre nr {i + 1} "))
letra = input("Ingrese la letra con la que quiere calcular la cantidad de nombres ")
print(f"Los nombres que arrancan con '{letra}' son {cant_nombre_con_letra(nombres, letra)}")
# --------------------------------------------------------------        
# Crear una función contar_vocales(), que reciba una palabra y cuente cuantas letras "a" tiene, 
# cuantas letras "e" tiene y así hasta completar todas las vocales.
# Se puede hacer que el usuario sea quien elija la palabra.
def contar_vocales(palabra):
    diccionario_vocales = {}
    diccionario_vocales['a'] = palabra.count('a') + palabra.count('A')
    diccionario_vocales['e'] = palabra.count('e') + palabra.count('E')
    diccionario_vocales['i'] = palabra.count('i') + palabra.count('I')
    diccionario_vocales['o'] = palabra.count('o') + palabra.count('O')
    diccionario_vocales['u'] = palabra.count('u') + palabra.count('U')
    return diccionario_vocales
result = contar_vocales(input("Ingrese una palabra "))
for vocal, num_rep in result.items():
    print(f"La vocal {vocal} se repite {num_rep} ")
# ------------------------------------------------------
# Escriba una función es_bisiesto() que determine si un año determinado es un año
# bisiesto.Un año bisiesto es divisible por 4, pero no por 100.
def es_bisiesto(anio):
    return (anio % 4 == 0) and (anio % 100 != 0)
anio = int(input("Ingrese un año "))
print(f"El año {anio} SI es bisiesto" if es_bisiesto(anio) else f"El año {anio} NO es bisiesto")
# ------------------------------------------------------
