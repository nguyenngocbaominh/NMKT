import pandas as pd
import re
import html
from bs4 import BeautifulSoup # Sử dụng BeautifulSoup để xử lý HTML phức tạp tốt hơn Regex thuần

def clean_description_and_title(df: pd.DataFrame) -> pd.DataFrame:
    """
    Áp dụng các bước làm sạch Text chuyên sâu: Loại bỏ HTML, giải mã ký tự thoát, và chuẩn hóa.
    """
    print("--- Running: clean_text.py (Làm sạch Văn bản & Tiêu đề) ---")

    # === 1. Hàm loại bỏ thẻ HTML (Sử dụng BeautifulSoup) ===
    # Sử dụng BeautifulSoup để xử lý các trường hợp HTML lồng nhau hoặc không hợp lệ tốt hơn Regex.
    def remove_html_tags(text):
        if pd.isna(text) or text is None:
            return text
        # Sử dụng BeautifulSoup để loại bỏ các thẻ HTML
        return BeautifulSoup(str(text), 'html.parser').get_text()

    # === 2. Hàm giải mã ký tự HTML và chuẩn hóa khoảng trắng ===
    def decode_and_normalize_text(text):
        if pd.isna(text) or text is None:
            return text
        
        # Giải mã các ký tự HTML (ví dụ: &amp; -> &)
        text = html.unescape(str(text))
        
        # Loại bỏ khoảng trắng kép, tabs, xuống dòng và chuẩn hóa thành một khoảng trắng duy nhất
        text = re.sub(r'\s+', ' ', text)
        
        # Loại bỏ khoảng trắng ở đầu và cuối
        text = text.strip()
        return text

    # === 3. ÁP DỤNG CÁC BƯỚC XỬ LÝ (TRỌNG TÂM LÀ description) ===
    
    # Áp dụng loại bỏ HTML cho cột description (chứa nhiều nhiễu nhất)
    df['description'] = df['description'].apply(remove_html_tags)
    
    # Áp dụng giải mã và chuẩn hóa cho cả description và title
    df['description'] = df['description'].apply(decode_and_normalize_text)
    
    if 'title' in df.columns:
        df['title'] = df['title'].apply(decode_and_normalize_text)
        # Chuẩn hóa Case cho Title (Ví dụ: Title Case)
        df['title'] = df['title'].str.title()
    
    print("   -> Đã hoàn tất làm sạch văn bản và chuẩn hóa tiêu đề.")
    return df
