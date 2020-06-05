import numpy as np
import cv2
import os
floderFile=raw_input('\n enter folder of user end press <return> ==>  ')
countImage = 0
IDUser=raw_input('\n enter IDUser end press <return> ==>  ')

if not os.path.exists(floderFile):
    print("There is no directory name like this")
else:  	
	path = str(floderFile)
	faceDetector=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
	imagePaths=[os.path.join(path,f) for f in os.listdir(path)] 
	for imagePath in imagePaths:
		img = cv2.imread(imagePath)
		gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
		faces = faceDetector.detectMultiScale(gray, 1.3, 5)
		for (x,y,w,h) in faces:
			cv2.rectangle(img, (x,y), (x+w,y+h), (255,0,0), 2)
			cv2.imshow('Frame',img)
			cv2.imwrite("dataSet/User."+str(IDUser) +'.'+ str(countImage) + ".jpg", gray[y:y+h,x:x+w])
			if cv2.waitKey(100) & 0xFF == ord('q'):
				break
		countImage+=1
cv2.waitKey()
cv2.destroyAllWindows()