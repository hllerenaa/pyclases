# Prompt para que los estudiantes trabajen con IA (Registro de Dispositivos)

**Para el docente:** copia el bloque de abajo (dentro del recuadro de código) y
entrégalo a los estudiantes tal cual — por Moodle, en un documento o incluso
impreso. Ellos deben pegarlo como primer mensaje en su conversación con la IA
(Gemini, ChatGPT, Claude, etc.) **antes** de pedir cualquier ayuda con el
ejercicio. El prompt está escrito en primera persona porque lo va a usar el
estudiante, no tú.

La idea de este prompt no es que la IA les resuelva el ejercicio de un
tirón, sino que los obligue a ir **paso a paso**, a construir la misma
estructura por carpetas que vimos en clase, y a **explicar lo que van
entendiendo** en el camino. Así llegan a clase pudiendo explicar su propio
código, que es la condición para usar IA en esta asignatura.

**Meta del ejercicio (lo que deben lograr replicar):**

```
pyclases/
├── main.py                 ← único archivo que se ejecuta
├── modelo/
│   ├── __init__.py
│   └── dispositivo.py      ← clase Dispositivo + función validar_ip()
├── vista/
│   ├── __init__.py
│   └── consola.py          ← clase Vista (menú, pedir datos, mostrar lista)
├── controlador/
│   ├── __init__.py
│   └── controlador.py      ← clase Controlador (agregar/listar/editar/eliminar)
└── media/
    └── basededatos.txt     ← se crea solo al agregar el primero
```

---

## Prompt para copiar y entregar a los estudiantes

