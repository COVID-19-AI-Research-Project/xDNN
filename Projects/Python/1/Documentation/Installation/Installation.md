# Peter Moss COVID-19 AI Research Project
## COVID-19 xDNN Python Classifier
[![GeniSysAI Server](../../../Media/Images/covid-19-ai-research-xdnn.png)](https://github.com/COVID-19-AI-Research-Project/xDNN)

&nbsp;

# Table Of Contents

- [Introduction](#introduction)
- [Required Hardware](#required-hardware)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Contributing](#contributing)
    - [Contributors](#contributors)
- [Versioning](#versioning)
- [License](#license)
- [Bugs/Issues](#bugs-issues)

&nbsp;

# Introduction
The following guide will take you through setting up and installing the  [ COVID-19 xDNN Python Classifier](https://github.com/COVID-19-AI-Research-Project/xDNN/Projects/Python " COVID-19 xDNN Python Classifier").

The xDNN Classifier is a process of predicting class or category from observed features or given data file in less time compared to the ordinary model. This is a lightweight model
and easy to consume dataspace for the training and testing features and provide necessary operation. there are many variants in the model which provide an accurate result with consuming huge
data from the server or the machine. this method provides an edge computing device freedom of evaluating the xDNN is utilizing models. Models are genuine preparing information tests
 (pictures), which are neighbourhood pinnacles of the observational information conveyance called regularity just as of the information thickness. This generative model is 
 distinguished in a shut structure and likens to the pdf yet is gotten consequently and altogether from the preparation information with no client or issue explicit edges, 
 boundaries or intercession. The proposed xDNN offers another profound learning design that consolidates thinking and learning in cooperative energy. 
 It is non-iterative and non-parametric, which clarifies its productivity regarding time and computational assets.

&nbsp;

# Required Hardware

Basic Computer Configuration:

1. Processor    - Intel i3 or above 
2. Ram          - 4 GB and above
3. Harddisk     - 10 GB space
4. Graphics Card - NVIDIA GTX1050

&nbsp;

# Prerequisites 

The required operating system can be Windows, Linux or MacOS. 

The software required are as follows:
1. [Anaconda IDE](https://www.anaconda.com/products/individual)
2. [Tensorflow Library](https://www.tensorflow.org/install/)
3. [PyTorch Libary](https://pytorch.org/) (Optional)
4. [Flask](https://flask.palletsprojects.com/en/1.1.x/)
 

&nbsp;

# Installation 

First install the Anaconda IDE and navigate to the command prompt. 
Create a new environment for Python 3.6 as by default the anaconda has python 3.7 installed. 
```
conda create -n myenv python=3.6
```

Go to the root directory of this project file and install the dependencies using the following command in the prompt. 
```
pip -r requirements.txt
```
It will ask rights for installing the libaries. Just type Y and enter when asked. This will take some time to install the dependencies as it may consume more data depending on the file. 

After completing the process. Restart the computer and open Anaconda Navigator and click on the spyder IDE. 


&nbsp;

# Data Pre-processing 

In this techniques, we need to process the data for training and testing model. The data should be downloaded from the given [link](http://www.kaggle.com/plameneduardo/sarscov2-ctscan-dataset) 
Extract the file and paste it in the (./Model/Data/) folder. 

run `Feature_Extraction_VGG16.py`(Feature_Extraction_VGG16.py) or `Feature_Extraction_VGG16_PyTorch.py`(Feature_Extraction_VGG16_PyTorch.py) file in spyder 

This will load the file and convert into the train and test feature file with the respect to the label and feature data in the csv format. This will be saved at (./Model/Features/) folder. 

We will be using [VGG16 Model](https://github.com/keras-team/keras-applications/blob/master/keras_applications/vgg16.py) for extracting features and data points. 

```
Model: "model"
_________________________________________________________________
Layer (type)                 Output Shape              Param #
=================================================================
input_1 (InputLayer)         [(None, 224, 224, 3)]     0
_________________________________________________________________
block1_conv1 (Conv2D)        (None, 224, 224, 64)      1792
_________________________________________________________________
block1_conv2 (Conv2D)        (None, 224, 224, 64)      36928
_________________________________________________________________
block1_pool (MaxPooling2D)   (None, 112, 112, 64)      0
_________________________________________________________________
block2_conv1 (Conv2D)        (None, 112, 112, 128)     73856
_________________________________________________________________
block2_conv2 (Conv2D)        (None, 112, 112, 128)     147584
_________________________________________________________________
block2_pool (MaxPooling2D)   (None, 56, 56, 128)       0
_________________________________________________________________
block3_conv1 (Conv2D)        (None, 56, 56, 256)       295168
_________________________________________________________________
block3_conv2 (Conv2D)        (None, 56, 56, 256)       590080
_________________________________________________________________
block3_conv3 (Conv2D)        (None, 56, 56, 256)       590080
_________________________________________________________________
block3_pool (MaxPooling2D)   (None, 28, 28, 256)       0
_________________________________________________________________
block4_conv1 (Conv2D)        (None, 28, 28, 512)       1180160
_________________________________________________________________
block4_conv2 (Conv2D)        (None, 28, 28, 512)       2359808
_________________________________________________________________
block4_conv3 (Conv2D)        (None, 28, 28, 512)       2359808
_________________________________________________________________
block4_pool (MaxPooling2D)   (None, 14, 14, 512)       0
_________________________________________________________________
block5_conv1 (Conv2D)        (None, 14, 14, 512)       2359808
_________________________________________________________________
block5_conv2 (Conv2D)        (None, 14, 14, 512)       2359808
_________________________________________________________________
block5_conv3 (Conv2D)        (None, 14, 14, 512)       2359808
_________________________________________________________________
block5_pool (MaxPooling2D)   (None, 7, 7, 512)         0
_________________________________________________________________
flatten (Flatten)            (None, 25088)             0
_________________________________________________________________
fc1 (Dense)                  (None, 4096)              102764544
_________________________________________________________________
fc2 (Dense)                  (None, 4096)              16781312
=================================================================
Total params: 134,260,544
Trainable params: 134,260,544
Non-trainable params: 0
_________________________________________________________________
```

The extracted features will be shown like this 

```
[[0.         0.         0.         ... 0.         0.         0.97085285]
 [2.2869196  0.         0.64155865 ... 0.         0.         1.4732528 ]
 [0.         0.         0.         ... 0.         0.         0.        ]
 ...
 [0.         0.         0.         ... 0.         0.         0.91862583]
 [0.         0.         0.         ... 0.         0.         0.7122305 ]
 [0.         0.         0.07393801 ... 0.         0.         0.75918955]]
['Covid (1).png;0' 'Covid (10).png;0' 'Covid (100).png;0' ...
 'Non-Covid (997).png;1' 'Non-Covid (998).png;1' 'Non-Covid (999).png;1']
```

# Training Model 

Run 'main.py' file from the main roote folder 

The extracted features are further process in the xDNN model for the training purpose. 
```
###################### Data Loaded ######################
Data Shape:
X train:  (1984, 4096)
Y train:  (1984, 2)
X test:  (497, 4096)
Y test:  (497, 2)
```

The model takes less time compared to the ordinary model training procedure. 

```
###################### Model Trained ####################
Time:  52.63 seconds
```

Further the results are shown on the Readme file. 

# Custom Classifier 

You can run `classifier.py` file for classifying the image from the CT Scan data. 
It will provide COVID or normal results with the prediction accurate score. 

# Contributing

Peter Moss COVID-19 AI Research Project encourages and welcomes code contributions, bug fixes and enhancements from the Github.

Please read the [CONTRIBUTING](../../CONTRIBUTING.md "CONTRIBUTING") document for a full guide to forking your repositories and submitting your pull requests. You will also find information about your code of conduct on this page.

## Contributors

- [Nitin Mane](https://www.leukemiaresearchassociation.ai/team/nitin-mane "Nitin Mane") - [Peter Moss Leukemia AI Research](https://www.leukemiaresearchassociation.ai "Peter Moss Leukemia AI Research") AI R&D, Aurangabad, India

&nbsp;

# Versioning

You use SemVer for versioning. For the versions available, see [Releases](../../releases "Releases").

&nbsp;

# License

This project is licensed under the **MIT License** - see the [LICENSE](../../LICENSE "LICENSE") file for details.

&nbsp;

# Bugs/Issues

You use the [repo issues](../../issues "repo issues") to track bugs and general requests related to using this project. See [CONTRIBUTING](../../CONTRIBUTING.md "CONTRIBUTING") for more info on how to submit bugs, feature requests and proposals.