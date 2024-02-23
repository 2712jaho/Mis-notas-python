#----------------
'''Ejercicio 1'''
print()
#Escribir un programa que guarde en una variable el diccionario {'Euro':'€', 'Dollar':'$', 'Yen':'¥'}, 
# pregunte al usuario por una divisa y muestre su símbolo o un mensaje de aviso si la divisa no está en 
# el diccionario.
'''#Forma senior
monedas = {'Euro':'€', 'Dollar':'$', 'Yen':'¥'}
moneda = input("Introduce una divisa: ")
print(monedas.get(moneda.title(), "La divisa no está."))
'''
dic_1 = dict(
    euro = '€',
    dollar = '$',
    yen = '¥'    
)
divisa = input("Ingrese una divisa ").lower()
print( dic_1[divisa] if divisa in dic_1 else "La divisa no esta en el diccionario" )
'''Fin de ejercicio 1'''
#----------------
'''Ejercicio 2'''
print()
#Escribir un programa que pregunte al usuario su nombre, edad, dirección y teléfono y lo guarde en un
# diccionario. Después debe mostrar por pantalla el mensaje <nombre> tiene <edad> años, vive en <dirección> 
# y su número de teléfono es <teléfono>.
dic_2 = dict()
dic_2['Nombre'] = input("Ingrese su nombre ")
dic_2['Edad'] = int(input("Ingrese su edad "))
dic_2['Direccion'] = input("Ingrese su direccion ")
dic_2['Telefono'] = int(input("Ingrese su numero celular "))
print(f"{dic_2.get('Nombre')} tiene {dic_2.items('Edad')} anos, vive en {dic_2.get('Direccion')} y su numero de telefono es {dic_2.get('Telefono')}")
'''Fin de ejercicio 2'''
#-------------------
'''Ejercicio 3'''
print()
#Escribir un programa que guarde en un diccionario los precios de las frutas de la tabla, pregunte al 
# usuario por una fruta, un número de kilos y muestre por pantalla el precio de ese número de kilos de fruta. 
# Si la fruta no está en el diccionario debe mostrar un mensaje informando de ello.
dic_3 = dict(
    Banana = 1.35,
    Manzana = 0.80,
    Pera = 0.85,
    Naranja = 0.70
)
fruta = (input("Ingrese una Fruta ")).title()
kilo = int(input("Ingrese los kilos a comprar "))
print( f"El precio total de los kilos de {fruta} es {(dic_3.get(fruta))*kilo}" if fruta in dic_3 else "No vendemos esa fruta " )
'''Fin de Ejercicio 3'''
#--------------
'''Ejercicio 4'''
print()
#Escribir un programa que pregunte una fecha en formato dd/mm/aaaa y muestre por pantalla la misma fecha 
# en formato dd de <mes> de aaaa donde <mes> es el nombre del mes.
dic_4 = {'1':'Enero','2':'Febrero','3': 'Marzo','4':'Abril', '5': 'Mayo','6': 'Junio', '7' : 'Julio', '8':'Agosto','9':'Septiembre','10': 'Octubre', '11': 'Noviembre', '12': 'Diciembre' }
lista_fecha = (input("Ingrese una fecha ")).split('/')
print(f"{lista_fecha[0]} de {dic_4.get(lista_fecha[1], "Mes invalido")} de {lista_fecha[2]}")
'''Fin de ejercicio 4'''
#--------------------
'''Ejercicio 5'''
print()
#Escribir un programa que almacene el diccionario con los créditos de las asignaturas de un curso 
# {'Matemáticas': 6, 'Física': 4, 'Química': 5} y después muestre por pantalla los créditos de cada 
# asignatura en el formato <asignatura> tiene <créditos> créditos, donde <asignatura> es cada una de 
# las asignaturas del curso, y <créditos> son sus créditos. Al final debe mostrar también el número total 
# de créditos del curso.
dic_5 = {'Matemáticas': 6, 'Física': 4, 'Química': 5}
cont_creditos = 0
for key,value in dic_5.items():
    print(f"{key} tiene {value} creditos")
    cont_creditos += value
print(f"El total de creditos es de {cont_creditos}")
'''Fin de ejercicio 5'''
#-------------------
'''Ejercicio 6'''
print()
#Escribir un programa que cree un diccionario vacío y lo vaya llenado con información sobre una persona 
# (por ejemplo nombre, edad, sexo, teléfono, correo electrónico, etc.) que se le pida al usuario. 
# Cada vez que se añada un nuevo dato debe imprimirse el contenido del diccionario.
respuesta = 1
dic_6 = {}
while(respuesta == 1):
    nombre_dato = (input("Ingrese que clase de dato añadira ")).title()
    dic_6[nombre_dato] = (input(f"Ingrese el {nombre_dato} de la persona ")).title()
    for llave, valor in dic_6.items():
        print(llave + ":", valor)
    respuesta = int(input("Presione '1' si quiere continuar o '0' si quiere parar " ))
