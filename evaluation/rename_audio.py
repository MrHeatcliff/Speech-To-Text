import os

FOLDER_NAME = "C:/Users/Heathcliff/Desktop/Speech-To-Text/evaluation/test-data"

def rename_files(directory):
    try:
        # Lấy danh sách các tệp trong thư mục
        files = sorted(f for f in os.listdir(directory) if f.endswith('.m4a'))

        # Đổi tên từng tệp
        for index, file_name in enumerate(files, start=1):
            # Tạo tên mới theo định dạng minh_000001.m4a
            new_name = f"minh_{index:06}.m4a"
            print(new_name)
            
            # Đường dẫn đầy đủ cho tệp cũ và mới
            old_path = os.path.join(directory, file_name)
            new_path = os.path.join(directory, new_name)

            # Đổi tên tệp
            os.rename(old_path, new_path)

        print("Đã đổi tên tất cả các tệp thành công!")
    except Exception as e:
        print(f"Có lỗi xảy ra: {e}")

rename_files(FOLDER_NAME)
