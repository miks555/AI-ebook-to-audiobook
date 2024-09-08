#########################start
print("starting...")
import os
os.environ["SUNO_USE_SMALL_MODELS"] = "True"
os.environ["SUNO_OFFLOAD_CPU"] = "True"
from bark import SAMPLE_RATE, generate_audio, preload_models
from scipy.io.wavfile import write as write_wav
from IPython.display import Audio
from pydub import AudioSegment
from pathlib import Path
preload_models()
##########################check if done or missing text
if(Path("file.wav").is_file()):
     print("file.wav already created, press enter to exit...")
     input()
     quit()
if(Path("ebook.txt").is_file() == False):
     print("ebook.txt with text does not exist, press enter to exit...")
     input()
     quit()
##########################language selection
print("select voice language 1 - english, 2 - polish")
flag_0 = 0
flag_0 = int(input())
if flag_0 == 1:
    SPEAKER = "v2/en_speaker_0"
elif flag_0 == 2:
    SPEAKER = "v2/pl_speaker_8"
else:
    print("invalid choice, default = 1")
    SPEAKER = "v2/en_speaker_0"
#########################split
print("loading file ebook.txt...")
parts = list()
ebook_0 = open("ebook.txt", "r", encoding="utf-8")
text_0 = ebook_0.read()
ebook_0.close()
current_part = ""
for character in text_0:
    current_part += character
    if character in ['.', '?', ',', '!', ':', ';', '\n', '\t', '\r', '\f']:
        parts.append(current_part.strip())
        current_part = ""
if current_part:
    parts.append(current_part)
##########################delete parts without alphanumeric symbol
filtered_parts = []
for part in parts:
  for character in part:
    if character.isalnum():
      filtered_parts.append(part)
      break
parts = filtered_parts
#########################check wavs
print("checking for already created files...")
start = len(parts)
for i in range(0 , len(parts)):
    if(Path(str(i)+'.wav').is_file()):
            pass
    else:
         start = i
         break
#########################transform
print("creating audio...")
for i in range(start, len(parts)):
    text_1 = parts[i]
    audio_array_0 = generate_audio(text_1 , history_prompt=SPEAKER)
    write_wav(str(i)+".wav", SAMPLE_RATE, audio_array_0)
    print("completed: " + str(i + 1) + "/" + str(len(parts)) + " " + str(((i + 1)/(len(parts)))*100)+ "% (" + str(i)+".wav)")
#########################merge
print("merging to file.wav...")
audio_parts = list()
combined_audio = AudioSegment.from_wav("0.wav")
for i in range(1, len(parts)):
    combined_audio = combined_audio + AudioSegment.from_wav(str(i) + ".wav")
combined_audio.export("file.wav", format="wav")
#######################delete
print("deleting files...")
for i in range(0, len(parts)):
    os.remove(str(i) + ".wav")
print("completed")
