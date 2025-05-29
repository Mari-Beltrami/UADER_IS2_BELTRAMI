# Ingeniería de Software II - UADER FCyT Concepción del Uruguay

📚 Repositorio de trabajo para la materia **Ingeniería de Software II** – Año 2025  
👩‍💻 Carrera: Licenciatura en Sistemas de Información  
📁 Docente: Dr. Colla Pedro  
📌 Alumna: Beltrami, María Lourdes

---

## 📂 Estructura del repositorio

El proyecto tiene la siguiente estructura de carpetas hasta el momento:

```
src/
├── factorial/ #Códigos del TP1 sobre factorial
│ ├── factorial.py
│ └── factorial_OOP.py
├── chatGPT/ #Códigos del TP2 sobre la API de ChatGPT
│ ├── chatgpt.py
│ ├── resultado_multimetric.txt #Memoria del análisis multimetric
│ └── .gitignore
├── tp3/ #Códigos del TP3 sobre Patrones de Creación
│ ├── ejercicio1.py #Singleton – Factorial
│ ├── ejercicio2.py #Singleton – Impuestos
│ ├── ejercicio3.py #Factory Method – Hamburguesas
│ ├── ejercicio4.py #Factory Method – Facturas
│ ├── ejercicio5.py #Builder – Avión
│ ├── ejercicio6.py #Prototype – Clonación
│ └── ejercicio7.txt #Abstract Factory – Justificación conceptual
├── tp4/                          # Códigos del TP4 sobre Patrones Estructurales
│   ├── ejercicio1.py             # Proxy
│   ├── ejercicio2.py             # Bridge
│   ├── ejercicio3.py             # Composite
│   ├── ejercicio4.py             # Decorator
│   └── ejercicio5.py             # Flyweight (Dentro del código está comentada la idea)
├── tp5/                          # Códigos del TP4 sobre Patrones Estructurales
│   ├── ejercicio1.py            
│   ├── ejercicio2.py            
│   ├── ejercicio3.py             
│   ├── ejercicio4.py             
│   └── ejercicio5.py     
├── tp6/ # Códigos del TP6 sobre Ingeniería Reversa
│   ├── getJason.py # Código corregido desde el .pyc original
│   ├── sitedata.json # Archivo de prueba con los tokens
│   └── getJason.pyc # Versión compilada original (bytecode)     
├── tp7/ # Códigos del TP7
│   ├── getJason.py       # Código final refactorizado con Singleton, robustez y branching by abstraction
│   ├── sitedata.json     # Archivo de prueba con claves y tokens para validar funcionamiento
│   └── getJason.pyc      # Archivo compilado original (bytecode) que fue base para la ingeniería reversa
├── tp8/ # Códigos del TP8
│   ├── get_jason.py      # Código final refactorizado con re-ingeniería, versión 1.2, Singleton, Chain of Responsibility e Iterator
│   ├── sitedata.json     # Archivo JSON con las claves de los bancos, usado por el Singleton TokenReader
│   └── getJason.pyc      # Archivo compilado original (bytecode) que fue base para aplicar ingeniería reversa, refactorización y re-ingeniería
├── collatz.py #Conjetura de Collatz con gráfico
├── doc/ 
├── bin/ 
└── script/ 
```
---

## ✅ TP1 – Gestión de la Configuración y Programación Python

**Objetivo:** familiarizarse con el control de versiones, GitHub y programación estructurada y orientada a objetos en Python.

### Actividades desarrolladas:

- ✔️ Instalación de Git, Python 3 y pip
- ✔️ Creación de repositorio GitHub con estructura: `src`, `doc`, `bin`, `script`
- ✔️ Subida de archivo `primos.py` y simulación de pérdida + recuperación vía Git
- ✔️ Uso de `README.md` con formato Markdown
- ✔️ Instalación de `matplotlib` y generación de gráficos con `line.py`
- ✔️ Desarrollo completo de:
  - `factorial.py`: cálculo de factorial con soporte para rangos (4-8), `-10`, `5-`
  - `factorial_OOP.py`: versión orientada a objetos con clase y método `run(min,max)`
  - `collatz.py`: conjetura de Collatz para n ∈ [1, 10000] + gráfico de pasos
- ✔️ Sincronización de todos los cambios con GitHub

### Capturas o recursos:

