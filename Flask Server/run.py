# -*- coding: utf-8 -*-

from flask import Flask, render_template, request
import os
import numpy as numpy

app = Flask(__name__)

##########################
# input codes
##########################

@app.route("/", methods=['GET', 'POST'])

def index():
	# default scene
	if request.method == 'GET':
		return render_template('index.html')

	# input data(click) = reload page
	#if request.method == 'POST':
		# result = request.form['result'] # parameter..
		# sentence = "__label__1"
		# result = classify(result)
		# return render_template('index.html', result=result)

if __name__ == '__main__':
	app.run(debug = True)