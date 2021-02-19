#########################################################################################################
#
# Organization:     Asociacion De Investigacion En Inteligencia Artificial Para La Leucemia Peter Moss
# Research Project: Peter Moss COVID-19 AI Research Project
# Repository:       COVID-19 xDNN Classifiers
# Project:          OpenVINO Raspberry Pi 4 COVID-19 xDNN Classifiers
#
# Author:           Nitin Mane 
# Contributors:
# Title:            Model Class
# Description:      Model functions for the Raspberry Pi 4 COVID-19 xDNN Classifiers.
# License:          MIT License
# Last Modified:    2021-02-19
#
#########################################################################################################

import cv2
import json
import os
import random
import requests
import time

os.environ["CUDA_VISIBLE_DEVICES"]="-1"

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras.applications.vgg16 import VGG16
from tensorflow.keras.preprocessing import image
from tensorflow.keras.applications.vgg16 import preprocess_input
from tensorflow.keras.models import Model
from xDNN_class import *
from xDNN_class import xDNN
from numpy import genfromtxt

from numpy.random import seed

from Classes.Helpers import Helpers

class Model():
	""" Model Class

	Model functions for the Raspberry Pi 4 COVID-19 xDNN Classifiers.
	"""

	def __init__(self):
		""" Initializes the class. """

		self.Helpers = Helpers("Model", False)

		os.environ["KMP_BLOCKTIME"] = "1"
		os.environ["KMP_SETTINGS"] = "1"
		os.environ["KMP_AFFINITY"] = "granularity=fine,verbose,compact,1,0"
		os.environ["OMP_NUM_THREADS"] = str(self.Helpers.confs["cnn"]["system"]["cores"])
		tf.config.threading.set_inter_op_parallelism_threads(1)
		tf.config.threading.set_intra_op_parallelism_threads(
			self.Helpers.confs["cnn"]["system"]["cores"])

		self.testing_dir = self.Helpers.confs["cnn"]["data"]["test"]
		self.valid = self.Helpers.confs["cnn"]["data"]["valid_types"]
		self.seed = self.Helpers.confs["cnn"]["data"]["seed"]

		self.colors = plt.rcParams['axes.prop_cycle'].by_key()['color']

		self.weights_file = self.Helpers.confs["cnn"]["model"]["weights"]
		self.model_json = self.Helpers.confs["cnn"]["model"]["model"]

		random.seed(self.seed)
		seed(self.seed)
		tf.random.set_seed(self.seed)

		self.Helpers.logger.info("Class initialization complete.")

	def load_model_and_weights(self):
		""" Loads the model and weights. """

		#with open(self.model_json) as file:
		#	m_json = file.read()

		#self.tf_model = tf.keras.models.model_from_json(m_json)
      self.tf_model = VGG16(weights='imagenet', include_top= True )
		#self.tf_model.load_weights(self.weights_file)

		self.Helpers.logger.info("Model loaded ")
      self.tf_model = VGG16(weights='imagenet', include_top= True )
      self.layer_name = 'fc2'
      self.tf_intermediate_layer_model = keras.Model(inputs=tf_model.input,outputs=tf_model.get_layer(layer_name).output)
      
      self.tf_intermediate_layer_model.summary()

		#self.tf_model.summary()

	 def load_xdnn_classifier(self):
        # Load the files, including features, images and labels.    

        X_train_file_path = r'../features/data_df_X_train_lite.csv'
        y_train_file_path = r'../features/data_df_y_train_lite.csv'

        X_train = genfromtxt(X_train_file_path, delimiter=',')
        y_train = pd.read_csv(y_train_file_path, delimiter=';',header=None)

        pd_y_train_labels = y_train[1]
        pd_y_train_images = y_train[0]

        # Convert Pandas to Numpy
        y_train_labels = pd_y_train_labels.to_numpy()
        y_train_images = pd_y_train_images.to_numpy()

        # Model Learning
        self.Input1 = {}

        self.Input1['Images'] = y_train_images
        self.Input1['Features'] = X_train
        self.Input1['Labels'] = y_train_labels

        self.Mode1 = 'Learning'

        self.Output1 = xDNN(self.Input1,self.Mode1)
        
        self.Helpers.logger.info("Loaded xDNN Model.")
        
    def test_classifier(self):
		""" Tests the trained model. """

		files = 0
		tp = 0
		fp = 0
		tn = 0
		fn = 0
		totaltime = 0

		for testFile in os.listdir(self.testing_dir):
			if os.path.splitext(testFile)[1] in self.valid:

				files += 1
				fileName = self.testing_dir + "/" + testFile

				start = time.time()
			   #img = cv2.imread(fileName).astype(np.float32)
            img = image.load_img(fileName)
				self.Helpers.logger.info("Loaded test image " + fileName)

				img = tf.image.resize(img, (self.Helpers.confs["cnn"]["data"]["dim"],
									   self.Helpers.confs["cnn"]["data"]["dim"]))
				img = self.reshape(img)
            img = self.image.img_to_array(img)
            img = self.np.expand_dims(img, axis=0)
            img = self.preprocess_input(img)
            features = self.intermediate_layer_model.predict(img)
            
            test = []
            test.append(features[0])
            np_feature = np.array(test)
            
            Input3 = {}
            Input3['xDNNParms'] = self.Output1['xDNNParms']
            Input3['Features'] = np_feature
            Mode3 = 'classify'
            
            Output3 = xDNN(Input3,Mode3)
            out1 = Output3['Scores'][0][0]
            out2 = Output3['Scores'][0][1]
            #prediction = self.get_predictions(img)
				end = time.time()
				benchmark = end - start
				totaltime += benchmark

				msg = ""
				if out1 > out2 and "_1." in testFile:
					tp += 1
					msg = "COVID-19 correctly detected (True Positive) in " + str(benchmark) + " seconds."
				elif out1 == out2 and "_0." in testFile:
					fp += 1
					msg = "COVID-19 incorrectly detected (False Positive) in " + str(benchmark) + " seconds."
				elif out2 > out1  0 and "_0." in testFile:
					tn += 1
					msg = "COVID-19 correctly not detected (True Negative) in " + str(benchmark) + " seconds."
				elif out2 == out1 and "_1." in testFile:
					fn += 1
					msg = "COVID-19 incorrectly not detected (False Negative) in " + str(benchmark) + " seconds."
				self.Helpers.logger.info(msg)

		self.Helpers.logger.info("Images Classifier: " + str(files))
		self.Helpers.logger.info("True Positives: " + str(tp))
		self.Helpers.logger.info("False Positives: " + str(fp))
		self.Helpers.logger.info("True Negatives: " + str(tn))
		self.Helpers.logger.info("False Negatives: " + str(fn))
		self.Helpers.logger.info("Total Time Taken: " + str(totaltime))

	def send_request(self, img_path):
		""" Sends image to the inference API endpoint. """

		self.Helpers.logger.info("Sending request for: " + img_path)

		_, img_encoded = cv2.imencode('.png', cv2.imread(img_path))
		response = requests.post(
			self.addr, data=img_encoded.tostring(), headers=self.headers)
		response = json.loads(response.text)

		return response

	def test_http_classifier(self):
		""" Tests the trained model via HTTP. """

		msg = ""

		files = 0
		tp = 0
		fp = 0
		tn = 0
		fn = 0

		self.addr = "http://" + self.Helpers.confs["cnn"]["system"]["server"] + \
			':'+str(self.Helpers.confs["cnn"]["system"]["port"]) + '/Inference'
		self.headers = {'content-type': 'image/jpeg'}

		for data in os.listdir(self.testing_dir):
			if os.path.splitext(data)[1] in self.valid:

				response = self.send_request(self.testing_dir + "/" + data)

				msg = ""
				if response["Diagnosis"] == "Positive" and "_1." in data:
					tp += 1
					msg = "COVID-19 correctly detected (True Positive)"
				elif response["Diagnosis"] == "Positive" and "_0." in data:
					fp += 1
					msg = "COVID-19 incorrectly detected (False Positive)"
				elif response["Diagnosis"] == "Negative" and "_0." in data:
					tn += 1
					msg = "COVID-19 correctly not detected (True Negative)"
				elif response["Diagnosis"] == "Negative" and "_1." in data:
					fn += 1
					msg = "COVID-19 incorrectly not detected (False Negative)"

				files += 1

				self.Helpers.logger.info(msg)
				time.sleep(7)

		self.Helpers.logger.info("Images Classifier: " + str(files))
		self.Helpers.logger.info("True Positives: " + str(tp))
		self.Helpers.logger.info("False Positives: " + str(fp))
		self.Helpers.logger.info("True Negatives: " + str(tn))
		self.Helpers.logger.info("False Negatives: " + str(fn))

	def http_classify(self, req):
		""" Classifies an image sent via HTTP. """

		if len(req.files) != 0:
			img = np.fromstring(req.files['file'].read(), np.uint8)
		else:
			img = np.fromstring(req.data, np.uint8)

		img = cv2.imdecode(img, cv2.IMREAD_UNCHANGED)
		img = cv2.resize(img, (self.Helpers.confs["cnn"]["data"]["dim"],
							   self.Helpers.confs["cnn"]["data"]["dim"]))
		img = self.reshape(img)

		return self.get_predictions(img)

	def get_predictions(self, img):
		""" Gets a prediction for an image. """

		predictions = self.tf_model.predict_proba(img)
		prediction = np.argmax(predictions, axis=-1)

		return prediction

	def reshape(self, img):
		""" Reshapes an image. """

		dx, dy, dz = img.shape
		input_data = img.reshape((-1, dx, dy, dz))

		return input_data
