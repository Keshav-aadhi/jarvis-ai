from fastapi import APIRouter

router = APIRouter()


@router.get("/")
def home():
    return {"message": "Jarvis API running"}


@router.get("/start")
def start_jarvis():
    return {
        "status": "online",
        "message": "Jarvis is running"
    }