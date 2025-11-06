import pandas as pd
# Import các hàm từ các file khác (đường dẫn tương đối)
from scripts.clean_text import clean_description_and_title
from scripts.clean_category import remove_duplicates_and_standardize
from scripts.clean_datetime import convert_published_time

# Đường dẫn tương đối (Lùi về 1 cấp từ scripts/ -> data-cleaning-project/)
INPUT_FILE = "../news_NMKT.csv"
OUTPUT_FILE = "../news_NMKT_CLEAN.csv"

def run_all_cleaning_steps():
    # 1. Đọc file thô
    try:
        df = pd.read_csv(INPUT_FILE)
        print(f"Đã đọc thành công {len(df)} dòng dữ liệu thô.")
    except FileNotFoundError:
        print(f"LỖI: Không tìm thấy file {INPUT_FILE}. Hãy kiểm tra đường dẫn tương đối.")
        return

    # 2. Áp dụng các bước làm sạch theo thứ tự (THỨ TỰ NÀY ĐÃ ĐƯỢC CHUẨN HÓA CHO NHÓM)
    df = remove_duplicates_and_standardize(df) # Người 2: Xóa trùng lặp trước
    df = clean_description_and_title(df)       # Người 1: Làm sạch văn bản
    df = convert_published_time(df)            # Người 3: Chuẩn hóa thời gian

    # 3. Lưu file đã được làm sạch đồng nhất
    df.to_csv(OUTPUT_FILE, index=False)
    print(f"\n--- THÀNH CÔNG ---")
    print(f"Quá trình làm sạch dữ liệu hoàn tất. File sạch đã được lưu tại {OUTPUT_FILE}")

if __name__ == '__main__':
    run_all_cleaning_steps()