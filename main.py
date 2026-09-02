from modelos import Categoria, Gasto
from database import (
    guardar_gasto, listar_gastos, editar_gasto, eliminar_gasto,
    guardar_categoria, listar_categorias
)
from api import obtener_tasa_cambio


def mostrar_menu():
    print("\n--- GESTOR DE GASTOS ---")
    print("1. Agregar gasto")
    print("2. Ver gastos")
    print("3. Editar gasto")
    print("4. Eliminar gasto")
    print("5. Ver gastos en USD")
    print("6. Salir")


def elegir_categoria():
    categorias = listar_categorias()

    print("\n--- Categorías ---")
    for cat_id, nombre in categorias:
        print(f"{cat_id}. {nombre}")
    print("0. Crear categoría nueva")

    opcion = input("Elige una categoría (número): ")

    if opcion == "0":
        nombre_nuevo = input("Nombre de la nueva categoría: ")
        guardar_categoria(nombre_nuevo)
        categorias = listar_categorias()
        return categorias[-1][0]
    else:
        return int(opcion)


while True:
    mostrar_menu()
    opcion = input("Elige una opción: ")

    if opcion == "1":
        descripcion = input("Descripción: ")
        monto = float(input("Monto: "))
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
        id_gasto = int(input("ID del gasto a editar: "))
        nueva_descripcion = input("Nueva descripción: ")
        nuevo_monto = float(input("Nuevo monto: "))
        editar_gasto(id_gasto, nueva_descripcion, nuevo_monto)

    elif opcion == "4":
        id_gasto = int(input("ID del gasto a eliminar: "))
        eliminar_gasto(id_gasto)

    elif opcion == "5":
        tasa = obtener_tasa_cambio("USD")
        gastos = listar_gastos()
        for fila in gastos:
            id_gasto, descripcion, monto, fecha, nombre_categoria = fila
            monto_usd = float(monto) * tasa
            print(f"[ID {id_gasto}] {descripcion} | ${monto} DOP = ${monto_usd:.2f} USD")

    elif opcion == "6":
        print("¡Hasta luego!")
        break

    else:
        print("Opción inválida, intenta de nuevo.")