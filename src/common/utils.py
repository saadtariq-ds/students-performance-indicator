import os
import sys
import yaml
import dill
from pathlib import Path
from sklearn.metrics import r2_score
from sklearn.model_selection import GridSearchCV
from src.common.exception import CustomException
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
        raise CustomException(e, sys)
    

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
            raise CustomException(e, sys)
        

def save_object(file_path: Path, file_object):
    """
    Saves data to a binary file using pickle.

    Args:
        file_object (Any): preprocessor_object.
        file_path (Path): The path to the pickle file.
    """
    try:
        with open(file=file_path, mode="wb") as file:
            dill.dump(file_object, file)
    except Exception as e:
            raise CustomException(e, sys)
    

def evaluate_models(X_train, y_train, X_test, y_test, models, param):
    """
    Evaluate Different Models
    """
    try:
        report = {}

        for i in range(len(list(models))):
            model = list(models.values())[i]
            para=param[list(models.keys())[i]]

            gs = GridSearchCV(model,para,cv=3)
            gs.fit(X_train,y_train)

            model.set_params(**gs.best_params_)
            model.fit(X_train,y_train)

            #model.fit(X_train, y_train)  # Train model

            y_train_pred = model.predict(X_train)

            y_test_pred = model.predict(X_test)

            train_model_score = r2_score(y_train, y_train_pred)

            test_model_score = r2_score(y_test, y_test_pred)

            report[list(models.keys())[i]] = test_model_score

        return report

    except Exception as e:
        raise CustomException(e, sys)