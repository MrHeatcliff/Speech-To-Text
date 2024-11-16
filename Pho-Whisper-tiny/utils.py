from pvrecorder import PvRecorder
import keyboard
import wave
import struct

import os
os.environ["KMP_DUPLICATE_LIB_OK"] = "TRUE"
from transformers import pipeline, AutoProcessor, AutoModelForSpeechSeq2Seq

def microphone_checking():
    """Check if microphone is available"""
    devices = PvRecorder.get_available_devices()
    print(devices)

def record_audio(file_name):
    """Record using speech_recognition library"""
    recorder = PvRecorder(device_index=-1, frame_length=512)
    audio = []

    try:
        print("Recording... Press e to stop")
        recorder.start()

        while True:
            try:
                frame = recorder.read()
                audio.extend(frame)
                if keyboard.is_pressed('e'):
                    break
            except Exception as e:
                print(f"Error during recording: {e}")
                break
        recorder.stop()
        with wave.open(file_name, 'w') as f:
            f.setparams((1, 2, 16000, 512, "NONE", "NONE"))
            f.writeframes(struct.pack("h" * len(audio), *audio))
    finally:
        recorder.delete()

def download_pho_whisper(foldername):
    """Download Pho Whisper from huggingface, save to foldername parameter"""
    model = AutoModelForSpeechSeq2Seq.from_pretrained("vinai/PhoWhisper-tiny")
    processor = AutoProcessor.from_pretrained("vinai/PhoWhisper-tiny")
    
    model.save_pretrained(foldername, safe_serialization=False)
    processor.save_pretrained(foldername)

def load_pho_whisper(foldername):
    """Load saved model"""
    transcriber = pipeline("automatic-speech-recognition", model=foldername, tokenizer=foldername, device='cuda')
    # model = AutoModelForSpeechSeq2Seq.from_pretrained(foldername)
    return transcriber

def pho_whisper_recognition(transcriber, file_name):
    """Predict using loaded model"""
    return transcriber(file_name)['text']