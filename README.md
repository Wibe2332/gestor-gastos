# Gestor de Gastos Personales

Aplicación de consola en Python para registrar, editar y consultar gastos personales, con persistencia en SQL Server y conversión de moneda en tiempo real mediante una API externa.

Proyecto de aprendizaje, construido desde cero para practicar programación orientada a objetos, SQL relacional, consumo de APIs y control de versiones con Git.

## Funcionalidades

- Registrar gastos con descripción, monto, fecha y categoría
- Crear categorías nuevas o elegir entre las existentes
- Ver todos los gastos registrados
- Editar y eliminar gastos por ID
- Convertir el total de gastos a USD usando una tasa de cambio en tiempo real

## Tecnologías

- **Python** — lógica de la aplicación, programación orientada a objetos
- **SQL Server** — base de datos relacional para persistencia
- **pyodbc** — conexión entre Python y SQL Server
- **requests** — consumo de la API de tasas de cambio
- **Git / GitHub** — control de versiones

## Cómo ejecutarlo

1. Clonar el repositorio
2. Crear un entorno virtual: `python -m venv venv`
3. Activarlo: `.\venv\Scripts\Activate.ps1`
4. Instalar dependencias: `pip install -r requirements.txt`
5. Crear la base de datos en SQL Server (ver `schema.sql`)
6. Ejecutar: `python main.py`

## Estructura del proyecto



## Autor

Wilberth