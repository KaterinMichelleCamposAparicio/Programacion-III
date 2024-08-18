""" Un almacén vende dispositivos electrónicos (celulares, tablets y portátiles).Todos PHR que es una nueva marca que 
    está entrando en el mercado. Se requiere almacenar sus 6 principales características. Todos son productos importados y 
    su precio de venta es igual al precio de compra multiplicado por 1.7 que corresponde a su margen de ganancia."""


class DispositivoElectronico:
    def __init__(self, tipo, modelo, capacidad, color, precio_compra, garantia):
        self.tipo = tipo
        self.modelo = modelo
        self.capacidad = capacidad
        self.color = color
        self.precio_compra = precio_compra
        self.garantia = garantia
        self.margen_ganancia = 1.7
        self.precio_venta = self.precio_compra * self.margen_ganancia
        self.marca = "PHR"

    def registrar(self):
        print(f"\nEl dispositivo {self.tipo.capitalize()} modelo {self.modelo} ha sido registrado.")

    def mostrar_informacion(self):
        print("\n--- Información del Dispositivo Registrado ---")
        print(f"Tipo: {self.tipo.capitalize()}")
        print(f"Modelo: {self.modelo}")
        print(f"Capacidad: {self.capacidad}")
        print(f"Color: {self.color}")
        print(f"Marca: {self.marca}")
        print(f"Precio de Compra: ${self.precio_compra}")
        print(f"Precio de Venta: ${self.precio_venta}")
        print(f"Garantía: {self.garantia} meses")

# Solicitar y registrar datos del dispositivo electrónico
tipo = input("Ingrese el tipo de dispositivo (celular/tablet/portátil): ").lower()
modelo = input("Ingrese el modelo del dispositivo: ")
capacidad = input("Ingrese la capacidad del dispositivo: ")
color = input("Ingrese el color del dispositivo: ")
precio_compra = float(input("Ingrese el precio de compra: "))
garantia = input("Ingrese la garantía (en meses): ")

# Crear instancia de DispositivoElectronico y mostrar la información
dispositivo = DispositivoElectronico(tipo, modelo, capacidad, color, precio_compra, garantia)
dispositivo.mostrar_informacion()
dispositivo.registrar()
