import pyodbc

def conectar():
    conexion = pyodbc.connect(
        "DRIVER={ODBC Driver 17 for SQL Server};"
        "SERVER=Happy;"
        "DATABASE=GestorGastos;"
        "Trusted_Connection=yes;"
    )
    return conexion

def guardar_gasto(gasto, categoria_id):
    conexion = conectar()
    cursor = conexion.cursor()

    cursor.execute(
        "INSERT INTO Gastos (descripcion, monto, categoria_id) VALUES (?, ?, ?)",
        gasto.descripcion, gasto.monto, categoria_id
    )

    conexion.commit()
    conexion.close()
    print("✅ Gasto guardado en la base de datos")

def listar_gastos():
    conexion = conectar()
    cursor = conexion.cursor()

    cursor.execute("""
        SELECT g.id, g.descripcion, g.monto, g.fecha, c.nombre
        FROM Gastos g
        JOIN Categorias c ON g.categoria_id = c.id
    """)

    filas = cursor.fetchall()
    conexion.close()
    return filas

def editar_gasto(id_gasto, nueva_descripcion, nuevo_monto):
    conexion = conectar()
    cursor = conexion.cursor()

    cursor.execute(
        "UPDATE Gastos SET descripcion = ?, monto = ? WHERE id = ?",
        nueva_descripcion, nuevo_monto, id_gasto
    )

    conexion.commit()
    conexion.close()
    print("✅ Gasto actualizado")


def eliminar_gasto(id_gasto):
    conexion = conectar()
    cursor = conexion.cursor()

    cursor.execute("DELETE FROM Gastos WHERE id = ?", id_gasto)

    conexion.commit()
    conexion.close()
    print("✅ Gasto eliminado")



if __name__ == "__main__":
    try:
        conn = conectar()
        print("✅ Conexión exitosa a SQL Server")
        conn.close()
    except Exception as e:
        print("❌ Error al conectar:", e)
        
