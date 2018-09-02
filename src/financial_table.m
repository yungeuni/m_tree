clc
clear all
close all

files = dir('./data/finance');

for k = 3:length(files)
    file_name = files(k).name;
    [filepath,name,ext] = fileparts(file_name);
    
%     finance{k-2} = readtable(['./data/finance/', file_name], 'FileEncoding', 'UTF-8');
    data = readtable(['./data/finance/', file_name], 'FileEncoding', 'UTF-8');
    pause;
end


data(find(strcmp(data(:,1).x______, '영업이익')), 2)

data.Properties.VariableNames




 