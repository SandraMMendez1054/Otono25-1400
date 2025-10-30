""" 1. Funcion de saludo """
# def saludo(nombre)
#     print(f"Hola {nombre})

#saludo("Juan")
#saludo("Maria")

""" 2. Funcion que calcule el area de un rectangulo """
def area_rectangulo(base, altura):
    area = base * altura
    return area 

""" 3. class"""
class Gato:
    #funcion requerida __init__
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def maullar(self):
        return "Miau!"

# crear objetos

tu_gato = Gato("Pelusa", 3)
print(tu_gato.nombre)  # Output: Pelusa
print(tu_gato.edad)    # Output: 3  

""" 4. clase propia"""
class Coche:
    def __init__(self, marca, modelo, ):
        self.marca = marca
        self.modelo = modelo

    def descripcion(self):
        return f"{self.anio} {self.marca} {self.modelo}"
    
""" 5. tiempo"""



    