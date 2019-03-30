from app import app
import json
from flask import render_template, jsonify, url_for, request, session, redirect
from pymongo import MongoClient

client = MongoClient('3.94.109.234')

Data = list(client.ci.builds.find())
data = Data[-1]
List = list(data.keys())
for obs in data:
	if obs == "history":
		history = data['history']
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

_id = data['_id']
build_time = data['build_time']
ACC = data['ACC']
HYPERPARAMETER = data['HYPERPARAMETER']
LOSS = data['LOSS']
NO_OF_CORRECT_PREDICTIONS = data['NO_OF_CORRECT_PREDICTIONS']
NO_OF_WRONG_PREDICTIONS = data['NO_OF_WRONG_PREDICTIONS']
PRECISION = data['PRECISION']
RECALL = data['RECALL']
TOTAL_PREDICTION_MADE = data['TOTAL_PREDICTION_MADE']
VAL_ACC = data['VAL_ACC']
VAL_LOSS = data['VAL_LOSS']
VAL_PRECISION = data['VAL_PRECISION']
VAL_RECALL = data['VAL_RECALL']


time=[]
for i in range(len(loss)):
	time.append(int(i+1))

values = []
values.append(loss)
values.append(acc)
values.append(precision)
values.append(recall)
values.append(fmeasure)
values.append(binary_crossentropy)
values.append(mean_squared_error)
values.append(mean_absolute_percentage_error)
values.append(mean_squared_logarithmic_error)
values.append(f1)
values.append(val_acc)
values.append(val_precision)
values.append(val_recall)
values.append(val_fmeasure)
values.append(val_binary_crossentropy)
values.append(val_mean_squared_error)
values.append(val_mean_absolute_percentage_error)
values.append(val_mean_squared_logarithmic_error)
values.append(val_f1)

info = []
info.append(_id)
info.append(build_time)
info.append(ACC)
info.append(HYPERPARAMETER)
info.append(LOSS)
info.append(NO_OF_CORRECT_PREDICTIONS)
info.append(NO_OF_WRONG_PREDICTIONS)
info.append(PRECISION)
info.append(RECALL)
info.append(TOTAL_PREDICTION_MADE)
info.append(VAL_ACC)
info.append(VAL_LOSS)
info.append(VAL_PRECISION)
info.append(VAL_RECALL)

@app.route('/')
def index():
    return render_template('index.html', labels=time, values=values, info = info)
