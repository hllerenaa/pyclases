"""
vista/consola.py
================
La VISTA: muestra el menu, pide los datos por teclado y muestra los
resultados. Es la parte que "se ve". Cuando hay que guardar o leer datos,
le pide ayuda al Controlador.
"""

from controlador.controlador import Controlador


class Vista:

    def __init__(self):
        # La Vista usa un Controlador para guardar y leer los datos.
        self.controlador = Controlador()

    def iniciar(self):
        # Este es el menu principal: se repite hasta que el usuario elige salir.
        while True:
            print("\n----- SISTEMA DE DISPOSITIVOS -----")
            print("1. Agregar dispositivo")
            print("2. Listar dispositivos")
            print("3. Editar dispositivo")
            print("4. Eliminar dispositivo")
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

    def mostrar(self, dispositivos):
        # Muestra la lista numerada (1, 2, 3...).
        if len(dispositivos) == 0:
            print("\nNo hay dispositivos guardados.")
            return
        print("\n----- DISPOSITIVOS -----")
        numero = 1
        for d in dispositivos:
            print(f"{numero}. {d.nombre} | IP: {d.ip} | Tipo: {d.tipo} | Estado: {d.estado}")
            numero = numero + 1

    def agregar(self):
        nombre = input("Nombre: ")
        tipo = input("Tipo (router, switch, servidor...): ")
        ip = input("Ingresar IP: ")
        self.controlador.agregar(nombre, ip, tipo)
        print("\nDispositivo agregado.")

    def listar(self):
        dispositivos = self.controlador.listar()
        self.mostrar(dispositivos)

    def editar(self):
        dispositivos = self.controlador.listar()
        self.mostrar(dispositivos)
        if len(dispositivos) == 0:
            return

        numero = input("\nNumero del dispositivo a editar: ")
        if not numero.isdigit():
            print("Eso no es un numero.")
            return
        numero = int(numero)
        if numero < 1 or numero > len(dispositivos):
            print("Ese numero no esta en la lista.")
            return

        print("Escribe los datos nuevos:")
        nombre = input("Nombre: ")
        tipo = input("Tipo (router, switch, servidor...): ")
        ip = input("Ingresar IP: ")
        self.controlador.editar(numero, nombre, ip, tipo)
        print("\nDispositivo actualizado.")

    def eliminar(self):
        dispositivos = self.controlador.listar()
        self.mostrar(dispositivos)
        if len(dispositivos) == 0:
            return

        numero = input("\nNumero del dispositivo a eliminar: ")
        if not numero.isdigit():
            print("Eso no es un numero.")
            return
        numero = int(numero)
        if numero < 1 or numero > len(dispositivos):
            print("Ese numero no esta en la lista.")
            return

        self.controlador.eliminar(numero)
        print("\nDispositivo eliminado.")
