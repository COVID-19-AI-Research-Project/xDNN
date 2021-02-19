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

import sys
import time
import logging
import logging.handlers as handlers
import json

from datetime import datetime


class Helpers():
	""" Helper Class

	Helper functions for the Raspberry Pi 4 COVID-19 xDNN Classifiers.
	"""

	def __init__(self, ltype, log=True):
		""" Initializes the Helpers Class. """

		self.confs = {}
		self.loadConfs()

		self.logger = logging.getLogger(ltype)
		self.logger.setLevel(logging.INFO)

		formatter = logging.Formatter(
			'%(asctime)s - %(name)s - %(levelname)s - %(message)s')

		allLogHandler = handlers.TimedRotatingFileHandler(
			'Logs/all.log', when='H', interval=1, backupCount=0)
		allLogHandler.setLevel(logging.INFO)
		allLogHandler.setFormatter(formatter)

		errorLogHandler = handlers.TimedRotatingFileHandler(
			'Logs/error.log', when='H', interval=1, backupCount=0)
		errorLogHandler.setLevel(logging.ERROR)
		errorLogHandler.setFormatter(formatter)

		warningLogHandler = handlers.TimedRotatingFileHandler(
			'Logs/warning.log', when='H', interval=1, backupCount=0)
		warningLogHandler.setLevel(logging.WARNING)
		warningLogHandler.setFormatter(formatter)

		consoleHandler = logging.StreamHandler(sys.stdout)
		consoleHandler.setFormatter(formatter)

		self.logger.addHandler(allLogHandler)
		self.logger.addHandler(errorLogHandler)
		self.logger.addHandler(warningLogHandler)
		self.logger.addHandler(consoleHandler)

		if log is True:
			self.logger.info("Class initialization complete.")

	def loadConfs(self):
		""" Load the program configuration. """

		with open('Model/config.json') as confs:
			self.confs = json.loads(confs.read())
