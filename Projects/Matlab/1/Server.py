############################################################################################
#
# Project:       Peter Moss COVID-19 AI Research Project
# Repository:    COVID-19 AI Classification
# Project:       COVID-19 Pneumonia Detection/Early Detection
#
# Author:        Aniruddh Sharma
# Title:         Predict CT Scan on Web Page
# Description:   Analyze the CT Scan images and predict whether they are COVID-19 or normal Scans by using Pretrained Model on a Web Page
# License:       MIT License
# Last Modified: 2020-06-09
#
############################################################################################
from flask import Flask, redirect, url_for, request, render_template
from werkzeug.utils import secure_filename
from gevent.pywsgi import WSGIServer
from PIL import Image
import jsonpickle
# coding=utf-8
import sys, os, glob, re, matlab.engine
import logging, json


#creating logger file
logger = logging.getLogger('Server.py')
logger.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
file_handler = logging.FileHandler('./Logs/allLogs.log')
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)

#Loads the program configuration
with open('config.json') as confs:
    confs = json.loads(confs.read())


categories = ["Normal Scan","COVID-19 Scan"]

def predict_image(file_path):
    eng = matlab.engine.start_matlab()
    logger.info("Matlab engine started, uploading Image in PredictImage function.")
    label = int(eng.PredictImage(file_path, nargout = 1))
    eng.quit()
    try:
        logger.info("The Uploaded CT Scan is {}".format(categories[label]))
        return categories[label]
    except:
        logger.info("Unable to predict Image")
    return 'Cannot detect image file at given location: {}'.format(filepath)

def make_empty_dir(dir_name):
    try:
        os.mkdir(dir_name)
        logger.info("{} Directory created in Project Root Folder".format(dir_name))
    except :
        logger.info("Unable to make {} Directory.".format(dir_name))
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
    logger.info("Image File {} processed and Converted in RGB channel PNG format.".format(img))

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
        logger.info('File upload request started.')
        f = request.files['file']
        dir_name = 'uploads'
        make_empty_dir(dir_name)
        # Save the file to ./uploads
        basepath = os.path.dirname(__file__)
        file_path = os.path.join(basepath, dir_name, secure_filename(f.filename))
        file_path = file_path.replace('\\','/')
        f.save(file_path)
        logger.info("Image file {} successfully saved in {} folder".format(f, dir_name))
        process_img(dir_name)
        # Make prediction
        preds = predict_image(dir_name)
        result = str(preds)              # Convert to string
        return result
    return None

if __name__ == '__main__':
    app.run(host = confs["server"]["ip"], port= confs["server"]["port"], debug=True)
