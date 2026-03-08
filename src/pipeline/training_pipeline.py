import sys
from src.components.data_ingestion import DataIngestion
from src.components.data_transformation import DataTransformation
from src.components.model_trainer import ModelTraining
from src.common.exception import CustomException
from src.common.logger import logging


class TrainingPipeline:
    def __init__(self):
        pass

    def train(self):
        try:
            logging.info("Initiating Data Ingestion")
            data_ingestion = DataIngestion()
            train_data_path, test_data_path = data_ingestion.initiate_data_ingestion()
            logging.info("Data Ingestion Completed")

            logging.info("Initiating Data Transformation")
            data_transformation = DataTransformation()
            train_data, test_data, _ = data_transformation.initiate_data_transformation(
                train_path=train_data_path,
                test_path=test_data_path
            )
            logging.info("Data Transformation Completed")

            logging.info("Initiating Model Training")
            model_training = ModelTraining()
            r2_square = model_training.initiate_model_training(
                train_data=train_data,
                test_data=test_data
            )
            print(f"Best Model has R2 Score of {r2_square*100} Percentage")
            logging.info("Model Training Completed")

        except Exception as e:
            raise CustomException(e, sys)
        

if __name__ == "__main__":
    TrainingPipeline().train()