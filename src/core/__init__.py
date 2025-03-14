from extract import fetch_data
from loader import load_data 
from transform import transform_data

def run_pipeline(path_dataset : str, path_tasks: str):
    """
    The start of the pipeline which consists of top level execution 
    Args:
        path_dataset (str): The path for the data set file
        path_tasks (str): The path for the tasks file
    """
    raw_df = fetch_data(path_dataset, path_tasks)
    result_df = transform_data(raw_df)
    load_data(result_df)
    

    
    
    