import os
from box.exceptions import BoxValueError
import yaml
from MLOPS_Data_Science_Project import logger
import json
import joblib
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import Any

@ensure_annotations
def read_yaml(file_path: str) -> ConfigBox:
    try:
        with open(path_to_yaml) as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f"YAML file : {path_to_yaml} read successfully.")
            return ConfigBox(content)
    except BoxValueError:
        raise ValueError("yaml file is empty")
    except Exception as e:

@ensure_annotations
def create_directories(path_to_directories: list , verbose=True):
    for path in path_to_directories:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logger.info(f"Directory created: {path}")
   
@ensure_annotations
def save_json(path:Path,data:dict):
    try:
        with open(path) as f:
            content= json.load(f)

        logger.info(f"JSON file : {path} read successfully from :{path}")    
        return ConfigBox(content)
    

@ensure_annotations
def save_bin(data:Any, path:Path):
        
        joblib.dump(value=data, filename=path)
        logger.info(f"Data saved successfully at {path}")
    
@ensure_annotations
def load_bin(path:Path) -> Any:

    data=joblib.load(path)
    logger.info(f"Binary file loaded from {path}")
    return data

@ensure_annotations
def get_size(path:Path) -> str:
   size_in_kb = round(os.path.getsize(path) / 1024)
   return f"~ {size_in_kb} KB"