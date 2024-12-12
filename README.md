# Click-Through Rate Prediction Using Random Forest

## Overview

This is my final project of Machine Learning.

This project focuses on predicting whether a user will click on an advertisement based on historical user and ad data. 

The dataset comes from the Avazu Click-Through Rate Prediction competition(from the Kaggle), which includes millions of user-click records with various categorical and numerical features. The goal is to use Random Forest to build a model that can predict user behavior effectively.


## Dataset
The dataset includes the following features:

    id: unique identifier for each instance
          
    hour: timestamp of the click
    
    C1: anonymized categorical variable
          
    banner_pos: position of the ad on the page
          
    device_*: device information
          
    site_* and app_*: site/app-related features
          
    Several anonymized categorical variables (e.g., C14, C15, ...).
          
    Target: click (1 if the ad was clicked, 0 otherwise).

The dataset is highly imbalanced, with a small percentage of clicks compared to non-clicks.


## The Basic Step
1. **Preprocess the dataset:** Handle missing values, encode categorical features, and balance the data.
2. **Random Forest:** Classifier to predict the probability of a click.
3. **Evaluation:** Evaluate model performance using metrics such as AUC-ROC, accuracy, and log-loss.
