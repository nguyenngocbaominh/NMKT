import pandas as pd

def clean_id_and_datetime(df: pd.DataFrame) -> pd.DataFrame:
    """
    Chuyển đổi cột thời gian 'published' sang kiểu datetime và kiểm tra/báo cáo về cột 'id'.
    """
    print("--- Running: clean_datetime.py (Chuẩn hóa Thời gian & ID) ---")

    #1: CHUYỂN ĐỔI ĐỊNH DẠNG THỜI GIAN
    
    df['published'] = pd.to_datetime(df['published'], errors='coerce', utc=True)
    
    # Chuyển đổi múi giờ và loại bỏ thông tin múi giờ để thống nhất định dạng
    try:
        df['published'] = df['published'].dt.tz_convert('Asia/Ho_Chi_Minh').dt.tz_localize(None)
        print("   -> Đã chuyển đổi cột 'published' sang kiểu datetime (múi giờ +07:00).")
    except Exception as e:
        # Xử lý trường hợp không thể chuyển đổi múi giờ (nếu có lỗi bất thường)
        print(f"   - Lỗi khi chuyển đổi múi giờ: {e}. Đã giữ nguyên định dạng thời gian.")
          
    # 2: KIỂM TRA TÍNH HỢP LỆ CỦA ID
    
    id_missing = df['id'].isnull().sum()
    id_duplicates = df['id'].duplicated().sum()
    
    print("   -> Kiểm tra tính hợp lệ của cột 'id':")
    print(f"      - Số ID bị thiếu: {id_missing}")

    if id_duplicates > 0:
        df.drop_duplicates(subset=['id'], keep='first', inplace=True)
        print(f"      - CẢNH BÁO: Phát hiện {id_duplicates} ID trùng lặp.")
        print(f" - Đã xóa {id_duplicates} dòng do ID trùng lặp.")
        
    if id_missing > 0:
        df.dropna(subset=['id'], inplace=True)
        print(f"      - Đã xóa {id_missing} dòng do thiếu ID.")
        
    print("   -> Đã hoàn tất xử lý thời gian và kiểm tra ID.")
    return df
