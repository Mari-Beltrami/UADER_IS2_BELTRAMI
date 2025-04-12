#importación de librerías necesarias para el funcionamiento del programa
import openai
from dotenv import load_dotenv
import os
import platform  #para determinar si se está usando Windows y evitar errores con readline
import sys       #es para leer argumentos como --convers
from datetime import datetime  #para incluir la fecha actual en el mensaje del sistema

#para importar readline según sistema operativo pq hubo error con WINDOWS y el cursor up
if platform.system() == "Windows":
    import pyreadline3 as readline
else:
    import readline

#esto es para cargar la clave API desde el archivo .env (mayor seguridad para poder subir el código a github)
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

#acá verifica si se pasa el argumento --convers
modo_conversacion = False
if len(sys.argv) > 1 and sys.argv[1] == "--convers":
    modo_conversacion = True

#buffer de conversación (si está activado)
historial = []

print("Bienvenido al asistente ChatGPT. Escribí tu consulta o Ctrl+C para salir.\n")

#función para generar el mensaje del sistema incluyendo la fecha actual
def generar_mensaje_sistema():
    fecha_actual = datetime.now().strftime("%A %d de %B de %Y")
    return f"Hoy es {fecha_actual}. Sos un asistente que responde en español de forma clara y breve."

#comienza el bucle principal del programa
while True:
    try:
        #leer la entrada del usuario
        consulta = input("Tu consulta: ").strip()

        if not consulta:
            print("La consulta no puede estar vacía.")
            continue

        #agregar "You: " antes de mostrar
        entrada_usuario = "You: " + consulta
        print(entrada_usuario)

        #acá se arman los mensajes según el modo conversacional
        mensajes = [
            {"role": "system", "content": generar_mensaje_sistema()}
        ]

        if modo_conversacion:
            #si hay historial, lo agregamos como parte del contexto
            mensajes.extend(historial)

        #agregar la nueva consulta
        mensajes.append({"role": "user", "content": entrada_usuario})

        #llamar a la API de OpenAI (esto puede fallar, por eso está en try)
        try:
            respuesta = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=mensajes,
                temperature=1,
                max_tokens=4096,
                top_p=1,
                frequency_penalty=0,
                presence_penalty=0
            )
        except Exception as api_error:
            print("Error al comunicarse con la API:", api_error)
            continue

        #obtener el texto de la respuesta
        respuesta_texto = respuesta['choices'][0]['message']['content']

        #mostrar respuesta con "chatGPT: " al inicio
        print("chatGPT:", respuesta_texto)

        if modo_conversacion:
            #agregar consulta y respuesta al historial
            historial.append({"role": "user", "content": entrada_usuario})
            historial.append({"role": "assistant", "content": respuesta_texto})

    except KeyboardInterrupt:
        print("\nSesión finalizada por el usuario. Chauu!")
        break
    except Exception as e:
        print("Ocurrió un error inesperado:", e)
