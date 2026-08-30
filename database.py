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


if __name__ == "__main__":
    try:
        conn = conectar()
        print("✅ Conexión exitosa a SQL Server")
        conn.close()
    except Exception as e:
        print("❌ Error al conectar:", e)
        
