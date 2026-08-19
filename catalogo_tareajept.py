registro_gastos = {
    "gasto_1": {
        "concepto": "super",
        "monto": 75.0,
        "tipo": "alimentos",
        "pagado": True
    },
    "gasto_2": {
        "concepto": "internet",
        "monto": 120.50,
        "tipo": "servicios",
        "pagado": False
    }
}

def agregar_gasto():
    nombre = input("nombre de gasto: ")
    concepto = input("Concepto: ")
    monto = input("monto: ")
    tipo = input("tipo de gasto: ")
    pagado = input("monto pagado? (s/n): ").lower

    if pagado == "s":
        pagado = True
    else:
        pagado = False

    registro_gastos[nombre] = {
        "concepto": concepto,
        "monto": monto,
        "tipo" : tipo,
        "pagado": pagado
    }

    print("Gasto guardado")

def ver_todos():
    for nombre, datos in registro_gastos.items():
        print(f"\nGasto: {nombre}")
        print(f"Concepto: {datos['concepto']}")
        print(f"Monto: {datos['monto']}")
        print(f"Categoria: {datos['tipo']}")
        print(f"Pagado: {datos['pagado']}")

def modificar_gasto():
    nombre = input("Ingrese el nombre del gasto que quiere modificar: ")

    if nombre in registro_gastos:
        print("\n¿Qué atributo desea modificar?")
        print("1. Concepto")
        print("2. Monto")
        print("3. Categoria")
        print("4. Pagado")

        atributo = input("Ingrese una opción: ")

        if atributo == "1":
            nuevo_concepto = input("Ingrese el nuevo concepto: ")
            registro_gastos[nombre]["concepto"] = nuevo_concepto

        elif atributo == "2":
            nuevo_monto = float(input("Ingrese el nuevo monto: "))
            registro_gastos[nombre]["monto"] = nuevo_monto

        elif atributo == "3":
            nueva_categoria = input("Ingrese la nueva categoria: ")
            registro_gastos[nombre]["categoria"] = nueva_categoria

        elif atributo == "4":
            nuevo_pagado = input("¿Está pagado? (s/n): ").lower()

            if nuevo_pagado == "s":
                registro_gastos[nombre]["pagado"] = True
            else:
                registro_gastos[nombre]["pagado"] = False

        else:
            print("Opción inválida.")
            return

        print("Gasto modificado correctamente.")

    else:
        print("Ese gasto no existe.")


flag = True

while flag:

    menu = """
    Registro de Gastos

    1. Ver todos los gastos del catálogo.
    2. Agregar un nuevo gasto al catálogo.
    3. Modificar un atributo de un gasto existente.
    4. Salir del programa.
    """

    print(menu)

    eleccion = input("Ingrese una opción: ")

    if len(eleccion) == 1:
        if ord(eleccion) >= 49 and ord(eleccion) <= 52:

            if int(eleccion) == 1:
                ver_todos()

            elif int(eleccion) == 2:
                agregar_gasto()

            elif int(eleccion) == 3:
                modificar_gasto()

            elif int(eleccion) == 4:
                print("Programa finalizado.")
                flag = False

        else:
            print("\nInput invalido. Debe estar entre 1 y 4.")
    else:
        print("\nInput invalido. Debe ser de 1 caracter.")


