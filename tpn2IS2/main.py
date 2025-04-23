import os
import openai
from dotenv import load_dotenv
import readline  # Para historial y tecla ↑

# Cargar la API key desde el archivo .env
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

# Contexto del asistente
context = "Eres un asistente útil y conciso."
usertask = "Interpreta las preguntas del usuario y responde de forma clara."

# Guardamos la última consulta
last_query = ""

while True:
    try:
        # Primer nivel: Aceptar entrada del usuario
        if last_query:
            readline.add_history(last_query)  # Agrega al historial si hubo una consulta anterior

        userquery = input("Ingresa tu consulta (↑ para editar la anterior, Enter vacío para salir): ").strip()

        if userquery == "":
            print("Fin del programa.")
            break

        last_query = userquery  # Guardamos la consulta para la próxima vez

        try:
            # Segundo nivel: Validar y preparar la consulta
            print("You:", userquery)

            try:
                # Tercer nivel: Invocar la API de ChatGPT
                response = openai.chat.completions.create(
                    model="gpt-4o-mini-2024-07-18",
                    response_format={ "type": "json_object" },
                    messages=[
                        { "role": "system", "content": context },
                        { "role": "user", "content": usertask },
                        { "role": "user", "content": userquery }
                    ],
                    temperature=1,
                    max_tokens=16384,
                    top_p=1,
                    frequency_penalty=0,
                    presence_penalty=0
                )

                jsonStr = response.choices[0].message.content
                print("chatGPT:", jsonStr)

            except Exception as e:
                print("❌ Error durante la invocación a la API de ChatGPT:", e)

        except Exception as e:
            print("❌ Error durante el tratamiento de la consulta:", e)

    except Exception as e:
        print("❌ Error al aceptar la consulta del usuario:", e)
