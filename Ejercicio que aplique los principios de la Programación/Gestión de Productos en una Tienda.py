"""
Situación Problemática:

Imagina que tienes una pequeña tienda que vende varios productos como alimentos, ropa, y accesorios. A medida que el negocio crece, te enfrentas
a desafíos en la gestión del inventario, el registro de ventas, y el cálculo de ingresos. Sin un sistema adecuado, es difícil saber cuántos 
productos tienes en existencia, cuáles se venden más, y cuánto has ganado en un periodo determinado.

Este programa está diseñado para abordar esos problemas permitiendo gestionar eficientemente el inventario, registrar ventas con posibles 
descuentos, y generar reportes de ventas. Así, puedes tomar decisiones informadas sobre la reposición de productos, promociones, y estrategias 
de venta.

Descripción del Programa:

El programa es una simulación básica de la gestión de inventario y ventas en una tienda. Utiliza los principios de la Programación Orientada a 
Objetos (POO) para modelar productos y las operaciones que una tienda podría realizar sobre ellos. Se compone de dos clases principales: 
ProductoTienda y Tienda

Funcionamiento del Programa:

Agregar Productos:

El usuario puede añadir productos a la tienda proporcionando el nombre, la cantidad en inventario, y el precio unitario de cada producto.

Registrar Ventas:

El usuario puede registrar la venta de un producto indicando la cantidad vendida y un posible descuento. El sistema verifica si hay suficiente 
inventario antes de proceder con la venta y actualiza la información del producto.

Mostrar Inventario:

Se puede consultar en cualquier momento el estado actual del inventario, viendo cuántos productos hay disponibles, su precio, y cuánto han 
generado en ingresos.

Generar Reporte de Ventas:

El programa genera un reporte que resume los ingresos totales generados por la tienda y destaca cuál ha sido el producto más vendido.

Problema que Resuelve:

Este programa resuelve el problema de la gestión manual y desorganizada del inventario en una tienda. Al automatizar el proceso de registro de 
ventas y control de inventario, se reduce el riesgo de errores, se mejora la eficiencia operativa, y se facilita la toma de decisiones. Con el 
reporte de ventas, el dueño de la tienda puede identificar qué productos son más populares y ajustar sus estrategias de compra y promoción en 
consecuencia.

En un entorno donde la precisión y la rapidez son cruciales para mantener la competitividad, este programa proporciona una solución simple pero 
efectiva para manejar los aspectos esenciales de la administración de una tienda.

"""


# Clase que representa un producto dentro de la tienda
class ProductoTienda:
    def __init__(self, nombre, cantidad, precio_unitario):
        # Inicialización de los atributos del producto
        self.nombre = nombre  # Nombre del producto
        self.cantidad = cantidad  # Cantidad disponible en inventario
        self.precio_unitario = precio_unitario  # Precio al que se vende cada unidad
        self.ventas_totales = 0  # Total de unidades vendidas
        self.ingresos_totales = 0.0  # Ingresos totales generados por este producto

    # Método para registrar una venta de este producto
    def vender_producto(self, cantidad_vendida, descuento=0):
        # Verifica si hay suficiente inventario para realizar la venta
        if cantidad_vendida <= self.cantidad:
            self.cantidad -= cantidad_vendida  # Reduce el inventario disponible
            self.ventas_totales += cantidad_vendida  # Actualiza el total de unidades vendidas
            # Calcula el precio final aplicando el descuento si es necesario
            precio_final = self.precio_unitario * (1 - descuento / 100)
            ingreso = cantidad_vendida * precio_final  # Calcula el ingreso por esta venta
            self.ingresos_totales += ingreso  # Actualiza los ingresos totales
            # Muestra un mensaje confirmando la venta
            print(f"Venta realizada: {cantidad_vendida} unidades de {self.nombre} a ${precio_final:.2f} cada una.")
        else:
            # Mensaje de error si no hay suficiente inventario
            print("Cantidad en inventario insuficiente para realizar la venta.")

    # Método para mostrar la información del producto
    def mostrar_informacion(self):
        # Muestra todos los detalles relevantes del producto
        print("\n--- Información del Producto ---")
        print(f"Nombre: {self.nombre}")
        print(f"Cantidad en Inventario: {self.cantidad}")
        print(f"Precio Unitario: ${self.precio_unitario:.2f}")
        print(f"Ventas Totales: {self.ventas_totales}")
        print(f"Ingresos Totales: ${self.ingresos_totales:.2f}")

