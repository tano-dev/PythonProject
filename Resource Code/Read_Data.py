# Khai báo thư viện
import os
import pandas as pd

# Lớp để quản lý việc load dữ liệu
class DataLoader:
    # Phương thức khởi tạo đường dẫn
    def __init__(self):
        # Thư mục chứa file .py hiện tại
        self.HERE = os.path.dirname(__file__)
        # Project root = thư mục cha của Resource Code
        self.PROJECT_ROOT = os.path.dirname(self.HERE)
        # Đường dẫn các file dữ liệu
        self.THPT2023_CT2006_CSV_PATH = os.path.join(
            self.PROJECT_ROOT,
            "Dataset for Project",
            "Data_Set_2023",
            "diem_thi_thpt_2023.csv"
        )
        self.THPT2024_CT2006_CSV_PATH = os.path.join(
            self.PROJECT_ROOT,
            "Dataset for Project",
            "Data_Set_2024",
            "diem_thi_thpt_2024.csv"
        )
        self.THPT2025_CT2006_XLSX_PATH = os.path.join(
            self.PROJECT_ROOT,
            "Dataset for Project",
            "Data_Set_2025",
            "diem_thi_thpt_2025-ct2006.xlsx"
        )
        self.THPT2025_CT2018_XLSX_PATH = os.path.join(
            self.PROJECT_ROOT,
            "Dataset for Project",
            "Data_Set_2025",
            "diem_thi_thpt_2025-ct2018a.xlsx"
        )
    
    # Phương thức load dữ liệu
    def load_data(self):
        df_THPT2023_CT2006 = pd.read_csv(self.THPT2023_CT2006_CSV_PATH, encoding='utf-8')
        df_THPT2024_CT2006 = pd.read_csv(self.THPT2024_CT2006_CSV_PATH, encoding='utf-8')
        df_THPT2025_CT2006 = pd.read_excel(self.THPT2025_CT2006_XLSX_PATH, engine="openpyxl")
        df_THPT2025_CT2018 = pd.read_excel(self.THPT2025_CT2018_XLSX_PATH, engine="openpyxl")
        return df_THPT2023_CT2006, df_THPT2024_CT2006, df_THPT2025_CT2006, df_THPT2025_CT2018

# Khởi tạo và load dữ liệu sử dụng OOP để xử lý
class DataProcessor:
    # Phương thức khởi tạo
    def __init__(self):
        self.data_loader = DataLoader()
        
        # Gọi phương thức khởi tạo đường dẫn
        self.data_loader.__init__()
        
        # Load dữ liệu khi khởi tạo
        (
            self.df_THPT2023_CT2006,
            self.df_THPT2024_CT2006,
            self.df_THPT2025_CT2006,
            self.df_THPT2025_CT2018
        ) = self.data_loader.load_data()

    # Phương thức tiền xử lý dữ liệu
    def load_and_preprocess_data(self):
        # Thực hiện các bước tiền xử lý dữ liệu tại đây nếu cần
        
        # Hiện tại chỉ trả về các DataFrame đã load
        return (
            self.df_THPT2023_CT2006,
            self.df_THPT2024_CT2006,
            self.df_THPT2025_CT2006,
            self.df_THPT2025_CT2018
        )
    
    

