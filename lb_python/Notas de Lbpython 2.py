#------------USO DE CACHING PARA FUNCIONES
#El uso de caching lo que hace es que almacena en un supuesto cache valores que devuelve la funcion dados ciertos
# parametros, para que de esa manera nosotros al volver a llamar a la funcion con esos parametros el tiempo de 
# ejecucion sea menos ya que se supone que almacenamos el return para la funcion con esos parametros
#Con caching
def fibonacci (indice, cache = {}):
    if indice not in cache:        
        if indice == 1:
            cache[indice] = 0
            return cache[indice]
        elif indice == 2:
            cache[indice] = 1
            return cache[indice]
        else:
            cache[indice] = fibonacci(indice-1) + fibonacci(indice-2)
            return cache[indice]
    return cache[indice]

print(fibonacci(35))
# 5702887
#Sin caching
def fibonacci_1 (indice):
    if indice == 1:
        return 0
    elif indice == 2:
        return 1
    else:
        return fibonacci_1(indice-1) + fibonacci_1(indice-2)

print(fibonacci_1(35))    
#--------OTRA FORMA DE HACER CACHING ES USANDO EL METODO "lru_cache" del modulo functools
from functools import lru_cache as cache
@cache(maxsize=32) #Usando maxsize podemos decir cuantos valores queremos almacenar 
def fibonacci_1 (indice):
    if indice == 1:
        return 0
    elif indice == 2:
        return 1
    else:
        return fibonacci_1(indice-1) + fibonacci_1(indice-2)

print(fibonacci_1(36))    
print(fibonacci_1(36))
fibonacci_1.cache_clear() #Para borrar el cache simplemente hacemos uso de "nombre_funcion.cache_clear"
#-------fin
#-------------PROGRAMACION FUNCIONAL USO DE REDUCE 
#Al usar reduce tenemos que saber que la funcion a la cual llamaremos tiene que tener dor parametros
# uno es el acumulador y otro representa los elementos de la secuencia
#Sintaxis
# reduce("funcion con 2 parametros","iterable sea lista,diccionario,tuplas", "valor de inicio del acumulador")
from functools import reduce as r
print(r(lambda factorial,num: factorial*num, [i for i in range(2,int(input('Ingrese un num ')) + 1)], 1))
#---MAS SOBRE LA FUNCION REDUCE y que pasa si yo no inicio el valor predefinido en reduce?
# La respuesta es que toma dos valores de la lista uno para result y otro para num por ende solo se llama a la funcion 9 veces
# Pero si yo inicializo el valor de reduce(suma, lista, 0) entonces la primera llamada solo toma un valor de la lista ya que
# el valor de result es 0 debido a reduce, por ende en este caso se llamaria a la funcion 10 veces
from functools import reduce as r
def suma(result,num, cont = []):
    cont.append(1)
    print(f"llamada num {sum(cont)}")    
    return result + num
print(r(suma, [i for i in range(1,int(input("Ingrese un numero ")) + 1)])) # Al no darle un valor incial al primer argumento "result"
print(sum([i for i in range(1,11)]))                                       # con la funcion reduce("funcion","iterable","valor incial")
                                                                           # la funcion reduce envia a "result" el primer elemento de
                                                                           # de la lista y luego a "num" el segundo elemento por ende
                                                                           # la primera llamada a suma es la unica toma dos element de 
                                                                           # la lista
#-------------WALRUS asignacion y impresion de datos en pantalla
print(edad := input('Ingrese su edad: '))# aqui usamos walrus asignando un str a la var "edad", pero a su vez podemos imprimir
                                         # en pantalla lo que trae la var "edad" al mismo tiempo
#-----fin
#------COMO VER LA CLASE DE UNA INSTANCIA: "type(self).__name__"----fin
#-------------Uso del TRY EXCEPT para los errores
# El bloque dentro del try es el posible codigo que nos puede dar error, si llega a haber algun fallo, el bloque
# except se ejecutara para hacernos saber de que fallo el codigo anterior, si No llegara a haber un fallo dentro
# de "try", se ejecutara el codigo dentro de "else" 
try:
    a = int(input("Ingrese a "))
    b = int(input("Ingrese b "))
    print(a/b)
except Exception as e: # "Exception" es la clase principal de las que heredan todos los errores y con type(e) podemos ver q error es
    print(f"{type(e)} No se puede dividir por cero")
