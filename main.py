"""
main.py
=======
Este es el archivo que se ejecuta para USAR el programa.

# Primero pregunta que quieres gestionar (dispositivos o clientes) y luego
# enciende la Vista correspondiente.
#
# Para ejecutar el programa, desde la carpeta del proyecto:
#     python main.py
"""

from vista.consola import Vista
from vista.consola_cliente import VistaCliente
from vista.consola_marca import VistaMarca


def main():
    print("===== QUE QUIERES GESTIONAR? =====")
    print("1. Dispositivos")
    print("2. Clientes")
    print("3. Marcas")
    opcion = input("Elige una opcion: ")

    if opcion == "1":
        Vista().iniciar()
    elif opcion == "2":
        VistaCliente().iniciar()
    elif opcion == "3":
        VistaMarca().iniciar()
    else:
        print("Opcion no valida.")


if __name__ == "__main__":
    main()
