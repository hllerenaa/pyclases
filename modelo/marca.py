"""
modelo/marca.py
===============
Define el MODELO de una marca: nombre y orden (numérico).
"""


class Marca:
    # Una marca guarda 2 datos: nombre y orden.
    def __init__(self, nombre, orden):
        self.nombre = nombre
        self.orden = orden
