import cv2
import os
cam = cv2.VideoCapture(0)
cam.set(3, 640)
cam.set(4, 480)

face_detector = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
floderFile=raw_input('\n enter folder of user end press <return> ==>  ')
IDUser=raw_input('\n enter IDUser end press <return> ==>  ')

count = 0

# Create target directory & all intermediate directories if don't exists
if not os.path.exists(floderFile):
    os.makedirs(floderFile)
    print("Directory " , floderFile ,  " Created ")
    while(True):
        ret, frame = cam.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_detector.detectMultiScale(frame, 1.3, 5)
        for(x, y, w, h) in faces:
            cv2.rectangle(frame, (x,y), (x+w, y+h), (0,225,0), 2)
            count +=1
            cv2.imwrite(str(floderFile) + '/User.'+str(IDUser) +'.'+str(count)+'.jpg', gray[y: y+ h, x: x+ w])
            print(str(floderFile) + '/User.'+str(IDUser) +'.'+str(count)+'.jpg')
        cv2.imshow('frame', frame)
        cv2.waitKey(1)

        if count > 199:
            break

    cam.release()
    cv2.destroyAllWindows()
else:    
    print("Directory " , floderFile ,  " already exists")    
