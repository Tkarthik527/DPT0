import polars as pl
    
def fetch_data(path_dataset, path_tasks = None, file_type = None):
    if file_type in ['xls', 'xlsx']:
        df_data, df_tasks = fetch_excel(path_dataset, path_tasks)
    elif file_type == 'csv':
        df_data, df_tasks = fetch_csv(path_dataset, path_tasks)
    else:
        raise TypeError
    return df_data, df_tasks
    
def fetch_csv(path_dataset, path_tasks):
    df_data = pl.read_csv(path_dataset, has_header=True)
    df_tasks = pl.read_csv(path_tasks, has_header=True)
    return df_data, df_tasks
    

def fetch_excel(path_dataset, path_tasks):
    df_data = pl.read_excel(path_dataset, has_header=True)
    df_tasks = pl.read_excel(path_tasks, has_header=True)
    return df_data, df_tasks 


#tasks = r"C:\Users\ktunga\OneDrive - FactSet\Documents\weighting_scheme.xlsx"

"""
CSV
Excel
Parquet
ORC
JSON
Avro
Text File
Log Files
XML
YAML
HTML
SQL Dump
HDF5
Feather
Protocol Buffers"""