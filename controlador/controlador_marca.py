"""
controlador/controlador_marca.py
================================
Controlador para CRUD de marcas. Persiste en media/basededatos_marcas.txt
Cada marca se guarda en una linea: Nombre,Orden
"""

import os

from modelo.marca import Marca


class ControladorMarca:

    def __init__(self):
        raiz = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        carpeta = os.path.join(raiz, "media")
        os.makedirs(carpeta, exist_ok=True)
        self.archivo = os.path.join(carpeta, "basededatos_marcas.txt")

    def listar(self):
        marcas = []
        try:
            with open(self.archivo, "r", encoding="utf-8") as archivo:
                for linea in archivo:
                    linea = linea.strip()
                    if linea == "":
                        continue
                    nombre, orden = linea.split(",")
                    m = Marca(nombre, orden)
                    marcas.append(m)
        except FileNotFoundError:
            pass
        return marcas

    def guardar(self, marcas):
        with open(self.archivo, "w", encoding="utf-8") as archivo:
            for m in marcas:
                archivo.write(f"{m.nombre},{m.orden}\n")

    def agregar(self, nombre, orden):
        marcas = self.listar()
        marcas.append(Marca(nombre, orden))
        self.guardar(marcas)

    def editar(self, numero, nombre, orden):
        marcas = self.listar()
        marcas[numero - 1] = Marca(nombre, orden)
        self.guardar(marcas)

    def eliminar(self, numero):
        marcas = self.listar()
        marcas.pop(numero - 1)
        self.guardar(marcas)
