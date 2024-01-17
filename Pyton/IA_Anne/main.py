import pyttsx3
import speech_recognition as sr
import webbrowser
import wikipedia
import datetime
import cv2
import requests
import json

# Função para converter texto em fala.
def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

# Função para reconhecer fala do usuário.

def recognize_speech():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("Ouvindo...")
        try:
            audio = recognizer.listen(source, timeout=5)
            print("Reconhecendo...")
            query = recognizer.recognize_google(audio, language='pt-BR')
            print(f"Usuário disse: {query}\n")
            return query.lower() if query else None
        except sr.UnknownValueError:
            print("Não entendi. Poderia repetir?")
        except sr.RequestError as e:
            print(f"Erro durante o reconhecimento de fala: {e}")
        return None

#  Função para abrir aplicativos ou sites.
    
def open_application(query):   
    if 'youtube' in query:
        webbrowser.open('https://www.youtube.com')
    elif 'gmail' in query:
        webbrowser.open('https://mail.google.com')
    elif 'google' in query:
        webbrowser.open('https://www.google.com')
    elif 'stack overflow' in query:
        webbrowser.open('https://stackoverflow.com')

# Função para obter a hora atual.
def get_current_time():
   
    current_time = datetime.datetime.now().strftime("%H:%M:%S")
    speak(f"A hora atual é {current_time}")

# Função para capturar uma foto.
def take_photo():
    
    cap = cv2.VideoCapture(0)
    cap.set(3, 640)
    cap.set(4, 480)

    result = True
    while result:
        ret, frame = cap.read()
        cv2.imshow('Tirar uma foto', frame)

        if cv2.waitKey(1) & 0xFF == ord('s'):
            cv2.imwrite('foto.jpg', frame)
            result = False

    cap.release()
    cv2.destroyAllWindows()

    speak("Foto tirada com sucesso")

# Função para pesquisar na Wikipedia.
    
def search_wikipedia(query):
    
    wiki_wiki = wikipedia.Wikipedia('pt-BR')

    page_py = wiki_wiki.page(query)

    if page_py.exists():
        results = page_py.text[:500]
        speak(f"De acordo com a Wikipedia, {results}")
    else:
        speak("Desculpe, não encontrei nada sobre isso na Wikipedia.")

# Função para prever o clima.
        
def predict_weather(city):   
    API_KEY = "sua_chave_api"
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}"

    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        temp = data['main']['temp']
        description = data['weather'][0]['description']
        speak(f"A temperatura em {city} é de {temp} graus Celsius, e o clima está {description}.")
    else:
        speak("Desculpe, não consegui obter informações sobre o clima para a cidade especificada.")

# Função para obter as principais manchetes de notícias.

def get_top_headlines():
    API_KEY = "sua_chave_api"
    url = f"https://newsapi.org/v2/top-headlines?country=br&apiKey={API_KEY}"

    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        articles = data['articles']

        for article in articles:
            speak(f"{article['title']} - {article['description']}")
    else:
        speak("Desculpe, não consegui obter as últimas manchetes.")

 # Função principal que interage com o usuário:
        
def main():
    speak("Olá, eu sou a Anne sua assistente pessoal virtual, como posso te ajudar hoje?")
    while True:
        query = recognize_speech()
        if query:
            if 'hora' in query:
                get_current_time()
            elif 'foto' in query:
                take_photo()
            elif 'pesquisar na wikipedia' in query:
                query = query.replace("pesquisar na wikipedia", "")
                search_wikipedia(query)
            elif 'clima' in query:
                query = query.replace("clima", "")
                city = query
                predict_weather(city)
            elif 'manchetes' in query:
                get_top_headlines()
            elif 'abrir' in query:
                query = query.replace("abrir", "")
                open_application(query)
            else:
                speak("Desculpe, não entendi isso.")
        else:
            speak("Desculpe, não consegui reconhecer sua fala. Poderia repetir?")

if __name__ == '__main__':
    main()
