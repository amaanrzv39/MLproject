import os
import sys
from src.exception import CustomException
from src.logger import logging
from src.utils import saved_obj, evaluate_models
from dataclasses import dataclass
from catboost import CatBoostRegressor
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score


@dataclass
class ModelTrainerConfig:
    trained_model_file_path = os.path.join("artifacts","model.pkl")


class ModelTrainer:
    def __init__(self):
        self.model_trainer_config = ModelTrainerConfig()
    
    def initiate_model_trainer(self, train_array, test_array):
        try:
            logging.info("Split data to X and y")
            X_train, y_train, X_test, y_test = (train_array[:,:-1], train_array[:,-1], test_array[:,:-1], test_array[:,-1])

            models = {"Linear regression": LinearRegression(), "Catboost":CatBoostRegressor()}

            model_report: dict = evaluate_models(X_train, y_train, X_test, y_test, models)

            best_model_score = max(sorted(model_report.values()))
            best_model_name = list(model_report.keys())[list(model_report.values()).index(best_model_score)]
            best_model = models[best_model_name]

            logging.info(f"{best_model_name} selected as model, r2_score: {best_model_score}")

            saved_obj(self.model_trainer_config.trained_model_file_path, best_model)


        except Exception as e:
            raise CustomException(e, sys)

