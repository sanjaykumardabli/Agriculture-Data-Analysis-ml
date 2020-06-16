from flask import Flask, render_template, request
from flask_debug import Debug
from sklearn.metrics import accuracy_score
import numpy as np
import pickle
import pandas as pd



app = Flask(__name__)



@app.route("/")
def index():
    return render_template("index.html")

@app.route("/file_resend",methods = ['GET','POST'])
def file_resend():
    if request.method == 'POST':
        a = int(request.form['url'])
        if a == 1:
            return render_template("clustering.html")
        elif a == 2:
            return render_template("classification.html")
        elif a == 3:
            return render_template("nkn.html")

@app.route("/predict",methods = ['GET','POST'])
def predict():
    ui = []
    if request.method == 'POST':
        ui.append(int(request.form['state']))
        ui.append(int(request.form['season']))
        ui.append(int(request.form['crop']))
        ui.append(int(request.form['yeild']))
        a = int(request.form['yeild'])
        if a == 0:
            return render_template('classification.html')

        l = []
        l.append(ui)
        rfc=pickle.load(open('model/nb_model.sav', 'rb'))

        result = rfc.predict(l)
        print(result)
        
        #engine.setProperty('voice', voices[1].id)
        
        #engine.setProperty('voice', voices[1].id)
        # o = []
        # o.append(result)
        if result == 0:
            
            
            res="Your going to get LOW yeild this year"
            
        elif result == 1:
            
            res="Your going to get an AVERAGE yeild this year"
            
        elif result == 2:
            
            res="Your going to get GOOD yeild this year"
            
        elif result == 3:
            import pyttsx3
            
            res="Your going to get VERY GOOD yeild this year"
            
        elif result == 4:
            
            res="Your going to get an Excelant yeild this year"
        #o.append(res)
        
        return render_template('classificationresult.html',u=res,re=result)
    
    return render_template('classification.html')


        


@app.route("/cluster",methods=['GET','POST'])
def cluster():
    return render_template("clusteResult.html")
if __name__ == '__main__':
    app.run(debug=False)
