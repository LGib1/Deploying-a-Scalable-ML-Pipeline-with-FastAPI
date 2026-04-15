import os
import pytest 
import pandas as pd
from sklearn.model_selection import train_test_split
from fastapi.testclient import TestClient
from main import app

# TODO: add necessary import

@pytest.fixture(scope="session")
def data():
    """ Loads the census data for testing. 
    """
    data_path = os.path.join(".", "data", "census.csv")
    data = pd.read_csv(data_path)
    return data

@pytest.fixture(scope="session")
def client():
    """ Creates a TestClient for the FastAPI app. 
    """
    return TestClient(app)

# TODO: implement the first test. Change the function name and input as needed

def test_complete_data_columns(data):
    """
    Checks to ensure all the required columns are present in the data. Note, 
    variables table, https://archive.ics.uci.edu/dataset/20/census+income, identifies 
    15 columns, and and has some variation in variable name. 
    """
    req_columns = ["age", "workclass", "education", "marital-status", "occupation", "relationship", 
                   "race", "sex", "native-country", "salary"]
    
    missing = set(req_columns) - set(data.columns)
    assert not missing, f'Missing columns: {missing}'


def test_train_test_split(data):
    """
    # Checks to ensure the train-test split is done correctly. 
    """
    train, test = train_test_split(data, test_size=0.3, random_state=42, shuffle=True)
    
    assert len(train) + len(test) == len(data), "Train and test datasets do not sum up to total data length."
    assert set(train.index).isdisjoint(set(test.index)), "Train and test datasets are not mutually exclusive."  
    assert abs(len(test) - 0.3 * len(data)) <= 1



def test_split_not_empty(data):
    """# Checks to ensure the train-test split is done correctly. 
    """    
    train, test = train_test_split(data, test_size=0.3, random_state=42, shuffle=True)
    assert not train.empty
    assert not test.empty

def test_api_root(client):
    """
    test that the API is up and running and can be connected to.
    """ 
    response = client.get("/")
    assert response.status_code == 200, "API is not reachable."
    assert "Welcome" in response.json().get("message", "")



