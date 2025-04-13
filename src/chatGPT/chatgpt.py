"""
Este programa permite interactuar desde consola con la API de OpenAI (ChatGPT).
Trabajo Práctico 2 - Ingeniería de Software II
"""

#importación de librerías necesarias para el funcionamiento del programa
import os
import platform  #para determinar si se está usando Windows y evitar errores con readline
import sys       #es para leer argumentos como --convers

#importación de librerías externas
import openai
from dotenv import load_dotenv

#en Linux readline ya está disponible, pero por compatibilidad lo importamos según el sistema operativo
if platform.system() == "Windows":
    import pyreadline3 as readline  #No se usa directamente, pero activa el historial en Windows
else:
    try:
        import readline  #No se usa directamente, pero activa el historial en Linux
    except ImportError:
        print("readline no está disponible, historial con flechas no activado")

#esto es para cargar la clave API desde el archivo .env (mayor seguridad para poder subir el código a github)
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

#acá verifica si se pasa el argumento --convers
modo_conversacion = False  # pylint: disable=invalid-name
if len(sys.argv) > 1 and sys.argv[1] == "--convers":
    modo_conversacion = True  # pylint: disable=invalid-name

#buffer de conversación (si está activado)
historial = []

#función para obtener la consulta del usuario
def obtener_consulta():
    """Solicita una consulta por teclado y la valida."""
    consulta = input("Tu consulta: ").strip()
    if not consulta:
        print("La consulta no puede estar vacía.")
        return None
    return "You: " + consulta

#función para construir el mensaje que se enviará a la API
def construir_mensajes(entrada_usuario):
    """Construye la estructura de mensajes para enviar a ChatGPT."""
    mensajes = [
        {
            "role": "system",
            "content": (
                "Sos un asistente que responde en español "
                "de forma clara y precisa."
            )
        }
    ]
    if modo_conversacion:
        mensajes.extend(historial)
    mensajes.append({"role": "user", "content": entrada_usuario})
    return mensajes

#función para enviar los mensajes a la API y obtener la respuesta
def obtener_respuesta_chatgpt(mensajes):
    """Envía los mensajes a la API de ChatGPT y devuelve la respuesta."""
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
        return respuesta['choices'][0]['message']['content']
    except Exception as api_error:  #pylint: disable=broad-exception-caught
        print("Error al comunicarse con la API:", api_error)
        return None

#inicio del programa
print("Bienvenido al asistente ChatGPT. Escribí tu consulta o Ctrl+C para salir.\n")

#comienza el bucle principal del programa
while True:
    try:
        entrada_usuario = obtener_consulta()
        if not entrada_usuario:
            continue

        print(entrada_usuario)
        mensajes = construir_mensajes(entrada_usuario)
        respuesta_texto = obtener_respuesta_chatgpt(mensajes)

        if respuesta_texto:
            print("chatGPT:", respuesta_texto)
            if modo_conversacion:
                historial.append({"role": "user", "content": entrada_usuario})
                historial.append({"role": "assistant", "content": respuesta_texto})

    except KeyboardInterrupt:
        print("\nSesión finalizada por el usuario. ¡chauu!")
        break
    except Exception as e:  # pylint: disable=broad-exception-caught
        print("Ocurrió un error inesperado:", e)


