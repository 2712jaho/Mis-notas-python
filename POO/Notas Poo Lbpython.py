#---------Aprendiendo HERENCIA EN POO Y USO DE "super()" PARA LLAMAR METODOS DE LA CLASE MADRE
class Media:
    def __init__(self, nombre, suerte):
        self.nombre = nombre
        self.suerte = suerte
        self.futuro = 'Prometedor'
    def datos(self):
        print(f"Datos:\nNombre: {self.nombre} \nClase: {self.suerte}")
    def Futuro_(self, dinero = "0"):        
        self.dinero = dinero
        print(f'Su futuro es {self.futuro} ya que tiene {self.dinero}')
                
ciudadano = Media('pedro', 'Adinerada')
ciudadano.datos()
ciudadano.Futuro_()
class Media_baja(Media):#para HEREDAR una clase madre simplemente al crear la clase hijo colocamos "(name madre)"
    def __init__(self, nombre, suerte):
        super().__init__(nombre, suerte)#Para heredar metodos usamos la palabra reservada "super().nombre metodo"        
        self.futuro = 'Casi prometedor'

    # def Futuro_(self, dinero):
    #     agregando codigo adicional...    
    #     return super().Futuro_(dinero)
ciudadano_poor = Media_baja('pedro', 'pal culo')
ciudadano_poor.Futuro_('90')#NOTA: se puede acceder desde una instancia de una clase hija directamente al metodo
                            # de la clase madre o tambien podemos crear un metodo en la clase hija con el mismo
                            # nombre que el de la clase madre "21-22" y llamarlo desde el metodo de la calse hija
                            # esto es util cuando queremos modificar o agregar codigo al metodo heredado
#NOTAS:
# 1 cuando creamos una hija si y no colocamos atributos y aparte llamamos a los atributos de la clase madre
# esto me dara error ya que nosotros no llamamos al metodo de la clase madre que me crea esos atributos
# por ende es como si no existieran en la clase hija

# 2 cuando llamemos a un metodo en la clase hija con "super()" y si dicho metodo tiene en su bloque de codigo
# la creacion de atributos estos se crearan para la clase hija de manera automatica 
ciudadano_poor = Media_baja('mateo', 'regular')
ciudadano_poor.datos()
# print(ciudadano_poor.futuro)
ciudadano_poor.Futuro_()
#---------------------------------DATO int y float
print(1.5e2)#la sgte notacion 1.5e2 hace referencia a: 1.5 * 10**2
#multiplicamos al valor que es antecedente a la letra e por "10" elevado a el posterior numero despues de "e"
print(int(23.9))#salida 23 ya que al converitir un float a int este truncara la parte entera borrando los decimales
#-------------------------------------------------------
#---------------------------TIPOS DE METODOS QUE SE UTILIZAN CONOCIENDO DECORADORES
#SON 3:
# 1)METODOS INSTANCIAS estan los metodos de instancias que son los mas usuales los cuales son llamados con una instacia
# y pueden modificar los atributos de un objeto y esos metodos tienen como primer parametro "self"
# En vista a esto, los métodos de instancia:
# Pueden acceder y modificar los atributos del objeto.
# Pueden acceder a otros métodos.
# Dado que desde el objeto self se puede acceder a la clase con ` self.class`, 
# también pueden modificar el estado de la clase

#2)METODOS DE CLASES son metodos que en ves de recibir una instancia como parametros, reciven a la propia clase
# se usan generalmente para modificar los atributos o estados de la clase ya que recordemos que hay 2 tipos de
# estados "atributos de instancias y de clases"
# Por lo tanto, los métodos de clase:
# No pueden acceder a los atributos de la instancia.
# Pero si pueden modificar los atributos de la clase.

#3)METODOS ESTATICOS no reciven como parametro ni instancias ni la propia clase por ende no pueden modificar
# los estados de la clase ni de las instancias y solo se limitan a ser funciones con argumentos normales 
# solo que estas se encuentran dentro de una clase
#-----------------------------------------------------------
#type(self).__name__ --->Para saber el nombre de la clase a la que pertence mi instancia
#------------------------- Verificacion para saber si una clase es hija de otra
# De hecho podemos ver como efectivamente la clase Perro es la hija de Animal usando __bases__
# print(Perro.__bases__)
# (<class '__main__.Animal'>,)
#-----------------------Verificacion para saber cuantas clases hijas vienen de una clase madre
# De manera similar podemos ver que clases descienden de una en concreto con __subclasses__.
# print(Animal.__subclasses__())
# [<class '__main__.Perro'>]
#------------------------------------------HERENCIA Y QUE PASAN SI MI CLASE ES HIJA DE VARIAS CLASES
#supongamos que tenemos la clase hija que proviene de varias clases madres y todas ellas tiene la misma funcion
# "saludar", entonces cuando yo llame a super().saludar, a que metodo me llamaria?
class Ingles():
    def saludar (self):
        print("Hi")
        
class Espanol():
    def saludar (self):
        print("Hola")
        
class chino():
    def saludar(self):
        print("konichiua")

class bilingue(Ingles, Espanol, chino):#Pues bien al metodo que llamaria seria al de la clase mas a la izquierda
    def llamada_para_saludar(self):        
        super().saludar()
    
