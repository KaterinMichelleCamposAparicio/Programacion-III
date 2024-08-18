class ArticuloPapeleria:
    def __init__(self, tipo, detalle, precio_compra):
        self.tipo = tipo
        self.detalle = detalle
        self.precio_compra = precio_compra
        self.margen_ganancia = 1.30
        self.precio_venta = self.precio_compra * self.margen_ganancia
        self.marca = "HOJITAS" if tipo == "cuaderno" else "RAYAS"

    def registrar(self):
        print(f"\nEl {self.tipo} de marca {self.marca} ha sido registrado.")

    def mostrar_informacion(self):
        print("\n--- Información del Artículo Registrado ---")
        print(f"Tipo: {self.tipo.capitalize()}")
        print(f"Detalle: {self.detalle}")
        print(f"Marca: {self.marca}")
        print(f"Precio de Compra: ${self.precio_compra:.2f}")
        print(f"Precio de Venta: ${self.precio_venta:.2f}")

# Solicitar y registrar datos del artículo de papelería
tipo = input("Ingrese el tipo de artículo (cuaderno/lapiz): ").lower()
if tipo == "cuaderno":
    detalle = input("Ingrese la cantidad de hojas (50/100): ")
    if detalle not in ["50", "100"]:
        print("Cantidad de hojas no válida.")
        exit()
elif tipo == "lapiz":
    detalle = input("Ingrese el tipo de lápiz (grafito/color): ").lower()
    if detalle not in ["grafito", "color"]:
        print("Tipo de lápiz no válido.")
        exit()
else:
    print("Tipo de artículo no reconocido.")
    exit()

precio_compra = float(input("Ingrese el precio de compra: "))

# Crear instancia de ArticuloPapeleria y mostrar la información
articulo = ArticuloPapeleria(tipo, detalle, precio_compra)
articulo.mostrar_informacion()
articulo.registrar()
