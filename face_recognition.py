import cv2
import numpy as np
from PIL import Image
#import pickle
import pymysql


faceDetect=cv2.CascadeClassifier('haarcascade_frontalface_default.xml');
cam=cv2.VideoCapture(0);
rec=cv2.face.LBPHFaceRecognizer_create();
rec.read("recognizer/trainningData.yml")
id=0
#set text style
fontface = cv2.FONT_HERSHEY_SIMPLEX
fontscale = 1
fontcolor = (203,23,252)

#get data from phpmyadmin by ID
def getProfile(id):
    connection = pymysql.connect(host="localhost", user="nguyenpc", passwd="nguyen1503", database="FaceBase")
    cursor = connection.cursor()
    cmd="SELECT * FROM People WHERE ID="+str(id)
    cursor.execute(cmd)
    data = cursor.fetchall()
    profile=None
    for row in data:
        profile=row
    connection.close()
    return profile

while(True):
    #camera read
    ret,img=cam.read();
    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    faces=faceDetect.detectMultiScale(gray,1.3,5);
    for(x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
        id,conf=rec.predict(gray[y:y+h,x:x+w])
        #id main 
        id = id -1
        profile=getProfile(id) 
        #set text to window
        if(profile!=None):
            #cv2.PutText(cv2.fromarray(img),str(id),(x+y+h),font,(0,0,255),2);
            cv2.putText(img, "Name: " + str(profile[1] + "Id: " + str(id)), (x,y+h+30), fontface, fontscale, fontcolor ,2)
        cv2.imshow('Face',img) 
    if cv2.waitKey(1)==ord('q'):
        break;
cam.release()
cv2.destroyAllWindows()
