import numpy as np
from flask import Flask, request, render_template
import os

from joblib import load,dump
# template_dir=os.path.dirname(os.path.abspath(os.path.dirname(__file__)))
# working='C:\VIT\Machine learning\flask'
# print(working==template_dir)
app = Flask(__name__)
loaded=load('final_model.joblib')



@app.route('/')
def home():
    return render_template('home.html')

@app.route('/predict',methods=['POST','GET'])
def predict():
    '''
    For rendering results on HTML GUI
    '''
    # int_features=[]
    print("cheeck")
    print(request.data)
    # int_features =int_features.append([float(x) for x in request.form.values()])
    # final_features = int_features
    
    # prediction = loaded.predict([[final_features]])

    # output = prediction

    return render_template('home.html')



if __name__ == "__main__":
    app.run(debug=True)