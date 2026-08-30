from modelos import Categoria, Gasto
from database import guardar_gasto

cat = Categoria("Entretenimiento")
g1 = Gasto("Cine", 500, cat)

guardar_gasto(g1, 1)   # el 1 es el id de "Entretenimiento" en SQL Server