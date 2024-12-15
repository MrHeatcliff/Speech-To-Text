import os
import csv
from jiwer import wer

def calculate_wer(csv_file, txt_file):
    try:
        # Đọc file CSV
        with open(csv_file, "r", encoding="utf-8") as csvfile:
            csv_reader = csv.DictReader(csvfile)
            transcriptions = [row["Transcription"] for row in csv_reader]

        # Đọc file TXT
        with open(txt_file, "r", encoding="utf-8") as txtfile:
            references = [line.strip() for line in txtfile]

        # Đảm bảo số dòng trong CSV và TXT bằng nhau
        if len(transcriptions) != len(references):
            print("Số dòng trong CSV và TXT không khớp!")
            return

        # Tính WER cho từng dòng
        total_wer = 0
        for i, (ref, hyp) in enumerate(zip(references, transcriptions), start=1):
            error = wer(ref, hyp)
            total_wer += error
            print(f"Dòng {i}: WER = {error:.2%}")

        # Tính WER trung bình
        average_wer = total_wer / len(transcriptions)
        print(f"WER trung bình: {average_wer:.2%}")
    except Exception as e:
        print(f"Có lỗi xảy ra: {e}")

# Đường dẫn tới file CSV và TXT
csv_file = "C:/Users/Heathcliff/Desktop/Speech-To-Text/evaluation/pho_whisper_tiny_predict.csv"  # Thay bằng đường dẫn tới file CSV
output_txt = "C:/Users/Heathcliff/Desktop/Speech-To-Text/evaluation/transcript.txt"  # Thay bằng đường dẫn tới file TXT

calculate_wer(csv_file, output_txt)
