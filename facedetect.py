import  cv2
import numpy as np




img = cv2.imread("data\\pictures\\dog\\7859(2).jpg")
kernel = np.ones((5,5),np.uint8)
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
#cv2.imshow("",gray)
haar_face_cascade=cv2.CascadeClassifier("./data/haarcascades/haarcascade_frontal_dog_face.xml")
faces = haar_face_cascade.detectMultiScale(gray,scaleFactor=1.1,minNeighbors=5)
print("Face Found",len(faces))
print(img.shape)
for x,y,w,h in faces:
    cv2.rectangle(img,(x,y),(x+w,y+h),(250,0,0),5)
    center_x=int(x+(w/2))
    center_y=int(y+(h/2))
    if x<=112:
        if y<=112:
            imgCropped = img[0:224,0:224]
        else:
            imgCropped = img[center_y+112:center_y+112,0:224]
    else:
        if y<=112:
            imgCropped = img[0:224,center_x-112:center_x+112]
        else:
            imgCropped = img[center_y-112:center_y+112,center_x-112:center_x+112]
    #imgCropped = img[y:y + h+100, x:x + w+100]
    # #imgCropped = img[y :y + w , x :x + h ]
    # if y>50&x>50:
    #     imgCropped = img[y - 50:y+174, x - 50:x + 174]
    # else:
    #     imgCropped = img[y :y +224, x :x + 224 ]
    # imgResized = cv2.resize(imgCropped, (224, 224))
    # print(x,y,w,h)
    # cv2.imshow("",imgResized)
    cv2.imshow("", imgCropped)

cv2.imshow("test",img)
cv2.waitKey(0)