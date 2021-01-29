############################################################################################
#
# Project:       Peter Moss COVID-19 AI Research Project
# Repository:    xDNN
# Project:       COVID-19 xDNN Python Classifier
#
# Author:        Adam Milton-Barker (AdamMiltonBarker.com)
# Contributors:
# Title:         Model Class
# Description:   Model functions for the COVID-19 xDNN Python Classifier.
# License:       MIT License
# Last Modified: 2020-05-19
#
############################################################################################

from Classes.Helpers import Helpers

class Model():
    """ Model helper class
    
    Model functions for the Tensorflow 2.0 AllDS2020 CNN.
    """

    def __init__(self):
        """ Initializes the class. """

        self.Helpers = Helpers("Model", False)