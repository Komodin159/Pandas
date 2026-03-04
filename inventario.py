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

        elif opcion == "2":
            print("----DICIONARIO----")

            if len(inventario) == 0:
                print("El inventario esta vacio")
            else:
                for item in inventario:
                    print(f"Producto: {item["Nombre"]}, el precio es de [{item["Precio"]}] y la cantidad existente es de [{item["Cantidad"]}]")
        elif opcion == "3":
            busqueda = input("Ingrese el nombre a buscar:\n").lower()
            encontrar = False

            for item in inventario:
                if item ["Nombre"].lower() == busqueda:
                    print(f"ENCONTRADO: el precio $ {item["Precio"]} y la cantidad de [{item["Cantidad"]}]")
                    encontrar = True
                    break

            if not encontrar:
                print("El producto no existe")

        elif opcion == "4":
            print("Saliendo del programa...")
        else:
            print("Opcion no valida, intente de nuevo")

if __name__ == "__main__":
    main()
