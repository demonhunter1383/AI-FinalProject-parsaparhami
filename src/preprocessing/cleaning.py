import pandas as pd
import numpy as np


def clean_telecom_data(df):
    """
    تمیزکاری داده‌های تلکام: تبدیل ستون TotalCharges و پر کردن مقادیر خالی
    """
    df_cleaned = df.copy()

    # تبدیل ستون TotalCharges از متن به عدد
    df_cleaned['TotalCharges'] = pd.to_numeric(df_cleaned['TotalCharges'], errors='coerce')

    # پر کردن مقادیر خالی با میانه
    median_val = df_cleaned['TotalCharges'].median()
    df_cleaned['TotalCharges'] = df_cleaned['TotalCharges'].fillna(median_val)

    # حذف ستون‌های بدون استفاده مثل customerID
    if 'customerID' in df_cleaned.columns:
        df_cleaned = df_cleaned.drop('customerID', axis=1)

    return df_cleaned
