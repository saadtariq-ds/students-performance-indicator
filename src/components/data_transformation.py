import sys
import pandas as pd
import numpy as np
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from src.config.configuration import ConfigurationManager
from src.common.utils import save_object
from src.common.exception import CustomException
from src.common.logger import logging

class DataTransformation:
    def __init__(self):
        self.data_transformation_config = ConfigurationManager().get_data_transformation_config()
        self.schema = self.data_transformation_config.all_schema

    def get_data_transformer_object(self):
        try:
            all_schema = self.data_transformation_config.all_schema
            numerical_columns = list(all_schema["numerical_columns"].keys())
            categorical_columns = list(all_schema["categorical_columns"].keys())

            numerical_pipeline = Pipeline(
                steps=[
                    ("imputer", SimpleImputer(strategy="median")),
                    ("scaler", StandardScaler(with_mean=False))
                ]
            )
            logging.info("Numerical Pipeline is Completed")

            categorical_pipeline = Pipeline(
                steps=[
                    ("imputer", SimpleImputer(strategy="most_frequent")),
                    ("one_hot_encoder", OneHotEncoder()),
                    ("scaler", StandardScaler(with_mean=False))
                ]
            )
            logging.info("Categorical Pipeline is Completed")

            preprocessor = ColumnTransformer(
                [
                    ("numerical_pipeline", numerical_pipeline, numerical_columns),
                    ("categorical_pipeline", categorical_pipeline, categorical_columns),
                ]
            )
            logging.info("Preprocessing is Completed")

            return preprocessor

        except Exception as e:
            raise CustomException(e, sys)

    def initiate_data_transformation(self, train_path, test_path):
        try:
            preprocessor = self.get_data_transformer_object()
            train_df = pd.read_csv(train_path)
            test_df = pd.read_csv(test_path)

            logging.info("Train and Test Data Read Successfully")

            target_column = self.schema["target_column"]

            input_feature_train_df = train_df.drop(columns=[target_column], axis=1)
            target_feature_train_df = train_df[target_column]
            input_feature_test_df = test_df.drop(columns=[target_column], axis=1)
            target_feature_test_df = test_df[target_column]

            logging.info("Data is Split into Training and Test Sets")

            logging.info("Applying Preprocssor Object on Training and Test DataFrame")
            input_feature_train_arr = preprocessor.fit_transform(input_feature_train_df)
            input_feature_test_arr = preprocessor.transform(input_feature_test_df)
            logging.info("Preprocessor is Applied on Training and Test DataFrame")

            train_array = np.c_[
                input_feature_train_arr, np.array(target_feature_train_df)
            ]
            test_array = np.c_[
                input_feature_test_arr, np.array(target_feature_test_df)
            ]

            save_object(
                file_path=self.data_transformation_config.preprocessor_object_file_path,
                file_object=preprocessor
            )
            logging.info("Preprocessor Object is Saved")

            return (
                train_array,
                test_array,
                self.data_transformation_config.preprocessor_object_file_path

            )

        except Exception as e:
            raise CustomException(e, sys)
        
if __name__ == "__main__":
    data_ingestion_config = ConfigurationManager().get_data_ingestion_config()
    train_path = data_ingestion_config.train_data_path
    test_path = data_ingestion_config.test_data_path

    data_transformation = DataTransformation()
    data_transformation.initiate_data_transformation(train_path=train_path, test_path=test_path)