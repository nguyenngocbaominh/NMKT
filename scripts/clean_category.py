import pandas as pd

def remove_duplicates_and_standardize(df: pd.DataFrame) -> pd.DataFrame:
    """
    Xóa bản ghi trùng lặp, xóa các bài báo thiếu thông tin, và chuẩn hóa danh mục/nguồn.
    """
    print("--- Running: clean_category.py (Xóa & Chuẩn hóa cấu trúc) ---")

    # --- 1. XÓA BẢN GHI TRÙNG LẶP & THIẾU URL ---
    initial_count = len(df)
    
    # Loại bỏ các hàng bị thiếu URL trước khi xóa trùng lặp
    df.dropna(subset=['url'], inplace=True)
    
    # Loại bỏ các bản ghi trùng lặp dựa trên 'url'
    df.drop_duplicates(subset=['url'], keep='first', inplace=True)
    
    deleted_duplicates = initial_count - len(df)


    # --- 2. XÓA CÁC BÀI BÁO THIẾU THÔNG TIN TRỌNG YẾU ---
    
    # Xác định các cột TỐI THIỂU CẦN CÓ DỮ LIỆU
    key_columns = ['title', 'published', 'category']
    missing_count_before_drop = len(df)
    
    # Xóa các dòng thiếu dữ liệu ở BẤT KỲ cột nào trong key_columns
    df.dropna(subset=key_columns, inplace=True)
    
    deleted_missing = missing_count_before_drop - len(df)
    print(f"   -> Đã xóa {deleted_duplicates} bản ghi trùng lặp.")
    print(f"   -> Đã xóa {deleted_missing} bài báo do thiếu thông tin ở: {', '.join(key_columns)}.")

    
    # --- 3. CHUẨN HÓA CỘT 'source' và 'category' (Dựa trên dữ liệu thực tế) ---

    # Áp dụng làm sạch khoảng trắng thừa cho tất cả các cột
    df['source'] = df['source'].str.strip()
    df['category'] = df['category'].str.strip()

    # Chuẩn hóa tên nguồn (VnExpress, Thanh Niên, VietNamNet, Tuổi Trẻ)
    source_mapping = {
        'VnExpress': 'VnExpress',
        'ThanhNien': 'Thanh Niên',
        'Vietnamnet': 'VietNamNet',
        'TuoiTre': 'Tuổi Trẻ'
    }
    # Chuyển tất cả về dạng Title Case rồi thay thế để bắt các biến thể sai Case
    df['source'] = df['source'].str.title().replace(source_mapping, regex=False)

    
    # Chuẩn hóa tên danh mục (Các danh mục đã có dấu chuẩn, chỉ cần đảm bảo thống nhất case)
    # Ví dụ: 'giải trí' -> 'Giải trí'
    df['category'] = df['category'].str.title()
    
    
    # --- 4. XỬ LÝ CÁC GIÁ TRỊ THIẾU CÒN LẠI ---
    
    # Cột 'description' (có thể thiếu, nhưng không xóa cả bài)
    df['description'].fillna('Không có mô tả', inplace=True)
    
    print("   -> Đã hoàn tất chuẩn hóa cấu trúc và danh mục.")
    return df
