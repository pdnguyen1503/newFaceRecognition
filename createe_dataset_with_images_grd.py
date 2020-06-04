import numpy as np
import cv2
import os

path = 'ThayTien'
ID=raw_input('\n enter user id end press <return> ==>  ')
faceDetector=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
imagePaths=[os.path.join(path,f) for f in os.listdir(path)] 

def recFace(faces, ID, index):
	if (len(faces) > 0):
		for (x,y,w,h) in faces:
			cv2.rectangle(img, (x,y), (x+w,y+h), (255,0,0), 2)
			imS = cv2.resize(img, (960, 540))  
			cv2.imshow('Frame',imS)
			cv2.imwrite("dataSetTest/User."+str(ID) +'.'+ str(index) + ".jpg", gray[y:y+h,x:x+w])
			if cv2.waitKey(100) & 0xFF == ord('q'):
				break
	else:
		print("can't find face with haarlike")
index = 0
for index in range(len(imagePaths)):
	img = cv2.imread(imagePaths[index])
	gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
	faces = faceDetector.detectMultiScale(gray, 1.3, 5)
	print(imagePaths[index])
	recFace(faces, ID, index)
print("finish")
cv2.waitKey()
cv2.destroyAllWindows()