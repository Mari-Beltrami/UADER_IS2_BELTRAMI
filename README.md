# Ingeniería de Software II - UADER FCyT Concepción del Uruguay

📚 Repositorio de trabajo para la materia **Ingeniería de Software II** – Año 2025  
👩‍💻 Carrera: Licenciatura en Sistemas de Información  
📁 Docente: Dr. Colla Pedro  
📌 Alumna: Beltrami, María Lourdes

---

## 📂 Estructura del repositorio

El proyecto tiene la siguiente estructura de carpetas hasta el momento:

```
├── src/
│   ├── factorial/            # Códigos del TP1 sobre factorial
│   │   ├── factorial.py
│   │   └── factorial_OOP.py
│   └── chatGPT/
│       ├── chatgpt.py                # Código final del TP2
│       ├── resultado_multimetric.txt # Memoria del análisis multimetric        
│       └── .gitignore
│   ├── collatz.py            # Cálculo de secuencias de Collatz
│   ├── doc/                  # Documentación y recursos teóricos
│   └── bin/, script/         # Estructura de carpetas para futuros TPs
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
📝 [Memoria resultados de multimetric] (https://github.com/Mari-Beltrami/UADER_IS2_BELTRAMI/blob/main/src/chatGPT/resultado_multimetric.txt) 
---

## 📌 Próximos TPs

| TP | Tema | Estado |
|----|------|--------|
| TP1 | Gestión de la Configuración + Python | ✅ Finalizado |
| TP2 | Arquitectura | ✅ Finalizado |
| TP3 | Patrones de creación | 🕸️ En desarrollo |
| TP4 | *(a completar más adelante)* | 🔒 Pendiente |

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

