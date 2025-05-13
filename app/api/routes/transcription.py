#app/api/routes/transcription.py
from fastapi import APIRouter, UploadFile, File, HTTPException
from app.services.whisper_service import WhisperService
import tempfile
import os

router = APIRouter()
whisper_service = WhisperService()

@router.post("/transcribe")
async def transcribe_audio(audio: UploadFile = File(...)):
    temp_audio = None
    try:
        temp_audio = tempfile.NamedTemporaryFile(delete=False, suffix=os.path.splitext(audio.filename)[1])
        content = await audio.read()
        temp_audio.write(content)
        temp_audio.flush()
        temp_path = temp_audio.name
        temp_audio.close()

        # No esperamos el resultado
        whisper_service.start_transcription(temp_path, audio.filename)

        return {
            "message": "Transcription started",
            "status": "processing"
        }
    except Exception as e:
        if temp_audio and os.path.exists(temp_audio.name):
            os.unlink(temp_audio.name)
        raise HTTPException(status_code=500, detail=str(e))