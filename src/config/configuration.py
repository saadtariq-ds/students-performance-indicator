import os
from src.constants import CONFIG_FILE_PATH
from src.common.utils import read_yaml, create_directories
from src.entity.config_entity import DataIngestionConfig

class ConfigurationManager:
    def __init__(self, config_file_path=CONFIG_FILE_PATH):
        self.config_file_path = read_yaml(path_to_yaml=config_file_path)

        create_directories([self.config_file_path["artifacts_root"]])

    def get_data_ingestion_config(self) -> DataIngestionConfig:
        config = self.config_file_path["data_ingestion"]

        create_directories([config["root_directory"]])

        data_ingestion_config = DataIngestionConfig(
            source_data_path=config["source_data_path"],
            root_directory=config["root_directory"],
            raw_data_path=config["raw_data_path"],
            train_data_path=config["train_data_path"],
            test_data_path=config["test_data_path"]
        )

        return data_ingestion_config

