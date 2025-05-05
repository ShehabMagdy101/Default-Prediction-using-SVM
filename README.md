# Default-Prediction-using-SVM

Using Logistic Regression, Python Flask Server and streamlit. I was able to build a robust machine learning project, that aqcuire relaibe back-end server and intuitive streamlit UI

## Project Overview
the project include a machine learning model that can predict wheather someone's Loan demand Approved or Rejected based on some features
the project can be described in 3 main parts:
- Machine learning model - a trained model that predicts the loan approval based on entered data.
- Flask server -  an intermediate layer that act between the trained machine Learning model and the Streamlit UI.
- Streamlit User Interface - a simple UI where user can enter data to get the prediction of Loan Approval.

## Deliverables

- `analysis and modeling.ipynb` jupyter notebook including the data preprocessing, analysis, model training and serialization
- `requirements.txt` Python packages used in the project
- `credit_model.pkl` Serialized saved trained machine leaning model
- `flask_app.py` Flask local server that have dedicated endpoint for prediciting new data points
- `streamlit_app.py` Sreamlit application that represents the user interface to enter the new data points to be predicted
- `modeling_functions.py` Object class of the model for abstraction

## Project Setup Instructions

1. Clone the Repo
```bash
git clone https://github.com/ShehabMagdy101/Default-Prediction-using-SVM.git
cd Default-Prediction-using-SVM
```

2. Install Python Packages

```bash
pip install -r requirements.txt
```

3. Run the server

```bash
python flask_app.py
```

4. Run the Streamlit application

```bash
streamlit run streamlit_app.py
```

## Project Structure

```
predict-loan-approval/
├── analysis and modeling.ipynb              
├── streamlit_app.py          
├── flask_app.py                 
├── credit_model.pkl                
├── requirements.txt           
├── modeling_functions.py           
└── README.md                  
```

## Requirements

- Python 3.12.10
- Packages Listed in (`requirements.txt`)
  - `pandas`
  - `numpy`
  - `scikit-learn`
  - `joblib`
  - `Flask`
  - `streamlit`
  - `requests`
