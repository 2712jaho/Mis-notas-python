#----------------------------------------------------------------------
'''Ejercicio que dado una longitud me da esa cantidad en dig diferentes y luego yo tengo que 
adivinar el orde'''
# Dime la longitud de la cadena: 4
# Intenta adivinar la cadena: 1234
# Con 1234 has adivinado 1 valores. Intenta adivinar
# la cadena: 1243
# Con 1243 has adivinado 0 valores. Intenta adivinar
# la cadena: 1432
# Con 1432 has adivinado 2 valores. Intenta adivinar
# la cadena: 2431
# Con 2431 has adivinado 4 valores.
# Felicidades
# from random import randint as random
# long_candena = int(input("Ingrese la longitud de la cadena "))
# num_principal = []
# for i in range(long_candena):
#     while True:
#         num_random = random(1,long_candena)
#         if str(num_random) not in num_principal :
#             num_principal.append(str(num_random))
#             break
        
# def cant_acertaciones (num_generado, intento_usuario):# ambas son listas
#     acertaciones = 0
#     for num_1, num_2 in zip(num_generado, intento_usuario):
#         if num_1 == num_2 :
#             acertaciones += 1
#     return acertaciones

# while True:
#     intento_usuario = list(input("Intenta adivinar la cadena: "))
#     num_acertados = cant_acertaciones(num_principal, intento_usuario)
#     print(f"Con {''.join(intento_usuario)} has adivinado {num_acertados} valores")
#     if num_acertados == len(num_principal):
#         break
# print("Felicidades!!! ganasteee")
#------------------------------------------------------------

# Escribe un programa que pida dos palabras y diga si riman o no. Si coinciden
# las tres últimas letras tiene que decir que riman. Si coinciden sólo las dos
# últimas tiene que decir que riman un poco y si no, que no riman.

# def rimas (pal_1, pal_2):
#     indice = 0
#     band = True
#     cont_rimas = 0
#     while((band == True) and (indice < 3)):
#         if pal_1[indice] != pal_2[indice] :
#             band = False
#         else:
#             cont_rimas += 1
#             indice += 1
#     if cont_rimas == 3:
#         print("Riman completamente")
#     elif cont_rimas == 2 :
#         print("Riman un poco")
#     else:
#         print("No riman")
# pal_1 = list(input("Ingrese la primera palabra: "))[::-1]#Invierto la palabra "hola" -> "aloh"
# pal_2 = list(input("Ingrese la segunda palabra: "))[::-1]#invierto la palabra
# pal_1 = pal_1[0:3] #Recorto los 3 ultimos caracteres de la palabra "aloh" -> "alo"
# pal_2 = pal_2[0:3] #Recorto los 3 ultimos caracteres de la palabra

# rimas(pal_1, pal_2)
#-----------------------------------------------------------------------
# Has un programa que pida al usuario una cantidad de dolares, una tasa de interés y un numero de años. 
# Muestra por pantalla en cuanto se habrá convertido el capital inicial transcurridos esos años si cada 
# año se aplica la tasa de interés introducida.
# Recordar que un capital C dolares a un interés del x por cien durante n años se convierte en
# C * (1 + x/100)elevado a n (años). Probar el programa sabiendo que una cantidad de 10000 dolares al 4.5% de 
# interés anual se convierte en 24117.14 dolares al cabo de 20 años.

# capital = float(input("Ingrese su capital "))
# interes = (float(input("Ingrese una taza de interes ")))/100
# plazo = int(input("Ingrese el plazo en años "))
# print(f"El capital {capital}",end= ' ')
# for i in range(plazo):
#     capital = capital + capital*interes
# print(f"en {plazo} años con interes de {interes}% valdra {round(capital,2)} dolares")

