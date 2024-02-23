from random import randint
''' Ejercicio 1'''
#Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, Física, 
# Química, Historia y Lengua) en una lista, pregunte al usuario la nota que ha sacado en cada asignatura,
# y después las muestre por pantalla con el mensaje En <asignatura> has sacado <nota> donde <asignatura> 
# es cada una des las asignaturas de la lista y <nota> cada una de las correspondientes notas introducidas 
# por el usuario.
n = int(input("Ingrese la cantidad de materias a grabar: "))
lista_materias = []
for i in range(n):
    lista_materias.append(input(f"Ingrese la materia nr {i+1} "))
lista_notas = []
iterador_materias = iter(lista_materias)
for i in range(n):
    lista_notas.append(int(input(f"Ingrese la nota para la materia de {next(iterador_materias)} : ")))
iterador_materias = iter(lista_materias)
for i in range(n):
    print(f"La materia '{next(iterador_materias)}' tiene como nota {lista_notas[i]}")
'''Fin de ejercicio 1'''
#-------------------------------
'''Ejercicio 2'''
#Escribir un programa que pregunte al usuario los números ganadores de la lotería primitiva, 
# los almacene en una lista y los muestre por pantalla ordenados de menor a mayor.
mi_lista = list(input("Ingrese los numeros ganadores de la Loteria: "))
mi_lista.sort()
print(mi_lista)
'''Fin de ejercicio 2'''
#-------------------------------
'''Ejercicio 3'''
#Escribir un programa que almacene en una lista los números del 1 al 10 y los muestre por pantalla 
# en orden inverso separados por comas.
lista_ejer_3 =[]
#Dos formas de hacer lo mismo
#forma 1
'''for i in range(10):
    num_rand = randint(1,10)
    while(num_rand in lista_ejer_3):
        num_rand = randint(1,10)
    lista_ejer_3.append(num_rand)'''
#forma 2------------------------------------NOTAS "SORT Y SORTED"
bandera = True                             #Ambas ordenan una lista de menor a mayor o viceversa, pero la 
for i in range(10):                        #diferencia esta en que sorted Crea una new list ordenada y sort
    while(bandera):                        #modifica la lista original ordenandola
        num_rand = randint(1,10)
        if(num_rand not in lista_ejer_3):
            lista_ejer_3.append(num_rand)
            bandera = False
    bandera = True    

print(f"La lista randomica original es: {lista_ejer_3}")
lista_ejer_3.reverse()
print(f"La lista en orden inverso es: {lista_ejer_3}", end= '\n\n')
'''Fin de ejercicio 3'''
#-------------------------------
#-------------------------------PARON PARA ENTENDER BUCLE FOR POR COMPLETO
    #Crear una algoritmon tal que reciva num para una lista y los devuelva invertidos 
lista_for = []
print("Lista de 5 elementos", end= '\n')
for i in range(1,6):
    lista_for.append(int(input(f"Ingrese el elemento nr {i}:")))
#Forma 1
print("Forma 1 para resolver:")
for i in range(len(lista_for) - 1, -1 , -1):#Mi for arranca en longuitud de la lista menos 1, hasta 0 y decrementa 1
    print(lista_for[i], end= " ; ")   
#Forma 2
print()
print("Forma 2 para resolver:")
for i in range(1, len(lista_for) + 1):#Mi for usa la propiedad "-i" que va mostrando elemt desde el final al inicio
    print(lista_for[-i], end= " ; ") 
    #Fin del ejercicio sobre el uso de "For"
#-------------------------------
'''Ejercicio 4'''
print()
#Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, Física, 
# Química, Historia y Lengua) en una lista, pregunte al usuario la nota que ha sacado en cada asignatura 
# y elimine de la lista las asignaturas aprobadas. Al final el programa debe mostrar por pantalla las 
# asignaturas que el usuario tiene que repetir.
materias = ['matematica', 'fisica', 'quimica', 'historia', 'lengua']
materias_reprob = []
for i in range(5):
    nota = int(input(f"Ingrese la nota de {materias[i]} "))
    if (nota < 51):
        materias_reprob.append(materias[i])
print("Las materias a recursar son:" + str(materias_reprob))
'''Fin de ejercicio 4'''
#--------------------------
'''Ejercicio 5'''
print()
#Escribir un programa que almacene el abecedario en una lista, elimine de la lista las letras que 
# ocupen posiciones múltiplos de 3, y muestre por pantalla la lista resultante.
lista_ejer_5 = [chr(i) for i in range(ord('A') , ord('Z') + 1)] #longitud de mi lista 26
mult = 24
while (mult > 0 ):
    lista_ejer_5.pop(mult)
    mult -= 3
