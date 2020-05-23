import cv2
import os

cam = cv2.VideoCapture(0)
#set for camera 
cam.set(3,640)
cam.set(4,640) 

faceDetector=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
#input id of user
idFace=raw_input('\n enter user id end press <return> ==>  ')
print("\n [INFO] Initializing face capture. Look the camera and wait ...")
sampleNum=0
while(True):
    _, img = cam.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = faceDetector.detectMultiScale(gray, 1.3, 5)
    for (x,y,w,h) in faces:
        cv2.rectangle(img, (x,y), (x+w,y+h), (255,0,0), 2)
        sampleNum+=1
        cv2.imshow('Frame',img)
        cv2.imwrite("dataSet/User."+str(idFace) +'.'+ str(sampleNum) + ".jpg", gray[y:y+h,x:x+w])
    if cv2.waitKey(100) & 0xFF == ord('q'):
        break
    elif sampleNum>=50:
        break
print("\n [INFO] Exiting Program and cleanup stuff")
cam.release()
cv2.destroyAllWindows()