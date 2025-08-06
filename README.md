# Credit Score Analysis

[Anton Markov et al (Credit scoring methods: Latest trends and points to consider, 2022)](https://www.sciencedirect.com/science/article/pii/S2405918822000095) suggest that University of California Irvine's datasets are among the most popular public sources for credit score modeling. I have chosen the [UCI (Statlog) German Credit Data](https://archive.ics.uci.edu/dataset/144/statlog+german+credit+data) to begin with.

## German Credit Data 

This dataset contains information about 1000 loan applications, including personal and financial data, credit history, and loan characteristics.

## Objective

Train models in order to predict whether a loan is benefitial or not, in other words predict its creditability for the finantial institution.

#### Absent classes

#### A4. Purpose
- A47: vacation

#### A9. Personal status and sex 
- A95: female - single

## Fayaad steps

### 1. Selection
### 2. Preprocessing
### 3. Transformation
### 4. Data mining
### 5. Evaluation

## Models

### 1. Logistic Regression

Due to some imbalanced columns, the logreg model presents difficulty in predicting "Bad" loans. To overcome this limitation we might consider oversampling the misrepresented categories in these columns.

### 2. Decision tree
### 3. Random forest
### 4. XGBoost
### 5. Support vector machine
### 6. Neural networks