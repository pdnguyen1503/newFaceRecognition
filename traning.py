import cv2,os
import numpy as np
from PIL import Image

#init from class
recognizer = cv2.face.LBPHFaceRecognizer_create()
detector = cv2.CascadeClassifier("haarcascade_frontalface_default.xml");
path='dataSet'

#Funtion to get image and labels of images
def getImagesAndLabels(path):
    imagePaths=[os.path.join(path,f) for f in os.listdir(path)] 
    faceSamples=[]
    IDs=[]
    for imagePath in imagePaths:
        faceImg=Image.open(imagePath).convert('L');
        faceNp=np.array(faceImg,'uint8')
        ID=int(os.path.split(imagePath)[-1].split('.')[1])
        faces = detector.detectMultiScale(faceNp)
        for (x, y, w, h) in faces:
            faceSamples.append(faceNp[y:y+h,x:x+w])
            IDs.append(ID)
        cv2.imshow("traning",faceNp)
        cv2.waitKey(10)
    return IDs, faceSamples
Ids,faces=getImagesAndLabels(path)
#Trainning then save in file traingingData
recognizer.train(faces, np.array(Ids))
recognizer.write('recognizer/trainningData.yml')
cv2.destroyAllWindows()