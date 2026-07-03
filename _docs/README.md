# Sistema de Registro de Dispositivos (MVC por carpetas)

**Asignatura:** Lenguaje de Programación Python
**Carrera:** Infraestructura de Redes y Ciberseguridad
**Docente:** Ing. Héctor Llerena — Máster en Inteligencia de Negocios
**Periodo:** ISTER 2026-1

---

## ¿Qué hace el programa?

Es un pequeño sistema de consola para registrar dispositivos de red
(nombre, IP, tipo). Permite **agregar, listar, editar y eliminar**
dispositivos, y guarda todo en un archivo de texto para no perder los datos
al cerrar el programa.

Menú del programa:

```
1. Agregar dispositivo
2. Listar dispositivos
3. Editar dispositivo
4. Eliminar dispositivo
5. Salir
```

---

## La idea central: separar el código en 3 partes (MVC)

En lugar de un solo archivo gigante, el programa está dividido en **3
carpetas**, cada una con una sola tarea. A esto se le llama patrón
**MVC (Modelo - Vista - Controlador)**:

| Carpeta | Nombre (MVC) | Su única tarea |
|---|---|---|
| `modelo/` | **Modelo** | Dice **qué es** un dispositivo (clase `Dispositivo`) y cómo saber si una IP es válida (`validar_ip`). |
| `vista/` | **Vista** | **Manda:** muestra el menú, pide los datos y muestra los resultados. Es lo que se ve. |
| `controlador/` | **Controlador** | **Guarda y lee** los datos en el archivo. No muestra ni pide nada. |

Cómo se conectan (muy simple, siempre en un solo sentido):

```
main.py  ->  Vista  ->  Controlador  ->  archivo .txt
                 \-----> Modelo (para revisar la IP)
```

La **Vista** es la que manda: cuando el usuario elige una opción, la Vista
hace su trabajo y, si necesita guardar o leer datos, le pide ayuda al
**Controlador**.

---

## Estructura de carpetas

```
pyclases/
├── main.py                     ← se ejecuta ESTE para usar el programa
│
├── modelo/
│   ├── __init__.py             ← (vacío) convierte la carpeta en "paquete"
│   └── dispositivo.py          ← clase Dispositivo + validar_ip()
│
├── vista/
│   ├── __init__.py
│   └── consola.py              ← clase Vista (menú y todo lo que se ve)
│
├── controlador/
│   ├── __init__.py
│   └── controlador.py          ← clase Controlador (guardar/leer/editar/eliminar)
│
├── media/
│   └── basededatos.txt         ← trae 3 dispositivos de ejemplo (ver abajo)
│
└── docs/
    └── README.md               ← este archivo
```

> El archivo `__init__.py` va **vacío**. Solo sirve para que Python trate la
> carpeta como un "paquete" y podamos escribir, por ejemplo,
> `from modelo.dispositivo import Dispositivo`.

---

## ¿Qué hay dentro de cada archivo?

### `modelo/dispositivo.py` — el Modelo (lo más corto)
- La función **`validar_ip(ip)`**: dice si una IP tiene 4 números del 0 al
  255 separados por puntos.
- La **clase `Dispositivo`**: guarda 4 datos (`nombre`, `ip`, `tipo`,
  `estado`). Nada más.

### `vista/consola.py` — la Vista (la que manda)
La **clase `Vista`** tiene:
- `iniciar()` → muestra el menú y lo repite hasta que se elige salir.
- `agregar()`, `listar()`, `editar()`, `eliminar()` → cada opción del menú.
- `pedir_ip()` → pide la IP hasta que sea válida.
- `mostrar(lista)` → imprime la lista numerada.

### `controlador/controlador.py` — el Controlador (solo datos)
La **clase `Controlador`** solo toca el archivo:
- `agregar(nombre, ip, tipo)` → guarda un dispositivo nuevo.
- `listar()` → devuelve la lista de dispositivos guardados.
- `editar(numero, ...)` → cambia un dispositivo.
- `eliminar(numero)` → borra un dispositivo.
- `guardar(lista)` → escribe toda la lista en el archivo.

