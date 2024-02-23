class Auto :
    def __init__ (self, modelo, ano, color):
        self.modelo = modelo
        self.ano = ano
        self.color = color
    def Get_atributos(self):        
        return (f"el modelo de tu auto es: {self.modelo}, es del año: {self.ano}, y es de color {self.color}")
    def Precio (self):
        print("bebe")
                        
Auto_de_papa = Auto("Toyota", 2012, "Rojo")
print(Auto_de_papa.Get_atributos())
Auto_de_papa.Precio()

def elevar_cuadrado (num):
    return num **2

    
