import argparse
from core import run_pipeline
import configparser


# Load environment.ini
config = configparser.ConfigParser()
config.read("config/environment.ini")

def main(args):
    path_dataset = args.dataset if args.dataset else config.get("PATH","DATASET_PATH")
    path_tasks = args.dataset if args.dataset else config.get("PATH","TASKS_PATH")
    
    run_pipeline(path_dataset = path_dataset, path_tasks = path_tasks ) 
        
if __name__ == "__main__":
    # Parse user arguments (dataset path + tasks file)
    parser = argparse.ArgumentParser(description="Automated Data Processing Tool")
    parser.add_argument("--dataset", type=str, required=False, help="Path to input dataset")
    parser.add_argument("--tasks", type=str, required=False, help="Path to JSON file with tasks")
    args = parser.parse_args()
    main(args)
