from pydub import AudioSegment
import math
import os

# Load MP3 file
audio = AudioSegment.from_mp3("full.mp3")

# Set chunk length in milliseconds (e.g., 30 seconds)
chunk_length = 30 * 1000
total_chunks = math.ceil(len(audio) / chunk_length)

# Create output folder
os.makedirs("output_chunks", exist_ok=True)

for i in range(total_chunks):
    start = i * chunk_length
    end = min(start + chunk_length, len(audio))
    chunk = audio[start:end]
    chunk.export(f"output_chunks/chunk_{i+1}.mp3", format="mp3")

print(f"Sliced into {total_chunks} chunks.")
