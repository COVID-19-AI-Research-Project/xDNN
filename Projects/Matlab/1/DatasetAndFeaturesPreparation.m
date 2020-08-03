%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

%                                      DatasetAndFeaturesPreparation File

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%
% Project Name:  Peter Moss COVID-19 AI Research Project
% Repository:    COVID-19 AI Classification
% Project title: COVID-19 Pneumonia Detection/Early Detection
% Author 1:      Aniruddh Sharma
% Author 2:      Nitin Mane
% Title:         For Preparing New Dataset and Features
% Description:   Prepare the IMDS and Feature MAT files for given Dataset
%
% License:       MIT License
% Last Modified: 2020-07-30
%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%


clc
clear all

%% Data input

dataset_path = ' ';      %Provide location of Dataset Folder

imds  = imageDatastore(fullfile(dataset_path), ...
    'IncludeSubfolders',true,'FileExtensions','.png','LabelSource','foldernames');
labelcount = countEachLabel(imds);
[imdsTrain, imdsValidation] = splitEachLabel(imds, 0.7, 'randomized');

layer = 'fc7';
net = vgg16;
inputSize = net.Layers(1).InputSize;

resizeImdsTrain = augmentedImageDatastore(inputSize(1:2), imdsTrain);
resizeImdsValidation = augmentedImageDatastore(inputSize(1:2),imdsValidation);


featuresTrain = activations(net, resizeImdsTrain, layer, 'OutputAs', 'Rows', ...
                'MiniBatchSize', 8);
featuresTest = activations(net, resizeImdsValidation, layer, 'OutputAs', 'Rows', ...
                'MiniBatchSize', 8);
