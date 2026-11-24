import webbrowser
import subprocess
import os
import psutil
import pyautogui
import platform
from app.assistant.volume import (
    volume_up,
    volume_down,
    mute_volume,
    unmute_volume
)
from app.assistant.search import (
    search_google,
    search_youtube,
    play_youtube_video
)
def execute_command(command):

    # OPEN YOUTUBE
    if "open youtube" in command:

        webbrowser.open("https://youtube.com")

        return "Opening YouTube"

    # OPEN GOOGLE
    if "open google" in command:

        webbrowser.open("https://google.com")

        return "Opening Google"

    # OPEN CHATGPT
    if "open chatgpt" in command:

        webbrowser.open("https://chatgpt.com")

        return "Opening ChatGPT"

    # OPEN NOTEPAD
    if "open notepad" in command:

        subprocess.Popen("notepad.exe")

        return "Opening Notepad"

    # OPEN CALCULATOR
    if "open calculator" in command:

        subprocess.Popen("calc.exe")

        return "Opening Calculator"

    # OPEN FILE EXPLORER
    if "open explorer" in command:

        subprocess.Popen("explorer.exe")

        return "Opening File Explorer"

    # CLOSE NOTEPAD
    if "close notepad" in command:

        os.system("taskkill /f /im notepad.exe")

        return "Closing Notepad"

    # CLOSE CALCULATOR
    if "close calculator" in command:

        os.system("taskkill /f /im CalculatorApp.exe")
        os.system("taskkill /f /im calc.exe")

        return "Closing Calculator"

    # CLOSE GOOGLE / YOUTUBE / CHATGPT / BROWSER
    if (
        "close google" in command
        or "close youtube" in command
        or "close chatgpt" in command
        or "close browser" in command
    ):

        os.system("taskkill /f /im chrome.exe")
        os.system("taskkill /f /im msedge.exe")
        os.system("taskkill /f /im firefox.exe")

        return "Closing browser"

    # CLOSE CHROME
    if "close chrome" in command:

        os.system("taskkill /f /im chrome.exe")

        return "Closing Chrome"

    # CLOSE EDGE
    if "close edge" in command:

        os.system("taskkill /f /im msedge.exe")

        return "Closing Edge"

    # CLOSE EXPLORER
    if "close explorer" in command:

        os.system("taskkill /f /im explorer.exe")
        subprocess.Popen("explorer.exe")

        return "Restarting Explorer"

    # BATTERY
    if "battery" in command:

        battery = psutil.sensors_battery()

        if battery:

            return f"Your battery is at {battery.percent} percent"

        return "Unable to read battery information"

    # CHARGING STATUS
    if "charging" in command:

        battery = psutil.sensors_battery()

        if battery and battery.power_plugged:

            return "Yes, your laptop is charging"

        return "No, your laptop is not charging"

    # CPU USAGE
    if "cpu usage" in command:

        cpu = psutil.cpu_percent(interval=1)

        return f"CPU usage is {cpu} percent"

    # RAM USAGE
    if "ram usage" in command:

        ram = psutil.virtual_memory()

        return f"RAM usage is {ram.percent} percent"

    # DISK SPACE
    if "disk space" in command:

        disk = psutil.disk_usage("C:\\")

        free = round(disk.free / (1024 ** 3), 2)

        total = round(disk.total / (1024 ** 3), 2)

        return (
            f"Disk has {free} gigabytes free "
            f"out of {total} gigabytes"
        )

    # SYSTEM INFO
    if "system info" in command:

        system = platform.system()

        version = platform.release()

        processor = platform.processor()

        return (
            f"You are running "
            f"{system} {version} "
            f"on {processor}"
        )

    # SCREENSHOT
    if "screenshot" in command:

        desktop = os.path.join(
            os.path.expanduser("~"),
            "Desktop"
        )

        file_path = os.path.join(
            desktop,
            "jarvis_screenshot.png"
        )

        screenshot = pyautogui.screenshot()

        screenshot.save(file_path)

        return "Screenshot saved on your desktop"

    # OPEN DOWNLOADS
    if "open downloads" in command:

        path = os.path.join(
            os.path.expanduser("~"),
            "Downloads"
        )

        subprocess.Popen(f'explorer "{path}"')

        return "Opening Downloads folder"

    # OPEN DOCUMENTS
    if "open documents" in command:

        path = os.path.join(
            os.path.expanduser("~"),
            "Documents"
        )

        subprocess.Popen(f'explorer "{path}"')

        return "Opening Documents folder"

    # OPEN DESKTOP
    if "open desktop" in command:

        path = os.path.join(
            os.path.expanduser("~"),
            "Desktop"
        )

        subprocess.Popen(f'explorer "{path}"')

        return "Opening Desktop folder"
    # VOLUME UP
    if "volume up" in command:

        return volume_up()

    # VOLUME DOWN
    if "volume down" in command:

        return volume_down()

    # MUTE
    if "mute volume" in command:

        return mute_volume()

    # UNMUTE
    if "unmute volume" in command:

        return unmute_volume()
    
    # PLAY SONG / VIDEO
    if command.startswith("play "):

        query = command.replace(
            "play",
            ""
        ).strip()

        return play_youtube_video(query)

    # GOOGLE SEARCH
    if command.startswith("search google for "):

        query = command.replace(
            "search google for",
            ""
        ).strip()

        return search_google(query)

    # YOUTUBE SEARCH
    if command.startswith("search youtube for "):

        query = command.replace(
            "search youtube for",
            ""
        ).strip()

        return search_youtube(query)
    return None