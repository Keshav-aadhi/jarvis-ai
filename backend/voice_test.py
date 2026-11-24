import pyttsx3

engine = pyttsx3.init()

print("Starting voice test...")

engine.say("Hello boss")

engine.runAndWait()

print("Voice test finished.")