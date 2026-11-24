import ollama

def ask_ai(prompt):

    system_prompt = """
```

    You are Jarvis, an advanced AI assistant inspired by Tony Stark's JARVIS.

    Rules:

    * Address the user as Boss or Sir.
    * Speak intelligently and naturally.
    * Be friendly and witty.
    * Use light humor occasionally.
    * Ask follow-up questions when appropriate.
    * Be supportive and encouraging.
    * Keep responses concise.
    """

    try:

  
        response = ollama.chat(
            model="phi3:latest",
            messages=[
                {
                    "role": "system",
                    "content": system_prompt
                },
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )

        return response["message"]["content"]


    except Exception as e:

        print("PHI3 ERROR:", e)

    try:

        response = ollama.chat(
            model="tinyllama:latest",
            messages=[
                {
                    "role": "system",
                    "content": system_prompt
                },
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )

        return response["message"]["content"]

    except Exception as e2:

        print("TINYLLAMA ERROR:", e2)

        return "Sorry Boss, my AI systems appear to be offline."

