import numpy as np
import pandas as pd
import scipy as sp
import seaborn as sns
import matplotlib.pyplot as plt

from scipy.stats import stats, mannwhitneyu
from sklearn.model_selection import train_test_split, KFold, cross_val_score, cross_val_predict
from sklearn import metrics, linear_model, model_selection
from sklearn.linear_model import LinearRegression, LogisticRegression
from sklearn.preprocessing import StandardScaler
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
#from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import r2_score
from textblob import TextBlob, Word
from nltk.stem.snowball import SnowballStemmer
from sklearn.feature_selection import SelectFromModel
from sklearn.tree import export_graphviz

# importing unicodedata to handle é in rosé wine variety
import unicodedata
%matplotlib inline

# Load dataset and save as 'wine' variable. After importing all dependencies we load our dataset called wine.
wine = pd.read_json(
    './wine-reviews/winemag-data-130k-v2.json', dtype='unicode')

# Cleaning up accent marks within dataset by replacing Rosé with Rose.
wine.loc[:, 'variety'].replace(u'Rosé', 'Rose', inplace=True)

# changing dtypes for points and price
wine['points'] = wine.points.astype(int)
wine['price'] = wine.price.astype(float)

# Dropping nan values
wine.dropna(inplace=True)

# Dummy Data The next step to building our model is to dummy the data. I've dummied country, designation, province, region_1, region_2, and variety. This will allow us to assign numeric values to categories which we'll use in our model.
dummy = pd.get_dummies(
    wine[['country']], prefix='dum_country', drop_first=True)
dummy = pd.get_dummies(wine[['designation']],
                       prefix='dum_designation', drop_first=True)
dummy = pd.get_dummies(
    wine[['province']], prefix='dum_province', drop_first=True)
dummy = pd.get_dummies(
    wine[['region_1']], prefix='dum_region_1', drop_first=True)
dummy = pd.get_dummies(
    wine[['region_2']], prefix='dum_region_2', drop_first=True)
dummy = pd.get_dummies(
    wine[['variety']], prefix='dum_variety', drop_first=True)

# Concatenate the original DataFrame and the dummy DataFrame (axis=0 means rows, axis=1 means columns).
dummy_wine = pd.concat([wine, dummy], axis=1)

# Feature Selection
# save the correlation function in a variable
corr_dummy_wine = dummy_wine.corr()

corr_points = corr_dummy_wine.loc[:, ['points']]
