from pydub import AudioSegment
from pydub.playback import play

import os

FOLDER_NAME = "C:/Users/Heathcliff/Desktop/Speech-To-Text/evaluation/test-data"
OUTPUT_FOLDER = "C:/Users/Heathcliff/Desktop/Speech-To-Text/evaluation/resampled_data"

# Load the audio file (requires ffmpeg/avlib installed and configured)
def resample_audio(input_file, output_file):
    try:
        # Read the .m4a file
        audio = AudioSegment.from_file(input_file, format="m4a")

        # Downmix to 1 channel (mono) if the audio is stereo
        audio = audio.set_channels(1)

        # Resample to 16000 Hz
        audio = audio.set_frame_rate(16000)

        # Export as .mp3
        audio.export(output_file, format="mp3")

        print(f"Audio successfully resampled and exported to {output_file}")
    except Exception as e:
        print(f"An error occurred: {e}")

# Replace 'input.m4a' and 'output.mp3' with your file paths
for file_name in os.listdir(FOLDER_NAME):
    if file_name.endswith('.m4a'):
        file_path = os.path.join(FOLDER_NAME, file_name)
        output_file = os.path.join(OUTPUT_FOLDER, file_name.replace(".m4a", ".mp3"))

        resample_audio(file_path, output_file)
