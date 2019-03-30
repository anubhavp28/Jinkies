from app import app
import json
from flask import render_template, jsonify, url_for, request, session, redirect
from pymongo import MongoClient

client = MongoClient('3.94.109.234')

Data = list(client.ci.builds.find())
data = Data[-1]
List = list(data.keys())
for obs in List:
	if obs == "history":
		loss = history['loss']
		acc = history['acc']
		precision = history['precision']
		recall = history['recall']
		fmeasure = history['fmeasure']
		binary_crossentropy = history['binary_crossentropy']
		mean_squared_error = history['mean_squared_error']
		mean_absolute_percentage_error = history['mean_absolute_percentage_error']
		mean_squared_logarithmic_error = history['mean_squared_logarithmic_error']
		f1 = history['f1']
		val_acc = history['val_acc']
		val_precision = history['val_precision']
		val_recall = history['val_recall']
		val_fmeasure = history['val_fmeasure']
		val_binary_crossentropy = history['val_binary_crossentropy']
		val_mean_squared_error = history['val_mean_squared_error']
		val_mean_absolute_percentage_error = history['val_mean_absolute_percentage_error']
		val_mean_squared_logarithmic_error = history['val_mean_squared_logarithmic_error']
		val_f1 = history['val_f1']

_id = list(data['_id'])
build_time = list(data['build_time'])
ACC = list(data['ACC'])
HYPERPARAMETER = list(data['HYPERPARAMETER'])
LOSS = list(data['LOSS'])
NO_OF_CORRECT_PREDICTIONS = list(data['NO_OF_CORRECT_PREDICTIONS'])
NO_OF_WRONG_PREDICTIONS = list(data['NO_OF_WRONG_PREDICTIONS'])
PRECISION = list(data['PRECISION'])
RECALL = list(data['RECALL'])
TOTAL_PREDICTION_MADE = list(data['TOTAL_PREDICTION_MADE'])
VAL_ACC = list(data['VAL_ACC'])
VAL_LOSS = list(data['VAL_LOSS'])
VAL_PRECISION = list(data['VAL_PRECISION'])
VAL_RECALL = list(data['VAL_RECALL'])



@app.route('/')
def index():
    return render_template('chart.html', labels=time, values=values)
