nro_cuenta = 1234
#DECORADOR QUE VALIDA UNA CONTRASEÑA PARA ACCEDER A UNA FUNCION 
def login (password):
    def decorador (funcion):
        def funcion_decorada (*args, **kwargs):
            cont = 5
            while (cont >= 1):
                if int(input("Ingrese la contraseña ")) == int(password):
                    funcion(*args, **kwargs)
                    break
                else:
                    cont -= 1
                    print(f'Contraseña incorrecta, quedan {cont} intentos')
            if cont == 0:
                print('Cuenta bloqueada')
        return funcion_decorada
    return decorador
    
@login('1111')
def cuenta_bancaria():
    print("El dinero en su cuenta de banco es de 1700 Bs")

cuenta_bancaria()

