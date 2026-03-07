from dataclasses import dataclass
from pathlib import Path

@dataclass
class DataIngestionConfig:
    source_data_path: str
    root_directory: str
    raw_data_path: str
    train_data_path: str
    test_data_path: str