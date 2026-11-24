from datetime import datetime
from app.assistant.speech import listen, speak
from app.assistant.commands import execute_command
from app.assistant.memory import remember, recall
from app.assistant.reminder import (
    add_reminder,
    get_reminders,
    clear_reminders,
    timed_reminder
)
from app.services.openai_service import ask_ai
from app.assistant.weather import get_weather
from app.assistant.news import get_news
from app.assistant.whatsapp import send_whatsapp_message

def run_jarvis():

    active = False

    speak("Jarvis initialized and waiting for wake word.")

    while True:

        command = listen()

        if not command:
            continue

        # WAKE WORD
        if not active and "hey jarvis" in command:

            active = True

            speak("Yes Boss, I am listening.")

            continue

        # IGNORE UNTIL ACTIVATED
        if not active:
            continue

        # SLEEP MODE
        if "go to sleep" in command:

            active = False

            speak("Going to sleep mode.")

            continue

        # SHUTDOWN
        if "shutdown buddy" in command:

            speak("Shutting down. Goodbye.")

            break

        # TIME
        if "time" in command:

            current_time = datetime.now().strftime("%I:%M %p")

            speak(f"The time is {current_time}")

            continue

        # DATE
        if "date" in command:

            today = datetime.now().strftime("%d %B %Y")

            speak(f"Today's date is {today}")

            continue

        # ABOUT JARVIS
        if "what is your name" in command:

            speak("My name is Jarvis.")

            continue

        if "who created you" in command:

            speak("I was created by my boss.")

            continue

        if "what can you do" in command:

            speak(
                "I can open applications, browse websites, remember information, answer questions, and assist you."
            )

            continue

        # NAME MEMORY
        if "my name is" in command:

            name = command.replace("my name is", "").strip()

            remember("name", name)

            speak(f"I will remember your name is {name}")

            continue

        if "what is my name" in command:

            name = recall("name")

            if name:

                speak(f"Your name is {name}")

            else:

                speak("I do not know your name yet")

            continue

        # GENERIC MEMORY
        if command.startswith("remember "):

            text = command.replace("remember ", "").strip()

            if " is " in text:

                key, value = text.split(" is ", 1)

                remember(key.strip(), value.strip())

                speak(f"I will remember that {key} is {value}")

            else:

                speak("Please tell me what to remember.")

            continue

        # GENERIC RECALL
        if command.startswith("what is "):

            key = command.replace("what is ", "").strip()

            value = recall(key)

            if value:

                speak(f"{key} is {value}")

                continue
            
        # TIMED REMINDER
        if "remind me in" in command:

            try:

                text = command.replace(
                    "remind me in",
                    ""
                ).strip()

                parts = text.split()

                minutes = int(parts[0])

                task = " ".join(parts[3:])

                timed_reminder(
                    minutes,
                    task
                )

                speak(
                    f"Okay boss. I will remind you in {minutes} minutes."
                )

            except:

                speak(
                    "Please say, remind me in 5 minutes to drink water."
                )

            continue
        # REMINDERS
        if "remind me to" in command:

            task = command.replace(
                "remind me to",
                ""
            ).strip()

            add_reminder(task)

            speak(f"Reminder saved: {task}")

            continue

        if "show reminders" in command:

            reminders = get_reminders()

            if not reminders:

                speak("You have no reminders.")

            else:

                speak(f"You have {len(reminders)} reminders.")

                for reminder in reminders:

                    speak(reminder["text"])

            continue

        if "clear reminders" in command:

            clear_reminders()

            speak("All reminders have been cleared.")

            continue
        # WEATHER
        if "weather" in command:

            weather_info = get_weather("Chennai")

            speak(weather_info)

            continue

        if "temperature" in command:

            weather_info = get_weather("Chennai")

            speak(weather_info)

            continue
        # TAMIL NADU NEWS
        if "tamil nadu news" in command:

            speak(
                get_news("tamilnadu")
            )

            continue


        # AI NEWS
        if "ai news" in command:

            speak(
                get_news("ai")
            )

            continue


        # TECHNOLOGY NEWS
        if "technology news" in command:

            speak(
                get_news("technology")
            )

            continue


        # SPORTS NEWS
        if "sports news" in command:

            speak(
                get_news("sports")
            )

            continue


        # GENERAL NEWS
        if "news" in command:

            speak(
                get_news("india")
            )

            continue
    
        # WHATSAPP MESSAGE
        if command.startswith("message "):

            try:

                text = command.replace("message ", "").strip()

                if " on whatsapp " not in text:

                    speak(
                        "Please say message mum on whatsapp hello"
                    )

                    continue

                contact, message = text.split(
                    " on whatsapp ",
                    1
                )

                phone_number = recall(
                    contact.strip()
                )

                if not phone_number:

                    speak(
                        f"I do not know the contact {contact}"
                    )

                    continue

                response = send_whatsapp_message(
                    phone_number,
                    message
                )

                speak(response)

                continue

            except Exception as e:

                print(
                    "WHATSAPP ERROR:",
                    e
                )

                speak(
                    "Unable to open WhatsApp."
                )

                continue

        # COMMANDS
        result = execute_command(command)

        if result:

            speak(result)

            continue

        # AI RESPONSE
        response = ask_ai(command)

        if response:

            speak(response[:700])

        else:

            speak("I could not generate a response.")