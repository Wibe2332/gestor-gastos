
class Categoria:
    def __init__(self, nombre):
        self.nombre = nombre

    def __str__(self):
        return self.nombre


class Gasto:
    def __init__(self, descripcion, monto, categoria, fecha=None):
        self.descripcion = descripcion
        self.monto = monto
        self.categoria = categoria
        self.fecha = fecha

    def __str__(self):
        return f"{self.fecha} | {self.descripcion} | ${self.monto} | {self.categoria}"