### `main.py` — el arranque
Es cortísimo: solo crea la `Vista` y la enciende con `iniciar()`.

---

## Cómo se guardan los datos

Los dispositivos se guardan en `media/basededatos.txt`. El proyecto ya
**incluye un archivo de ejemplo con 3 dispositivos**, para que al elegir
"2. Listar" se vea algo de inmediato (y se pueda probar editar y eliminar)
sin tener que registrar primero:

```
Router-Sala1,192.168.1.1,router,encendido
Switch-Lab,10.0.0.5,switch,encendido
Servidor-Web,192.168.1.100,servidor,apagado
```

> ¿Quieres empezar de cero? Borra el contenido de `media/basededatos.txt`
> (o el archivo entero: el programa lo vuelve a crear solo al agregar el
> primer dispositivo).

Cada dispositivo es una línea con los datos separados por comas (como un CSV). No es casualidad: cada
línea es como una futura **fila** de una tabla y cada dato como una futura
**columna**, para cuando más adelante cambiemos este archivo por una base
de datos **SQLite**.

Para editar o eliminar, el programa **lee toda la lista, la cambia y la
vuelve a escribir completa**. Es la forma más simple de hacerlo con un
archivo de texto (y también deja ver por qué una base de datos real será
más cómoda).

---

## Cómo ejecutar el programa

Abre una terminal **en la carpeta del proyecto** (`pyclases/`) y escribe:

```
python main.py
```

(En Linux/Mac puede ser `python3 main.py`.) No hay que crear la carpeta
`media/` a mano: el programa la crea sola.

> **Importante:** el único archivo que se ejecuta es `main.py`. Los demás
> archivos (`modelo/`, `vista/`, `controlador/`) **no** se ejecutan solos:
> solo guardan sus clases y funciones para que `main.py` las use. Por eso
> hay un solo `main` en todo el proyecto.

---

## Guía rápida para explicar en clase

1. **Empieza por el Modelo** (`modelo/dispositivo.py`): es lo más corto.
   `validar_ip` es una función y `Dispositivo` es una clase (repaso del foro).
2. **Sigue con el Controlador** (`controlador/controlador.py`): solo guarda
   y lee del archivo. Recorran `agregar`, `listar`, `editar`, `eliminar`.
3. **Termina con la Vista** (`vista/consola.py`): es la que manda. El menú
   está dentro de `iniciar()` y cada opción llama a un método corto.
4. **Muestra `main.py`**: lo corto que es y que solo enciende la Vista.

**Idea que deben llevarse:** cada carpeta tiene una sola tarea. Si falla
cómo se ve el menú → Vista. Si falla una regla (como la IP) → Modelo. Si
falla el guardado → Controlador. No hay que buscar en un archivo gigante.

**Preguntas típicas:**
- *¿Por qué `validar_ip` está en el Modelo y no en la Vista?* Porque es una
  **regla del dato**; la Vista solo la usa para revisar lo que se escribe.
- *¿Para qué el `__init__.py` vacío?* Para que la carpeta sea un paquete y
  se pueda importar (`from modelo.dispositivo import ...`).
- *¿Por qué `while` al pedir la IP?* Con `if` se revisa una vez; con `while`
  se sigue pidiendo hasta que esté bien.
- *¿Por qué al editar o eliminar se reescribe todo el archivo?* Porque en un
  archivo de texto es lo más simple: leer la lista, cambiarla y guardarla.

**Cierre sugerido:** abre `basededatos.txt` y pregunta: *"¿y si hubiera mil
dispositivos y quisiéramos buscar solo los apagados?"*. Esa incomodidad es
el gancho natural hacia la próxima unidad de **bases de datos (SQLite)**.

---

**Ing. Héctor Llerena, MSc** — Lenguaje de Programación Python — ISTER 2026-1
