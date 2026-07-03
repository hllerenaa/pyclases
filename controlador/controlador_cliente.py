"""
controlador/controlador_cliente.py
==================================
El CONTROLADOR de clientes: solo GUARDA y LEE los clientes en el archivo.
No muestra menus ni pide datos (de eso se encarga la Vista).

# Cada cliente se guarda como una linea de texto separada por comas:
#   Ana,Perez Lopez,25
"""

import os

from modelo.cliente import Cliente


class ControladorCliente:

    def __init__(self):
        # Preparamos la ruta del archivo: media/clientes.txt
        raiz = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        carpeta = os.path.join(raiz, "media")
        os.makedirs(carpeta, exist_ok=True)   # crea la carpeta si no existe
        self.archivo = os.path.join(carpeta, "clientes.txt")

    def listar(self):
        # Lee el archivo y devuelve una lista de clientes.
        clientes = []
        try:
            with open(self.archivo, "r", encoding="utf-8") as archivo:
                for linea in archivo:
                    linea = linea.strip()
                    if linea == "":
                        continue
                    nombre, apellidos, edad = linea.split(",")
                    clientes.append(Cliente(nombre, apellidos, edad))
        except FileNotFoundError:
            # Si el archivo todavia no existe, devolvemos la lista vacia.
            pass
        return clientes

    def guardar(self, clientes):
        # Escribe TODA la lista en el archivo (borra lo viejo y pone lo nuevo).
        with open(self.archivo, "w", encoding="utf-8") as archivo:
            for c in clientes:
                archivo.write(f"{c.nombre},{c.apellidos},{c.edad}\n")

    def agregar(self, nombre, apellidos, edad):
        clientes = self.listar()
        clientes.append(Cliente(nombre, apellidos, edad))
        self.guardar(clientes)

    def editar(self, numero, nombre, apellidos, edad):
        clientes = self.listar()
        clientes[numero - 1] = Cliente(nombre, apellidos, edad)  # -1: las listas empiezan en 0
        self.guardar(clientes)

    def eliminar(self, numero):
        clientes = self.listar()
        clientes.pop(numero - 1)   # -1: las listas empiezan en 0
        self.guardar(clientes)
