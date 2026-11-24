from threading import Thread
import uvicorn

from app.assistant.brain import run_jarvis


def start_jarvis():

    jarvis_thread = Thread(
        target=run_jarvis,
        daemon=True
    )

    jarvis_thread.start()


if __name__ == "__main__":

    start_jarvis()

    uvicorn.run(
        "app.main:app",
        host="127.0.0.1",
        port=8000,
        reload=True
    )