print(bilingue.mro()) #devuelve una lista con el orden de prioridades de llamadas para la clase bilingue
persona_bilingue = bilingue()
persona_bilingue.llamada_para_saludar() #salida: "hi" ya que es la clase madre mas a la izquierda que hay
#----------------FIN
#--------------------------APRENDIENDO USO DEL DECORADOR "PROPERTY" PARA CONVERTIR UN METODO EN UN ATRIBUTO
class Clase:
    def __init__(self, mi_atributo):
        self.__mi_atributo = mi_atributo # "__" antes de "mi_atrubuto", lo hace inaccecible desde afuera de la clase

    @property
    def mi_atributo(self):        
        return self.__mi_atributo
mi_clase = Clase("valor_atributo")
mi_clase.mi_atributo #Notese que cuando llamamos a mi metodo "mi_atributo" que ya no es un metodo sino mas
# bien es un atributo lo hacemos sin "()" ya que si usamos los "()" se interpretaria como llamar a un metodo
# el cual no existe
# EL SENTIDO DE todo esto esta relacionado con "ENCAPSULAMIENTO", a veces es necesario impedir la modificaciones
# de atributos de manera externa, tambien colocar "__" antes de un atributo como en el caso de __init__
# significa que no puede ser accedido desde afuera de la clase y esta como privado 
#-----------------------LEER TOD0 SOBRE "PROPERTY" Y TAMBIEN EL DECORADOR SETTER 
#---Fin
#------------------LLAMANDO A ATRIBUTOS GLOBALES DENTRO DE UN METODO 
class MiClase:
    atributo_de_clase = 10
    def mi_metodo(self):
        # Acceder al atributo de clase utilizando cls
        print(f"Atributo de clase: {self.__class__.atributo_de_clase}")#Podemos hacerlo de esta forma, 
# Crear una instancia de la clase                                      # como tambien podemos hacerlo usando
objeto = MiClase()                                                     # directamente el nombre de la clase
# Llamar al método que accede al atributo de clase                     # "MiClase.atributo_de_clase"
objeto.mi_metodo()
#---------Verificar si una clase es heredada de otra con issubclass(clase_hija,clase_padre)
#---------------CLASE ABSTRACTA  -------INTERFACES FORMALES
#Una clase abstracta es aquella que solo tiene metodos abstractos sin implementacion por ende dicha clase 
# no puede ser instanciada mas bien es una especie de contrato para las clases que las hereden ya que dichas 
# clases hijas deben cumplir el contrato de la clase abstracta implementando todos y cada uno de sus metodos 
# sino cuando instanciemos un objeto de la clase hija nos daria error!!
from abc import ABC
from abc import abstractmethod
class contrato (ABC):
    
    @abstractmethod
    def metodo_a_implementar(self):
        pass
    
    @abstractmethod
    def otro_metodo_a_implementar(self):
        pass

class clase_hija (contrato):
    def __init__(self) -> None:
        pass
    
    def metodo_a_implementar(self):
        pass #Introduciendo codigo para respetar el contrato 
    
#------COMBINANDO EL METODO ASBTRACTO CON LOS TIPOS DE METODOS ANTES VISTOS "classmethod" y "staticmethod"
# es posible combinar el decorador @abstractmethod con los decoradores @classmethod y @staticmethod 
# que ya vimos anteriormente. Nótese que @abstractmethod debe ser usado siempre justo antes del método.
class Clase(ABC):
    @classmethod
    @abstractmethod
    def metodo_abstracto_de_clase(cls):
        pass
    @staticmethod
    @abstractmethod
    def metodo_abstracto_estatico():
        pass
    @property   #Tambien podemos usarlo con el decorador property para obligar a crear atributos especificos
    @abstractmethod
    def metodo_abstracto_propiedad(self):
        pass
#-----fin
#---------------CLASE VIRTUAL/ABSTRACTA USANDO "REGISTER"
#El metodo register logra que una clase concreta cumpla la implementacion de la interfaz es decir cumpla el
# contrato de la clase abstracta y de esta manera sea aceptada como su hija SIN LA NECESIDAD de que implemente
# sus metodos abstractos. te dejo la def de chatgpt:
# En otras palabras, register indica que la clase concreta cumple con los requisitos para ser considerada 
# una instancia de la clase abstracta, pero no impone la obligación de proporcionar implementaciones 
# concretas para los métodos abstractos. Esto significa que al utilizar register, puedes hacer que una 
# clase existente sea reconocida como una implementación válida de una clase abstracta sin tener que 
# odificar la implementación de la clase existente para cumplir con todos los métodos abstractos de la 
# clase abstracta.
from abc import ABC 
from abc import abstractmethod

class clase_virtual (ABC):
    
    @abstractmethod
    def metodo_virtual(self):
        pass
    
class clase ():
    def __init__(self) -> None:
        print('instanciando la clase')
        
clase_virtual.register(clase)

mi_clase = clase()
print(issubclass(clase,clase_virtual)) #Logramos que la clase "clase" cumpla la implementacion de la interfaz 
                                       # y sea considerada como hija de "clase_virtual" sin la necesidad de que
                                       # implemente los metodos abstractos 
#---------fin
#-----------USO DEL ATRIBUTO ESPECIAL "__dict__" que nos devuelve un diccionario {atributo:valor,..}
#Este atributo permite que dada una instancia de una clase, nosotros podamos ver sus atributos junto con
# sus respectivos valores en forma de diccionario
#--Nota sobre nombrar un atributo privado usando "__"
#Internamente cuando usamos "__" delante de un atributo de instancia lo que hace python es que renombra a ese
# atributo con _nameClase__nameAtributo, es decir que no es que prohibe su acceso, sino hace que sea mas 
# complicado acceder a el






