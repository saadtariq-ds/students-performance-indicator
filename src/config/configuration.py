import os
from src.constants import CONFIG_FILE_PATH, SCHEMA_FILE_PATH
from src.common.utils import read_yaml, create_directories
from src.entity.config_entity import (
    DataIngestionConfig, DataTransformationConfig
)

class ConfigurationManager:
    def __init__(self, config_file_path=CONFIG_FILE_PATH, schema_file_path=SCHEMA_FILE_PATH):
        self.config_file_path = read_yaml(path_to_yaml=config_file_path)
        self.schema_file_path = read_yaml(path_to_yaml=schema_file_path)

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
    
    def get_data_transformation_config(self) -> DataTransformationConfig:
        config = self.config_file_path["data_transformation"]
        schema = self.schema_file_path["columns"]

        create_directories([config["root_directory"]])

        data_transformation_config = DataTransformationConfig(
            root_directory=config["root_directory"],
            preprocessor_object_file_path=config["preprocessor_object_file_path"],
            all_schema=schema

        )

        return data_transformation_config
