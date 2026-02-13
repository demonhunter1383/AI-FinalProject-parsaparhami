import pandas as pd
import numpy as np


def clean_telecom_data(df):

    df_cleaned = df.copy()

    df_cleaned['TotalCharges'] = pd.to_numeric(df_cleaned['TotalCharges'], errors='coerce')

    median_val = df_cleaned['TotalCharges'].median()
    df_cleaned['TotalCharges'] = df_cleaned['TotalCharges'].fillna(median_val)

    if 'customerID' in df_cleaned.columns:
        df_cleaned = df_cleaned.drop('customerID', axis=1)

    return df_cleaned
