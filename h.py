from flask import Flask, render_template, request,jsonify
import pandas as pd
import pickle
import numpy as np
import os

app = Flask(__name__)

model = pickle.load(open("b.pkl", 'rb'))
@app.route('/')
def index():
    result= ' '
    return render_template('h.html', **locals())

@app.route('/predict', methods=['POST', 'GET'])
def predict():
    Absolute_Magnitude = float(request.form['absolutemagnitude'])
    Est_Dia_in_KM = float(request.form['estdiainkm'])
    Relative_velocity = float(request.form['relativevelocity'])
    Miss_Dist = float(request.form['missdist'])
    Orbit_Uncertainty = float(request.form['orbituncertainity'])
    Minimum_Orbit_Intersection = float(request.form['minimumorbit'])     
    Jupiter_Tisserand_Invariant = float(request.form['jupiter'])
    Epoch_Osculation = float(request.form['epoch'])
    Eccentricity = float(request.form['eccentricity'])
    Semi_Major_Axis = float(request.form['semimajoraxis'])
    Inclination = float(request.form['inclination'])
    Asc_Node_Longitude = float(request.form['longitude'])        
    Orbital_Period = float(request.form['orbitalperiod'])
    Perihelion_Distance = float(request.form['periheliondistance'])
    Perihelion_Arg = float(request.form['perihelionarg'])
    Aphelion_Dist = float(request.form['apheliondistance'])
    Perihelion_Time = float(request.form['periheliontime'])
    Mean_Anomaly = float(request.form['meananomaly'])
    Mean_Motion = float(request.form['meanmotion'])
    



    result = model.predict([[Absolute_Magnitude, Est_Dia_in_KM, Relative_velocity, Miss_Dist,
                Orbit_Uncertainty, Minimum_Orbit_Intersection, Jupiter_Tisserand_Invariant, Epoch_Osculation,
                Eccentricity, Semi_Major_Axis, Inclination, Asc_Node_Longitude, Orbital_Period,
                Perihelion_Distance, Perihelion_Arg, Aphelion_Dist, Perihelion_Time, Mean_Anomaly, Mean_Motion]])[0]

    return render_template('h.html', result=result)

if __name__ == "__main__":
    app.run(debug=True)
    
    

    
    
    
    

