"""
modelo/dispositivo.py
=====================
El MODELO: aqui solo definimos QUE es un dispositivo y como saber si una
IP esta bien escrita. Nada mas: no pide datos ni muestra menus.
"""

class Dispositivo:
    # Un dispositivo guarda 4 datos: nombre, ip, tipo y estado.
    def __init__(self, nombre, ip, tipo):
        self.nombre = nombre
        self.ip = ip
        self.tipo = tipo
        self.estado = "encendido"
