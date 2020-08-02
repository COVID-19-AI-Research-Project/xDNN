%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

%                                      xDNN SARS MAIN File 

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%
% Project Name:  Peter Moss COVID-19 AI Research Project
% Repository:    COVID-19 AI Classification
% Project title: COVID-19 Pneumonia Detection/Early Detection
% Author 1:      Aniruddh Sharma
% Author 2:      Nitin Mane
% Title:         Predict CT Scan
% Description:   Analyze the CT Scan images and predict whether they are COVID-19 or normal Scans by using Pretrained Model
% License:       MIT License
% Last Modified: 2020-07-30
%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%% Close all and clear 
clear all; 
close all;
clc;

%% load the data  

% Set data path 
Data_path = ('./Model/Data/'); 
disp('Loading the dataset')
%% Dataset store imds 
imds  = imageDatastore(fullfile(Data_path), ...
    'IncludeSubfolders',true,'FileExtensions','.png','LabelSource','foldernames');

disp('Creating the Image Datastore extensions')
%% Set the labels in index
labelcount = countEachLabel(imds);

disp('Count labels')
%% Split the data from the dataset
[imdsTrain, imdsTest] = splitEachLabel(imds, 0.8, 'randomized');

disp('Spliting the Dataset to train and test')
%% Load the vgg16 model 
net = vgg16;
disp('Loading VGG16 Model')
% set layer for extraction
layer = 'fc7';
% set the first layer input size
inputSize = net.Layers(1).InputSize;
disp('Change input layers and final layer for pre-processing')

%% Augumentation for the pre-processing data in the model 
augimdsTrain = augmentedImageDatastore(inputSize(1:2), imdsTrain);
augimdsTest = augmentedImageDatastore(inputSize(1:2),imdsTest);

disp('Augmentation process for the datastore')
%% Extract features from the model using augumentation method. 
featuresTrain = activations(net, augimdsTrain, layer, 'OutputAs', 'Rows', ...
                'MiniBatchSize', 8);
featuresTest = activations(net, augimdsTest, layer, 'OutputAs', 'Rows', ...
                'MiniBatchSize', 8);

disp('Processing features in train and test')
%% xDNN pre-processing 

Label =grp2idx(imdsTrain.Labels);

Input1.Features=featuresTrain;
Input1.Labels=grp2idx(imdsTrain.Labels);
Input1.Images=imdsTrain.Files;

tic
Mode='Learning';
[Output1]=xDNN(Input1,Mode);
toc

% %% Validation 
Label1 =grp2idx(imdsTest.Labels);

Input2.xDNNParms=Output1.xDNNParms;
Input2.Images=imdsTest.Files; 
Input2.Features=featuresTest;
Input2.Labels=Label1; 
Mode='Validation';
[Output2]=xDNN(Input2,Mode);

%% Displaying and plotting results
disp('Results: ')
Acset = Output2.ClasAcc;
Accuracy = Acset * 100 
loss = 100 - Accuracy; 
% 
piResult = [Accuracy, loss]; 
figure (1)
pie(piResult,{'Accuracy','loss'});
labels = {'Accuracy','loss'};
legend(labels,'Location','southoutside','Orientation','horizontal');

precision = Output2.ConfMat(1,1) / (Output2.ConfMat(1,1) + Output2.ConfMat(2,1))
recall = Output2.ConfMat(1,1) / (Output2.ConfMat(1,1) + Output2.ConfMat(1,2))
F1 = (2 * precision * recall) / (precision + recall)

% plotting graph 
MatSet = categorical({'Precision', 'recall', 'F1'});
MatSet = reordercats(MatSet,{'Precision', 'recall', 'F1'});
MatResult = [precision, recall, F1];
figure (2)
bar(MatSet,MatResult);


[X,Y,T,AUC] = perfcurve(Input2.Labels,Output2.EstLabs,2); 
AUC

% Plot the AUC model
figure(3)
plot(X,Y,'LineWidth',3)
xlabel('False positive rate') 
ylabel('True positive rate')
title('ROC for Classification by xDNN')


Confusion_Matrix = Output2.ConfMat

% Plotting Confusion matrix
conMat = Output2.ConfMat;
xvalues = {'COVID','Non-COVID'};
yvalues = {'COVID','Non-COVID',};
figure (4)
h = heatmap(xvalues,yvalues,conMat);