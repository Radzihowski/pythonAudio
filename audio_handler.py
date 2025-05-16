from openai import OpenAI

client = OpenAI()
audio_file= open("output_chunks/chunk_1.mp3", "rb")

transcription = client.audio.transcriptions.create(
    model="gpt-4o-mini-transcribe",
    file=audio_file
)

print(transcription.text)