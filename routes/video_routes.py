from uuid import UUID
from fastapi import APIRouter, File, UploadFile
from starlette import status

from models.audio import Audio
from models.video import Video

def video_router(video_model: Video, audio_model: Audio):
    router = APIRouter(tags=['Video'])

    @router.post('/', status_code=status.HTTP_200_OK, response_model=str)
    async def upload(file: UploadFile = File(...)):
        return str(await video_model.create(file))

    @router.get('/{file_id}/detect-silence', status_code=status.HTTP_200_OK, response_model=list[list[float]])
    async def detect_silence(
        file_id: str
    ):
        file_id = UUID(file_id) 
        return await audio_model.detect_silence(file_id)

    return router