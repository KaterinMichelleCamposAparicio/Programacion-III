""" Un concesionario de autos vende vehículos nacionales e importados. Todos tienen 4 ruedas y capacidad para 5 pasajeros.
    Esta información debe registrarse siempre por razones de ley. Requiere un programa que le permita almacenar las 10 principales
    características de los autos.El precio de venta de cada auto es igual al precio de compra multiplicado por 1.4 que corresponde 
    a su margen de ganancia."""


class Auto:
    def __init__(self, marca, modelo, año, color, tipo_motor, precio_compra):
        self.marca = marca
        self.modelo = modelo
        self.año = año
        self.color = color
        self.tipo_motor = tipo_motor
        self.precio_compra = precio_compra
        self.margen_ganancia = 1.4
        self.precio_venta = self.precio_compra * self.margen_ganancia
        self.ruedas = 4
        self.capacidad_pasajeros = 5

    def registrar(self):
        print(f"\nEl auto {self.marca} {self.modelo} ha sido registrado.")

    def mostrar_informacion(self):
        print("\n--- Información del Auto Registrado ---")
        print(f"Marca: {self.marca}")
        print(f"Modelo: {self.modelo}")
        print(f"Año: {self.año}")
        print(f"Color: {self.color}")
        print(f"Tipo de motor: {self.tipo_motor}")
        print(f"Precio de Compra: ${self.precio_compra}")
        print(f"Precio de Venta: ${self.precio_venta}")
        print(f"Ruedas: {self.ruedas}")
        print(f"Capacidad de pasajeros: {self.capacidad_pasajeros}")

# Solicitar y registrar datos del auto
marca = input("Ingrese la marca del auto: ")
modelo = input("Ingrese el modelo del auto: ")
año = input("Ingrese el año del auto: ")
color = input("Ingrese el color del auto: ")
tipo_motor = input("Ingrese el tipo de motor: ")
precio_compra = float(input("Ingrese el precio de compra: "))

# Crear instancia de Auto y mostrar la información
auto = Auto(marca, modelo, año, color, tipo_motor, precio_compra)
auto.mostrar_informacion()
auto.registrar()
