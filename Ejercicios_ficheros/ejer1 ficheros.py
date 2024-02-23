#Programa que cuenta cuantas lineas tiene un archivo tipo texto y cual es la longuitud de cada linea
def contador_lineas_con_str_COMO_GENERADOR(nombre_fichero):
    print("Forma 1 usando una funcion genereador...........")
    with open( fr"C:\Users\josealejandro\Documents\{nombre_fichero}.txt", 'r') as archivo:
        lista_result = archivo.readlines()
    for indice, linea in enumerate(lista_result):
        if linea == '\n':
            lista_result.pop(indice)
    for indice, linea in enumerate(lista_result):
        if (indice + 1) == len(lista_result):
            yield f'La linea / fila con texto nr {indice + 1} tiene {len(linea)} caracteres'
        else:
            yield f'La linea / fila con texto nr {indice + 1} tiene {len(linea) - 1} caracteres'

cont = 0
for result in contador_lineas_con_str_COMO_GENERADOR(input('Ingrese el nombre del archivo ')):
    cont += 1
    print(result)
print(f'La cantidad total de filas con texto es de {cont}')    

def contador_lineas_con_str(nombre_fichero):
    print("Forma 2 usando una funcion normal...........")
    with open( fr"C:\Users\josealejandro\Documents\{nombre_fichero}.txt", 'r') as archivo:
        lista_result = archivo.readlines()
    for indice, linea in enumerate(lista_result):
        if linea == '\n':
            lista_result.pop(indice)
    for indice, linea_str in enumerate(lista_result):
        if (indice + 1) == len(lista_result):
            print(f'La linea / fila con texto nr {indice + 1} tiene {len(linea_str)} caracteres')
        else:
            print(f'La linea / fila con texto nr {indice + 1} tiene {len(linea_str) - 1} caracteres')
    print(f'La cantidad total de filas con texto es de {len(lista_result)}')    
    
contador_lineas_con_str(input('Ingrese el nombre del archivo '))

#Nombre del archivo es: ejer_1 de arch.txt






