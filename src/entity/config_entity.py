from dataclasses import dataclass
from pathlib import Path

@dataclass
class DataIngestionConfig:
    source_data_path: str
    root_directory: str
    raw_data_path: str
    train_data_path: str
    test_data_path: str

@dataclass
class DataTransformationConfig:
    root_directory: str
    preprocessor_object_file_path: str
    all_schema: dict

@dataclass
class ModelTrainerConfig:
    root_directory: str
    trained_model_file_path: str
