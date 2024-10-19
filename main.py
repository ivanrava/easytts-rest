import os

from fastapi import FastAPI
import gtts
import mmh3
from pydantic import BaseModel

app = FastAPI()
lang = 'it'


class Message(BaseModel):
    text: str


def play(path: str):
    print(path)


@app.post("/speak/")
async def say_hello(message: Message):
    h = mmh3.hash128(message.text+lang, signed=False)
    path = f"cache/{h:x}.mp3"
    if not os.path.exists(path):
        tts = gtts.gTTS(message.text, lang=lang)
        tts.save(path)
    play(path)
    return {"text": message.text, "status": "The message is playing"}
