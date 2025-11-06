import pandas as pd
from scripts.clean_text import clean_description_and_title
from scripts.clean_category import remove_duplicates_and_standardize
from scripts.clean_datetime import clean_description_and_title

INPUT_FILE = "../news_NMKT.csv"
OUTPUT_FILE = "../news_NMKT_CLEAN.csv"

def run_all_cleaning_steps():
    # 1. Đọc file
    try:
        df = pd.read_csv(INPUT_FILE)
        print(f"Đã đọc thành công {len(df)} dòng dữ liệu thô.")
    except FileNotFoundError:
        print(f"LỖI: Không tìm thấy file {INPUT_FILE}. Hãy kiểm tra đường dẫn tương đối.")
        return

    # 2. Clean 
    df = remove_duplicates_and_standardize(df) # Xóa trùng lặp trước
    df = clean_description_and_title(df)       #  Làm sạch văn bản
    df = clean_description_and_title(df)            #  Chuẩn hóa thời gian

    # 3. Lưu file đã được làm sạch đồng nhất
    df.to_csv(OUTPUT_FILE, index=False)
    print(f"\n--- THÀNH CÔNG ---")
    print(f"Quá trình làm sạch dữ liệu hoàn tất. File sạch đã được lưu tại {OUTPUT_FILE}")

if __name__ == '__main__':
    run_all_cleaning_steps()
