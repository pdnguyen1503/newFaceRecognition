import cv2
import numpy as np
import os 
import pymysql

recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read('recognizer/trainningData.yml')
cascadePath = "haarcascade_frontalface_default.xml"
faceCascade = cv2.CascadeClassifier(cascadePath);

font = cv2.FONT_HERSHEY_SIMPLEX

#iniciate id counter
id = 0

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
# Initialize and start realtime video capture
cam = cv2.VideoCapture(0)
cam.set(3, 720) # set video widht
cam.set(4, 720) # set video height

# Define min window size to be recognized as a face
minW = 0.1*cam.get(3)
minH = 0.1*cam.get(4)

while True:

    ret, img =cam.read()
    #img = cv2.flip(img, -1) # Flip vertically
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale( 
        gray,
        scaleFactor = 1.2,
        minNeighbors = 5,
        minSize = (int(minW), int(minH)),
       )
    for(x,y,w,h) in faces:
        cv2.rectangle(img, (x,y), (x+w,y+h), (0,255,0), 2)
        id, confidence = recognizer.predict(gray[y:y+h,x:x+w])
        print(id-1)
        print('---')
        print(confidence)
        # Check if confidence is less them 100 ==> "0" is perfect match 
        if (confidence < 100):
            name = personAll[id-1]
            confidence = "  {0}%".format(round(100 - confidence))
        else:
            name = "unknown"
            confidence = "  {0}%".format(round(100 - confidence))
        cv2.putText(img, str(name) + "-" + str(id) , (x+5,y-5), font, 1, (255,255,255), 2)
        cv2.putText(img, str(confidence), (x+5,y+h-5), font, 1, (255,255,0), 1)  
    cv2.imshow('camera',img) 

    k = cv2.waitKey(10) & 0xff # Press 'ESC' for exiting video
    if k == 27:
        break

# Do a bit of cleanup
print("\n [INFO] Exiting Program and cleanup stuff")
cam.release()
cv2.destroyAllWindows()