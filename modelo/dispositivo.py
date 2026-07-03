"""
modelo/dispositivo.py
=====================
El MODELO: aqui solo definimos QUE es un dispositivo y como saber si una
IP esta bien escrita. Nada mas: no pide datos ni muestra menus.
"""


def validar_ip(ip):
    # Una IP valida tiene 4 numeros del 0 al 255 separados por puntos.
    # Ejemplo valido: 192.168.1.1
    partes = ip.split(".")

    if len(partes) != 4:
        return False

    for parte in partes:
        if not parte.isdigit():
            return False
        numero = int(parte)
        if numero < 0 or numero > 255:
            return False

    return True


class Dispositivo:
    # Un dispositivo guarda 4 datos: nombre, ip, tipo y estado.
    def __init__(self, nombre, ip, tipo):
        self.nombre = nombre
        self.ip = ip
        self.tipo = tipo
        self.estado = "encendido"
