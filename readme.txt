The program is based on https://github.com/GuillaumeMougeot/DogFaceNet.git
The program uses the following anaconda environment:



If you don't have data source or want to get the latest data source ,please run "python getAllPicture.py" firs. If there is an error, please check the path first. If the program run properly,you will get a data.csv which saved the picture name and valuable title.

run python facedetect.py to process the source data,you can put new haarcascade into data/haarcascades and change the code after "import area" in facedetect.py to improve the code
,in the " for x, y, w, h in faces" you can define the size of output pictures, which may effect the final result.
Then you need some manual work, clean the useless picture, to make sure output pictures are all useful and get a good result. from data/pictures/somedoghead folder,you can find some processed images.

finally you can run python mydogfacenet，model will saved in data/model, if the progress is interupt,it will not restart from begining , it will reload the saved model and continue. but for now it will not showed in the progress (maybe add a text file to save the current epoch will make this part better, to do this ,you will need change already_step in the define area)

from output_original you can get all the output from by GuillaumeMougeot's DogFaceNet with his data source, and output_new is using somedoghead as data source. In my opinion, the backgrond of pictures(which ), dog's head size in pictures and the size of data source