# Clase que representa la tienda en sí
class Tienda:
    def __init__(self, nombre):
        # Inicialización de la tienda con su nombre y una lista de productos
        self.nombre = nombre  # Nombre de la tienda
        self.productos = []  # Lista de productos que tiene la tienda

    # Método para añadir un producto al inventario de la tienda
    def agregar_producto(self, producto):
        self.productos.append(producto)  # Añade el producto a la lista
        # Muestra un mensaje confirmando la adición del producto
        print(f"Producto '{producto.nombre}' añadido al inventario.")

    # Método para mostrar el inventario de la tienda
    def mostrar_inventario(self):
        # Verifica si hay productos en el inventario
        if not self.productos:
            print("No hay productos en el inventario.")
            return

        # Muestra la información de cada producto en el inventario
        print(f"\n--- Inventario de {self.nombre} ---")
        for producto in self.productos:
            producto.mostrar_informacion()

    # Método para generar un reporte de ventas
    def generar_reporte(self):
        print(f"\n--- Reporte de Ventas de {self.nombre} ---")
        # Calcula los ingresos totales sumando los ingresos de cada producto
        ingresos_totales = sum([producto.ingresos_totales for producto in self.productos])
        # Encuentra el producto más vendido
        producto_mas_vendido = max(self.productos, key=lambda p: p.ventas_totales, default=None)
        
        # Muestra los ingresos totales generados por la tienda
        print(f"Ingresos Totales: ${ingresos_totales:.2f}")
        # Muestra el producto más vendido si existe
        if producto_mas_vendido:
            print(f"Producto Más Vendido: {producto_mas_vendido.nombre} ({producto_mas_vendido.ventas_totales} unidades)")

# Ejemplo de uso del programa
nombre_tienda = input("Ingrese el nombre de la tienda: ")  # Solicita el nombre de la tienda al usuario
tienda = Tienda(nombre_tienda)  # Crea una instancia de la tienda con el nombre proporcionado

# Bucle principal para interactuar con el usuario
while True:
    # Menú de opciones para el usuario
    print("\n¿Qué deseas hacer?")
    print("1. Añadir producto")
    print("2. Vender producto")
    print("3. Mostrar inventario")
    print("4. Generar reporte de ventas")
    print("5. Salir")
    opcion = input("Seleccione una opción (1-5): ")

    # Opción 1: Añadir un producto al inventario
    if opcion == "1":
        nombre = input("Ingrese el nombre del producto: ")  # Solicita el nombre del producto
        cantidad = int(input("Ingrese la cantidad disponible en inventario: "))  # Solicita la cantidad en inventario
        precio_unitario = float(input("Ingrese el precio unitario: "))  # Solicita el precio unitario del producto
        producto = ProductoTienda(nombre, cantidad, precio_unitario)  # Crea una instancia del producto
        tienda.agregar_producto(producto)  # Añade el producto al inventario de la tienda

    # Opción 2: Registrar una venta de un producto
    elif opcion == "2":
        nombre = input("Ingrese el nombre del producto que deseas vender: ")  # Solicita el nombre del producto a vender
        # Busca el producto en el inventario
        for producto in tienda.productos:
            if producto.nombre == nombre:
                cantidad_vendida = int(input("Ingrese la cantidad a vender: "))  # Solicita la cantidad a vender
                descuento = float(input("Ingrese el descuento (0-100)%: "))  # Solicita el descuento a aplicar
                producto.vender_producto(cantidad_vendida, descuento)  # Registra la venta del producto
                break
        else:
            # Mensaje de error si el producto no se encuentra en el inventario
            print(f"No se encontró el producto '{nombre}' en el inventario.")

    # Opción 3: Mostrar el inventario de la tienda
    elif opcion == "3":
        tienda.mostrar_inventario()  # Muestra el inventario de la tienda

    # Opción 4: Generar un reporte de ventas
    elif opcion == "4":
        tienda.generar_reporte()  # Genera un reporte de ventas

    # Opción 5: Salir del programa
    elif opcion == "5":
        print("Saliendo...")  # Mensaje de salida
        break  # Finaliza el bucle y cierra el programa

    # Si el usuario ingresa una opción no válida
    else:
        print("Opción no reconocida.")  # Mensaje de error
