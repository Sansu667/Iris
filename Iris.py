import pyttsx3
import speech_recognition as sr
import pywhatkit
import yfinance as yf
import pyjokes
import webbrowser
import datetime
import wikipedia

# Escuchar y reconocer la voz del usuario con el micrófono del sistema 

def transformar_audio_en_texto():

    # Inicializar el reconocedor de voz
    r = sr.Recognizer() 
    
    # Usar el micrófono del sistema
    
    with sr.Microphone() as source:
        r.pause_threshold = 0.8 # Tiempo de pausa para considerar que terminó la frase
        print('Escuchando...') # Mensaje para el usuario
        audio = r.listen(source) # Escuchar el audio del usuario
        
        try:
            # Buscar en la web
            pedido = r.recognize_google(audio, language='es-ar') # Reconocer el audio
            
            print('Has dicho: ' + pedido) # Mostrar el texto reconocido
            
            return pedido # Devolver el texto reconocido

        except sr.UnknownValueError:
            print('No se ha entendido el audio') # Mensaje para el usuario en caso de no entender el audio
            
            return 'No se ha entendido el audio' # Devolver un mensaje de error
        
        except sr.RequestError:
            print('No hay conexión a internet') # Mensaje para el usuario en caso de no tener conexión a internet
            
            return 'No hay conexión a internet' # Devolver un mensaje de error

        except:
            print('Error desconocido') # Mensaje para el usuario en caso de un error desconocido
            
            return 'Error desconocido' # Devolver un mensaje de error

# Hablar con el usuario

def hablar(mensaje):
    
    # Inicializar el motor de texto a voz
    engine = pyttsx3.init()
    
    # Establecer el idioma
    engine.setProperty('rate', 150) # Velocidad de habla
    engine.setProperty('volume', 1) # Volumen
    
    voices = engine.getProperty('voices') # Obtener las voces disponibles
    engine.setProperty('voice', voices[0].id) # Establecer la voz
    
    # Hablar el mensaje
    engine.say(mensaje)
    engine.runAndWait()
    
    # Cerrar el motor
    engine.stop()

# Informar el día de la semana

def informar_dia_de_la_semana():
        
        # Obtener la fecha actual
        fecha = datetime.date.today()
        print(fecha)
        
        # Obtener el día de la semana
        dia = fecha.weekday()
        print(dia)
        
        # Diccionario con los días de la semana
        dias = {0: 'lunes', 1: 'martes', 2: 'miércoles', 3: 'jueves', 4: 'viernes', 5: 'sábado', 6: 'domingo'}
        
        # Informar el día de la semana
        hablar('Hoy es ' + dias[dia])
        
# Informar la hora actual

def informar_hora_actual():
        
        # Obtener la hora actual
        hora = datetime.datetime.now().strftime('%I:%M %p')
        
        # Informar la hora actual
        hablar('La hora actual es ' + hora)

# Saludo inicial

def saludo_inicial():
    
    # Obtener la hora actual
    hora = datetime.datetime.now().hour
    
    # Saludo de acuerdo a la hora del día
    if hora >= 0 and hora < 12:
        hablar('Buenos días, soy Iris, tu asistente virtual')
    elif hora >= 12 and hora < 18:
        hablar('Buenas tardes, soy Iris, tu asistente virtual')
    else:
        hablar('Buenas noches, soy Iris, tu asistente virtual')
        
    hablar('¿En qué puedo ayudarte?')
    
# Funcion central

def pedir_cosas():
    
    saludo_inicial() # Saludo inicial
    
    comenzar = True # Bandera para comenzar el ciclo
    
    while comenzar:
        
        pedido = transformar_audio_en_texto().lower() # Transformar el audio en texto
        
        if 'abre youtube' in pedido: # Reproducir música en YouTube
            hablar("Iniciando YouTube...")
            webbrowser.open('https://www.youtube.com')
            continue
        elif "reproduce" in pedido: # Reproducir música en YouTube
            cancion = pedido.replace("reproduce", "")
            hablar("Reproduciendo " + cancion + " en YouTube...")
            pywhatkit.playonyt(cancion)
            continue
        elif "abre google" in pedido: # Abrir Google
            hablar("Iniciando Google...")
            webbrowser.open('https://www.google.com')
            continue
        elif 'abre gmail' in pedido: # Abrir Gmail
            hablar("Iniciando Gmail...")
            webbrowser.open('https://mail.google.com')
            continue
        elif "qué día es hoy" in pedido: # Informar el día de la semana
            informar_dia_de_la_semana()
            continue
        elif "qué hora es" in pedido: # Informar la hora actual
            informar_hora_actual()
            continue
        elif "chiste" in pedido: # Contar un chiste
            chiste = pyjokes.get_joke("es", "neutral")
            hablar(chiste)
            continue
        elif "busca en wikipedia" in pedido:
            hablar("Buscando en Wikipedia...")
            pedido = pedido.replace("buscar en wikipedia", "")
            wikipedia.set_lang("es") # Establecer el idioma de búsqueda
            resultado = wikipedia.summary(pedido, sentences=2) # Buscar en Wikipedia
            hablar("Según Wikipedia...") # Informar al usuario  
            hablar(resultado) # Mostrar el resultado
            continue
        
        elif "busca en google" in pedido:
            hablar("Buscando en Google...")
            pedido = pedido.replace("buscar en google", "")
            webbrowser.open('https://www.google.com/search?q=' + pedido)
            
            continue
        elif "enviar mensaje de whatsapp" in pedido:
            hablar("Enviando mensaje de WhatsApp...")
            pedido = pedido.replace("enviar mensaje de whatsapp", "")
            pywhatkit.sendwhatmsg("+5491122334455", pedido, 0, 0)
            continue
        
        elif "desactívate" in pedido:
            hablar("Hasta luego, que tengas un buen día")
            comenzar = False
            break
        
        
        
pedir_cosas() # Llamar a la función central
    