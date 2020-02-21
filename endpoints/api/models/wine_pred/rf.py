import numpy as np
import pandas as pd
import scipy as sp
from scipy.stats import stats, mannwhitneyu
from sklearn.model_selection import train_test_split, KFold, cross_val_score, cross_val_predict
from sklearn import metrics, linear_model, model_selection
from sklearn.preprocessing import StandardScaler
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from sklearn.metrics import r2_score
from sklearn.ensemble import RandomForestRegressor
from textblob import TextBlob, Word
from nltk.stem.snowball import SnowballStemmer
from sklearn.feature_selection import SelectFromModel
from sklearn.tree import export_graphviz
import joblib
# importing unicodedata to handle é in rosé wine variety
import unicodedata


class RandomForestClassifier:
    def __init__(self):
        path_to_artifacts = "../backend/endpoints/api/models/wine_pred/"
        self.values_fill_missing = joblib.load(
            path_to_artifacts + "A2_train.joblib")
        self.model = joblib.load(path_to_artifacts + "rfreg.joblib")

    def preprocessing(self, input_data):
        # JSON to pandas DataFrame
        input_data = pd.DataFrame(input_data, index=[0])
        # fill missing values
        input_data.fillna(self.values_fill_missing)

        return input_data

    def predict(self, input_data):
        return self.model.predict_proba(input_data)

    def compute_prediction(self, input_data):
        try:
            input_data = self.preprocessing(input_data)
            prediction = self.predict(input_data)[0]  # only one sample
        except Exception as e:
            return {"status": "Error", "message": str(e)}

        return prediction
