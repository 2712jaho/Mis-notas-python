#---------------------------------------------------------------------
# Vamos a crear una clase llamada Persona. Sus atributos son: nombre, edad y DNI. 
# Construye los siguientes métodos para la clase:
''' Un constructor, donde los datos pueden estar vacíos.
    Los setters y getters para cada uno de los atributos. Hay que validar las entradas de datos.
    Mostrar(): Muestra los datos de la persona.
    esMayorDeEdad(): Devuelve un valor lógico indicando si es mayor de edad.'''
class Persona:
    def __init__(self, nombre = "", edad = 0, dni = 0):
        self.__nombre = nombre
        self.__edad = edad
        self.__dni = dni
    @property
    def nombre(self):        
        return self.__nombre
    
    @nombre.setter
    def nombre(self,nuevo_nombre):
        if nuevo_nombre != "":
            self.__nombre = nuevo_nombre
        else:
            print("Error vuelva a intentar")
    
    @property
    def edad(self):
        return self.__edad
    
    @edad.setter
    def edad(self,nueva_edad ):
        if nueva_edad > 0:
            self.__edad = nueva_edad
        else:
            print("Error vuelva a intentar")
    
    @property
    def dni(self):
        return self.__dni
    
    @dni.setter
    def dni(self,nuevo_dni ):
        if len(str(nuevo_dni)) == 8: #95578533
            self.__dni = nuevo_dni
        else:
            print("Error vuelva a intentar!!")
            
    def mostrar(self):        
        datos = {}
        datos['Nombre '] = self.__nombre
        datos['Edad '] = self.__edad
        datos['Dni '] =  self.dni
        return datos
        
    def es_mayor_edad(self):
        return True if self.__edad > 17 else False
            
def getter(persona, instancias, indice):
    if indice == 1:
        return instancias[persona].nombre
    elif indice == 2:
        return instancias[persona].edad
    else:
        return instancias[persona].dni
def setter(persona, instancias, indice, nuevo_valor ):
    if indice == 1:
        instancias[persona].nombre = nuevo_valor        
    elif indice == 2:
        instancias[persona].edad = nuevo_valor
    else:
        instancias[persona].dni = nuevo_valor
    
def instanciar(nueva_persona, instancias):
    nombre = input("Introduce el nombre: ")
    while nombre == "":
        nombre = input("Vacio, introduce el nombre")    
    edad = int(input("Introduce la edad: "))
    while edad < 1:
        edad = int(input("Invalido, Introduce la edad: "))
    dni = int(input("Introduce el dni (8 digitos): "))
    while len(str(dni)) != 8:
        dni = int(input("Dni invalido, Introduce el dni (8 digitos): "))
    instancias[nueva_persona] = Persona(nombre, edad, dni)
    
def tabla():
    print("\n\t\t\t\tPrograma Persona\n\n" + "\t\tindice".ljust(20,' ') + "Operacion\n")
    print("\t\t1-".ljust(20,'.')+"Crear nuevo Objeto")
    print("\t\t2-".ljust(20,'.')+"Mostrar Instancias")
    print("\t\t3-".ljust(20,'.')+"Getter")
    print("\t\t4-".ljust(20,'.')+"Setter")
    print("\t\t5-".ljust(20,'.')+"mostrar datos")
    print("\t\t6-".ljust(20,'.')+"Mayoria de edad")
