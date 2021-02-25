import os
from PIL import Image
import numpy as np

#for now this function is only to check all pictures are 224*224
#path is where you store the dataset

# PATH = '../data/dogfacenet/aligned/after_4_bis/'
PATH = './data/pictures/somedoghead'

file_list = []


filenames = np.empty(0)
labels = np.empty(0)
idx = 0
for root, dirs, files in os.walk(PATH):
    if len(files) > 1:
        for i in range(len(files)):
            files[i] = root + '/' + files[i]
        filenames = np.append(filenames, files)

        labels = np.append(labels, np.ones(len(files)) * idx)

assert len(labels) != 0, '[Error] No data provided.'

for file_path in filenames:
        img = Image.open(file_path)
        if(img.size[0]!=224 or img.size[1]!=224):
            file_list.append(file_path)

if file_list==[]:
    print("all good")
else:
    for i in file_list:
        print(i)

