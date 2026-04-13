import pickle
from xml.parsers.expat import model
from sklearn.metrics import fbeta_score, precision_score, recall_score
from ml.data import process_data
# TODO: add necessary import
import os
import pandas as pd
import numpy as np
from sklearn.preprocessing import OneHotEncoder, LabelBinarizer
from sklearn.metrics import make_scorer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import GridSearchCV
from typing import Union


# Optional: implement hyperparameter tuning.
def train_model(X_train: Union[pd.DataFrame, np.ndarray], 
                y_train: Union[pd.Series, np.ndarray],
                parameters: dict = None) -> LogisticRegression:
    """
    Trains a machine learning model and returns it.

    Inputs
    ------
    X_train : np.array
        Training data.
    y_train : np.array
        Labels.
    Returns
    -------
    model
        Trained machine learning model.
    """
    # TODO: implement the function
    clf = LogisticRegression(random_state=72925)
    scorer = make_scorer(fbeta_score,  beta=1)
    grid_object = GridSearchCV(clf, parameters, scoring=scorer, n_jobs=-1, cv=5)
    grid_fit = grid_object.fit(X_train, y_train)
    best_clf = grid_fit.best_estimator_
    best_clf.fit(X_train, y_train)

    return best_clf

def compute_model_metrics(y: Union[pd.Series, np.ndarray], preds: Union[pd.Series, np.ndarray]):
    """
    Validates the trained machine learning model using precision, recall, and F1.

    Inputs
    ------
    y : np.array
        Known labels, binarized.
    preds : np.array
        Predicted labels, binarized.
    Returns
    -------
    precision : float
    recall : float
    fbeta : float
    """
    fbeta = fbeta_score(y, preds, beta=1, zero_division=1)
    precision = precision_score(y, preds, zero_division=1)
    recall = recall_score(y, preds, zero_division=1)
    return precision, recall, fbeta


def inference(model: LogisticRegression, X: Union[pd.DataFrame, np.ndarray]) -> Union[np.ndarray, pd.Series]:
    """ Run model inferences and return the predictions.

    Inputs
    ------
    model : RandomForestClassifier
        Trained machine learning model.
    X : np.array
        Data used for prediction.
    Returns
    -------
    preds : np.array
        Predictions from the model.
    """
    # TODO: implement the function
    return model.predict(X)

def save_model(model, path: str) -> None:
    """ Serializes model to a file.

    Inputs
    ------
    model
        Trained machine learning model or OneHotEncoder.
    path : str
        Path to save pickle file.
    """
    # TODO: implement the function
    #pass
    if os.path.exists(path):
        os.unlink(path) #remove the file if it already exists
    with open(path, 'wb') as pickle_file:
        pickle.dump(model, pickle_file)

def load_model(path):
    """ Loads pickle file from `path` and returns it."""
    # TODO: implement the function
    #pass
    with open(path, 'rb') as pickle_file:
        model = pickle.load(pickle_file)
    return model

def performance_on_categorical_slice(
    data, column_name, slice_value, categorical_features, label, encoder, lb, model
):
    """ Computes the model metrics on a slice of the data specified by a column name and

    Processes the data using one hot encoding for the categorical features and a
    label binarizer for the labels. This can be used in either training or
    inference/validation.

    Inputs
    ------
    data : pd.DataFrame
        Dataframe containing the features and label. Columns in `categorical_features`
    column_name : str
        Column containing the sliced feature.
    slice_value : str, int, float
        Value of the slice feature.
    categorical_features: list
        List containing the names of the categorical features (default=[])
    label : str
        Name of the label column in `X`. If None, then an empty array will be returned
        for y (default=None)
    encoder : sklearn.preprocessing._encoders.OneHotEncoder
        Trained sklearn OneHotEncoder, only used if training=False.
    lb : sklearn.preprocessing._label.LabelBinarizer
        Trained sklearn LabelBinarizer, only used if training=False.
    model : RandomFrostClassifier
        Model used for the task.

    Returns
    -------
    precision : float
    recall : float
    fbeta : float

    """
    # TODO: implement the function
    X_slice, y_slice, _, _ = process_data(
        # your code here
        # for input data, use data in column given as "column_name", with the slice_value 
        # use training = False
        sliced_data, 
        categorical_features, 
        label, 
        encoder, 
        lb, 
        training=False, 
        std_scaler=std_scaler
    )
    preds = inference(model=model, X=X_slice) #None # your code here to get prediction on X_slice using the inference function
    precision, recall, fbeta = compute_model_metrics(y_slice, preds)
    return precision, recall, fbeta
