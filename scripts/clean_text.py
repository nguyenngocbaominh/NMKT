import pandas as pd
import re
import html
from bs4 import BeautifulSoup

def clean_description_and_title(df: pd.DataFrame) -> pd.DataFrame:
    print("--- Running: clean_text.py (Làm sạch Văn bản & Tiêu đề) ---")

    # 0) Chuẩn hóa tên entity về lowercase: &Apos; -> &apos;
    _entity_case_fix = re.compile(r'&([A-Za-z]+);')
    def normalize_entity_case(text: str) -> str:
        if pd.isna(text) or text is None:
            return text
        return _entity_case_fix.sub(lambda m: f"&{m.group(1).lower()};", str(text))

    # 1) Bóc thẻ HTML an toàn
    def remove_html_tags(text):
        if pd.isna(text) or text is None:
            return text
        return BeautifulSoup(str(text), "html.parser").get_text()

    # 2) Unescape nhiều tầng + chuẩn hóa khoảng trắng & unicode "kì cục"
    def decode_and_normalize_text(text):
        if pd.isna(text) or text is None:
            return text
        s = str(text)

        # Sửa viết hoa entity, ví dụ &Apos; -> &apos;
        s = normalize_entity_case(s)

        # Unescape lặp (xử lý &amp;apos;...): dừng khi không đổi nữa
        for _ in range(3):
            new_s = html.unescape(s)
            if new_s == s:
                break
            s = new_s

        # Thay các ký tự "vô hình" phổ biến
        s = (s.replace('\xa0', ' ')
               .replace('\u2019', "'")   # right single quote → '
               .replace('\u2018', "'")
               .replace('\u201c', '"')
               .replace('\u201d', '"'))

        # Chuẩn hóa whitespace
        s = re.sub(r'\s+', ' ', s).strip()
        return s

    # 3) Áp dụng pipeline
    # 3a) description
    if 'description' in df.columns:
        df['description'] = df['description'].apply(remove_html_tags)
        df['description'] = df['description'].apply(decode_and_normalize_text)

    # 3b) title (bóc thẻ + unescape như description)
    if 'title' in df.columns:
        df['title'] = df['title'].apply(remove_html_tags)
        df['title'] = df['title'].apply(decode_and_normalize_text)
        # Nếu cần Title Case thì bật dòng dưới (nhưng dễ làm sai tiếng Việt có dấu)
        # df['title'] = df['title'].str.title()

    print("   -> Đã hoàn tất làm sạch văn bản và chuẩn hóa tiêu đề.")
    return df
