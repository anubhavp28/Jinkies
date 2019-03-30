from app import app
import json
from flask import render_template, jsonify, url_for, request, session, redirect
# values is a list of lists
time = ["10","20","30","40","50","60","70","80"]
values = [10,9,8,7,6,4,7,8]

@app.route('/')
def index():
    return render_template('chart.html', labels=time, values=values)
