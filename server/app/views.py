from app import app
import json
from flask import render_template, jsonify, url_for, request, session, redirect
from pymongo import MongoClient
import pymongo
import time



@app.template_filter('ctime')
def timectime(s):
    return time.ctime(s)

@app.route('/build/<num>')
def index(num):
	num = int(num)
	client = MongoClient('3.94.109.234')
	db = client.ci
	buildList = list(db.builds.find().sort([('build_time', pymongo.DESCENDING)]))
	curbuild = buildList[num] 
	return render_template('index.html', plotData = curbuild['history'], hyperparameters=curbuild['HYPERPARAMETER'], \
	dataset_commit=curbuild.get('last_dataset_commit', 0), code_commit=curbuild.get('last_code_commit', 0))

@app.route('/')
def home():
	client = MongoClient('3.94.109.234')
	db = client.ci
	buildList = list(db.builds.find().sort([('build_time', pymongo.DESCENDING)]))
	return render_template('home.html', builds=buildList)