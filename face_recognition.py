import cv2
import numpy as np
from PIL import Image
import pymysql

#init from class
#read from file Tranning
recognizer=cv2.face.LBPHFaceRecognizer_create()
recognizer.read("recognizer/trainningData.yml")
#frontface default
faceDetect=cv2.CascadeClassifier('haarcascade_frontalface_default.xml');
#set text style
fontface = cv2.FONT_HERSHEY_SIMPLEX
fontscale = 1
fontcolor = (203,23,252)

id = 0

#get all user from phpmyadmin by ID
def getProfile():
    connection = pymysql.connect(host="localhost", user="nguyenpc", passwd="nguyen1503", database="FaceBase")
    cursor = connection.cursor()
    cmd="SELECT * FROM `People`"
    cursor.execute(cmd)
    people = cursor.fetchall()
    peopleArray  = np.array(people)
    #print(peopleArray)
    i = 0
    personArray = ['unkown']
    while i<len(peopleArray):
    	#print(peopleArray[i][1])
    	personArray.append(peopleArray[i][1])
    	#print(personArray)
    	i+=1
    return personArray
personAll = getProfile()

#set up for camera
cam=cv2.VideoCapture(0)
cam.set(3,480)
cam.set(4,480) 
# Define min window size to be recognized as a face
minW = 0.1*cam.get(3)
minH = 0.1*cam.get(4)

print(personAll)
print("\n [INFO] Initializing face capture. Look the camera and wait ...")
while(True):
    #camera read
    ret, img=cam.read();
    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    faces=faceDetect.detectMultiScale(
        gray,
        scaleFactor = 1.3,
        minNeighbors =5,
        minSize = (int(minW), int(minH)),
        );
    for(x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
        id,conf=recognizer.predict(gray[y:y+h,x:x+w])
        #id main 
        print(id)
        print("----")
        print(conf)
        if conf < 30:
            namePerson = "unknown"
            conf = "  {0}%".format(round(100 - conf))
        if conf >30 and conf <100 and id >0:
            namePerson = personAll[id-1]
            conf = "  {0}%".format(round(100 - conf))
        cv2.putText(img, "Name: " + str(namePerson), (x,y+h+30), fontface, fontscale, fontcolor ,2)
        cv2.putText(img, str(conf), (x+5,y+h-5), fontface, fontscale, fontcolor, 1)  
        cv2.imshow('Face',img) 
    if cv2.waitKey(1)==ord('q'):
        break;
cam.release()
cv2.destroyAllWindows()
