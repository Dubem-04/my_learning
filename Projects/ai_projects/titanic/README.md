# 🚢 Titanic Survival Prediction

## Overview

Predicting which passengers survived the Titanic disaster using passenger data.
A binary classification problem — my first end-to-end ML project.

## Dataset

- Source: [Kaggle Titanic Competition](https://kaggle.com/competitions/titanic)
- Files: `train.csv`, `test.csv`, `gender_submission.csv`

## Tools Used

- Python, Pandas, NumPy
- Matplotlib, Seaborn
- Scikit-learn

## Approach

### Attempt 1 (Minimal Baseline Model)
**Overview:**
This submission establishes a minimal baseline using a Random Forest Classifier. The objective of this model is to provide a concrete performance floor using only the raw numeric and easily encoded categorical data, with zero advanced feature engineering.

**Data Preprocessing:**

    Feature Selection: Retained only Pclass, Sex, Age, SibSp, Parch, and Fare.

    Dropped Features: Excluded all text and highly incomplete columns (Name, Ticket, Cabin, Embarked) to allow for immediate model compilation.

    Encoding: Applied simple binary integer mapping to the Sex column (male: 0, female: 1).

**Imputation Strategy:**

    Used Scikit-learn's SimpleImputer with a median strategy to handle missing values, specifically targeting the Age and Fare columns.

    The imputer was fitted exclusively on the training dataset to prevent data leakage into the test set.

**Model Architecture & Hyperparameters:**

    Algorithm: Scikit-learn RandomForestClassifier

    random_state: 42 (Ensured reproducibility).

**Validation Strategy:**

    Evaluated locally prior to full training using an 80/20 train_test_split.

    The final submission model was retrained on the entire imputed training dataset before generating predictions on the blind competition test set.


## Results

| Attempt | Model | Kaggle Score |
| ------- | ----- | ------------ |
| 1       | RandomForestClassifier | 0.73684 |

## Key Learnings

- For a model to be good enough, there are a lot of factors to be considered. From how missing values are handled, choice of model, hyperparameter tuning

- When `max_depth` is high, the tree is allowed to grow incredibly deep. If it is `None`, the tree will keep splitting until every single leaf node contains only one class of data.

## Next Improvements

Create a git branch with the following changes.