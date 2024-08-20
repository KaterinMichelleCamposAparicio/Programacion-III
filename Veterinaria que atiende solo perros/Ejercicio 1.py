""" Una veterinaria atiende solamente perros y los registra en una base de datos. Se requiere un programa que lea la información básica del perro
   (no más de 8 características) y se muestre en pantalla. En esta veterinaria, todos los animales que llegan, entran con el estado inicial de 
   NO ATENDIDO y cuando se registran se cambia automáticamente a ATENDIDO. Por ahora, como la veterinaria solo atiende perros, basado en el peso
   (menos de 10 kg o más de 10 kg) los registra como "Perro Grande" o "Perro Pequeño"."""

class Perro:
    def __init__(self, nombre, raza, edad, peso, color, altura, vacunas, comportamiento):
        self.nombre = nombre
        self.raza = raza
        self.edad = edad
        self.peso = peso
        self.color = color
        self.altura = altura
        self.vacunas = vacunas
        self.comportamiento = comportamiento
        self.tipo = "Perro Grande" if peso >= 10 else "Perro Pequeño"
        self.estado = "NO ATENDIDO"  # Estado inicial

    def registrar(self):
        self.estado = "ATENDIDO"  # Cambiar estado a "ATENDIDO"
        print(f"\nEl perro {self.nombre} ha sido registrado como {self.tipo}. Estado: {self.estado}")

    def mostrar_informacion(self):
        print("\n--- Información del Perro Registrado ---")
        print(f"Nombre: {self.nombre}")
        print(f"Raza: {self.raza}")
        print(f"Edad: {self.edad}")
        print(f"Peso: {self.peso} kg")
        print(f"Color: {self.color}")
        print(f"Altura: {self.altura}")
        print(f"Vacunas: {self.vacunas}")
        print(f"Comportamiento: {self.comportamiento}")
        print(f"Tipo: {self.tipo}")
        print(f"Estado: {self.estado}")

# Solicitar y registrar datos del perro
nombre = input("Ingrese el nombre del perro: ")
raza = input("Ingrese la raza del perro: ")
edad = int(input("Ingrese la edad del perro: "))
peso = float(input("Ingrese el peso del perro en kg: "))
color = input("Ingrese el color del perro: ")
altura = input("Ingrese la altura del perro: ")
vacunas = input("Ingrese el estado de vacunas (Sí/No): ")
comportamiento = input("Ingrese el comportamiento del perro: ")

# Crear instancia de Perro y mostrar la información
perro = Perro(nombre, raza, edad, peso, color, altura, vacunas, comportamiento)
perro.mostrar_informacion()
perro.registrar()
