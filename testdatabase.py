import numpy as np
import cv2
import os
path = 'ImagesObama'
faceDetector=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
imagePaths=[os.path.join(path,f) for f in os.listdir(path)] 
for imagePath in imagePaths:
	IDSample=int(os.path.split(imagePath)[-1].split('.')[1])
	ID=int(os.path.split(imagePath)[-1].split('.')[0])
	ID = ID + 3
	img = cv2.imread(imagePath)
	gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
	faces = faceDetector.detectMultiScale(gray, 1.3, 5)
	for (x,y,w,h) in faces:
	    cv2.rectangle(img, (x,y), (x+w,y+h), (255,0,0), 2)
	    cv2.imshow('Frame',img)
	    if cv2.waitKey(100) & 0xFF == ord('q'):
	        break
	    cv2.imwrite("dataSet/User."+str(ID) +'.'+ str(IDSample) + ".jpg", gray[y:y+h,x:x+w])
#cv2.imshow('image',img)
#cv2.startWindowThread()
#cv2.namedWindow("preview")
#cv2.imshow("preview", img)
cv2.waitKey()
cv2.destroyAllWindows()
