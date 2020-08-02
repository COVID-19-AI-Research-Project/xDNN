%% Copyright (c) 2020, Plamen P. Angelov and Eduardo Soares


%% Programmed by Eduardo
function [Output]=xDNN(Input,Mode)
if strcmp(Mode,'Learning')==1
    Images=Input.Images;
    Features=Input.Features;
    Labels=Input.Labels;
    CN=max(Labels);
    [RBPARAM]=OnlineDeepRuleBaseIdentification(Images,Features,Labels,CN);
    Output.xDNNParms.Parameters=RBPARAM;
    MemberLabels={};
    for ii=1:1:CN
        MemberLabels{ii}=Input.Labels(Input.Labels==ii);
    end
    Output.xDNNParms.CurrentNumberofClass=CN;
    Output.xDNNParms.OriginalNumberofClass=CN;
    Output.xDNNParms.MemberLabels=MemberLabels;
end
if strcmp(Mode,'Updating')==1
    Images=Input.Images;
    Features=Input.Features;
    Labels=Input.Labels;
    CN=Input.xDNNParms.OriginalNumberofClass;
    RBPARAM=Input.xDNNParms.Parameters;
    [RBPARAM]=OnlineDeepRuleBaseUpdating(Images,Features,Labels,CN,RBPARAM);
    Output.xDNNParms.Parameters=RBPARAM;
    MemberLabels=Input.xDNNParms.MemberLabels;
    for ii=1:1:CN
        MemberLabels{ii}=[MemberLabels{ii};Input.Labels(Input.Labels==ii)];
    end
    Output.xDNNParms.CurrentNumberofClass=Input.xDNNParms.CurrentNumberofClass;
    Output.xDNNParms.OriginalNumberofClass=CN;
    Output.xDNNParms.MemberLabels=MemberLabels;
end
if strcmp(Mode,'Validation')==1
    Params=Input.xDNNParms;
    datates=Input.Features;
    [EstimatedLabels,Scores]=TestResult(Params,datates);
    Output.EstLabs=EstimatedLabels;
    Output.Scores=Scores;
    Output.ConfMat=confusionmat(Input.Labels,Output.EstLabs);
    Output.ClasAcc=sum(sum(Output.ConfMat.*eye(length(Output.ConfMat))))/length(Input.Labels);
end
end
function [RBPARAM]=OnlineDeepRuleBaseIdentification(Image,GlobalFeature,LABEL,CL)
data={};
image={};
label={};
for ii=1:1:CL
    seq=find(LABEL==ii);
    data{ii}=GlobalFeature(seq,:);
    for jj=1:1:length(seq)
        image{ii}{jj}=Image{seq(jj)};
    end
    label{ii}=ones(length(seq),1)*ii;
end
   for ii=1:1:CL
    [RBPARAM{ii}]=xDNNclassifier_online(data{ii},image{ii});
end
end
function [PARAM]=xDNNclassifier_online(Data,Image)
[L,W]=size(Data);
or=0.0000001;
Xnorm = sqrt(sum(Data.^2, 2));
data = Data ./ Xnorm(:,ones(1,W));
Centre=data(1,:);
X=sum(data(1,:).^2);
Support=1;
NoC=1;
GMean=Centre;
Radius=or;
ND=1;
VisualPrototype{1}=Image{1};
for ii=2:1:L
    GMean=(ii-1)/ii*GMean+data(ii,:)/ii;
    CentreDensity=sum((Centre-repmat(GMean,NoC,1)).^2,2);
    [CDmax]=max(CentreDensity);
    [CDmin]=min(CentreDensity);
    DataDensity=sum((data(ii,:)-GMean).^2);
    distance=(pdist2(data(ii,:),Centre,'minkowski',2));
    [value,position]=min(distance);
    value=value^2;
    if DataDensity>CDmax||DataDensity<CDmin||value>2*Radius(position)
        Centre=[Centre;data(ii,:)];
        NoC=NoC+1;
        VisualPrototype{NoC}=Image{ii};
        X=[X;ND];
        Support=[Support;1];
        Radius=[Radius;or];
    else
        Centre(position,:)=Centre(position,:)*(Support(position)/(Support(position)+1))+data(ii,:)/(Support(position)+1);
        Support(position)=Support(position)+1;
        Radius(position)=0.5*Radius(position)+0.5*(X(position,:)-sum(Centre(position,:).^2))/2;
    end
