def normalize_tamil_command(command):

    replacements = {
        "weather enna": "weather",
        "time enna": "time",
        "google open pannu": "open google",
        "youtube open pannu": "open youtube",
        "chatgpt open pannu": "open chatgpt",
        "battery evlo iruku": "battery",
        "charging aagutha": "charging",
        "news sollu": "news",
        "sports news sollu": "sports news",
        "technology news sollu": "technology news",
        "sleep pannu": "go to sleep",
        "screenshot edu": "screenshot",
        "downloads open pannu": "open downloads",
        "desktop open pannu": "open desktop",
        "documents open pannu": "open documents"
    }

    command = command.lower()

    return replacements.get(command, command)

