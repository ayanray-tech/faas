# Function As A Service
=============


This repository serves as a boilerplate for deploying machine learning models
as RESTful web services following factory and strategy design patterns.


## Salient Features:


1. RESTful web service
2. ML Model scoring as a Service
3. Single Responsibility Principle
4. Design patterns
5. Factory Design pattern
6. Strategy Design pattern


### It consists of two API endpoints:


1. model/score/usingfactory
2. model/score/usingstrategy


### Each endpoint expects the following inputs:


1. algorithm
2. field names
3. source data url


### Below is a sample payload:


`{
  "algorithm": "LR",
 "field_names": "'preg', 'plas', 'pres', 'skin', 'test', 'mass', 'pedi', 'age', 'class'", "source_url": "https://raw.githubusercontent.com/jbrownlee/Datasets/master/pima-indians-diabetes.data.csv"
}`


### Each endpoint when successfully executed returns the following output:


1. ML Algorithm which was executed
2. Mean Accuracy
3. Standard Deviation Accuracy


### Below is a sample Response:


`{
  "Algorithm": "Logistic Regression",
  "Mean Accuracy": 0.7695317840054681,
  "Standard deviation Accuracy": 0.05328344234318639
}`


## Deployment steps:

```
git clone https://github.com/ayanray-tech/faas.git
cd faas
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
cd faas/mlaas
python app.py
```


## API URL:
http://localhost:8888/api/
