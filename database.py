
import pyodbc
from rich.console import Console

console = Console()

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
    console.print("[green]✅ Gasto guardado en la base de datos[/green]")

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
    console.print("[green]✅ Gasto actualizado[/green]")


def eliminar_gasto(id_gasto):
    conexion = conectar()
    cursor = conexion.cursor()

    cursor.execute("DELETE FROM Gastos WHERE id = ?", id_gasto)

    conexion.commit()
    conexion.close()
    console.print("[green]✅ Gasto eliminado[/green]")

def guardar_categoria(nombre):
    conexion = conectar()
    cursor = conexion.cursor()

    cursor.execute(
        "INSERT INTO Categorias (nombre) VALUES (?)",
        nombre
    )

    conexion.commit()
    conexion.close()
    console.print("[green]✅ Categoría guardada[/green]")


def listar_categorias():
    conexion = conectar()
    cursor = conexion.cursor()

    cursor.execute("SELECT id, nombre FROM Categorias")
    filas = cursor.fetchall()
    conexion.close()
    return filas

def total_por_categoria():          # ← AGREGAR AQUÍ, al final
    conexion = conectar()
    cursor = conexion.cursor()

    cursor.execute("""
        SELECT c.nombre, SUM(g.monto) AS total
        FROM Gastos g
        JOIN Categorias c ON g.categoria_id = c.id
        GROUP BY c.nombre
    """)

    filas = cursor.fetchall()
    conexion.close()
    return filas

if __name__ == "__main__":
    try:
        conn = conectar()
        console.print("[green]✅ Conexión exitosa a SQL Server[/green]")
        conn.close()
    except Exception as e:
        console.print(f"[red]❌ Error al conectar: {e}[/red]")
        

