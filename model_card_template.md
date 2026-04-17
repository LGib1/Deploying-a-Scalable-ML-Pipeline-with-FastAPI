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

## Evaluation Data

## Metrics
_Please include the metrics used and your model's performance on those metrics._

## Ethical Considerations

## Caveats and Recommendations