```
Soy estudiante de la asignatura Lenguaje de Programación Python (carrera
Infraestructura de Redes y Ciberseguridad, ISTER). Quiero que me ayudes a
construir un ejercicio paso a paso, con reglas estrictas, porque después
tengo que explicar mi código en clase sin ninguna ayuda.

LO QUE YA VIMOS EN CLASE (puedes usar esto libremente):
- Variables, tipos de datos, operadores.
- Condicionales (if/elif/else) y bucles (for, while).
- Funciones: parámetros, valores por defecto, alcance de variables (scope).
- Listas, tuplas, diccionarios y manejo de cadenas (f-strings, split).
- Programación orientada a objetos básica: class, __init__, self,
  atributos y métodos.
- Lectura y escritura de archivos de texto con open(), modos "r", "a", "w".
- Organizar un programa en CARPETAS separadas tipo Modelo - Vista -
  Controlador (MVC), donde cada carpeta es un "paquete" de Python (tiene
  un archivo __init__.py vacío) y los archivos se conectan con import,
  por ejemplo: from modelo.dispositivo import Dispositivo.

LO QUE TODAVÍA NO HE VISTO (no lo uses aunque te parezca "más elegante"):
- @property, @staticmethod, @classmethod, dataclasses.
- Herencia, clases abstractas, polimorfismo.
- Bases de datos (SQLite u otras). Por ahora guardo los datos en un
  archivo .txt.
- Librerías externas que no sean de la biblioteca estándar de Python.

QUÉ QUIERO CONSTRUIR:
Un mini sistema de consola de "Registro de Dispositivos de Red" (o el
tema que te indique más adelante), organizado EN CARPETAS así:

  main.py                    -> único archivo que se ejecuta; solo crea la
                                Vista y la enciende.
  modelo/dispositivo.py      -> clase Dispositivo (nombre, ip, tipo, estado)
                                y la función validar_ip(). Solo datos y reglas.
  controlador/controlador.py -> clase Controlador: SOLO guarda y lee los
                                datos en media/basededatos.txt. No muestra
                                menús ni pide nada por teclado.
  vista/consola.py           -> clase Vista: es la que MANDA. Muestra el menú
                                dentro de un método iniciar(), pide los datos
                                y, cuando hay que guardar o leer, le pide
                                ayuda al Controlador.

Cada carpeta (modelo, vista, controlador) debe tener un __init__.py vacío
para ser un paquete. IMPORTANTE: solo main.py se ejecuta; los demás
archivos NO tienen su propio main, solo contienen su clase o funciones.

El programa debe tener un menú con estas opciones:
1. Agregar dispositivo  (pedir nombre, tipo e IP; validar la IP).
2. Listar dispositivos  (mostrarlos numerados: 1, 2, 3...).
3. Editar dispositivo   (elegir uno por su número y cambiar sus datos).
4. Eliminar dispositivo (elegir uno por su número y borrarlo).
5. Salir.

Reglas de datos:
- La IP es válida solo si tiene 4 números del 0 al 255 separados por punto.
- Cada dispositivo se guarda como una línea de texto separada por comas,
  por ejemplo:  Router-Sala1,192.168.1.1,router,encendido
- La carpeta media/ y el archivo se deben crear solos la primera vez.
- Para probar rápido las opciones de listar, editar y eliminar sin tener
  que registrar primero, puedo crear a mano el archivo media/basededatos.txt
  con 2 o 3 líneas de ejemplo usando ese mismo formato.

CÓMO QUIERO QUE ME AYUDES (muy importante, síguelo al pie de la letra):
1. No me des todo el código de un tirón. Guíame UN ARCHIVO A LA VEZ, y
   dentro de cada archivo, una función o un método a la vez.
2. Sigue este orden: primero el Modelo (modelo/dispositivo.py), luego el
   Controlador (controlador/controlador.py), luego la Vista (vista/
   consola.py) y al final main.py. La Vista se hace después del Controlador
   porque la Vista lo usa.
3. Antes de escribir código nuevo, pregúntame qué creo yo que hay que
   hacer o qué método sigue. Espera mi respuesta.
4. Explícame el POR QUÉ de cada decisión, no solo el CÓMO. Por ejemplo:
   por qué validar_ip va en el Modelo y no en la Vista; por qué la carpeta
   necesita un __init__.py; por qué para editar o eliminar leo toda la
   lista, la cambio y la vuelvo a escribir completa.
5. Cuando me des un método, explícamelo línea por línea con palabras
   simples, como si nunca hubiera visto ese código.
6. Si me equivoco, NO me des la solución de inmediato: primero dame una
   pista y deja que lo intente otra vez.
7. Al terminar cada archivo, hazme 2 o 3 preguntas para comprobar que
   entiendo lo que escribí, antes de pasar al siguiente.
8. Cuando el programa esté completo, guíame para probarlo con
   "python main.py" y ayúdame a interpretar lo que aparece en pantalla.
9. Al final, hazme un "quiz" de 5 preguntas sobre MI propio código, para
   practicar cómo lo voy a explicar en clase.

Empecemos por el Modelo. Antes de darme nada, hazme la primera pregunta.
```

---

## Cómo se conecta este prompt con la clase

- **Refuerza el foro anterior** (función vs. clase): `validar_ip` es una
  función y `Dispositivo` es una clase; el prompt hace que el estudiante
  distinga por qué cada cosa es lo que es.
- **Obliga a construir la estructura por carpetas**, no un solo archivo,
  que es justo la habilidad nueva de esta unidad.
- **Prepara SQLite:** guardar "a mano" en un `.txt` hace evidente lo
  incómodo que es buscar/editar/eliminar en un archivo de texto, y eso es
  el gancho hacia la unidad de bases de datos.
- **Condición para usar IA:** como el prompt fuerza explicaciones paso a
  paso y un quiz final, el estudiante llega pudiendo defender su código.

**Señal de que lo hicieron bien:** pueden abrir cualquiera de sus archivos
y explicar, en sus palabras, qué hace cada clase y por qué está en esa
carpeta y no en otra.

---

**Ing. Héctor Llerena, MSc** — Lenguaje de Programación Python — ISTER 2026-1
