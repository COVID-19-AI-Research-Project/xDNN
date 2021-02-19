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
import jsonpickle

from flask import Flask, request, Response

from Classes.Helpers import Helpers

class Server():
	""" Server helper class

	Server functions for the Raspberry Pi 4 COVID-19 xDNN Classifiers.
	"""

	def __init__(self, model, iotJumpWay):
		""" Initializes the class. """

		self.Helpers = Helpers("Server", False)

		self.model = model
		self.iot = iotJumpWay

		self.Helpers.logger.info("Class initialization complete.")

	def start(self):
		""" Starts the server. """

		app = Flask(__name__)
		@app.route('/Inference', methods=['POST'])
		def Inference():
			""" Responds to standard HTTP request. """

			message = ""
			classification = self.model.http_classify(request)

			if classification == 1:
				message = "COVID-19 detected!"
				diagnosis = "Positive"
			elif classification == 0:
				message = "COVID-19 not detected!"
				diagnosis = "Negative"

			# Send iotJumpWay notification
			self.iot.channelPub("Sensors", {
				"Type": "GeniSysAI",
				"Sensor": "ALL Classifier",
				"Value": diagnosis,
				"Message": message
			})

			resp = jsonpickle.encode({
				'Response': 'OK',
				'Message': message,
				'Diagnosis': diagnosis
			})

			return Response(response=resp, status=200, mimetype="application/json")

		app.run(host = self.Helpers.confs["cnn"]["system"]["server"],
				port = self.Helpers.confs["cnn"]["system"]["port"])
