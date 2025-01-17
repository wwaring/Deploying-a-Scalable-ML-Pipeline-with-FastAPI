import pytest
import pandas as pd
import numpy as np
from sklearn.preprocessing import OneHotEncoder, LabelBinarizer
from sklearn.ensemble import RandomForestClassifier
from ml.data import process_data
from ml.model import compute_model_metrics, train_model
# TODO: add necessary import

# TODO: implement the tests. Change the function name and input as needed.
def test_metrics():
    """
     Test_metrics is test one and it checks that the compute_model_metric
     which is the function that calculates precision and recall is working as expected
     and does not return empty or missing values.
    """
    y_actual = [0,1,1,0,0,1,0,1]
    y_preds = [0,1,0,1,0,1,0,1]
    precision, recall, f1 = compute_model_metrics(y_actual, y_preds)
    assert precision is not None, "precision missing"
    assert recall is not None, "recall missing"
    assert f1 is not None, "F1 missing"

def test_model_type():
    """
    Test_model_type is the second test which ensures that the model training
    function creates a Random Forest model as expected.
    """
    X = [[0,1,1,0,0,1,0,1],[1,0,0,0,1,1,0,0],[1,1,0,0,1,0,1,0],[0,1,1,0,0,1,0,1],[1,0,1,1,0,1,0,0]]
    y = [0,1,1,0,0]
    model = train_model(X,y)
    assert isinstance(model, RandomForestClassifier), "Not a Random Forest"


def test_three():
    """
    Test three verifies that the process_data which is the function that preprocesses
    the data outputs the correct data types. This includes a feature array, 
    a  label array and an encoder.
    """
    data = pd.DataFrame({
        "workclass": ["Private", "Private", "self-emp-not-inc", "Private"],
        "education": ["Bachelors", "HS-grad", "HS-grad", "HS-grad"],
        "marital-status": ["never-married", "married-civ-spouse", "never-married", "never-married"],
        "occupation": ["craft-repair", "craft-repair", "craft-repair", "exec-managerial"],
        "relationship": ["unmarried", "husband", "unmarried", "unmarried"],
        "race": ["White", "Black", "White", "White"],
        "sex": ["Male", "Male", "Female", "Female"],
        "native-country": ["United States", "United States", "Mexico", "United States"],
        "salary": [">50k", "<=50k", ">50k", "<=50k"]
    })
        
    categorical_features = [
        "workclass",
        "education",
        "marital-status",
        "occupation",
        "relationship",
        "race",
        "sex",
        "native-country"
    ]
        
    X, y, encoder, lb = process_data(
        data,
        categorical_features = categorical_features,
        label = "salary",
        training = True
    )

    assert isinstance(X, np.ndarray), "X Not a np array"
    assert isinstance(y, np.ndarray), "y Not a np array"
    assert isinstance(encoder, OneHotEncoder), "Encoder not a One Hot Encoder"
    assert isinstance(lb, LabelBinarizer), "lb not a LabelBinarizer"
    
