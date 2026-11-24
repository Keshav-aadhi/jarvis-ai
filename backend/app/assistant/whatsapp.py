import webbrowser
import urllib.parse
import time
import pyautogui

def send_whatsapp_message(phone_number, message):


    try:

        phone_number = str(phone_number).replace(
            " ",
            ""
        )

        if not phone_number.startswith("91"):

            phone_number = "91" + phone_number

        encoded_message = urllib.parse.quote(
            message
        )

        url = (
            f"https://web.whatsapp.com/send?"
            f"phone={phone_number}"
            f"&text={encoded_message}"
        )

        webbrowser.open(url)

        time.sleep(12)

        pyautogui.press("enter")

        return "WhatsApp message sent."

    except Exception as e:

        print(
            "WHATSAPP ERROR:",
            e
        )

        return "Unable to send WhatsApp message."
