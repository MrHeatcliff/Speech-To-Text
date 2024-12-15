from utils import *
# import keyboard
import os

import csv
import time

os.environ['KMP_DUPLICATE_LIB_OK']='True'

# FILE_NAME = "temp_audio.wav"
FILE_NAME = "../test-data/1.mp3"
MODEL_FOLDER_NAME = "pho_whisper_tiny"

FOLDER_NAME = "C:/Users/Heathcliff/Desktop/Speech-To-Text/evaluation/resampled_data"
CSV_FILE_NAME = "pho_whisper_tiny_predict.csv"


if not os.path.isdir(MODEL_FOLDER_NAME):
    download_pho_whisper(MODEL_FOLDER_NAME)

model = load_pho_whisper(MODEL_FOLDER_NAME)

csv_file = open(CSV_FILE_NAME, mode='w', newline='', encoding='utf-8')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['Filename', 'Transcription', 'Process_time'])

fnum = 0
overall_time = 0

for file_name in os.listdir(FOLDER_NAME):
    if file_name.endswith('.mp3'):
        fnum+=1
        file_path = os.path.join(FOLDER_NAME, file_name)
        try:
            start = time.time()
            text = pho_whisper_recognition(model, file_path)
            processed_time = time.time() - start
            overall_time +=processed_time
            # Get the recognized text from the dictionary
            transcription = text

            # Write the filename and transcription to the CSV file
            csv_writer.writerow([file_name, transcription, processed_time])
            # Print status for each file
            print(f"Processed {file_name}: {transcription}, time: {processed_time}")
        
        except Exception as e:
            print(f"Error processing {file_name}: {str(e)}")
print("Transcription completed and saved to", CSV_FILE_NAME)
print("overall processed time:", overall_time/fnum)