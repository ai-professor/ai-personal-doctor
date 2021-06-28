from flask import Flask, render_template, url_for, flash, redirect
import joblib
from flask import request
import numpy as np

app = Flask(__name__, template_folder='templates')

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/Heart")
def heart():
    return render_template("heart.html")

@app.route("/Diabetes")
def diabetes():
    return render_template("diabetes.html")

@app.route("/Liver")
def liver():
    return render_template("liver.html")

@app.route("/Kidney")
def kidney():
    return render_template("kidney.html")

@app.route("/BreastCancer")
def breastCancer():
    return render_template("cancer.html")



def ValuePredictorDia(to_predict_list_dia, size):
    to_predictDia = np.array(to_predict_list_dia).reshape(1,size)
    if(size==6):
        loaded_model_dia = joblib.load('diabetes_model.pkl')
        resultDia = loaded_model_dia.predict(to_predictDia)
    return resultDia[0]
    

def ValuePredictorHeart(to_predict_list_heart, size):
    to_predictHeart = np.array(to_predict_list_heart).reshape(1,size)
    if(size==7):
        loaded_model_heart = joblib.load('heart_model.pkl')
        resultHeart = loaded_model_heart.predict(to_predictHeart)
    return resultHeart[0]


def ValuePredictorLiver(to_predict_list_liver, size):
    to_predictLiver = np.array(to_predict_list_liver).reshape(1,size)
    if(size==7):
        loaded_model_liver = joblib.load('liver_model.pkl')
        resultLiver = loaded_model_liver.predict(to_predictLiver)
    return resultLiver[0]

def ValuePredictorKidney(to_predict_list_kidney, size):
    to_predictKidney = np.array(to_predict_list_kidney).reshape(1,size)
    if(size==7):
        loaded_model_kidney = joblib.load('liver_model.pkl')
        resultKidney = loaded_model_kidney.predict(to_predictKidney)
    return resultKidney[0]

def ValuePredictorCancer(to_predict_list_cancer, size):
    to_predictCancer = np.array(to_predict_list_cancer).reshape(1,size)
    if(size==5):
        loaded_model_cancer = joblib.load('cancer_model.pkl')
        resultCancer = loaded_model_cancer.predict(to_predictCancer)
    return resultCancer[0]


@app.route('/predictDia', methods = ["POST"])
def predictDia():
    if request.method == "POST":
        to_predict_list_dia = request.form.to_dict()
        to_predict_list_dia = list(to_predict_list_dia.values())
        to_predict_list_dia = list(map(float, to_predict_list_dia))
         #diabetes
        if(len(to_predict_list_dia)==6):
            resultDia = ValuePredictorDia(to_predict_list_dia,6)
    
    if(int(resultDia)==1):
        predictionDia = "Sorry! Maybe you have chances to getting the Diabetes. Please consult the your doctor immediately"
    else:
        predictionDia = "Don't Worry,. You don't have any Symptoms of the Diabetes"
    return(render_template("result.html", prediction_text=predictionDia)) 


@app.route('/predictHeart', methods = ["POST"])
def predictHeart():
    if request.method == "POST":
        to_predict_list_heart = request.form.to_dict()
        to_predict_list_heart = list(to_predict_list_heart.values())
        to_predict_list_heart = list(map(float, to_predict_list_heart))
         #diabetes
        if(len(to_predict_list_heart)==7):
            resultHeart = ValuePredictorHeart(to_predict_list_heart,7) 

    if(int(resultHeart)==1):
        predictionHeart = "Sorry! Maybe you have chances to getting the Heart Diseases. Please consult the your doctor immediately"
    else:
        predictionHeart = "Don't Worry,. You don't have any Symptoms of the Heart Diseases"
    return(render_template("result.html", prediction_text=predictionHeart))


@app.route('/predictLiver', methods = ["POST"])
def predictLiver():
    if request.method == "POST":
        to_predict_list_liver = request.form.to_dict()
        to_predict_list_liver = list(to_predict_list_liver.values())
        to_predict_list_liver = list(map(float, to_predict_list_liver))
         #diabetes
        if(len(to_predict_list_liver)==7):
            resultLiver = ValuePredictorLiver(to_predict_list_liver,7) 

    if(int(resultLiver)==1):
        predictionLiver = "Sorry! Maybe you have chances to getting the Liver Infections. Please consult the your doctor immediately"
    else:
        predictionLiver ="Don't Worry,. You don't have any Symptoms of about Liver Infections"
    return(render_template("result.html", prediction_text=predictionLiver)) 

@app.route('/predictKidney', methods = ["POST"])
def predictKidney():
    if request.method == "POST":
        to_predict_list_kidney = request.form.to_dict()
        to_predict_list_kidney = list(to_predict_list_kidney.values())
        to_predict_list_kidney = list(map(float, to_predict_list_kidney))
         #diabetes
        if(len(to_predict_list_kidney)==7):
            resultKidney = ValuePredictorKidney(to_predict_list_kidney,7) 

    if(int(resultKidney)==1):
        predictionKidney = "Sorry! Maybe you have chances to getting the Kidney Diseases. Please consult the your doctor immediately"
    else:
        predictionKidney = "Don't Worry,. You don't have any Symptoms of the Kidney Diseases"
    return(render_template("result.html", prediction_text=predictionKidney))

@app.route('/predictCancer', methods = ["POST"])
def predictCancer():
    if request.method == "POST":
        to_predict_list_cancer = request.form.to_dict()
        to_predict_list_cancer = list(to_predict_list_cancer.values())
        to_predict_list_cancer = list(map(float, to_predict_list_cancer))
         #diabetes
        if(len(to_predict_list_cancer)==5):
            resultCancer = ValuePredictorCancer(to_predict_list_cancer,5) 

    if(int(resultCancer)==1):
        predictionCancer = "Sorry! Maybe you have chances to getting Breast Cancer. Please consult the your doctor immediately"
    else:
        predictionCancer = "Don't Worry,. You don't have any Symptoms of the Breast Cancer"
    return(render_template("result.html", prediction_text=predictionCancer)) 


       

if __name__ == "__main__":
    app.run(debug=True, port=8000)