instancias = {}
while True:    
    tabla()
    indice = input("\nSeleccione un Indice --> ")    
    if indice == '1':
        nueva_persona = input("Ingrese el nombre de la nueva persona ")
        if nueva_persona in instancias:
            print(f"Invalido, La persona {nueva_persona} ya fue instanciada")
        else:            
            instanciar(nueva_persona, instancias)
            print("Persona creada con exito!!")
    elif indice == '2':
        print("listas de Objetos instanciados\n")
        for objeto in instancias:
            print(objeto)
        print()
    elif indice == '3':
        print("\n\t\tMostrar:\n" + "\n\t\t1-".ljust(8,' ') + "Nombre" + "\n\t\t2-".ljust(8,' ') + "Edad" + "\n\t\t3-".ljust(8,' ') + "Dni")
        sub_indice = int(input('Seleccione un indice: '))
        instancia = input("Ingrese el nombre de la instancia: ")
        dic_auxi = {1:"Nombre ", 2:"Edad ", 3:"Dni "}        
        print(f"{dic_auxi[sub_indice]}" + str(getter(instancia, instancias, sub_indice)))
    elif indice == "4":
        dic_auxi = {1:"Nombre ", 2:"Edad ", 3:"Dni "}
        print("\n\t\tSeleccione que va a cambiar:\n" + "\n\t\t1-".ljust(8,' ') + "Nombre" + "\n\t\t2-".ljust(8,' ') + "Edad" + "\n\t\t3-".ljust(8,' ') + "Dni")
        sub_indice = int(input('Seleccione un indice: '))
        if sub_indice != 1:
            nuevo_valor = int(input(f"Ingrese el nuevo valor de {dic_auxi[sub_indice]} "))
        else:
            nuevo_valor = input(f"Ingrese el nuevo valor de Nombre ")            
        instancia = input("Ingrese el nombre de la instancia: ")
        setter(instancia, instancias,sub_indice, nuevo_valor) 
        print("Nuevo valor del atributo guardado con exito!")
    elif indice == '5':
        instancia = input("Ingrese el nombre de la instancia: ")
        for indic3, valor in (instancias[instancia].mostrar()).items():
            print(f"{indic3}{valor}")
    elif indice == '6':
        instancia = input("Ingrese el nombre de la instancia: ")
        print(instancias[instancia].es_mayor_edad())                        
    if int(input("Presione 1 si desea continuar o 0 para salir ")) == 0:
        break
#--------------------------------------------------------------
# Realizar una clase que administre una agenda. Se debe almacenar para cada contacto el nombre, 
# el teléfono y el email. Además deberá mostrar un menú con las siguientes opciones

# Añadir contacto
# Lista de contactos
# Buscar contacto (mostrar sus atributos)
# Editar contacto
# Cerrar agenda
    
class agenda():
    def __init__(self, nombre, telefono, email):
        self.__nombre = nombre
        self.__telefono = telefono
        self.__email = email
        
    @property
    def nombre (self):
        return self.__nombre
    @nombre.setter
    def nombre (self, new_name):
        if new_name != "":
            self.__nombre = new_name
        else:
            print("ERROR, NO introdujo un nombre")
        
    @property
    def telefono (self):
        return self.__telefono
    @telefono.setter
    def telefono (self, new_telf):
        if len(str(new_telf)) == 8:
            self.__telefono = new_telf
        else:
            print("ERROR Numero invalido ")

    @property
    def email (self):
        return self.__email
    @email.setter
    def email (self, new_email):
        self.__email = new_email

contactos = {}
def instanciar (new_contacto, telf, email):
    if new_contacto in contactos:
        print("El contacto ya existe!")        
    else:
        contactos[new_contacto] = agenda(new_contacto, telf, email)
        print("Contacto creado con exito\n")
                
def get (contacto):
    if contacto in contactos:
        print(f"Nombre: {contacto}\nTelefono: {contactos[contacto].telefono}\nEmail: {contactos[contacto].email}\n")
    else:
        print("El contacto no esta en tu agenda")        

def set(contacto, indice, new_value):
    if contacto in contactos:
        if indice == "1":
            contactos[contacto].nombre = new_value
            print("Modificacion de nombre exitosa!")
        elif indice == "2":
            contactos[contacto].telefono = int(new_value)
            print("Modificacion de telefono exitosa!")
        elif indice == "3":
            contactos[contacto].email = new_value
            print("Modificacion de email exitosa!")
        else:
            print("ERROR, indice invalido")
    else:
        print(f'{contacto} no es un contacto de tu agenda')

