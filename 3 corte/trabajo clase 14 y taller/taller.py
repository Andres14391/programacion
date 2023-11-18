class Prducto:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio
        self.stock = 0

    def info(self):
        return f"Producto: {self.nombre}, Precio: ${self.precio:.2f}, Stock: {self.stock} unidades"

    def reducir_stock(self):
        if self.stock > 0:
            self.stock -= 1

    def disponible(self):
        return self.stock > 0


class Snack(Prducto):
    def __init__(self, nombre, precio, categoria):
        super().__init__(nombre, precio)
        self.categoria = categoria

    def info(self):
        return super().info() + f", Categoría: {self.categoria}"


class Bebida(Prducto):
    def __init__(self, nombre, precio, tamaño):
        super().__init__(nombre, precio)
        self.tamaño = tamaño

    def info(self):
        return super().info() + f", Tamaño: {self.tamaño} ml"


class maquina_dispensadora:
    def __init__(self):
        self.articulos = []
        self.total_ventas = 0

    def agregar_articulo(self, articulo):
        stock = int(input(f"Ingrese la cantidad inicial de {articulo.nombre}: "))
        articulo.stock = stock
        self.articulos.append(articulo)

    def realizar_venta(self, articulo):
        if articulo.disponible():
            articulo.reducir_stock()
            self.total_ventas += articulo.precio
            return True
        else:
            return False

    def total_ventas(self):
        return f"Total de ventas: ${self.total_ventas}"


dispensador = maquina_dispensadora()

while True:
    print('\n---------Máquina Dispensadora----------\n')
    print("1.Agregar un artículo")
    print("2.Realizar una venta")
    print("3.Ver total de ventas")
    print("4.Ver todos los artículos")
    print("5.Salir")
    opcion = input("Seleccione una opción: ")
    print('\n---------------------------------------\n')
    if opcion == "1":
        categoria = input("Ingrese la categoría del artículo (aperitivo o bebida): ")
        nombre = input("Ingrese el nombre del artículo: ")
        precio = float(input("Ingrese el precio del artículo: "))
        if categoria.lower() == "aperitivo":
            tipo_aperitivo = input("Ingrese la categoría del aperitivo (snack o tapa): ")
            articulo = Snack(nombre, precio, tipo_aperitivo)
        elif categoria.lower() == "bebida":
            tamaño = input("Ingrese el tamaño de la bebida (pequeño o grande): ")
            articulo = Bebida(nombre, precio, tamaño)
        else:
            print("Categoría de artículo no válida. Intente de nuevo.")
            continue
        dispensador.agregar_articulo(articulo)
        print(f"{articulo.nombre} agregado correctamente al stock.")
    elif opcion == "2":
        nombre = input("Ingrese el nombre del artículo que desea comprar: ")
        articulo = next((a for a in dispensador.articulos if a.nombre == nombre), None)
        if articulo is not None and dispensador.realizar_venta(articulo):
            print(f"Venta realizada: {articulo.nombre}. Gracias por su compra.")
        else:
            print(f"Venta no realizada. {articulo.nombre} no está disponible en este momento.")
    elif opcion == "3":
        print(dispensador.total_ventas())
    elif opcion == "4":
        for articulo in dispensador.articulos:
            print(articulo.info())
    elif opcion == "5":
        break
    else:
        print("Opción no válida. Intente de nuevo.")