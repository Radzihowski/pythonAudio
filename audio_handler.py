from openai import OpenAI
from settings import config

api_key = config["OPENAI_API_KEY"]
client = OpenAI(api_key=api_key)
# audio_file= open("output_chunks/chunk_10.mp3", "rb")
audio_file= open("input/full.mp3", "rb")

transcription = client.audio.transcriptions.create(
    model="gpt-4o-transcribe",
    file=audio_file
)
with open("output/transcript.txt", "w", encoding="UTF-8") as file:
    file.write(transcription.text)
print(transcription.text)
