import speech_recognition as sr
import pyttsx3
import threading
from app.assistant.tamil_helper import normalize_tamil_command

def speak(text):

    print("Jarvis:", text)

    def worker():

        try:

            engine = pyttsx3.init()

            engine.say(text)

            engine.runAndWait()

            engine.stop()

        except Exception as e:

            print("SPEAK ERROR:", e)

    threading.Thread(
        target=worker,
        daemon=True
    ).start()


def listen():

    recognizer = sr.Recognizer()

    try:

        with sr.Microphone() as source:

            print("\nListening...\n")

            recognizer.adjust_for_ambient_noise(source, duration=1)

            audio = recognizer.listen(source)

        command = recognizer.recognize_google(audio)
        

        command = command.lower()
        

        command = normalize_tamil_command(command)

        print("You said:", command)

        return command

    except Exception as e:

        print("MIC ERROR:", e)

        return ""