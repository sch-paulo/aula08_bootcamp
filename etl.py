import os
import glob
import pandas as pd

# Extract
# # Ler arquivo
# # Concatenar os arquivos
def extract_and_consolidate_data(file: str) -> pd.DataFrame:
    json_files = glob.glob(os.path.join(file, '*.json'))
    df_list = [pd.read_json(arquivo) for arquivo in json_files]
    df_total = pd.concat(df_list, ignore_index=True)
    return df_total

# Transform
# # Transformar os arquivos
def calculate_kpi_of_total_sales(df: pd.DataFrame) -> pd.DataFrame:
    df['Total'] = df['Quantidade'] * df['Venda']
    return df

# Load
# # Carregar arquivos (decidir entre dois caminhos)
def load_data(df: pd.DataFrame, output_format: str):
    '''
    Function that load data either in CSV or Parquet format (or both), 
    depending on what the user defines in "output_format"'''
    if 'csv' in output_format.lower():
        df.to_csv('data.csv', index=False)
    if 'parquet' in output_format.lower():
        df.to_parquet('data.parquet', index=False)
    else:
        print('Output format not recognized. Try again.')

def pipeline_calculate_kpi_of_total_sales_consolidated(file: str, output_format: str):
    df = extract_and_consolidate_data(file)
    df_calculated = calculate_kpi_of_total_sales(df)
    load_data(df_calculated, output_format)