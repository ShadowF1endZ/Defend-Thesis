# utils/db_utils.py
import pandas as pd
import os

def load_data(filepath):
    return pd.read_excel(filepath)

def save_report(df, filename):
    output_folder = 'outputs/reports'
    os.makedirs(output_folder, exist_ok=True)
    df.to_csv(f'{output_folder}/{filename}.csv', index=False)
    print(f'Report saved to {output_folder}/{filename}.csv')
