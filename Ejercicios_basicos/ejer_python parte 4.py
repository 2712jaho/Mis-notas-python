#----------------------------------------------------------------
# from random import randint 
# def descuento_random ():
#     num_aletorio = randint(1,5)
#     if(num_aletorio == 1):
#         return ['Blanco']
#     elif (num_aletorio == 2):
#         return ['Roja', 10]
#     elif (num_aletorio == 3):
#         return [ 'Azul', 20]
#     elif (num_aletorio == 4):
#         return ['Verde', 25]
#     elif (num_aletorio == 5):
#         return['Amarilla', 50]
    
# while (True):
#     monto = float(input("Introduzca la cantidad total de la compra "))
#     if (monto < 100):
#         print("Su gasto NO iguala o supera los 100, NO participa en la promocion")        
#     else:
#         print("Su gasto SI iguala o supera los 100, SI participa en la promocion")
#         print("\t\tColor\t\t\t\tDescuento", end='\n\n')
#         print("\t     ", end='')
#         print("Bola Blanca".ljust(35,' '), end='');print("No tiene")
#         print("\t     ", end='')
#         print("Bola Roja".ljust(33,' '), end='');print("10 por ciento")
#         print("\t     ", end='')
#         print("Bola Azul".ljust(33,' '), end='');print("20 por ciento")
#         print("\t     ", end='')
#         print("Bola Verde".ljust(33,' '), end='');print("25 por ciento")
#         print("\t     ", end='')
#         print("Bola Amarilla".ljust(33,' '), end='');print("50 por ciento")
#         print()
#         result_promocion = descuento_random()
#         if len(result_promocion) == 1 :
#             print(f"Aleatoriamente usted obtuvo una Bola {result_promocion[0]} , por lo tanto no tiene descuento")
#             print(f"Su monto a pagar es {monto}")
#         else:
#             print(f"Aleatoriamente usted obtuvo una Bola {result_promocion[0]}")
#             print(f"Felicidades, ha ganado un descuento de {result_promocion[1]} porciento")
#             print(f"Su nuevo monto a pagar es {round(monto - (monto*(result_promocion[1]/100)),2)}")
#     if input("Si desea salir presione 1 o de lo contrario otro numero ") == '1':
#         break
#-------------------------------------------------------------------            
# def sistema (codigo_produc):
#     if codigo_produc == 1 :
#         return ['Camisa', 80]
#     elif codigo_produc == 2:
#         return ['Cinturon', 40]
#     elif codigo_produc == 3:
#         return [ 'Zapatos', 350]
#     elif codigo_produc == 4:
#         return [ 'Pantalon', 100]
#     elif codigo_produc == 5:
#         return ['Calcetines', 10]
#     elif codigo_produc == 6:
#         return ['Faldas', 50]
#     elif codigo_produc == 7:
#         return ['Gorras', 10]
#     elif codigo_produc == 8: 
#         return ['Sueter', 200]
#     elif codigo_produc == 9:
#         return ['Corbata', 35]
#     elif codigo_produc == 10:
#         return ['Chaqueta', 250]
    
# print("Elija el producto deseado")
# mostrar = {'Camisa': '1', 'Cinturon': '2', 'Zapatos': '3', 'Pantalon': '4', 'Calcetines': '5', 'Faldas': '6', 'Gorras': '7', 'Sueter': '8', 'Corbata': '9', 'Chaqueta': '10'}
# print("\t\t\tPROCUTO\t\t\t\tCODIGO\n\t\t\t", end='') 
# for producto, codigo in mostrar.items():
#     print(producto.ljust(34,'.') + codigo + "\n\t\t\t", end='')
# print()
# total = {}
# while True:
#     datos_producto = sistema(int(input("Introduzca el Codigo: ")))#[nombre, precio]
#     print(f"El precio de {datos_producto[0]} es: {datos_producto[1]}.00 Bs")
#     unidades = int(input('Introduzca el numero de unidades: '))
#     if total.get(datos_producto[0], '0') == '0':
#         total[datos_producto[0]] = datos_producto[1]*unidades
#     else:
#         total[datos_producto[0]] = total[datos_producto[0]] + (datos_producto[1]* unidades)
#     if input("Si desea continuar agregando cosas al carrito presione 1 caso contrario presione 0 ") == '0':
#         break
# print("Factura de la compra:")
# for nombre_pro, valor_total in total.items():
#     print(f"El total de {nombre_pro} es".ljust(35,' ') + f"{valor_total}.00 Bs")
# print(f"El total de todo es ".ljust(35,' ') + f"{sum(list(total.values()))}.00 Bs")
#----------------------------------------------------
# print("\tCATEGORIA\t\tPRECIO\t\tCODIGO\t\tRECARGO/DIA DE ATRASO")
# mostrar = {'Favoritos': ['$2.50', '1', '$0.50'], 'Nuevos': ['$3.00', '2', '$0.75'], 'Estrenos': ['$3.50', '3', '$1.00'], 'Super Estrenos': ['$4.00', '4', '$1.50']}
# for cat, lista in mostrar.items():
#     print(f"\t{cat}".ljust(25,' ') + f"{lista[0]}".ljust(18,' ') + f"{lista[1]}".ljust(22,' ') + f"{lista[2]}")
# datos = {'1': [2.50, 0.50], '2':[3, 0,75], '3':[3.50,1], '4':[4,1.50]}
# while True:
#     precio_recargo = datos[input("Ingrese el codigo de la categoria de la pelicula: ")]
#     recargo = int(input("Introduzca el numero de dias de atraso en la devolucion: "))
#     print(f"El total a pagar es de ${precio_recargo[0] + (precio_recargo[1] * recargo)} dolares")
#     if input("Si desea salir presione 1 o de lo contrario presione otro numero ") == '1':
#         break
#--------------------------------------------------------        
