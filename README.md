# Gestor de Gastos Personales

Aplicación de consola en Python para registrar, editar y consultar gastos personales, con persistencia en SQL Server, conversión de moneda en tiempo real mediante una API externa, y una interfaz de consola con colores y tablas.

Proyecto de aprendizaje, construido desde cero para practicar programación orientada a objetos, SQL relacional, consumo de APIs, manejo de errores y control de versiones con Git.

## Funcionalidades

- Registrar gastos con descripción, monto, fecha y categoría
- Crear categorías nuevas o elegir entre las existentes, con validación de entradas
- Ver todos los gastos registrados en una tabla
- Editar y eliminar gastos por ID
- Convertir el total de gastos a USD usando una tasa de cambio en tiempo real
- Reporte de totales por categoría y total general
- Manejo de errores en las entradas del usuario (evita que el programa se rompa con datos inválidos)
- Interfaz de consola con colores y tablas (rich)

## Tecnologías

- **Python** — lógica de la aplicación, programación orientada a objetos
- **SQL Server** — base de datos relacional para persistencia
- **pyodbc** — conexión entre Python y SQL Server
- **requests** — consumo de la API de tasas de cambio (open.er-api.com)
- **rich** — tablas y colores en la interfaz de consola
- **Git / GitHub** — control de versiones

## Cómo ejecutarlo

1. Clonar el repositorio
2. Crear un entorno virtual: `python -m venv venv`
3. Activarlo: `.\venv\Scripts\Activate.ps1`
4. Instalar dependencias: `pip install -r requirements.txt`
5. Crear la base de datos en SQL Server (ver sección "Base de datos" abajo)
6. Ejecutar: `python main.py`

## Base de datos

Ejecutar en SQL Server Management Studio:

```sql
CREATE DATABASE GestorGastos;
GO

USE GestorGastos;
GO

CREATE TABLE Categorias (
    id INT IDENTITY(1,1) PRIMARY KEY,
    nombre NVARCHAR(50) NOT NULL UNIQUE
);

CREATE TABLE Gastos (
    id INT IDENTITY(1,1) PRIMARY KEY,
    descripcion NVARCHAR(200) NOT NULL,
    monto DECIMAL(10,2) NOT NULL,
    fecha DATE NOT NULL DEFAULT GETDATE(),
    categoria_id INT NOT NULL,
    FOREIGN KEY (categoria_id) REFERENCES Categorias(id)
);
```

## Estructura del proyecto



## Posibles mejoras futuras

- Validar más entradas (fechas, montos negativos)
- Manejo de errores de conexión (SQL Server o internet caídos)
- Interfaz gráfica (Tkinter) o web (Flask)

## Autor

Wilberth