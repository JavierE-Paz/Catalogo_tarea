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



