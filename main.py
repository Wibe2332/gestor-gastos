from modelos import Categoria, Gasto
from database import (
    guardar_gasto, listar_gastos, editar_gasto, eliminar_gasto,
    guardar_categoria, listar_categorias, total_por_categoria
)
from api import obtener_tasa_cambio


def mostrar_menu():
    print("\n--- GESTOR DE GASTOS ---")
    print("1. Agregar gasto")
    print("2. Ver gastos")
    print("3. Editar gasto")
    print("4. Eliminar gasto")
    print("5. Ver gastos en USD")
    print("6. Ver reporte por categoría")
    print("7. Salir")


def elegir_categoria():
    categorias = listar_categorias()

    print("\n--- Categorías ---")
    for cat_id, nombre in categorias:
        print(f"{cat_id}. {nombre}")
    print("0. Crear categoría nueva")

    ids_validos = [cat_id for cat_id, nombre in categorias]

    while True:
        opcion = input("Elige una categoría (número): ")

        if opcion == "0":
            nombre_nuevo = input("Nombre de la nueva categoría: ")
            guardar_categoria(nombre_nuevo)
            categorias = listar_categorias()
            return categorias[-1][0]

        try:
            opcion_numero = int(opcion)
        except ValueError:
            print("❌ Eso no es un número válido, intenta de nuevo.")
            continue

        if opcion_numero in ids_validos:
            return opcion_numero
        else:
            print("❌ Ese ID de categoría no existe, intenta de nuevo.")
            

def pedir_numero(mensaje, tipo=float):
    while True:
        entrada = input(mensaje)
        try:
            return tipo(entrada)
        except ValueError:
            print("❌ Eso no es un número válido, intenta de nuevo.")


while True:
    mostrar_menu()
    opcion = input("Elige una opción: ")

    if opcion == "1":
        descripcion = input("Descripción: ")
        monto = pedir_numero("Monto: ", float)
        categoria_id = elegir_categoria()

        cat = Categoria("")
        g = Gasto(descripcion, monto, cat)
        guardar_gasto(g, categoria_id)

    elif opcion == "2":
        gastos = listar_gastos()
        for fila in gastos:
            id_gasto, descripcion, monto, fecha, nombre_categoria = fila
            cat = Categoria(nombre_categoria)
            g = Gasto(descripcion, monto, cat, fecha)
            print(f"[ID {id_gasto}] {g}")

    elif opcion == "3":
        id_gasto = pedir_numero("ID del gasto a editar: ", int)
        nueva_descripcion = input("Nueva descripción: ")
        nuevo_monto = pedir_numero("Nuevo monto: ", float)
        editar_gasto(id_gasto, nueva_descripcion, nuevo_monto)

    elif opcion == "4":
        id_gasto = pedir_numero("ID del gasto a eliminar: ", int)
        eliminar_gasto(id_gasto)

    elif opcion == "5":
        tasa = obtener_tasa_cambio("USD")
        gastos = listar_gastos()
        for fila in gastos:
            id_gasto, descripcion, monto, fecha, nombre_categoria = fila
            monto_usd = float(monto) * tasa
            print(f"[ID {id_gasto}] {descripcion} | ${monto} DOP = ${monto_usd:.2f} USD")

    elif opcion == "6":
        totales = total_por_categoria()
        total_general = 0

        print("\n--- REPORTE POR CATEGORÍA ---")
        for nombre_categoria, total in totales:
            print(f"{nombre_categoria}: ${total:.2f}")
            total_general += float(total)

        print(f"\nTOTAL GENERAL: ${total_general:.2f}")

    elif opcion == "7":
        print("¡Hasta luego!")
        break

    else:
        print("Opción inválida, intenta de nuevo.")