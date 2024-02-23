#Crear una programa que tenga 3 listas "1" donde se encuentran los nombres de clientes del banco fie
# "2" con los apellidos de dichos clientes y "3" con el monto de dinero que tienen en el banco

with open(r"C:\Users\josealejandro\Documents\nombres.txt", 'r') as nombres:
    lista_nombres = nombres.readlines()
#['1.  Hugo \n'] asi se ve cada elemento de la lista nombres
for i in range(len(lista_nombres)):
    # lista_nombres[i] = (lista_nombres[i])[4:len(lista_nombres[i]) - 1]
    lista_nombres[i] = (lista_nombres[i])[4:]
    lista_nombres[i] = lista_nombres[i].strip()

with open(r"C:\Users\josealejandro\Documents\apellidos.txt", 'r') as apellidos:
    lista_apellidos = apellidos.readlines()
#['García\n'] asi se ve cada elemento de la lista apellidos
for j in range(len(lista_apellidos)-1):
#    lista_apellidos[j] = (lista_apellidos[j])[:len(lista_apellidos[j]) - 1]
   lista_apellidos[j] = lista_apellidos[j].strip()

with open(r"C:\Users\josealejandro\Documents\nr cuenta.txt", 'r') as nr_cuenta:
    lista_nr_cuenta = nr_cuenta.readlines()
#['738643\n'] asi se ve cada elemento de la lista nr de cuenta
for k in range(len(lista_nr_cuenta)):
    lista_nr_cuenta[k] = lista_nr_cuenta[k].strip()

lista_datos = list(zip(lista_nombres, lista_apellidos, lista_nr_cuenta))

for i in range(100):
    print(f"{i+1}- {(lista_datos[i][0]).ljust(15,' ')}{(lista_datos[i][1]).ljust(15,' ')}N° Cuenta {lista_datos[i][2]}")

    