'''Fin de ejercicio 6'''
#-------------------
'''Ejercicio 7'''
print()
#Escribir un programa que cree un diccionario simulando una cesta de la compra. 
# El programa debe preguntar el artículo y su precio y añadir el par al diccionario, hasta que el usuario 
# decida terminar. Después se debe mostrar por pantalla la lista de la compra y el coste total, con el 
# siguiente formato
respuesta = True
cesta = {}
while respuesta :
    articulo = (input("Ingrese el nombre del articulo ")).title()
    cesta[articulo] = input(f"Ingrese el precio del articulo {articulo} ")
    respuesta = True if (input("Presione 1 para continuar o 0 para salir ")) == '1' else False    
total = 0
for art,precio in cesta.items():
    print(art.ljust(13,' '), precio)
    total += float(precio)
print(("Total").ljust(13,' '),total )

'''Fin ejercicio 7'''
#-------------------
'''Ejercicio 8'''
print()
#Escribir un programa que cree un diccionario de traducción español-inglés. 
# El usuario introducirá las palabras en español e inglés separadas por dos puntos, y cada 
# par <palabra>:<traducción> separados por comas. El programa debe crear un diccionario con las palabras 
# y sus traducciones. Después pedirá una frase en español y utilizará el diccionario para traducirla palabra 
# a palabra. Si una palabra no está en el diccionario debe dejarla sin traducir.
print("Ingrese las palabras con sus respectivas traducciones <palabra>:<traducción> separados por ' , ' ", end='\n')
lista_palabras = (input("-")).split(',')
diccionario ={}
for word in lista_palabras:
    palabra = (word[:word.index(':')]).strip()
    diccionario[palabra] = (word[word.index(':') + 1:]).strip() #traduccion de la palabra
lista_frase = (input("Ingrese la frase ")).split(' ')
traduccion = ""
for pal_español in lista_frase:
    traduccion += diccionario.get((pal_español).strip(), pal_español) + " "
print(traduccion)

'''Fin ejercicio 8'''
#---------------------
'''Ejercicio 9'''
print()
#Escribir un programa que gestione las facturas pendientes de cobro de una empresa. 
# Las facturas se almacenarán en un diccionario donde la clave de cada factura será el número de factura 
# y el valor el coste de la factura. El programa debe preguntar al usuario si quiere añadir una nueva 
# factura, pagar una existente o terminar. Si desea añadir una nueva factura se preguntará por el número
# de factura y su coste y se añadirá al diccionario. Si se desea pagar una factura se preguntará por el
# número de factura y se eliminará del diccionario. Después de cada operación el programa debe mostrar 
# por pantalla la cantidad cobrada hasta el momento y la cantidad pendiente de cobro.
print("Programa de Facturas H.O")    
Lista_facturas ={}
cant_pagada = 0

def Cant_a_pagar(lista_values):
    cant_por_pagar = 0
    for i in lista_values:
        cant_por_pagar += i
    return cant_por_pagar

while True :
    num = input("\tPresione 1 Para añadir factura\n\tPresione 2 Para pagar factura\n\tPresione 3 Para salir\n-")
    # num = input("Ingrese un numero")
    if num == '1':
        factura_añadir = input("Ingrese el numero de factura a añadir ")
        Lista_facturas[factura_añadir] = float(input("Ingrese el monto de la factura "))
        print(f"Cantidad por pagar {Cant_a_pagar(Lista_facturas.values())}\nCantidad pagada {cant_pagada}")                   
    elif num == '2':
        cant_pagada += Lista_facturas.pop(input("Ingrese el numero de factura a pagar "))
        print(f"Cantidad por pagar {Cant_a_pagar(Lista_facturas.values())}\nCantidad pagada {cant_pagada}") 
    else:
        break
'''Fin ejercicio 9'''
#---------------
'''Ejercicio 10'''
print()
# Escribir un programa que permita gestionar la base de datos de clientes de una empresa. 
# Los clientes se guardarán en un diccionario en el que la clave de cada cliente será su NIF, 
# y el valor será otro diccionario con los datos del cliente (nombre, dirección, teléfono, correo, preferente),
# donde preferente tendrá el valor True si se trata de un cliente preferente. 
# El programa debe preguntar al usuario por una opción del siguiente menú: 
# (1) Añadir cliente, (2) Eliminar cliente, (3) Mostrar cliente, (4) Listar todos los clientes,
# (5) Listar clientes preferentes, (6) Terminar. 
# En función de la opción elegida el programa tendrá que hacer lo siguiente:

