from modelos import Categoria, Gasto
from database import guardar_gasto, listar_gastos, editar_gasto, eliminar_gasto

def mostrar_menu():
    print("\n--- GESTOR DE GASTOS ---")
    print("1. Agregar gasto")
    print("2. Ver gastos")
    print("3. Editar gasto")
    print("4. Eliminar gasto")
    print("5. Salir")

while True:
    mostrar_menu()
    opcion = input("Elige una opción: ")

    if opcion == "1":
        descripcion = input("Descripción: ")
        monto = float(input("Monto: "))

        cat = Categoria("Entretenimiento")
        g = Gasto(descripcion, monto, cat)
        guardar_gasto(g, 1)

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
        print("¡Hasta luego!")
        break

    else:
        print("Opción inválida, intenta de nuevo.")