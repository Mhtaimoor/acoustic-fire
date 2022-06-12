from flask import Flask, render_template,request
import pickle
import numpy as np
#from sklearn.ensemble.forest import RandomForestClassifier

app= Flask(__name__)


svc_model = pickle.load(open('svc_trained_model.pkl', 'rb'))


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/predict', methods=['POST'])
def predict():
    inputs = []
    inputs.append(request.form['size'])
    inputs.append(request.form['fuel'])
    inputs.append(request.form['distance'])
    inputs.append(request.form['desibel'])
    inputs.append(request.form['airflow'])
    inputs.append(request.form['frequency'])
    
    size = request.form['size']
    fuel = request.form['fuel']
    distance = request.form['distance']
    desibel = request.form['desibel']
    airflow = request.form['airflow']
    frequency = request.form['frequency']
    
    
    final_inputs = [np.array(inputs)]
    prediction = svc_model.predict(final_inputs)
    
    
    if prediction[0] == 1:
        categorical_array = "Extinction State"
    if prediction[0] == 0:
        categorical_array = "Non-Extinction State"
        
        
    result = categorical_array
    
    if size == "1":
        size = "7 cm"
    if size == "2":
        size = "12 cm"
    if size == "3":
        size = "14 cm"
    if size == "4":
        size = "16 cm"
    if size == "5":
        size = "20 cm"
    if size == "6":
        size = "Half Throttle"
    if size == "7":
        size = "Full Throttle"
        
    if fuel == "1":
        fuel = "Gasoline"
    if fuel == "2":
        fuel = "Karosene"
    if fuel == "3":
        fuel = "Thinner"
    if fuel == "4":
        fuel = "LPG"
        
    if (distance >= 10 & distance <=70):
        distance = "greater than 10 and less than 70"
    if (distance > 70 & distance <=190):
        distance = "greater than 70 and less than 190"
        
    if (desibel >= 72 & desibel <=100):
        desibel = "greater than 72 and less than 100"
    if (desibel > 101 & desibel <=113):
        desibel = "greater than 101 and less than 113"
    
    
    if (airflow >= 0 & airflow <=17):
        airflow = "greater than 0 and less than 17"
        
    if (frequency >= 1 & frequency <=75):
        frequency = "greater than 1 and less than 75"
    
    
    return render_template('index.html', status_1=result, size_1 = size, fuel_1 = fuel, distance_1 = distance, airflow_1 = airflow, desibel_1 = desibel, frequency_1 = frequency )


if __name__ == "__main__":
    app.run(debug=True, use_reloader=False)
    
   