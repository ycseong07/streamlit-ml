# server.py
from fastapi import FastAPI, File, UploadFile
from transformers import Wav2Vec2ForCTC, Wav2Vec2Processor
import soundfile as sf
import torch

app = FastAPI()
tokenizer = Wav2Vec2Processor.from_pretrained("facebook/wav2vec2-base-960h")
model = Wav2Vec2ForCTC.from_pretrained("facebook/wav2vec2-base-960h")

def asr_pipeline(input_file):
    speech, _ = sf.read(input_file)
    input_values = tokenizer(speech, return_tensors="pt").input_values
    logits = model(input_values).logits
    predicted_ids = torch.argmax(logits, dim=-1)
    transcription = tokenizer.batch_decode(predicted_ids)[0]
    return transcription

@app.post("/transcribe")
async def transcribe_audio(file: UploadFile = File(...)):
    return {"transcription": asr_pipeline(file.file)}