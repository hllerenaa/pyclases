"""
modelo/cliente.py
=================
El MODELO del cliente: aqui solo definimos QUE es un cliente.
Nada mas: no pide datos ni muestra menus.
"""


class Cliente:
    # Un cliente guarda 3 datos: nombre, apellidos y edad.
    def __init__(self, nombre, apellidos, edad):
        self.nombre = nombre
        self.apellidos = apellidos
        self.edad = edad
