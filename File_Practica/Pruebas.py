# with open(r"C:\Users\josealejandro\Downloads\cotizacion.csv", 'r') as f:
#     lineas = f.read().split('\n')    
# for linea in lineas:
#     columna = linea.split(';')
#     for columnita in columna:
#         print(columnita.ljust(15,' '), end=' ')
#     print()
def funcion_generadora():
    yield [i for i in range(1,6)]
    yield 'segundo elemento, quedan 3'
    yield 'tercer elemento, quedan 2'
    yield 'cuarto elemento, quedan 1'
    yield 'quinto elemento, quedan 0'

iteradora = funcion_generadora()
# print(next(iteradora))
# print(next(iteradora))
# print(next(iteradora))
# print(next(iteradora))
# print(next(iteradora))
# cache = {}
# def verif_primo (num, cache):
#     if num not in cache :
#         for i in range(2,num):
#             if num % i == 0:
#                 cache[num] = False
#                 break
#             else:
#                 cache[num] = True
#     return cache[num]


def suma (num, lista = []):
    lista.append(num)
    return sum(lista)

print(suma(4))
print(suma(10,[60]))
print(suma(100))
print('hola mundo')




