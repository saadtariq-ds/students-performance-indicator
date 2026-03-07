import os
import yaml
from pathlib import Path
from src.common.logger import logging


def read_yaml(path_to_yaml: Path):
    """
    Reads a YAML file and returns its contents as a dictionary.

    Args:
        path_to_yaml (Path): The path to the YAML file.

    Returns:
        dict: Dictionary containing YAML contents.
    """

    try:
        with open(path_to_yaml, "r") as yaml_file:
            content = yaml.safe_load(yaml_file)
            logging.info(f"YAML file '{path_to_yaml}' read successfully.")
            return content

    except Exception as e:
        logging.error(f"Error reading YAML file '{path_to_yaml}': {e}")
        raise e
    

def create_directories(path_to_directories: list, verbose=True):
    """
    Creates directories if they do not exist.

    Args:
        path_to_directories (list): A list of directory paths to create.
        verbose (bool): If True, logs the creation of directories.
    """
    for path in path_to_directories:
        try:
            os.makedirs(path, exist_ok=True)
            logging.info(f"Directory '{path}' created successfully or already exists.")
        except Exception as e:
            logging.error(f"Error creating directory '{path}': {e}")
            raise ValueError(f"Error creating directory '{path}': {e}")