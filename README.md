faas
=============

This repository contains boilerplate code for Function as a Service


Steps to replicate:

git clone https://github.com/ayanray-tech/faas.git
cd faas
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
cd faas/mlaas
python app.py

API URL:
http://localhost:8888/api/

Sample Payload to Test:
{
  "algorithm": "LDA",
  "field_names": "'preg', 'plas', 'pres', 'skin', 'test', 'mass', 'pedi', 'age', 'class'",
  "source_url": "https://raw.githubusercontent.com/jbrownlee/Datasets/master/pima-indians-diabetes.data.csv"
}
