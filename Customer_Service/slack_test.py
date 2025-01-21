import sys
import time
sys.path.append('/home/snparada/Spacionatural/Libraries/')

from slack_lib.messages import SlackMessages

def wait_for_response(slack, channel, thread_ts, expected_response="Si"):
    while True:
        # Leer mensajes del hilo
        messages = slack.read_thread_messages(channel, thread_ts)
        
        # Revisar si hay respuestas nuevas (ignorando el mensaje original y la pregunta)
        for message in messages[2:]:  # Ignoramos los primeros 2 mensajes
            if message.get('text') == expected_response:
                return True
        
        # Esperar 2 segundos antes de revisar nuevamente
        time.sleep(2)

# Crear instancia
slack = SlackMessages()

# Enviar mensaje inicial
result = slack.create_channel_message("test-emma", "¡Hola! Soy el nuevo bot de Spacionatural")

if result:
    print("¡Mensaje enviado exitosamente!")
    message_id = result['message_id']
    channel = result['channel']
    
    # Preguntar en el hilo
    slack.create_thread_message(channel, message_id, "¿Lo leíste?")
    
    # Esperar respuesta
    if wait_for_response(slack, channel, message_id):
        # Responder "Bacán" cuando el usuario responda "Si"
        slack.create_thread_message(channel, message_id, "Bacán")
else:
    print("Hubo un error al enviar el mensaje")