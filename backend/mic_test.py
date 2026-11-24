import speech_recognition as sr

recognizer = sr.Recognizer()

print("CHECKING MICROPHONE...")


try:

    mic = sr.Microphone()

    print("MICROPHONE DETECTED")

    with mic as source:

        print("Listening...")

        recognizer.adjust_for_ambient_noise(source)

        audio = recognizer.listen(source)

    print("Recognizing...")

    text = recognizer.recognize_google(audio)

    print("You said:", text)

except Exception as e:

    print("ERROR:", e)