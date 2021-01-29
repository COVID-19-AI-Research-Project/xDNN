#!/usr/bin/env python3
# -*- coding:utf-8 -*-

# Importing libraries
import tensorflow as tf
import os
import numpy as np
import classifier as clf
import local_config as lc

from flask import Flask, request, redirect, url_for, render_template
from flask_bootstrap import Bootstrap
from werkzeug.utils import secure_filename

# Setting up environment
if not os.path.isdir(lc.OUTPUT_DIR):
    print('Creating static folder..')
    os.mkdir(lc.OUTPUT_DIR)

app = Flask(__name__)
Bootstrap(app)
app.config['UPLOAD_FOLDER'] = lc.OUTPUT_DIR

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # Check if the post request has the file part
        if 'file' not in request.files:
            print('No file part')
            return redirect(request.url)
        file = request.files['file']
        # Check if no file was submitted to the HTML form
        if file.filename == '':
            print('No selected file')
            return redirect(request.url)
        if file and clf.allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            output = clf.make_prediction(filename)
            path_to_image = url_for('static', filename = filename)
            result = {
                'output': output,
                'path_to_image': path_to_image,
                'size': lc.SIZE
            }
            return render_template('show.html', result=result)
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)
    