while True:
    print("\n\t\tAGENDA")
    print("\t1- Añadir contacto\n\t2- Mostrar lista de contactos\n\t3- Buscar contacto\n\t4- Modificar contacto\n\t5- Cerrar agenda")
    indice = int(input("\nSeleccione una opcion "))
    if indice == 1:
        nombre = input("Añadiendo nuevo contacto\nIntroduzca su nombre: ")
        telefono = input("Introduzca su telefono: ")
        email = input("Introduzca su email: ")
        instanciar(nombre,telefono, email)
    elif indice == 2:
        cont = 0
        for clave in contactos:
            cont += 1
            print(f"{cont}- {clave}")
        print()
    elif indice == 3:
        get(input("Introduzca el nombre del contacto: "))
    elif indice == 4:        
        sub_indice = input("\n\t\tMODIFICACION\n\t1- Nombre\n\t2- Telefono\n\t3- Email\nSeleccione una opcion ")
        dic_auxi = {'1': 'Nombre', '2': 'Telefono', '3': 'Email'}
        nuevo_valor = input(f"Seleccione el nuevo valor del {dic_auxi[sub_indice]} ")
        nombre = input("Introduzca el nombre del contacto ")
        set(nombre, sub_indice, nuevo_valor)
    else: 
        print("Cerrando agenda....")
        break
#--------------------------------------------------------
#En un banco tienen clientes que pueden hacer depósitos y extracciones de dinero. 
#El banco requiere también al final del día calcular la cantidad de dinero que se ha depositado.
#Se deberán crear dos clases, la clase cliente y la clase banco. 
#La clase cliente tendrá los atributos nombre y cantidad y los métodos __init__, depositar, extraer, mostrar_total_de_cuenta
#La clase banco tendrá como atributos 3 objetos de la clase cliente y los métodos __init__, operar y deposito_total.

class cliente ():
    def __init__(self):
        print("Creando cliente...")
        self.__nombre = input("Ingrese el nombre del cliente ")
        self.__cantidad = float(input("Ingrese la cantidad de dinero en su cuenta "))
    
    @property
    def nombre(self):
        return self.__nombre    
                #Notese que no tengo el decorador .setter ya que desde afuera yo no modificare ninguno de los
                # atributos nombre/cantidad solo modificare cantidad desde metodos de esta clase 
    @property
    def cantidad (self): 
        return self.__cantidad

    def depositar(self):
        deposito = float(input("Ingrese la cantidad a depositar "))    
        self.__cantidad = self.__cantidad + deposito
        print(f"Se deposito {deposito}, tu cuenta actualmente tiene {self.__cantidad}")
        return deposito

    def extraer (self):
        sacar = float(input("Ingrese la cantidad a extraer de la cuenta "))
        if sacar <= self.__cantidad:
            self.__cantidad = self.__cantidad - sacar
            print(f"Se extrajo {sacar}, tu cuenta actualmente tiene {self.__cantidad}")
        else:
            print("No se puede extraer mas de lo que se encuentra depositado")

    def mostrar_total (self):
        print(f"Tienes {self.__cantidad} en tu cuenta")
    
class Banco ():
    def __init__(self):
        self.cliente_1 = cliente()
        self.cliente_2 = cliente()
        self.cliente_3 = cliente()      
        self.Clientes = [self.cliente_1.nombre, self.cliente_2.nombre, self.cliente_3.nombre] 
        self.deposito_total = 0 
    
    def operaciones (self):
        print("\t\tClientes\n")
        for indice,valor in enumerate(self.Clientes):
            print(f"\t{indice + 1}- {valor}")
        indice_cliente = int(input("\nSeleccione un cliente: "))  
        if indice_cliente == 1 :
            cliente_seleccionado = self.cliente_1
        elif indice_cliente == 2:
            cliente_seleccionado = self.cliente_2
        elif indice_cliente == 3:
            cliente_seleccionado = self.cliente_3
        print(f"\n\t\tDatos\n\tNombre: {cliente_seleccionado.nombre}\n\tDinero disponible: {cliente_seleccionado.cantidad}")
        print("\n\t\tOperaciones\n")
        print("\t1- Extrarer dinero\n\t2- Depositar dinero\n\t3- Mostrar total\n\t4- Salir\n")
        indice = int(input("Seleccione un indice: "));print()        
        if indice == 1:
            cliente_seleccionado.extraer()
        elif indice ==  2:
            self.deposito_total += cliente_seleccionado.depositar()
        elif indice == 3:
            cliente_seleccionado.mostrar_total()
        elif indice == 4:
            print(f"El total actual del banco es de {self.cliente_1.cantidad + self.cliente_2.cantidad + self.cliente_3.cantidad}")
            print(f"El total depositado el dia de hoy es de {self.deposito_total}")
            exit()
        self.operaciones()
        
                
clientes = Banco()
clientes.operaciones()
#---------------------------------------------------------------------------                






    
    