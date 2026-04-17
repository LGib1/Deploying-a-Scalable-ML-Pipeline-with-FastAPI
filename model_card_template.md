# Model Card

For additional information see the Model Card paper: https://arxiv.org/pdf/1810.03993.pdf

## Model Details
* Model Type: RandomForestClassifier
* Framework: Scikit-learn
* Version: 1.0
* Developed By: Lisa Gibbons, student project for Udacity in conjunction with WGU
* Date: 2026
* Input Data: Demographic and employment attributes from the UCI Census Income dataset, citation below: 

Kohavi, R. (1996). Census Income [Dataset]. UCI Machine Learning Repository. https://doi.org/10.24432/C5GP7S.
Alternate Input Data Link: https://archive.ics.uci.edu/dataset/20/census+income

* Output Data: Predicts whether an individual’s income is > $50,000.00 or <= $50,000.00 as a binary classification.

* Hyperparameters:
RandomForest hyperparameters:
        n_estimators=100        
        max_depth=None,
        min_samples_split=2,
        min_samples_leaf=1,
        n_jobs=-1,
        random_state=42
    

## Intended Use
Developed for educational purposes as part of an Udacity course offered at WGU to teach:

* ML model development
* Data processing pipelines
* Model Deployment with FastAPI
* Slice-based fairness analysis

 ** Not intended for real-world use. ** 

## Training Data
The model creates a train-test split of the Input Data (identified above) with 70% to the train set, and a hold-out of 30% to the test set. 

The Input Data contains 48,842 rows and 15 columns and was extracted from the 1994 Census database. Of the 15 columns, the following, categorical features, were included in the model: 

* workclass
* education
* marital-status
* occupation
* relationship
* race
* sex
* native-country

Categorical features were one-hot encoded using a fitted OneHotEncoder.
The target label (“salary”) was binarized using LabelBinarizer.

## Evaluation Data
Evaluation was performed on the held-out 30% creating the test set. The same encoder and label binarizer was used to ensure consistency. 

Slice-based evaluation was performed across the above identified categorical features, and results were logged in slice_output.txt. 

## Metrics
The following metrics were computed and reflect the model’s ability to predict an individual’s binary category for earnings:

* Precision: 0.7220, which means that the model correctly predicts an individual’s salary > $50,000.00 approximately 72% of the time. 
* Recall: 0.6219, which means the model captures approximately 62% of individuals with income > $50,000.00. 
* F1: 0.6682, which balances Precision and Recall into a single measure. 

The model performed slice-based performance to evaluate slices of key categorical features. The output is logged in slice_output.txt. 
A review of the slice_output.txt identified limited sample size for certain categorical data including but not limited to 
lower education levels (specifically preschool levels), and certain native countries. 

## Ethical Considerations

## Caveats and Recommendations