end
PARAM.NoC=NoC;
PARAM.Centre=Centre;
PARAM.Support=Support;
PARAM.Radius=Radius;
PARAM.GMean=GMean;
PARAM.Prototype=VisualPrototype;
PARAM.L=L;
PARAM.X=X;
end
function [RBPARAM]=OnlineDeepRuleBaseUpdating(Image,GlobalFeature,LABEL,CL,RBPARAM)
data={};
image={};
label={};
for ii=1:1:CL
    seq=find(LABEL==ii);
    data{ii}=GlobalFeature(seq,:);
    for jj=1:1:length(seq)
        image{ii}{jj}=Image{seq(jj)};
    end
    label{ii}=ones(length(seq),1)*ii;
end
for ii=1:1:CL
    [RBPARAM{ii}]=xDNNclassifier_onlineupdating(data{ii},image{ii},RBPARAM{ii});
end
end
function [EstimatedLabels,Scores]=TestResult(Params,datates)
PARAM=Params.Parameters;
CurrentNC=Params.CurrentNumberofClass;
LAB=Params.MemberLabels;
VV=1;
LTes=size(datates,1);
EstimatedLabels=zeros(LTes,1);
Scores=zeros(LTes,CurrentNC);
for ii=1:1:LTes
    data=datates(ii,:);
    Xnorm = sqrt(sum(data.^2, 2));
    data = data ./ Xnorm;
    
    R=zeros(VV,CurrentNC);
    Value=zeros(CurrentNC,1);
    for kk=1:1:CurrentNC
        distance=sort((pdist2(data,PARAM{kk}.Centre,'minkowski',2)),'ascend');
        R(:,kk)=distance(1:1:VV)';
        Value(kk)=distance(1);
    end
    Value=exp(-1*(Value).^2);
    Scores(ii,:)=Value;
    [Value,Idx]=sort(Value,'descend');
    EstimatedLabels(ii)=Idx(1);
end
LABEL1=zeros(CurrentNC,1);
for ii=1:1:CurrentNC
    [a,b]=hist(LAB{ii},unique(LAB{ii}));
    [~,t]=max(a);
    LABEL1(ii)=b(t);
end
EstimatedLabels=LABEL1(EstimatedLabels);
end
function [PARAM]=xDNNclassifier_onlineupdating(Data,Image,PARAM)
[L,W]=size(Data);
or=0.1;
Xnorm = sqrt(sum(Data.^2, 2));
data = Data ./ Xnorm(:,ones(1,W));
ND=1;
NoC=PARAM.NoC;
Centre=PARAM.Centre;
Support=PARAM.Support;
Radius=PARAM.Radius;
GMean=PARAM.GMean;
VisualPrototype=PARAM.Prototype;
K=PARAM.L;
X=PARAM.X;
for ii=K+1:1:L+K
    GMean=(ii-1)/ii*GMean+data(ii-K,:)/ii;
    CentreDensity=sum((Centre-repmat(GMean,NoC,1)).^2,2);
    [CDmax]=max(CentreDensity);
    [CDmin]=min(CentreDensity);
    DataDensity=sum((data(ii-K,:)-GMean).^2);
    distance=(pdist2(data(ii-K,:),Centre,'minkowski',2));
    [value,position]=min(distance);
    value=value^2;
    if DataDensity>CDmax||DataDensity<CDmin||value>2*Radius(position)
        Centre=[Centre;data(ii-K,:)];
        NoC=NoC+1
        VisualPrototype{NoC}=Image{ii-K};
        X=[X;ND];
        Support=[Support;1];
        Radius=[Radius;or];
    else
        Centre(position,:)=Centre(position,:)*(Support(position)/(Support(position)+1))+data(ii-K,:)/(Support(position)+1);
        Support(position)=Support(position)+1;
        Radius(position)=0.5*Radius(position)+0.5*(X(position,:)-sum(Centre(position,:).^2))/2;
    end
end
PARAM.NoC=NoC;
PARAM.Centre=Centre;
PARAM.Support=Support;
PARAM.Radius=Radius;
PARAM.GMean=GMean;
PARAM.Prototype=VisualPrototype;
PARAM.L=L+K;
PARAM.X=X;
end