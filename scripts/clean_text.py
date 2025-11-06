import pandas as pd
import re

def clean_description_and_title(df: pd.DataFrame) -> pd.DataFrame:
    """
    Áp dụng các bước làm sạch Text chuyên sâu cho cột description và title.
    Người 1 sẽ thêm code xử lý vào đây.
    """
    print("--- Running: clean_text.py ---")

    # [TASK 1] XỬ LÝ HTML/KÝ TỰ THOÁT trong 'description'
    # TODO: Người 1 sẽ thêm logic làm sạch HTML, ví dụ:
    # df['description'] = df['description'].apply(lambda x: re.sub(r'<[^>]+>', '', x))
    # df['description'] = df['description'].str.replace('&amp;', '&')
    
    # [TASK 2] CHUẨN HÓA TIÊU ĐỀ 'title'
    # TODO: Người 1 sẽ thêm logic chuẩn hóa Title Case, xóa khoảng trắng thừa.
    
    return df

if __name__ == '__main__':
    # Đoạn này chỉ để test riêng lẻ, không chạy khi import vào main_run.py
    # Bạn có thể bỏ qua hoặc để trống.
    pass