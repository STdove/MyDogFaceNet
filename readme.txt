The program is based on https://github.com/GuillaumeMougeot/DogFaceNet.git
the source of pictures is from https://hundehof-meikeva.hpage.com/gallery459656.html  
get anaconda environment:
conda env create -f environment.yaml


If you don't have data source(original pictures with dogs) or want to get the latest data source ,please run "python getAllPicture.py". I have comment a key code in getAllPicture.py please read the code first and uncomment it,after that if there is an error, please check the path. If the program run properly,you will also get a data.csv which saved the picture name and valuable title.

run python facedetect.py to process the original data,you can put new haarcascade into data/haarcascades and change the code after "import area" in facedetect.py to improve the code,in the " for x, y, w, h in faces" you can define the size of output pictures, which may effect the final result.(if you change this you will also need change some setting where with 224*224*3)

Then you need some manual work, clean the useless picture, to make sure output pictures are all useful and get a good result. from data/pictures/somedoghead folder,you can find some processed images.

finally you can run python mydogfacenet，model will saved in data/model, if the progress is interupt,it will not restart from begining , it will reload the saved model and continue. but for now it will not showed in the progress (maybe add a text file to save the current epoch will make this part better, to do this ,you will need change already_step in the define area)

from output_original you can get all the output from by GuillaumeMougeot's DogFaceNet with his data source, and output_new is using somedoghead as data source. In my opinion, the background of pictures, dog's head size in pictures and the size of data source may effect the result
