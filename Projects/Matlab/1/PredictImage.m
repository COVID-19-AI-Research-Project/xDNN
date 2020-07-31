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
