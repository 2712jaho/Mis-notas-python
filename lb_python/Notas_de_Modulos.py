#-------------USO DE MODULOS, SYS.PATH Y DEMAS---
#Notas importantes:
# 1) al importar un modulo, lo que ocurre es que se ejecutara todo el codigo que no se encuentre dentro 
#    if __name__ == '__main__' de dicho modulo importado
# 2) cuando importas un modulo python busca dicho modulo en la lista de carpetas que el tiene y si dicho
#    script no se encuentra, dara el error "ModuleNotFoundError"
# 3) para ver que la lista de rutas en las que python busca tus modulos solo importas el modulo sys y
#    escribes sys.path --> que te devuelve la lista de rutas
# 4) puedes agregar una ruta de un modulo que no este en sys.path de la sgte manera: "sys.path.append(\ruta\)""
#    cabe aclarar que esta nueva ruta agregada a la lista es temporal para cada ejecucion y no se guarda 
#    de forma permanente 
# 5) supongamos que estamos en el script "ejemplo.py" y queremos importar un modulo que se encuentra en una 
#    sub-carpeta de la ubicacion del script "ejempl.py", mira el ejemplo:
    # ├── ejemplo.py
    # ├── carpeta
    # │   └── modulo.py
#    en este caso nosotros podemos acceder al modulo "modulo.py" de la sgte manera:
#    from carpeta.modulo import * 
# 6) uso de "dir()" q da una lista con todas las variables, funciones, clases,etc existentes en nuestro script
# 7) el uso de "_" antes de una funcion, variable, clase,etc es una convencion para decirles a los programadores
#    que dichos objetos no deberian ser accedidos desde otros scripts cuando se importa dicho modulo 








