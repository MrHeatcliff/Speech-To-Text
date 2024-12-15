# Chuyển đổi định dạng trong file txt
def number_to_words(number):
    words = {
        "0": "không", "1": "một", "2": "hai", "3": "ba", "4": "bốn", 
        "5": "năm", "6": "sáu", "7": "bảy", "8": "tám", "9": "chín"
    }
    return " ".join(words[digit] for digit in str(number))

def process_line(line):
    # Tách mã số và khối lượng
    parts = line.strip().split(", ")
    ma_so = parts[0].split(" ")[2]  # Lấy số sau 'Mã số'
    khoi_luong = parts[1].split(" ")[2]  # Lấy số sau 'khối lượng'

    # Đổi số sang chữ
    ma_so_words = number_to_words(ma_so)

    # Tách phần nguyên và phần thập phân của khối lượng
    khoi_luong_parts = khoi_luong.split(".")
    khoi_luong_words = number_to_words(khoi_luong_parts[0]) + " chấm " + number_to_words(khoi_luong_parts[1])

    return f"mã số {ma_so_words} khối lượng {khoi_luong_words}"

def process_file(input_file, output_file):
    with open(input_file, "r", encoding="utf-8") as infile, open(output_file, "w", encoding="utf-8") as outfile:
        for line in infile:
            new_line = process_line(line)
            outfile.write(new_line + "\n")
    print(f"File đã được chuyển đổi và lưu tại {output_file}")

# Đường dẫn tới file txt
input_txt = "C:/Users/Heathcliff/Desktop/Speech-To-Text/evaluation/beo.txt"  # Thay bằng đường dẫn tới file đầu vào
output_txt = "C:/Users/Heathcliff/Desktop/Speech-To-Text/evaluation/transcript.txt"  # Thay bằng đường dẫn tới file đầu ra

process_file(input_txt, output_txt)
