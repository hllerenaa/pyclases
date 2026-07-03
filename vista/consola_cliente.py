"""
vista/consola_cliente.py
========================
La VISTA de clientes: muestra el menu, pide los datos por teclado y muestra
los resultados. Cuando hay que guardar o leer, le pide ayuda al Controlador.
"""

from controlador.controlador_cliente import ControladorCliente


class VistaCliente:

    def __init__(self):
        # La Vista usa un Controlador para guardar y leer los datos.
        self.controlador = ControladorCliente()

    def iniciar(self):
        # Menu de clientes: se repite hasta que el usuario elige salir.
        while True:
            print("\n----- SISTEMA DE CLIENTES -----")
            print("1. Agregar cliente")
            print("2. Listar clientes")
            print("3. Editar cliente")
            print("4. Eliminar cliente")
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

    def pedir_edad(self):
        # Pide la edad y no deja avanzar hasta que sea un numero.
        edad = input("Edad: ")
        while not edad.isdigit():
            print("La edad debe ser un numero.")
            edad = input("Edad: ")
        return edad

    def mostrar(self, clientes):
        # Muestra la lista numerada (1, 2, 3...).
        if len(clientes) == 0:
            print("\nNo hay clientes guardados.")
            return
        print("\n----- CLIENTES -----")
        numero = 1
        for c in clientes:
            print(f"{numero}. {c.nombre} {c.apellidos} | Edad: {c.edad}")
            numero = numero + 1

    def agregar(self):
        nombre = input("Nombre: ")
        apellidos = input("Apellidos: ")
        edad = self.pedir_edad()
        self.controlador.agregar(nombre, apellidos, edad)
        print("\nCliente agregado.")

    def listar(self):
        clientes = self.controlador.listar()
        self.mostrar(clientes)

    def editar(self):
        clientes = self.controlador.listar()
        self.mostrar(clientes)
        if len(clientes) == 0:
            return

        numero = input("\nNumero del cliente a editar: ")
        if not numero.isdigit():
            print("Eso no es un numero.")
            return
        numero = int(numero)
        if numero < 1 or numero > len(clientes):
            print("Ese numero no esta en la lista.")
            return

        print("Escribe los datos nuevos:")
        nombre = input("Nombre: ")
        apellidos = input("Apellidos: ")
        edad = self.pedir_edad()
        self.controlador.editar(numero, nombre, apellidos, edad)
        print("\nCliente actualizado.")

    def eliminar(self):
        clientes = self.controlador.listar()
        self.mostrar(clientes)
        if len(clientes) == 0:
            return

        numero = input("\nNumero del cliente a eliminar: ")
        if not numero.isdigit():
            print("Eso no es un numero.")
            return
        numero = int(numero)
        if numero < 1 or numero > len(clientes):
            print("Ese numero no esta en la lista.")
            return

        self.controlador.eliminar(numero)
        print("\nCliente eliminado.")
