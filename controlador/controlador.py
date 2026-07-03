"""
controlador/controlador.py
==========================
El CONTROLADOR: solo se encarga de GUARDAR y LEER los dispositivos en el
archivo. No muestra menus ni pide datos (de eso se encarga la Vista).

# Cada dispositivo se guarda como una linea de texto separada por comas:
#   Router-Sala1,192.168.1.1,router,encendido
"""

import os

from modelo.dispositivo import Dispositivo


class Controlador:

    def __init__(self):
        # Preparamos la ruta del archivo: media/basededatos.txt
        raiz = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        carpeta = os.path.join(raiz, "media")
        os.makedirs(carpeta, exist_ok=True)   # crea la carpeta si no existe
        self.archivo = os.path.join(carpeta, "basededatos.txt")

    def listar(self):
        # Lee el archivo y devuelve una lista de dispositivos.
        dispositivos = []
        try:
            with open(self.archivo, "r", encoding="utf-8") as archivo:
                for linea in archivo:
                    linea = linea.strip()
                    if linea == "":
                        continue
                    nombre, ip, tipo, estado = linea.split(",")
                    d = Dispositivo(nombre, ip, tipo)
                    d.estado = estado
                    dispositivos.append(d)
        except FileNotFoundError:
            # Si el archivo todavia no existe, devolvemos la lista vacia.
            pass
        return dispositivos

    def guardar(self, dispositivos):
        # Escribe TODA la lista en el archivo (borra lo viejo y pone lo nuevo).
        with open(self.archivo, "w", encoding="utf-8") as archivo:
            for d in dispositivos:
                archivo.write(f"{d.nombre},{d.ip},{d.tipo},{d.estado}\n")

    def agregar(self, nombre, ip, tipo):
        dispositivos = self.listar()
        dispositivos.append(Dispositivo(nombre, ip, tipo))
        self.guardar(dispositivos)

    def editar(self, numero, nombre, ip, tipo):
        dispositivos = self.listar()
        dispositivos[numero - 1] = Dispositivo(nombre, ip, tipo)  # -1: las listas empiezan en 0
        self.guardar(dispositivos)

    def eliminar(self, numero):
        dispositivos = self.listar()
        dispositivos.pop(numero - 1)   # -1: las listas empiezan en 0
        self.guardar(dispositivos)
