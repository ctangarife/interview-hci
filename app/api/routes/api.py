from fastapi import APIRouter, HTTPException
from app.services.llm_service import LLMService
from app.services.tts_service import TTSService

router = APIRouter()
llm_service = LLMService()
tts_service = TTSService()

@router.post("/generate-response")
async def generate_response(prompt: str):
    try:
        response = await llm_service.generate_response(prompt)
        return {"response": response}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/text-to-speech")
async def text_to_speech(text: str):
    try:
        audio_path = await tts_service.generate_speech(text)
        return {"audio_path": audio_path}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))