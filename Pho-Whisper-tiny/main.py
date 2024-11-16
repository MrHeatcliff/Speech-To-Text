from utils import *
import keyboard
import os


os.environ['KMP_DUPLICATE_LIB_OK']='True'

FILE_NAME = "temp_audio.wav"
FOLDER_NAME = "pho_whisper_tiny"


if not os.path.isdir(FOLDER_NAME):
    download_pho_whisper(FOLDER_NAME)

model = load_pho_whisper(FOLDER_NAME)
print(f"Listenning...")
while True:
    if keyboard.is_pressed("l"):
        record_audio(FILE_NAME)
        text = pho_whisper_recognition(model, FILE_NAME)
        print(text)
        print(f"Listening...")