# 1 Preguntar los datos del cliente, crear un diccionario con los datos y añadirlo a la base de datos.
# 2 Preguntar por el NIF del cliente y eliminar sus datos de la base de datos.
# 3 Preguntar por el NIF del cliente y mostrar sus datos.
# 4 Mostrar lista de todos los clientes de la base datos con su NIF y nombre.
# 5 Mostrar la lista de clientes preferentes de la base de datos con su NIF y nombre.
# 6 Terminar el programa.
print("Base de Datos H.O")
lista_10 = {}
respuesta_10 = '0'
while respuesta_10 != '6':
    respuesta_10 = input("\t(1) Añadir cliente\n\t(2) Eliminar cliente\n\t(3) Mostrar cliente\n\t(4) Listar todos los clientes\n\t(5) Listar clientes preferentes\n\t(6) Terminar\n-")
    if respuesta_10 == '1':
        nuevo_cliente = {}
        nif = input("Introduzca el Nif del nuevo cliente ")
        nuevo_cliente['Nombre'] = (input("Introduzca el nombre ")).title()
        nuevo_cliente['Direccion'] = (input("Introduzca la direccion ")).title()
        nuevo_cliente['Telefono'] = (input("Introduzca el telefono ")).title()
        nuevo_cliente['Correo'] = (input("Introduzca el correo electronico ")).title()
        nuevo_cliente['Preferente'] = True if ((input("Presione Y/N si quiere al cliente como preferente ")).upper()) == 'Y' else False
        lista_10[nif] = nuevo_cliente.copy()
        print()
    if respuesta_10 == '2':
        nif_borrar = input("Ingrese el Nif del cliente a borrar ")
        if nif_borrar in lista_10:
            lista_10.pop(nif_borrar)
            print(f"El cliente {nif_borrar} ha sido borrado con exito")
        else:
            print(f"El cliente {nif_borrar} no se encuentra en nuestra base de datos")
        print()
    if respuesta_10 == '3':
        nif_mostrar = input("Ingrese el Nif del cliente a mostrar ")
        print(f"Cliente : {nif_mostrar}")
        for dato, valor in ((lista_10[nif_mostrar]).items()):
            print((dato).ljust(15,' '), valor)        
        print()
    if respuesta_10 == '4':
        for nif_cliente, dicc_cliente in lista_10.items():
            print(f"Cliente: {nif_cliente} Nombre: {dicc_cliente.get('Nombre')}" )            
        print()
    if respuesta_10 == '5':
        for nif_cliente, dicc_cliente in lista_10.items():
            if dicc_cliente.get('Preferente'):
                print(f"Cliente : {nif_cliente} Nombre: {dicc_cliente.get('Nombre')}")
        print()
'''fin ejercicio 10'''
#----------------------
'''Ejercico 11'''
print()
#Escribir un programa que genere un diccionario con la información del directorio, 
# donde cada elemento corresponda a un cliente y tenga por clave su nif y por valor otro diccionario 
# con el resto de la información del cliente. Los diccionarios con la información de cada cliente tendrán 
# como claves los nombres de los campos y como valores la información de cada cliente correspondientes
# a los campos. Es decir, un diccionario como el siguiente
print("Programa De Clientes H.O")
# {'01234567L': {'nombre': 'Luis González', 'email': 'luisgonzalez@mail.com', 'teléfono': '656343576', 'descuento': 12.5}, '71476342J': {'nombre': 'Macarena Ramírez', 'email': 'macarena@mail.com', 'teléfono': '692839321', 'descuento': 8.0}, '63823376M': {'nombre': 'Juan José Martínez', 'email': 'juanjo@mail.com', 'teléfono': '664888233', 'descuento': 5.2}, '98376547F': {'nombre': 'Carmen Sánchez', 'email': 'carmen@mail.com', 'teléfono': '667677855', 'descuento': 15.7}}
diccinario_padre ={}
lista_11 = (input("Ingrese la unica linea con toda la informacion ")).split('\\n')
print(lista_11)
for i in range(1, len(lista_11)):
      sub_lista = (lista_11[i]).split(';')
      diccinario_hijo = {'Nombre:':sub_lista[1], 'Email':sub_lista[2], 'Telefono': sub_lista[3], 'Descuento': sub_lista[4]}
      diccinario_padre[sub_lista[0]] = diccinario_hijo
print(diccinario_padre)    
'''Fin ejercicio 11'''