else:
    print("division exitosa!!")
#---fin
#-----------USO DEL ASSERT PARA VERIFICAR UNA CONDICION
#El uso de assert es para verificar una condicion bool, la cual si retorna false provocara la excepcion assert y DETENDRA el programa
# podemos pasarle un segundo argumento que seria el texto que queremos mostrar si la expresion bool es falsa
# Hay que tener cuidado con la sintaxis de "assert" ya que no todo va dentro de parentesis, la forma correcta seria la sgte:
# assert(condicion bool), "texto para mostrar en pantalla si ocurre la excepcion"
# Cuando ocurre la excepcion la terminal muestra:
#------Terminal
# File "tu_archivo.py", line X, in <module>
    # assert b != 0, 'No se puede dividir por cero!!'
# AssertionError: No se puede dividir por cero!!
#------fin Terminal
# En esta salida, la traza de la excepción te indicará en qué archivo (tu_archivo.py), en qué línea (line X), y en qué contexto 
# ocurrió el AssertionError. Además, se mostrará el mensaje asociado al assert ("No se puede dividir por cero!!").
def division (a,b):
    assert(b != 0), 'No se puede dividir por cero!!'
    return a/b

print(division(10,0))
#---fin
#-----------Script en python
#Un "script" en el contexto de programación generalmente se refiere a un archivo que contiene código 
# ejecutable. 
# En el contexto de Python, un script es simplemente un archivo de código fuente que contiene instrucciones 
# que pueden ser ejecutadas por el intérprete de Python. Este archivo podría contener un conjunto de funciones,
# clases o simplemente un conjunto de instrucciones que realizan alguna tarea específica.
#---fin
#------------USO DEL MODULO UNITTEST PARA TESTEAR UNA FUNCION CON VARIOS METODOS
#Creamos una clase Test<NombreDeLoQueSePrueba> que hereda de unittest.TestCase.
#Definimos varios tests como métodos de la clase, usando test_<NombreDelTest> para nombrarlos.
#En cada test ejecutamos las comprobaciones necesarias, usando self.assertEqual en vez de assert, 
#pero su comportamiento es totalmente análogo.
from File_Practica.funciones import media as calcula_media
import unittest 
class TestCalculaMedia(unittest.TestCase):
    def test_1(self):
        resultado = calcula_media([10, 10, 10])
        self.assertEqual(resultado, 2)

    def test_2(self):
        resultado = calcula_media([5, 3, 4])
        self.assertEqual(resultado, 4)
if __name__ == '__main__':#el test solo se ejecutara si el name de este script es el name principal 
    unittest.main()#Para activar el test usamos "unittest.main()"
#------NOTA PRINCIPAL SOBRE USO DE IF __name__ == '__main_':
# lo que se encuentre dentro del if no se podra importar desde otro script, es decir si nosotros importamos
# este archivo desde otro script y buscamos la funcion pepito para usarla y si pepito esta dentro del if
# no se podra acceder desde otro modulo solo la podremos usar si el modulo de pepito es el script principal
#--------NOTAS SOBRE FICHEROS Y DIRECOTIROS CON FUNCIONES DEL MODULO "OS"
#---OPERACIONES CON FICHEROS

# os.rename(ruta1, ruta2) : Renombra y mueve el fichero de la ruta ruta1 a la ruta ruta2.
# os.remove(ruta) : Borra el fichero de la ruta ruta.
# os.path.isfile(ruta) : Devuelve True si existe un fichero en la ruta ruta y False en caso contrario.

#---OPERACIONES CON DIRECTORIOS

# os.listdir(ruta) : Devuelve una lista con los ficheros y directiorios contenidos en la ruta ruta.
# os.mkdir(ruta) : Crea un nuevo directorio en la ruta ruta.
# os.chdir(ruta) : Cambia el directorio actual al indicado por la ruta ruta.
# os.getcwd() : Devuelve una cadena con la ruta del directorio actual.
# os.rmdir(ruta) : Borra el directorio de la ruta ruta, siempre y cuando esté vacío.

#---ABRIR UN FICHERO DE INTERNET
from urllib import request
f = request.urlopen('https://raw.githubusercontent.com/asalber/asalber.github.io/master/README.md')
print(f.read())
#----fin







