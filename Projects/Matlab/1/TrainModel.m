%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

%                                      TrainModel File

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%
% Project Name:  Peter Moss COVID-19 AI Research Project
% Repository:    COVID-19 AI Classification
% Project title: COVID-19 Pneumonia Detection/Early Detection
% Author 1:      Aniruddh Sharma
% Author 2:      Nitin Mane
% Title:         Train the xDNN Model for given Dataset
% Description:   Train the Model for the provided processed Dataset of
%                SARS-COV-2 Ct-Scan Dataset
% License:       MIT License
% Last Modified: 2020-07-30
%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%% Close all and clear
close all;
clc;

%% Data input and Training

load ./Model/Imds/imdsTrain
Label =grp2idx(imdsTrain.Labels);
load ./Model/Features/featuresTrain

Input1.Features=featuresTrain;
Input1.Labels=grp2idx(imdsTrain.Labels);
Input1.Images=imdsTrain.Files;

tic
Mode='Learning';
[Output1]=xDNN(Input1,Mode);
toc

%% Validation
load ./Model/Imds/imdsValidation
Label1 =grp2idx(imdsValidation.Labels);
load ./Model/Features/featuresTest


Input2.xDNNParms=Output1.xDNNParms;
Input2.Images=imdsValidation.Files;
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
