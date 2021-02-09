# Peter Moss COVID-19 AI Research Project

## COVID-19 xDNN

### COVID-19 xDNN Matlab Classifier

[![xDNN](../../../Media/Images/covid-19-ai-research-xdnn.png)]()

[![VERSION](https://img.shields.io/badge/VERSION-0.0.0-blue.svg)](https://github.com/COVID-19-AI-Research-Project/xDNN/tree/0.0.0) [![DEV BRANCH](https://img.shields.io/badge/DEV%20BRANCH-0.1.0-blue.svg)](https://github.com/COVID-19-AI-Research-Project/xDNN/tree/0.1.0) [![Issues Welcome!](https://img.shields.io/badge/Contributions-Welcome-lightgrey.svg)](CONTRIBUTING.md) [![Issues](https://img.shields.io/badge/Issues-Welcome-lightgrey.svg)](issues) [![LICENSE](https://img.shields.io/badge/LICENSE-MIT-blue.svg)](LICENSE)

&nbsp;

# Table Of Contents

- [Introduction](#introduction)
- [DISCLAIMER](#disclaimer)
- [Installation](#installation)
- [Train](#train)
  - [Start Training](#start-training)
  - [Training Results](#training-results)
  - [Metrics Overview](#metrics-overview)
  - [Figures Of Merit](#figures-of-merit)
  - [Training on your own Dataset](#training-on-your-own-dataset)
- [Real World Testing](#real-world-testing)
- [Citation](#citation)
- [Contributing](#contributing)
  - [Contributors](#contributors)
- [Versioning](#versioning)
- [License](#license)
- [Bugs/Issues](#bugsissues)


#  Introduction

The contamination by SARS-CoV-2 which causes the COVID-19 disease has generally spread everywhere throughout the world since the start of 2020. On January 30, 2020, the World Health Organization (WHO) proclaimed a worldwide health crisis. Analysts of various orders work alongside general health authorities to comprehend the SARS-CoV-2 pathogenesis and together with the policymakers direly create techniques to control the spread of this new disease.

Recent findings have observed imaging patterns on computed tomography (CT) for patients infected by SARS-CoV-2.

In this research, we have used a public available [SARS-COV-2 Ct-Scan Dataset](https://www.kaggle.com/plameneduardo/sarscov2-ctscan-dataset),
containing 1252 CT scans that are positive for SARS-CoV-2 infection (COVID-19) and 1230 CT scans for patients non-infected by SARS-CoV-2.
This dataset of CT scans for SARS-CoV-2 (COVID-19) identification is created by our collaborators, Plamenlancaster:
[Professor Plamen Angelov](https://www.lancaster.ac.uk/lira/people/#d.en.397371) from [Lancaster University](https://www.lancaster.ac.uk/)/
Centre Director @ [Lira](https://www.lancaster.ac.uk/lira/), & his researcher,
[Eduardo Soares PhD](https://www.lancaster.ac.uk/sci-tech/about-us/people/eduardo-almeida-soares).

These data have been collected from real patients in hospitals from Sao Paulo, Brazil.

The aim of this dataset is to encourage the research and development of artificial intelligent methods which are able to identify if a person is is infected by SARS-CoV-2 through the analysis of his/her CT scans.
As baseline result for this dataset we used an eXplainable Deep Learning approach (xDNN) which we could achieve an F1 score of **0.9672** which is very promising.

&nbsp;

# DISCLAIMER

This project should be used for research purposes only. The purpose of the project is to show the potential of Artificial Intelligence for medical support
systems such as diagnosis systems. Although the program is fairly accurate and shows good results both on paper and in real world testing, it is not meant
to be an alternative to professional medical diagnosis. I am a self taught developer with some experience in using Artificial Intelligence for detecting
certain types of cancer and COVID-19. I am not a doctor, medical or cancer/COVID-19 expert. Please use this system responsibly.

&nbsp;

# Installation

Please follow the [Installation Guide](../1/Documentation/Installation/Installation.md) to install COVID-19 xDNN Python Classifier.

# Train

Assuming you have completed the installation guide, you can now begin training.

## Start Training

Open Python IDE or Anaconda IDE (Command prompt or spyder) and navigate to the project root directory and execute the following command:

```
TrainModel
```

## Training Results

The trained model is processed in the workspace of the python IDE, this contains a Model file which is trained on 1737 images containing xDNN Parameters.
 When the training finishes the model will show the results related to metrics and figures of merit.

```
Elapsed time is 68.74 seconds.
Results:

Accuracy =

   0.967807


precision =

    0.967807


recall =

    0.967807


F1 =

    0.967807


AUC =

    0.935607


Confusion_Matrix =

   247     2
    14   234
```

![Accuracy](../1/Media/Images/Accuracy_chart.png)

_Fig 1. Accuracy_

![Precision](../1/Media/Images/recall.png)

_Fig 2. Precision, Recall and F1_

![Confusion Matrix](../1/Media/Images/confusion_matrix.png)

_Fig 3. Confusion Matrix_

### Metrics Overview

| Accuracy  | Recall     | Precision  | AUC/ROC   |
| --------- | ---------- | ---------- | --------- |
| 0.967807  |  0.967807    | 0.967807     | 0.935607    |

### Figures Of Merit

| Figures of merit     | Amount/Value      | Percentage  |
| -------------------- | ------------------| ------------|
| True Positives       | 247               | 67.65892% |
| False Positives      | 2                 | 0.398699%  |
| True Negatives       | 234               | 63.97529% |
| False Negatives      | 14                | 1.179623%  |
| Misclassification    | 12                | 1.345706%  |
| Sensitivity / Recall | 0.9894            | 98%         |

## Training on your own Dataset

The Python file [Feature_Extraction_VGG16.py](../1/Feature_Extraction_VGG16.py) can be used to make the dataloader and Features extracted in csv files for training
on your own dataset. Before running the above script, paste the dataset folder with containing subfolders in the project root directory. After running
the above script save the generated Train and Test files in [**data**](../1/Model/data) and features files of data_df_X_train_lite, data_df_y_train_lite, data_df_X_test_lite, data_df_y_test_lite in
[**Features**](../1/Model/Features) Folder.

&nbsp;

# Real World Testing

For testing the model and getting the results on random CT Scan Images, we will upload an Image on a webpage for the given default IP Address and
Port in [config.json](../1/config.json#L2), then it will provide the result for the given Image.The webpage interface to upload and predict images is
one using Flask API and we will use python script [Server.py](../1/Server.py), which will call Flask API to interact with the webpage and
call the [xDNN.py](../1/src/xDNN.py) classify function through which uses the pretrained model to classify the uploaded Image.

To test an Image, navigate to the project root(../xDNN/Projects/Python/1/) and execute the following command in command prompt:

```
python Server.py
```

The Script will start running and initiate both MATLAB Engine API and Flask API.

```
 * Serving Flask app "app" (lazy loading)
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: on
 * Restarting with stat
C:\Users\mniti\anaconda3\envs\py365\lib\site-packages\numpy\_distributor_init.py:32: UserWarning: loaded more than 1 DLL from .libs:
C:\Users\mniti\anaconda3\envs\py365\lib\site-packages\numpy\.libs\libopenblas.NOIJJG62EMASZI6NYURL6JBKM4EVBGM7.gfortran-win_amd64.dll
C:\Users\mniti\anaconda3\envs\py365\lib\site-packages\numpy\.libs\libopenblas.TXA6YQSD3GCQQC22GEQ54J2UDCXDXHWN.gfortran-win_amd64.dll
  stacklevel=1)
 * Debugger is active!
 * Debugger PIN: 131-166-024
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
```

Now go to your default browser and search for given HTTP address. You will see a web page as shown below:

![WebPage1](../1/Media/Project_Images/Server_Start.png)

Go the browser and on the given HTTP address assigned you will be prompt to a webpage. 

![WebPage2](../1/Media/Project_Images/Webpage_image.png)

Now Upload any JPG, JPEG or PNG CT Scan image file by clicking **Upload Image**. Keep in Mind that the Image file should have at atleast size of
 (224,224) image pixels. After Uploading Image, click on **Show Results**:

 ![WebPage2](../1/Media/Project_Images/webpage_input.png)

The Web Page will provide a predict button to classify the image from the server. 

![WebPage3](../1/Media/Project_Images/webpage_predict.png)

After Sometime it will give results for the uploaded Image as shown:

![WebPage4](../1/Media/Project_Images/webpage_covid.png)

&nbsp;

# Citation

```
Angelov, Plamen, and Eduardo Almeida Soares. "EXPLAINABLE-BY-DESIGN APPROACH FOR COVID-19 CLASSIFICATION VIA CT-SCAN." medRxiv (2020).
Soares, Eduardo, Angelov, Plamen, Biaso, Sarah, Higa Froes, Michele, and Kanda Abe, Daniel. "SARS-CoV-2 CT-scan dataset: A large dataset of real
patients CT scans for SARS-CoV-2 identification." medRxiv (2020). doi: https://doi.org/10.1101/2020.04.24.20078584.

Link:
https://www.medrxiv.org/content/10.1101/2020.04.24.20078584v2
```

&nbsp;

# Contributing

The Peter Moss COVID-19 AI Research Project encourages and welcomes code contributions, bug fixes and enhancements from the Github.

Please read the [CONTRIBUTING](../../../CONTRIBUTING.md "CONTRIBUTING") document for a full guide to forking our repositories and submitting your pull
requests. You will also find information about our code of conduct on this page.

## Contributors

- [Nitin Mane](https://www.leukemiaresearchassociation.ai/team/nitin-mane "Nitin Mane") - [Peter Moss Leukemia AI Research](https://www.leukemiaresearchassociation.ai "Peter Moss Leukemia AI Research")
AI R&D, Aurangabad, India.

&nbsp;

# Versioning

We use SemVer for versioning. For the versions available, see [Releases](../../../../../releases "Releases").

&nbsp;

# License

This project is licensed under the **MIT License** - see the [LICENSE](../../../LICENSE "LICENSE") file for details.

&nbsp;

# Bugs/Issues

We use the [repo issues](../../../../../issues "repo issues") to track bugs and general requests related to using this project. See
[CONTRIBUTING](../../../CONTRIBUTING.md "CONTRIBUTING") for more info on how to submit bugs, feature requests and proposals.
