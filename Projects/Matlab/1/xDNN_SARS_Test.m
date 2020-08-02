%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

%                              Prediction Script 

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
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

%% clear all file from workspace and clear command window
clear all; 
close all;
clc;

%% Loading the model 

% load ("./Model/Imds/train/imdsTrain")
% Label =grp2idx(imdsTrain.Labels);
% load ("./Model/features/train/featuresTrain")
% 
% Input1.Features=featuresTrain;
% Input1.Labels=grp2idx(imdsTrain.Labels);
% Input1.Images=imdsTrain.Files;
% 
% tic
% Mode='Learning';
% [Output1]=xDNN(Input1,Mode);
% toc

load ('./Model/classifier/Output1.mat')
disp('Model Loaded ....');
disp('-------------------------------------------');

disp('Loading data');
test_path = ('./test_sample'); 
disp('Loaded data');

disp('Test data pre-processing');

imds_test  = imageDatastore(fullfile(test_path), ...
            'IncludeSubfolders',true,'FileExtensions','.png','LabelSource','foldernames');

labelcount2 = countEachLabel(imds_test);

disp('Pre-processing done');
disp('----------------------------------------------------');
disp('Loading VGG16 Model');
net = vgg16;
disp('Loaded VGG16 Model');

layer = 'fc7'; % 4096
inputSize = net.Layers(1).InputSize;
disp('data processing');

augimdsPredict = augmentedImageDatastore(inputSize(1:2),imds_test); % resize

featuresPredict = activations(net, augimdsPredict, layer, 'OutputAs', 'Rows', ...
                    'MiniBatchSize', 8);

disp('Classifying the image');
Label3 = grp2idx(imds_test.Labels);
Input3.xDNNParms=Output1.xDNNParms;
Input3.Images = imds_test.Files;
Input3.Features=featuresPredict;
Input3.Labels=Label3; 
Mode='Validation'; 
[Output3]=xDNN(Input3,Mode);

disp('Done');

classes = Output3.EstLabs;

for classint = 1:length(classes) 
    for i = 1:classint
        if classes(i) == 1
            class = ('COVID'); 
        elseif classes(classint) == 2
            class = ('Non-COVID');
        else
            class = ('Not defined');
        end  
    end
    prediction = class;
end

out = convertCharsToStrings(prediction);

predictImg = imageDatastore(test_path);
disp('Prediction:');
disp(out);
while hasdata(predictImg) 
    img = read(predictImg) ;             % read image from datastore
    figure, imshow(img); title(prediction);  % creates a new window for each image
end
