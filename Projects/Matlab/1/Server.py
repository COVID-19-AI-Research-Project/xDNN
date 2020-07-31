############################################################################################
#
# Project:       Peter Moss COVID-19 AI Research Project
# Repository:    COVID-19 AI Classification
# Project:       COVID-19 Pneumonia Detection/Early Detection
#
# Author:        Aniruddh Sharma
# Title:         Predict CT Scan
# Description:   Analyze the CT Scan images and predict whether they are COVID-19 or normal Scans by using Pretrained Model
# License:       MIT License
# Last Modified: 2020-06-09
#
############################################################################################
from __future__ import division, print_function
from flask import Flask, redirect, url_for, request, render_template
from werkzeug.utils import secure_filename
from gevent.pywsgi import WSGIServer
from PIL import Image

# coding=utf-8
import sys, os, glob, re, matlab.engine
import numpy as np
categories = ["COVID-19 Scan","Normal Scan"]

def predict_image(file_path):
    eng = matlab.engine.start_matlab()
    label = int(eng.PredictImage(file_path, nargout = 1))
    eng.quit()
    if label == 1:
        return categories[0]
    elif label == 0:
        return categories[1]
    return 'Cannot detect image file at given location: {}'.format(filepath)

def make_empty_dir(dir_name):
    try:
        os.mkdir(dir_name)
    except :
        pass

    for filename in os.listdir(dir_name):
            file_path = os.path.join(dir_name, filename)
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)

def process_img(dir_name):
    for file in os.listdir(dir_name):
        img_path = os.path.join(dir_name, file)
        img_name, img_ext = os.path.splitext(file)
        if not img_ext == '.png':
            img = Image.open(img_path).convert("RGB")
            new_img = img.save('{}{}{}{}'.format(dir_name, '/', img_name, '.png'), 'png')
            os.remove(img_path)

app = Flask(__name__)

     #provides the path of your trained CNN model
@app.route('/', methods=['GET'])
def index():
    # Main page
    return render_template('index.html')

@app.route('/predict', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        # Get the file from post request
        f = request.files['file']
        dir_name = 'uploads'
        make_empty_dir(dir_name)
        # Save the file to ./uploads
        basepath = os.path.dirname(__file__)
        file_path = os.path.join(basepath, dir_name, secure_filename(f.filename))
        file_path = file_path.replace('\\','/')
        f.save(file_path)
        process_img(dir_name)
        # Make prediction
        preds = predict_image(dir_name)
        result = str(preds)              # Convert to string
        return result
    return None

if __name__ == '__main__':
    app.run(debug=True)
