"""
vista/consola_marca.py
=======================
Vista de consola para el mantenimiento CRUD de marcas.
Pide datos por teclado y delega la persistencia al controlador.
"""

from controlador.controlador_marca import ControladorMarca


class VistaMarca:

    def __init__(self):
        self.controlador = ControladorMarca()

    def iniciar(self):
        while True:
            print("\n----- MANTENIMIENTO DE MARCAS -----")
            print("1. Agregar marca")
            print("2. Listar marcas")
            print("3. Editar marca")
            print("4. Eliminar marca")
            print("5. Salir")
            opcion = input("Elige una opcion: ")

            if opcion == "1":
                self.agregar()
            elif opcion == "2":
                self.listar()
            elif opcion == "3":
                self.editar()
            elif opcion == "4":
                self.eliminar()
            elif opcion == "5":
                print("\nHasta luego.")
                break
            else:
                print("\nOpcion no valida. Elige del 1 al 5.")

    def pedir_orden(self):
        orden = input("Orden (numero): ")
        while not orden.isdigit():
            print("El orden debe ser un numero.")
            orden = input("Orden (numero): ")
        return orden

    def mostrar(self, marcas):
        if len(marcas) == 0:
            print("\nNo hay marcas guardadas.")
            return
        print("\n----- MARCAS -----")
        numero = 1
        for m in marcas:
            print(f"{numero}. {m.nombre} | Orden: {m.orden}")
            numero = numero + 1

    def agregar(self):
        nombre = input("Nombre: ")
        orden = self.pedir_orden()
        self.controlador.agregar(nombre, orden)
        print("\nMarca agregada.")

    def listar(self):
        marcas = self.controlador.listar()
        self.mostrar(marcas)

    def editar(self):
        marcas = self.controlador.listar()
        self.mostrar(marcas)
        if len(marcas) == 0:
            return

        numero = input("\nNumero de la marca a editar: ")
        if not numero.isdigit():
            print("Eso no es un numero.")
            return
        numero = int(numero)
        if numero < 1 or numero > len(marcas):
            print("Ese numero no esta en la lista.")
            return

        print("Escribe los datos nuevos:")
        nombre = input("Nombre: ")
        orden = self.pedir_orden()
        self.controlador.editar(numero, nombre, orden)
        print("\nMarca actualizada.")

    def eliminar(self):
        marcas = self.controlador.listar()
        self.mostrar(marcas)
        if len(marcas) == 0:
            return

        numero = input("\nNumero de la marca a eliminar: ")
        if not numero.isdigit():
            print("Eso no es un numero.")
            return
        numero = int(numero)
        if numero < 1 or numero > len(marcas):
            print("Ese numero no esta en la lista.")
            return

        self.controlador.eliminar(numero)
        print("\nMarca eliminada.")
