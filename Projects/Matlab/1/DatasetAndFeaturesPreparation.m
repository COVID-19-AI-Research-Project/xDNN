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
