import cv2

cam = cv2.VideoCapture(0)
cam.set(3,640)
cam.set(4,640) 

faceDetector=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
id=raw_input('\n enter user id end press <return> ==>  ')
print("\n [INFO] Initializing face capture. Look the camera and wait ...")
sampleNum=0
while(True):
    ret, img = cam.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = faceDetector.detectMultiScale(gray, 1.3, 5)
    for (x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
        sampleNum=sampleNum+1
        #cv2.imwrite("dataSet/User."+id +'.'+ str(sampleNum) + ".jpg", gray[y:y+h,x:x+w])
        cv2.imshow('frame',img)
    if cv2.waitKey(100) & 0xFF == ord('q'):
        break
    elif sampleNum>50:
        break
cam.release()
cv2.destroyAllWindows()