print("Lista resultado" + str(lista_ejer_5))
'''Fin de ejercicio 5'''
#--------------------------
'''Ejercicio 6'''
print()
#Escribir un programa que pida al usuario una palabra y muestre por pantalla si es un palíndromo.
lista_ejer_6 = list(input("Ingrese una palabra: "))
list_auxi = lista_ejer_6.copy() # Cuando yo pongo " = " en vez de "copy" lo que hago es copiar la ruta de 
list_auxi.reverse()           # en la memoria por ende ambos apuntan a la misma direccion en memoria
if (lista_ejer_6 == list_auxi): #y si yo modifico uno de ellos eso le afectara al otro ya que son la misma cosa
    print(f"La palabra { ''.join(lista_ejer_6)} Si es Palindrome")
else:
    print(f"La palabra { ''.join(lista_ejer_6)} No es Palindrome")
'''Fin de ejercicio 6'''
#--------------------------
'''Ejercicio 7'''
#Escribir un programa que pida al usuario una palabra y muestre por pantalla el número de veces que
# contiene cada vocal.
vocales = ['a', 'e', 'i', 'o', 'u']
lista_ejer_7 = list(input("Ingrese una la palabra "))
for i  in range(5):
    if (vocales[i] in lista_ejer_7) :
        print(f"La vocal {vocales[i]} se repite {lista_ejer_7.count(vocales[i])} veces")
'''Fin de ejercicio 7'''
#--------------------------
'''Ejercicio 8'''
print()
#Escribir un programa que almacene en una lista los siguientes precios, 50, 75, 46, 22, 80, 65, 8, 
# y muestre por pantalla el menor y el mayor de los precios.
"""Como lo hace un senior:
prices = [50, 75, 46, 22, 80, 65, 8]
min = max = prices[0]
for price in prices:
    if price < min:
        min = price
    elif price > max:
        max = price 
print("El mínimo es " + str(min)) 
print("El máximo es " + str(max))
"""
lista_ejer_8 =[ 50, 75, 46, 22, 80, 65, 8 ]
for i in range(2):
    num_selec = lista_ejer_8[0]
    if i == 0:
        for j in lista_ejer_8:
            if j > num_selec :
                num_selec = j
        print(f"El numero mayor es { num_selec}")
    else:
        for j in lista_ejer_8:
            if j < num_selec :
                num_selec = j
        print(f"El numero menor es { num_selec}")
'''Fin de ejercicio 8'''
#--------------------------
'''Ejercicio 9'''
#Escribir un programa que almacene los vectores (1,2,3) y (-1,0,2) en dos listas y muestre por 
# pantalla su producto escalar.
vector_1 = [1,2,3]
vector_2 = [-1,0,2]
result = 0
for i in range(3):
    result = result + (vector_1[i] * vector_2[i])
print(f"El producto escalar de {vector_1} por {vector_2} da {result}")
'''Fin de ejercicio 9'''
#--------------------------
'''Ejercicio 10'''
#Escribir un programa que almacene las matrices en una lista y muestre por pantalla su producto.
#Nota: Para representar matrices mediante listas usar listas anidadas, representando cada vector 
# fila en una lista.
m1 = [
    [1,2,3],
    [4,5,6] 
]
m2 = [
    [-1,0],
    [0,1],
    [1,1]
]
list_fila = []
m_result =[]
for i in range(2):    
    for k in range(2):
        result_ejer_10 = 0
        for j in range(3):
            result_ejer_10 = result_ejer_10 + (m1[i][j] * m2[j][k])
        list_fila.append(result_ejer_10)
    m_result.append(list_fila.copy())#NOTA IMPORTANTE cuando yo agrego una lista a otra con el metodo append, esta ultima lo que hace
    list_fila.clear()                # en realidad es apuntar a la misma direccion de memoria por ende cuando borro "list_fila.clear()"
for i in range(2):                   # lo que pasa es que tambien se va a borrar en "m_result"  ya "m_result" referencia a lo que hay
    print(m_result[i])               # en list_fila y cuando yo borro esto ultimo eso tambien ocurre en m_result
'''Fin de ejercicio 10'''












