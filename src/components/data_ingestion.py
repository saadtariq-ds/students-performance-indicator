import sys
import pandas as pd
from sklearn.model_selection import train_test_split
from src.config.configuration import ConfigurationManager
from src.common.exception import CustomException
from src.common.logger import logging


class DataIngestion:
    def __init__(self):
        self.config = ConfigurationManager()
        self.data_ingestion_config = self.config.get_data_ingestion_config()

    def initiate_data_ingestion(self):
        try:
            df = pd.read_csv(self.data_ingestion_config.source_data_path)
            logging.info("Read the Dataset from Source Path")

            df.to_csv(self.data_ingestion_config.raw_data_path, index=False, header=True)
            logging.info("Initiating Train Test Split")

            train_set, test_set = train_test_split(df, test_size=0.2, random_state=42)
            train_set.to_csv(self.data_ingestion_config.train_data_path, index=False, header=True)
            test_set.to_csv(self.data_ingestion_config.test_data_path, index=False, header=True)
            logging.info("Train and Test Data Split is Completed")

            return(
                self.data_ingestion_config.train_data_path,
                self.data_ingestion_config.test_data_path,
            )
        except Exception as e:
            raise CustomException(e, sys)
