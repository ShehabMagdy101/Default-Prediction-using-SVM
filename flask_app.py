from flask import Flask, request, jsonify
import joblib
import numpy as np
import pandas as pd

from model_functions import CreditRiskModel

app = Flask(__name__)

#Load the trained model
model = joblib.load('credit_model.pkl')

@app.route('/')
def home():
    return "Model API is running"

@app.route('/predict',methods = ['POST'])
def predict():
    try:
        data = request.get_json()

        columns = ['LIMIT_BAL', 'SEX', 'EDUCATION', 'MARRIAGE', 'AGE', 'PAY_1', 'PAY_2', 'PAY_3', 'PAY_4', 'PAY_5', 'PAY_6', 'BILL_AMT1', 'PAY_AMT1', 'PAY_AMT2', 'PAY_AMT3', 'PAY_AMT4', 'PAY_AMT5', 'PAY_AMT6']
        features = pd.DataFrame(np.array([data['features']]), columns = columns)
        prediction = model.predict(features)
        if prediction == 0:
            result = "Customer will not default"
        else:
            result = "Customer will default"

        return jsonify({'prediction': result})
    except Exception as e:
        return jsonify({'error': str(e)})
    
if __name__ == '__main__':
    app.run(debug=True)
