import pandas as pd

def remove_duplicates_and_standardize(df: pd.DataFrame) -> pd.DataFrame:
    """
    Xóa bản ghi trùng lặp và chuẩn hóa các biến danh mục (category, source).
    Người 2 sẽ thêm code xử lý vào đây.
    """
    print("--- Running: clean_category.py ---")

    # [TASK 1] XÓA TRÙNG LẶP (Dựa trên URL)
    # TODO: Người 2 sẽ thêm logic xóa trùng lặp, ví dụ:
    # df.drop_duplicates(subset=['url'], keep='first', inplace=True)

    # [TASK 2] CHUẨN HÓA DANH MỤC 'category' và 'source'
    # TODO: Người 2 sẽ thêm logic thống nhất tên, ví dụ:
    # df['source'] = df['source'].replace({'VNE': 'VnExpress', 'TuoiTre': 'Tuổi Trẻ'})
    
    return df