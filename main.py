"""
main.py
=======
Este es el archivo que se ejecuta para USAR el programa.

# Es cortisimo a proposito: solo crea la Vista y la enciende. La Vista
# muestra el menu; el Modelo dice que es un dispositivo; el Controlador
# guarda y lee los datos.
#
# Para ejecutar el programa, desde la carpeta del proyecto:
#     python main.py
"""

from vista.consola import Vista


def main():
    programa = Vista()
    programa.iniciar()


if __name__ == "__main__":
    main()
