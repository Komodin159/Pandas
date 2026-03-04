def main():
    inventario = []

    while True:
        opcion = input("Ingrese su opcion:\n")
        if opcion == "1":
            print("----NUEVO PRODUCTO----")
            nombre = input("Nombre de producto:\n")

            try:
                precio = float(input("Ingrese precio: "))
                stock = int(input("Ingrese cantidad: "))

                producto = {
                    "Nombre": nombre,
                    "Precio": precio,
                    "Cantidad": stock
                }
                inventario.append(producto)

                print("El producto se guardo correctamente")

            except ValueError:
                print("El producto y precio no son validos")


if __name__ == "__main__":
    main()
