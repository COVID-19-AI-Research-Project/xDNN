############################################################################################
#
# Project:       Peter Moss COVID-19 AI Research Project
# Repository:    COVID-19 AI Classification
# Project:       COVID-19 Pneumonia Detection/Early Detection
#
# Author:        Nitin Mane
# Title:         Predict CT Scan on Web Page
# Description:   Analyze the CT Scan images and predict whether they are COVID-19 or normal Scans by using Pretrained Model on a Web Page
# License:       MIT License
# Last Modified: 2021-04-07
#
############################################################################################

from tensorflow import keras
from tensorflow.keras.applications.vgg16 import VGG16
from tensorflow.keras.preprocessing import image
from tensorflow.keras.applications.vgg16 import preprocess_input
from tensorflow.keras.models import Model
import numpy as np
import time
import os

import pandas as pd
import logging
logging.getLogger('tensorflow').disabled = True

from Classes.xDNN_class import *
from Classes.xDNN_class import xDNN
from numpy import genfromtxt
from sklearn.metrics import accuracy_score
from sklearn.metrics import precision_score
from sklearn.metrics import recall_score
from sklearn.metrics import f1_score
from sklearn.metrics import cohen_kappa_score
from sklearn.metrics import roc_auc_score
from sklearn.metrics import confusion_matrix
from sklearn.metrics import roc_curve, auc
import matplotlib.pyplot as plt


# Load the files, including features, images and labels.    

X_train_file_path = r'./Model/Features/data_df_X_train_lite.csv'
y_train_file_path = r'./Model/Features/data_df_y_train_lite.csv'

X_train = genfromtxt(X_train_file_path, delimiter=',')
y_train = pd.read_csv(y_train_file_path, delimiter=';',header=None)

print ("###################### Data Loaded ######################")
print("Data Shape:   ")
print("X train: ",X_train.shape)
print("Y train: ",y_train.shape)

pd_y_train_labels = y_train[1]
pd_y_train_images = y_train[0]

# Convert Pandas to Numpy
y_train_labels = pd_y_train_labels.to_numpy()
y_train_images = pd_y_train_images.to_numpy()


# Model Learning
Input1 = {}

Input1['Images'] = y_train_images
Input1['Features'] = X_train
Input1['Labels'] = y_train_labels

Mode1 = 'Learning'

start = time.time()
Output1 = xDNN(Input1,Mode1)

end = time.time()

print ("###################### Model Trained ####################")

print("Time: ",round(end - start,2), "seconds")

#sLoad VGG-16 model
model = VGG16(weights='imagenet', include_top= True )
layer_name = 'fc2'
intermediate_layer_model = keras.Model(inputs=model.input,outputs=model.get_layer(layer_name).output)

print ("###################### Results ##########################")

input_image = ('./Model/Sample/<enter the image name>')
img = image.load_img(input_image, target_size=(224, 224))

def ext_feature(img):
    x = image.img_to_array(img)
    x = np.expand_dims(x, axis=0)
    x = preprocess_input(x)
    features = intermediate_layer_model.predict(x)
    test = []
    test.append(features[0])
    np_feature = np.array(test)
    
    return np_feature

out_fe = ext_feature(img)
Input3 = {}
Input3['xDNNParms'] = Output1['xDNNParms']
Input3['Features'] = out_fe
Mode3 = 'classify'

startTest = time.time()
Output3 = xDNN(Input3,Mode3)

endTest = time.time()

out1 = Output3['Scores'][0][0]
out2 = Output3['Scores'][0][1]

print("Result Time: ", round(endTest - startTest,2), "seconds")

print('Input Image:', os.path.basename(input_image))

if out1 > out2:
    print('Result: COVID')
    print('Prediction',out1)
else:
    print('Result: Normal')
    print('Prediction',out2)