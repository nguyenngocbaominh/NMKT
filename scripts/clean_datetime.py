import pandas as pd

def convert_published_time(df: pd.DataFrame) -> pd.DataFrame:
    """
    Chuyển đổi và chuẩn hóa cột thời gian 'published'.
    Người 3 sẽ thêm code xử lý vào đây.
    """
    print("--- Running: clean_datetime.py ---")

    # [TASK 1] CHUYỂN ĐỔI DATETIME & MÚI GIỜ
    # TODO: Người 3 sẽ thêm logic chuyển đổi, ví dụ:
    # df['published'] = pd.to_datetime(df['published'], utc=True).dt.tz_convert('Asia/Ho_Chi_Minh')
    
    # [TASK 2] KIỂM TRA ID
    # TODO: Người 3 sẽ thêm logic kiểm tra ID rỗng hoặc trùng lặp (nếu cần).
    
    return df