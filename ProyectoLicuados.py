# Datos del cliente
nombre_cliente = input("Ingrese su nombre: ")
nit_cliente = input("¿Desea ingresar su NIT? (s/n): ")


# Detalles del pedido por defecto
licuado = "Licuado de fresa"
precio_licuado = 20.00
tamaño_licuado = "normal"
azucar = 0
tipo_leche = "leche deslactosada"
descuento_leche = 0
aumento_tamaño = 0
confirmado = False

# Menú interactivo con match
while not confirmado:
    opcion_menu = input("\nMenú:\n1. Ver información del pedido\n2. Agregar azúcar\n3. Modificar leche\n4. Agrandar\n5. Confirmar\nSeleccione una opción: ")

    match opcion_menu:
        case "1":
            print("\nInformación del pedido:")
            print("Nombre del cliente:", nombre_cliente)
            print("NIT del cliente:", nit_cliente)
            print("Licuado:", licuado)
            print("Precio del licuado:", precio_licuado)
            print("Tamaño del licuado:", tamaño_licuado)
            print("Cantidad de azúcar:", azucar)
            print("Tipo de leche:", tipo_leche)
            print("Descuento por tipo de leche:", descuento_leche)
            print("Aumento de tamaño:", aumento_tamaño)

        case "2":
            if azucar < 2:
                azucar += 1
                precio_licuado += 0.50
                print("Se agregó una cucharada de azúcar al licuado.")
                print("Cantidad de azúcar total:", azucar)
                print("Precio adicional por azúcar:", azucar * 0.50)
            else:
                print("No se puede agregar más azúcar.")

        case "3":
            print("Opciones de leche:")
            print("1. Sin leche (únicamente con agua)")
            print("2. Leche deslactosada")
            print("3. Leche entera")
            print("4. Leche de soya")
            opcion_leche = input("Seleccione una opción de leche: ")
            match opcion_leche:
                case "1":
                    tipo_leche = "agua"
                    descuento_leche = 2.00
                    precio_licuado -= descuento_leche
                    print("Se ha restado Q2.00 por seleccionar agua como leche.")
                case "2":
                    tipo_leche = "leche deslactosada"
                    descuento_leche = 0
                    precio_licuado += descuento_leche  # No se cambia el precio
                case "3":
                    tipo_leche = "leche entera"
                    descuento_leche = 0
                    precio_licuado += descuento_leche  # No se cambia el precio
                case "4":
                    tipo_leche = "leche de soya"
                    descuento_leche = 3.00
                    precio_licuado += descuento_leche
                    print("Se ha aumentado Q3.00 por seleccionar leche de soya.")

        case "4":
            if aumento_tamaño == 0:
                aumento_tamaño = precio_licuado * 0.05
                precio_licuado += aumento_tamaño
                tamaño_licuado = "grande"
                print("El licuado se ha agrandado.")
                print("Precio adicional por agrandar:", aumento_tamaño)
            else:
                print("No se puede agrandar más de una vez.")

        case "5":
            confirmado = True
            print("\nConfirmación del pedido:")
            print("Nombre del cliente:", nombre_cliente)
            if nit_cliente:
                print("NIT del cliente:", nit_cliente)  # Agregamos esta línea para mostrar el NIT si está disponible
            print("Detalle del pedido:")
            print("Licuado:", licuado)
            print("Precio total del licuado:", precio_licuado)
            print("Tamaño del licuado:", tamaño_licuado)
            print("Cantidad de azúcar:", azucar)
            print("Tipo de leche:", tipo_leche)
            print("Descuento por tipo de leche:", descuento_leche)
            print("Aumento de tamaño:", aumento_tamaño)
            print("¡Gracias por su compra!")


        case _:
            print("Opción inválida. Por favor, seleccione nuevamente.")