📝 [TP 1 FINAL](https://docs.google.com/document/d/1Dzc15F1y19sDcs5hDmzbuyzJrYl2byIaSQNTp71mulw/edit?usp=sharing)

## TP2 – Arquitectura del Software y Calidad del Código

**Objetivo:** desarrollar una aplicación en Python que interactúe con la API de ChatGPT desde consola, con funcionalidades específicas como historial de conversación, uso de variables de entorno, control de errores, y posterior análisis de calidad con herramientas estáticas.

### Actividades desarrolladas en este caso:

- ✔️ Configuración de entorno virtual (`venv`) en Linux Mint
- ✔️ Instalación de dependencias: `openai`, `python-dotenv`, `pylint`, `multimetric`
- ✔️ Desarrollo del script `chatgpt.py` con:
  - Uso de variables de entorno desde `.env` para ocultar la API Key
  - Soporte para Windows y Linux (`readline`)
  - Validación de entrada vacía
  - Modo conversacional activado con `--convers`
  - Historial de preguntas y respuestas
  - Captura de errores con `try/except`
- ✔️ Modularización del código en funciones:
  - `obtener_consulta()`
  - `construir_mensajes()`
  - `obtener_respuesta_chatgpt()`
- ✔️ Incorporación de docstrings y reordenamiento de imports
- ✔️ Ejecución de análisis con `multimetric` y `pylint`
  - Análisis de métricas Halstead, ciclomática, mantenimiento, comentarios
  - Correcciones aplicadas para subir el puntaje de `pylint`
- ✔️ Revisión del código por ChatGPT con sugerencias para futuras mejoras

### Métricas obtenidas:

- `comment_ratio`: 31.10%
- `cyclomatic_complexity`: 7
- `halstead_effort`: 43436.36
- `halstead_timerequired`: 2413.13 seg
- `halstead_bugprop`: 0.586
- `maintainability_index`: 60.5
- `pylint score`: 5.45/10 → 8.70/10 luego de correcciones

### Capturas o recursos:

📝 [TP 2 FINAL](https://docs.google.com/document/d/1i1W88IJGQceqJWMwR5wzTOzjfpeBcEXOvT0Q40yctd4/edit?usp=sharing)

📝 [Memoria resultados de multimetric](https://github.com/Mari-Beltrami/UADER_IS2_BELTRAMI/blob/main/src/chatGPT/resultado_multimetric.txt)

## TP3 – Patrones de Creación

**Objetivo:** aplicar los principales patrones de diseño creacionales (Singleton, Factory Method, Builder y Prototype) para resolver distintos ejercicios en Python, basados en situaciones prácticas del desarrollo de software.

### Actividades desarrolladas:

- ✔️ Análisis de los distintos patrones de creación y su aplicabilidad en casos concretos
- ✔️ Implementación del patrón **Singleton** para:
  - Cálculo de factorial reutilizable desde una única instancia
  - Servicio de cálculo de impuestos (IVA, IIBB, contribuciones municipales)
- ✔️ Implementación del patrón **Factory Method** para:
  - Diferentes métodos de entrega de hamburguesas (mostrador, retiro, delivery)
  - Emisión de facturas según condición impositiva del cliente
- ✔️ Implementación del patrón **Builder** para la construcción paso a paso de un objeto complejo: un avión con cuerpo, alas, turbinas y tren de aterrizaje
- ✔️ Implementación del patrón **Prototype** para clonar objetos de forma segura, incluyendo la clonación de clones
- ✔️ Justificación escrita de cada elección de patrón en función del problema planteado
- ✔️ Redacción de una situación real donde sería útil aplicar el patrón **Abstract Factory** (sin implementación requerida)

### Capturas o recursos:

📝 [TP 3 FINAL (expliación de patrones utilizados)](https://docs.google.com/document/d/1E7eUtB18OApEi_NZP_vQOc4jI_WAVJU2WyaGRjGD7JY/edit?usp=sharing)

📝 [Archivos subidos](https://github.com/Mari-Beltrami/UADER_IS2_BELTRAMI/tree/main/src/tp3)

## TP4 – Patrones Estructurales

**Objetivo:** implementar distintos patrones de diseño estructurales (Proxy, Bridge, Composite, Decorator, Flyweight), aplicándolos a problemas específicos modelados en Python.

### Actividades desarrolladas:

- ✔️ Implementación del patrón **Proxy** para controlar el acceso a una clase que realiza operaciones de red (`ping`), redirigiendo o validando según la IP
- ✔️ Implementación del patrón **Bridge** para desacoplar una lámina de acero de su método de producción, permitiendo seleccionar entre dos trenes laminadores
- ✔️ Implementación del patrón **Composite** para modelar un ensamblado jerárquico de subconjuntos y piezas, incluyendo un subconjunto adicional opcional
- ✔️ Implementación del patrón **Decorator** para aplicar modificaciones sucesivas sobre un número original, anidando operaciones como suma, multiplicación y división
- ✔️ Justificación conceptual del patrón **Flyweight** con ejemplo aplicado a la reutilización de caracteres en un editor de texto, optimizando memoria

📝 [Archivos subidos](https://github.com/Mari-Beltrami/UADER_IS2_BELTRAMI/tree/main/src/tp4)

## TP5 – Patrones de Comportamiento

**Objetivo:** aplicar los principales patrones de comportamiento (Chain of Responsibility, Iterator, Observer, State, Memento)

### Actividades desarrolladas:
- ✔️ Implementación del patrón **Chain of Responsibility** 
- ✔️ Implementación del patrón **Iterator** 
- ✔️ Implementación del patrón **Observer** 
- ✔️ Modificación del archivo `IS2_taller_scanner.py` 
- ✔️ Modificación del archivo `IS2_taller_memory.py` 

📝 [Archivos subidos](https://github.com/Mari-Beltrami/UADER_IS2_BELTRAMI/tree/main/src/tp5)

## TP6 – Ingeniería Reversa, Re-factoría y Re-Ingeniería

**Objetivo:** aplicar la metodología de ingeniería reversa sobre un programa legado compilado (`getJason.pyc`), recuperar su código fuente, corregirlo según la documentación, y dejarlo listo para su reutilización. Finalmente, realizar casos de prueba que validen su funcionamiento.

### Actividades desarrolladas:

- ✔️ Análisis de los archivos proporcionados: `getJason.pyc`, `sitedata.json` y consigna del TP.
- ✔️ Ejecución del archivo `.pyc` para observar su comportamiento: se detectó que el programa no coincidía con la documentación, ya que tomaba el argumento como nombre de archivo, no como clave de un JSON.
- ✔️ Aplicación de los 6 pasos de la metodología de Ingeniería Reversa:
  1. Recolección de artefactos
  2. Ejecución y observación del sistema
  3. Comparación con la documentación esperada
  4. Identificación de estructuras clave
  5. Formulación de hipótesis de funcionamiento
  6. Plan de ingeniería inversa
- ✔️ Decompilación del archivo con la herramienta PyLingual y obtención del código original.
- ✔️ Verificación del código decompilado: reproduce el mismo error que el binario original.
- ✔️ Identificación de diferencias con la documentación: el archivo esperaba como argumento el nombre de archivo y usaba la clave fija `"token1"`, cuando debía aceptar cualquier clave como argumento y usar `"token1"` como valor por defecto.
- ✔️ Reescritura del archivo `getJason.py` para:
  - Leer siempre desde el archivo `sitedata.json`
  - Usar como argumento la clave a recuperar (si no se indica ninguna, toma `"token1"`)
- ✔️ Documentación del nuevo código con ejemplo de uso y encabezado formal.
- ✔️ Ejecución de **casos de prueba** con diferentes argumentos, incluyendo claves válidas, inválidas y ausencia de argumento. El script respondió correctamente en todos los casos esperados.

### Casos de prueba:

| Nº | Comando ejecutado                         | Salida esperada              | Resultado |
|----|-------------------------------------------|------------------------------|-----------|
| 1  | `python3 getJason.py`                     | `C598-ECF9-F0F7-881A`        | ✅ OK     |
| 2  | `python3 getJason.py token1`              | `C598-ECF9-F0F7-881A`        | ✅ OK     |
| 3  | `python3 getJason.py token2`              | `C598-ECF9-F0F7-881B`        | ✅ OK     |

### Recursos:

📝 [Archivos subidos](https://github.com/Mari-Beltrami/UADER_IS2_BELTRAMI/tree/main/src/tp6)
📝 [TP6 RESULTADO FINAL](https://docs.google.com/document/d/18IJth5XFlOHihDJImOKLCpE1Z0Lgl79sHB3ZxaBN8nk/edit?tab=t.0)

## TP7 – Re-factorización

**Objetivo:** aplicar la metodología de re-factorización sobre el programa `getJason.py` previamente recuperado en el TP6, reorganizándolo con programación orientada a objetos, aplicando el patrón Singleton, mejorando la robustez y la calidad del código, y utilizando estrategias como branching by abstraction.

### Actividades desarrolladas:

- ✔️ Transformación del código para usar programación orientada a objetos.
- ✔️ Implementación del patrón **Singleton** para asegurar una única instancia.
- ✔️ Inclusión de control robusto de errores para evitar fallas no controladas.
- ✔️ Aplicación de **branching by abstraction** para permitir usar la versión antigua o la nueva.
- ✔️ Incorporación de una opción `-v` para mostrar la versión del programa (`versión 1.1`).
- ✔️ Adición de comentarios explicativos y carátula legal con copyright.
- ✔️ Ejecución del analizador estático **pylint** y corrección de observaciones hasta alcanzar un puntaje ≥ 8/10.

### Resultado pylint:

✅ El código final alcanzó un puntaje de **8.83/10**, cumpliendo con el requisito del práctico.

### Recursos:

📝 [Archivos subidos](https://github.com/Mari-Beltrami/UADER_IS2_BELTRAMI/tree/main/src/tp7)
📝 [TP7 RESULTADO FINAL](https://docs.google.com/document/d/18IJth5XFlOHihDJImOKLCpE1Z0Lgl79sHB3ZxaBN8nk/edit?usp=sharing)

## TP8 – Re-ingeniería

**Objetivo:** aplicar la metodología de re-ingeniería sobre el programa `get_jason.py`, reorganizándolo para automatizar la selección del banco, mejorar la mantenibilidad, y aplicar nuevos patrones de diseño, dejando el sistema listo para evolucionar a futuro.

### Actividades desarrolladas:

- ✔️ Automatización de la selección de banco para pagos, eliminando la decisión manual.
- ✔️ Implementación del patrón **Singleton** para acceder a claves de los bancos desde `sitedata.json`.
- ✔️ Aplicación del patrón **Chain of Responsibility** para controlar las cuentas y balancear pagos entre ellas.
- ✔️ Aplicación del patrón **Iterator** para listar pagos realizados de forma cronológica.
- ✔️ Inclusión de una opción `-v` para mostrar la versión (`1.2`).
- ✔️ Manejo robusto de errores, evitando caídas inesperadas.
- ✔️ Documentación detallada con carátula, comentarios y docstrings.
- ✔️ Ejecución del analizador estático **pylint**, obteniendo un puntaje final de **8.83/10**.

### Recursos:

📝 [Archivos subidos](https://github.com/Mari-Beltrami/UADER_IS2_BELTRAMI/tree/main/src/tp8)
📝 [TP8 RESULTADO FINAL](https://docs.google.com/document/d/1-pMSWu814CG5S1Y0ML0KHon1BgDR6Yifd4HkiKfZFcw/edit?usp=sharing)

---

## 📌 Próximos TPs

| TP | Tema | Estado |
|----|------|--------|
| TP1 | Gestión de la Configuración + Python | ✅ Finalizado |
| TP2 | Arquitectura | ✅ Finalizado |
| TP3 | Patrones de creación | ✅ Finalizado  |
| TP4 | Patrones estructurales | ✅ Finalizado |
| TP5 | Patrones de comportamiento | ✅ Finalizado |
| TP6 | Ingeniería reversa | ✅ Finalizado |
| TP7 | Re-factorización | ✅ Finalizado |
| TP8 | Re-ingeniería | ✅ Finalizado |
| TP9 | ... | 🕸️ En desarrollo |
| TP10 | *(a completar más adelante)* | 🔒 Pendiente |
---

## Referencias

- [Python.org](https://www.python.org)
- [GitHub Docs](https://docs.github.com)
- [Matplotlib](https://matplotlib.org)
- [Conjetura de Collatz - Wikipedia](https://es.wikipedia.org/wiki/Conjetura_de_Collatz)

---

## Figura del Proyecto

![Figura del proyecto](/is2_readme.jpg)

---

