#########################################################################################################
#
# Organization:     Asociacion De Investigacion En Inteligencia Artificial Para La Leucemia Peter Moss
# Research Project: 
# Repository:       
# Project:          
#
# Author:           
#
# Title:            
# Description:      
# License:          MIT License
# Last Modified:    
#
#########################################################################################################

import sys

from Classes.Helpers import Helpers
from Classes.Model import Model
from Classes.Server import Server
import xdnn 

class ALLoneAPI():
	""" ALLoneAPI RPI4 CNN Core Class

	
	"""

	def __init__(self):
		""" Initializes the class. """

		self.Helpers = Helpers("Core")
		self.Core = Model()
		self.Helpers.logger.info("ALLoneAPI RPI4 CNN initialization complete.")

	def do_load_model(self):
		""" Loads the model """

		self.Core.load_model_and_weights()

	def do_classify(self):
		""" Loads model and classifies test data """

		self.do_load_model()
		self.Core.test_classifier()

	def do_server(self):
		""" Loads the API server """

		self.do_load_model()
		self.Server = Server(self.Core)
		self.Server.start()

	def do_http_classify(self):
		""" Loads model and classifies test data """

		self.Core.test_http_classifier()

ALLoneAPI = ALLoneAPI()

def main():

	if len(sys.argv) < 2:
		print("You must provide an argument")
		exit()
	elif sys.argv[1] not in ALLoneAPI.Helpers.confs["cnn"]["core"]:
		print("Mode not supported! Server, Train or Classify")
		exit()

	mode = sys.argv[1]

	if mode == "Classify":
		""" Runs the classifier locally."""
		ALLoneAPI.do_classify()

	elif mode == "Server":
		""" Runs the classifier in server mode."""
		ALLoneAPI.do_server()

	elif mode == "Client":
		""" Runs the classifier in client mode. """
		ALLoneAPI.do_http_classify()

if __name__ == "__main__":
	main()
