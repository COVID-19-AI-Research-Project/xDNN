%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

%                                      PredictImage File

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%
% Project Name:  Peter Moss COVID-19 AI Research Project
% Repository:    COVID-19 AI Classification
% Project title: COVID-19 Pneumonia Detection/Early Detection
% Author 1:      Aniruddh Sharma
% Author 2:      Nitin Mane
% Title:         Testing Function for Image
% Description:   Tests the PNG Image for a given path and return the integers 0 and 1 for Normal and
%                COVID-19 CT Scans
% License:       MIT License
% Last Modified: 2020-07-30
%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

function image_file = PredictImage(file)
    try
        imds_predict  = imageDatastore(fullfile(file), ...
                'IncludeSubfolders',true,'FileExtensions','.png','LabelSource','foldernames');
    layer = 'fc7';
    net = vgg16;

    inputSize = net.Layers(1).InputSize;

    resizeImdsPredict = augmentedImageDatastore(inputSize(1:2),imds_predict);
    featuresPredict = activations(net, resizeImdsPredict, layer, 'OutputAs', 'Rows', ...
                        'MiniBatchSize', 8);

    load ./Model/Pretrained/Output1
    Label1 = grp2idx(imds_predict.Labels);
    Input1.xDNNParms = Output1.xDNNParms;
    Input1.Images = imds_predict.Files;
    Input1.Features = featuresPredict;
    Input1.Labels = Label1;

    Mode='Validation';
    [Output4] = xDNN(Input1,Mode);

    image_file = Output4.EstLabs;
    catch
        disp('Cannot find file at given location.')
    end
if image_file == 1
    image_file = 1;
elseif image_file == 2
    image_file = 0;
end
