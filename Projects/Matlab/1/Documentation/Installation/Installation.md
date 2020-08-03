# Peter Moss COVID-19 AI Research Project

## COVID-19 xDNN

### COVID-19 xDNN Matlab Classifier

[![GeniSysAI Server](../../Media/Images/covid-19-ai-research-xdnn.png)](https://github.com/aniruddh-1/xDNN/tree/master/Projects/Matlab/1)

&nbsp;

# Table Of Contents

- [Introduction](#introduction)
- [Required Hardware](#required-hardware)
    - [Desktop/Laptop:](#desktoplaptop)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
        - [Steps for downloading the MATLAB Software :](#steps-for-downloading-the-matlab-software-)
- [Project - MATLAB xDNN](#project---matlab-xdnn)
  - [Contributors](#contributors)
- [Versioning](#versioning)
- [License](#license)
- [Bugs/Issues](#bugsissues)

&nbsp;

# Introduction
The following guide will take you through setting up and installing the  [ COVID-19 xDNN Matlab Classifier](https://github.com/COVID-19-AI-Research-Project/xDNN/Projects/Matlab " COVID-19 xDNN Matlab Classifier").


&nbsp;

# Required Hardware

### System Configurations:

1. Processor - i3, 4th GEN(min)
2. Graphic Card - Geforce 920MX(min)
3. RAM Card - 4 GB(min)
4. Disk Space - 24 GB(min)

&nbsp;

# Prerequisites

## MATLAB Software R2020a
It is mandatory to download the copy of [MATLAB](https://in.mathworks.com/) or the MATLAB installer onto your system after you fill out the required information to get it. Some users choose to receive a DVD in the mail instead of downloading the product online. No matter which technique you use, you eventually get a copy of MATLAB to install.

In most cases, you need to download the copy of MATLAB or the MATLAB installer onto your system after you fill out the required information to get it. Some users choose to receive a DVD in the mail instead of downloading the product online. No matter which technique you use, you eventually get a copy of MATLAB to install.

## Python3
Download the [Python 3](https://www.python.org/downloads/) as MATLAB 2020 will support releases upto Python 3.7 for calling MATLAB functions through MATLAB engine from python scripts.

After downloading the package, follow the below Environment Setup and add the PATH for the given Python Version.

![Python Environment Setup](../../Projects/Matlab/1/Media/Images/Installation/python_img.png)

## Clone the Repository

Clone the [COVID-19 xDNN]https://github.com/COVID-19-AI-Research-Project/xDNN " COVID-19 xDNN") repository from the [Peter Moss COVID-19 AI Research](https://github.com/COVID-19-AI-Research-Project "Peter Moss COVID-19 AI Research") Github Organization.

To clone the repository and install the COVID-19 Tensorflow DenseNet Classifier, make sure you have Git installed. Now navigate to the home directory on your device using terminal/commandline, and then use the following command.

```
  $ git clone https://github.com/COVID-19-AI-Research-Project/xDNN.git
```

Once you have used the command above you will see a directory called **xDNN** in your home directory.

```
ls
```

Using the ls command in your home directory should show you the following.

```
COVID-19-AI-Research-Project
```

Navigate to **COVID-19-AI-Research-Project/Projects/Matlab/1** directory, this is your project root directory for this tutorial.

### Developer Forks

Developers from the Github community that would like to contribute to the development of this project should first create a fork, and clone that repository. For detailed information please view the [CONTRIBUTING](../../../../CONTRIBUTING.md "CONTRIBUTING") guide. You should pull the latest code from the development branch.

```
  $ git clone -b "0.2.0" https://github.com/COVID-19-AI-Research-Project/xDNN.git
```

The **-b "0.2.0"** parameter ensures you get the code from the latest master branch. Before using the below command please check our latest master branch in the button at the top of the project README.


&nbsp;

# Installation

## Installing Matlab

#### Follow these steps to install the MATLAB 2020 in correct manner.
1. Open browser and Type MATLAB in search bar or click on the link.
MATLAB-Trial-R2020a
[![MATHWORKS](../../Projects/Matlab/1/Media/Images/Installation/matlab_01.jpg)]

2. After clicking on the download option the page will be diverted to the login.
[![login](../../Projects/Matlab/1/Media/Images/Installation/matlab_02.jpg)]

3. Type the email-id and password if not then signup from the same page. It will pop-up a verification message.
[![verification](../../Projects/Matlab/1/Media/Images/Installation/matlab_03.jpg)]

4. After sign in to the account. It will show this page.
[![license page](../../Projects/Matlab/1/Media/Images/Installation/matlab_04.jpg)]

5. In the trial section, it is notified with the trial license if using fist time.
[![trial page](../../Projects/Matlab/1/Media/Images/Installation/matlab_05.jpg)]

6. Click in the license section, a new window will open. Select the install and activate option.
[![license selection page](../../Projects/Matlab/1/Media/Images/Installation/matlab_06.jpg)]

7. Click Download installer button.
[![installation](../../Projects/Matlab/1/Media/Images/Installation/matlab_07.jpg)]

8. A new page will open and diverted to the downloading files. Select the files depending on the operating system.
[![File Download](../../Projects/Matlab/1/Media/Images/Installation/matlab_08.jpg)]

9. Installer File will be getting downloaded.
[![downloading](../../Projects/Matlab/1/Media/Images/Installation/matlab_09.jpg)]

10. After downloading file. It will show like the .exe file for windows.
[![downloading](../../Projects/Matlab/1/Media/Images/Installation/matlab_10.jpg)]

11. Click on the matlab_R2020a_win64.exe file. This will extract the installation file setup in the temporary file.
[![File Extract](../../Projects/Matlab/1/Media/Images/Installation/matlab_11.jpg)]

12. After extracting the application will ask for the running file. Accept it and you will see MATLAB Logo.
[![File Extract](../../Projects/Matlab/1/Media/Images/Installation/matlab_12.jpg)]

13. The application will ask for the email and password.
[![Matlab Installation window](../../Projects/Matlab/1/Media/Images/Installation/matlab_13.jpg)]

14. It will again ask for the verification code which is sent to the mobile phone.
[![Verification code](../../Projects/Matlab/1/Media/Images/Installation/matlab_14.jpg)]

15. Read all the license agreement and accept it.
[![License Agreement](../../Projects/Matlab/1/Media/Images/Installation/matlab_15.jpg)]

16. Select the license type.
[![License Selection](../../Projects/Matlab/1/Media/Images/Installation/matlab_16.jpg)]

17. Select the destination path or leave it as default path, click next
[![License Selection](../../Projects/Matlab/1/Media/Images/Installation/matlab_17.jpg)]

18. Select the packages which are needed to installed in custom or select all, click next
[![License Selection](../../Projects/Matlab/1/Media/Images/Installation/matlab_19.jpg)]

19. In the option, select the add shortcut to desktop and click next.
[![License Selection](../../Projects/Matlab/1/Media/Images/Installation/matlab_20.jpg)]

20. The MATLAB software will be getting installed and get confirmed.

21. Now select the MATLAB R2020a icon on the desktop and double click.
[![MATLAB Software](../../Projects/Matlab/1/Media/Images/Installation/matlab_21.jpg)]

22. The software will show this UI and need to wait for few minutes for inital setup and configuration in the backend program.
[![MATLAB Software GUI](../../Projects/Matlab/1/Media/Images/Installation/matlab_22.jpg)]

## Manually Installing Required Python Libraries
The following dependencies for Project will required to be installed as follows:

```
pip3 install sys
pip3 install os
pip3 install glob
pip3 install re
pip3 install pillow
pip3 install flask
pip3 install gevent
pip3 install numpy
pip3 install werkzeug
```

#### For installing the Matlab Engine API to run matlab functions from python scripts, choose one of the following step:

1. At a Windows operating system prompt —

```
cd "matlabroot\extern\engines\python"
python setup.py install
```

You might need administrator privileges to execute these commands.

2. At a macOS or Linux operating system prompt —

```
cd "matlabroot/extern/engines/python"
python setup.py install
```

You might need administrator privileges to execute these commands.

3. At the MATLAB command prompt —

```
cd (fullfile(matlabroot,'extern','engines','python'))
system('python setup.py install')
```

After a successfull installation of MATLAB Engine API, start Python, import the module, and start the MATLAB engine:

```
import matlab.engine
eng = matlab.engine.start_matlab()
```

## Configuration

You will find the configuration file in the project 2 root directory.
```
{   "data": {
        "allowed": [
            ".png", ".jpeg", ".jpg"
        ],
        "batch": 8,
        "channels": 3,
        "dim": 224,
        "rotations": 1,
        "test_size": 0.3,
        "train" : ["Model/Imds", "Model/Features"]
    },
    "model": {
        "labels": [
            0,
            1
        ],
        "weights": "Model/Pretrained/Output1.mat"
    },
    "modes": [
        "Server",
        "DatasetAndFeaturesPreparation",
        "PredictImage",
        "TrainModel",
    ],
    "server": {
        "ip": "127.0.0.1",
        "port": 5000
    }
}

```
&nbsp;

# Continue

Now continue with the [COVID-19 xDNN](../../README.md "COVID-19 xDNN") tutorial.


## Contributors

- [Aniruddh Sharma](https://www.leukemiaresearchassociation.ai/team/aniruddh-sharma "Aniruddh Sharma") - [Peter Moss Leukemia AI Research](https://www.leukemiaresearchassociation.ai "Peter Moss Leukemia AI Research") R&D Junior, Ahmedabad, Gujarat, India

- [Nitin Mane](https://www.leukemiaresearchassociation.ai/team/nitin-mane "Nitin Mane") - [Peter Moss Leukemia AI Research](https://www.leukemiaresearchassociation.ai "Peter Moss Leukemia AI Research") AI R&D, Aurangabad, India

&nbsp;

# Versioning

You use SemVer for versioning. For the versions available, see [Releases](../../releases "Releases").

&nbsp;

# License

This project is licensed under the **MIT License** - see the [LICENSE](../../../../../LICENSE "LICENSE") file for details.

&nbsp;

# Bugs/Issues

We use the [repo issues](../../../../../../../issues "repo issues") to track bugs and general requests related to using this project. See [CONTRIBUTING](../../../../../CONTRIBUTING.md "CONTRIBUTING") for more info on how to submit bugs, feature requests and proposals.
