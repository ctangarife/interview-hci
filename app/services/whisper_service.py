#app/services/whisper_service.py
import whisper
from datetime import datetime
import os
from concurrent.futures import ThreadPoolExecutor

class WhisperService:
    def __init__(self):
        self.model = whisper.load_model("small")
        self.output_dir = "/app/interview/transcriptions"
        self.executor = ThreadPoolExecutor()

    def start_transcription(self, audio_path: str, original_filename: str) -> dict:
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        output_filename = f"{timestamp}_{original_filename.replace(' ', '_')}.txt"
        output_path = os.path.join(self.output_dir, output_filename)

        # Iniciar procesamiento en segundo plano
        self.executor.submit(self._process_transcription, audio_path, output_path)

        # Devolvemos información sin esperar
        return {
            "message": "Transcription started",
            "status": "processing",
            "file_path": output_path
        }

    def _process_transcription(self, audio_path: str, output_path: str):
        try:
            result = self.model.transcribe(audio_path)
            with open(output_path, 'w', encoding='utf-8') as f:
                f.write(result["text"])
        except Exception as e:
            print(f"Error in transcription: {str(e)}")
        finally:
            if os.path.exists(audio_path):
                os.unlink(audio_path)