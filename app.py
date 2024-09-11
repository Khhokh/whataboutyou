from flask import Flask,render_template,request,redirect
from flask_cors import CORS,cross_origin
import pickle
import pandas as pd
import numpy as np

app=Flask(__name__)
cors=CORS(app)


#///////////////////////////////////////////// BOTH MODELS ///////////////////////////////////////////////////////
#/////////////////////////////////////////////////////////////////////////////////////////////////////////////////
model=pickle.load(open('bikePre.pkl','rb'))
model1 = pickle.load(open('LinearRegressionModel2(1).pkl','rb'))




#//////////////////////////////////// FOR THE RENDERING OF THE HTML PAGES ///////////////////////////////////////
#///////////////////////////////////////////////////////////////////////////////////////////////////////////////
@app.route('/',methods=['GET','POST'])
def index():
    return render_template('index1.html')


@app.route('/about')
def index2():
    return render_template('index.html')


@app.route('/about-next')
def index3():
    return  render_template('index2.html')




#/////////////////////////// FOR THE BIKE PRICE PREDECTION MODEL ///////////////////////////
#///////////////////////////////////////////////////////////////////////////////////////////

@app.route('/predict',methods=['POST'])
@cross_origin()
def predict():

    Sno=request.form.get('Sno')

    Fuel_type=request.form.get('Fuel_type')
    CC=request.form.get('CC')
    Fuel_Capacity=request.form.get('Fuel_Capacity')
    Bike_company_name=request.form.get('Bike_company_name')

    predict=model.predict(pd.DataFrame(columns=['S.no', 'Fuel_type', 'CC(Cubic capacity)', 'Fuel_Capacity', 'Bike_company_name'],
                                       data=np.array([Sno,Fuel_type,CC,Fuel_Capacity,Bike_company_name]).reshape(1, 5)))
    print(predict)

    return str(np.round(predict[0],2))




#///////////////////////// FOR THE MODEL CAR PRICE PREDECTIONS ////////////////////////////////////////
#//////////////////////////////////////////////////////////////////////////////////////////////////////
@app.route('/predict2',methods=['POST'])
@cross_origin()
def predict2():
    company=request.form.get('company')

    car_model=request.form.get('car_models')
    year=request.form.get('year')
    fuel_type=request.form.get('fuel_type')
    driven=request.form.get('kilo_driven')

    predict=model1.predict(pd.DataFrame(columns=['name', 'company', 'year', 'kms_driven', 'fuel_type'],
                                       data=np.array([car_model,company,year,driven,fuel_type]).reshape(1, 5)))
    print(predict)

    return str(np.round(predict[0],2))



if __name__=='__main__':
    app.run()