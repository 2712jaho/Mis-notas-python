from random import randint as r
lista = [(r(1,100),r(1,100)) for _ in range(15)]
lista_result = [sum(tupla) for tupla in lista]
print(lista)
print(lista_result)
lista_result[3] = 0
lista_result[14] = 0
#Haciendo TESTING
def suma(tupla):
    return sum(tupla)

#testing
for i in range(len(lista)):
    try:    
        assert(suma(lista[i]) == lista_result[i])
    except Exception as e:
        print(f'La funcion suma fallo en {lista[i][0]} + {lista[i][1]} = {lista_result[i]}')
    else:
        print(f'test num {i + 1} pasado')



