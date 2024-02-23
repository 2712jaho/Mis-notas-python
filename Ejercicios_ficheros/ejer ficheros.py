#-----------
'''Ejercicio 1'''
print()
# Escribir una función que pida un número entero entre 1 y 10 y guarde en un fichero con el nombre tabla-n.txt
# la tabla de multiplicar de ese número, done n es el número introducido.
def tabla_mult (num):
    try:
        f = open(fr"C:\Users\josealejandro\Documents\Tabla del {num}.txt", 'x')                        
    except Exception as e:
        print('ERROR fichero existente boludo')
    else:
        for i in range(1,11):
            f.write(f'{i} x {num} = {i*num}\n')
        f.close()

def mostrar_fichero(fichero):
    try:
        f = open(fr"C:\Users\josealejandro\Documents\{fichero}.txt", 'r')  
    except Exception as e:
        print('ERROR fichero algo salio mal boludo')
    else:
        print(f.read())
        f.close()
        
while(True):
    eleccion = int(input('Ingrese una opcio\n1) crear una tabla\n2) leer una tabla\n3) salir del codigo\n'))
    if eleccion == 1:
        tabla_mult(int(input('Ingrese un numero del 1 al 10 ')))
    elif eleccion == 2:
        mostrar_fichero(input('Ingrese el nombre de la tabla a mostrar '))
    else:
        break
print('Feliz dia bb')

'''Fin ejer 1'''
#--------------
'''Ejercicio 2'''
print()
import os
def Verif_listin ():
    return os.path.isfile(r'C:\Users\josealejandro\Documents\listin.txt')

def crear_listin():
    listin = open(r'C:\Users\josealejandro\Documents\listin.txt', 'x')
    listin.close()

def consult (nombre:str)->str:
    with open(r'C:\Users\josealejandro\Documents\listin.txt', 'r') as listin:
        agenda = listin.readlines()
    puntero = -1
    for indice, elemento in enumerate(agenda):
        if elemento.find(nombre) != -1:
            puntero = indice
            break
    if puntero == -1:
        return f'{nombre} no se encuentra en la lista'
    else:
        return agenda[puntero][-9:-1]

def agregar (nombre:str, numero:str):
    with open(r'C:\Users\josealejandro\Documents\listin.txt', 'a') as listin:
        listin.write(f"{nombre}, {numero}\n")
        print(f'{nombre} fue agregado con exito!')

def eliminar (nombre:str):
    with open(r'C:\Users\josealejandro\Documents\listin.txt', 'r') as listin:
        agenda = listin.readlines()
    puntero = -1
    for indice, elemento in enumerate(agenda):
        if elemento.find(nombre) != -1:
            puntero = indice
            break
    if puntero == -1:
        return f'{nombre} no se encuentra en la lista'
    else:
        agenda.pop(puntero)
        listin = open(r'C:\Users\josealejandro\Documents\listin.txt', 'w')
        listin.writelines(agenda)
        listin.close()
        return f'{nombre} fue borrado con exito'
         
def menu ():
    while True:    
        indice = int(input('Seleccione una opcion\n1- Agregar\n2- Consultar\n3- Eliminar\n'))
        if indice == 1:
            if Verif_listin() == False:
                crear_listin()
            nombre = input('Ingrese el nombre completo ')
            numero = input('Ingrese el N° de cel ')
            agregar(nombre, numero)
        elif indice == 2:
            nombre = input('Ingrese el nombre completo ')
            print(consult(nombre))
        elif indice == 3:
            nombre = input('Ingrese el nombre completo ')
            print(eliminar(nombre))
        if input('Presione 1 para salir, 0 para continuar ') == '1':
            break
    
menu()
'''fin ejer'''
#------------






