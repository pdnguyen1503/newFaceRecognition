import cv2
import os 

cam = cv2.VideoCapture(0)
#cai dat cho cam o che do 720
cam.set(3,480)
cam.set(4,480) 

face_detector = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
# moi nguoi nhap vao 1 id
face_id = input('\n enter user id end press <return> ==>  ')

print("\n [INFO] Initializing face capture. Look the camera and wait ...")
# Initialize individual sampling face count

count = 0

while(True):

    _, img = cam.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) #tao anh xam tu anh goc.
    #phat hien cac doi tuong co kich thuoc khac nhau dau vao,-> tra ve voi danh sach hinh chu nhat
    faces = face_detector.detectMultiScale(gray, 1.3, 5) #anh, kich thuoc toi thieu co the(doi tuong nho hon thi bo qua), kich thuoc toi da
    #print(faces)
    for (x,y,w,h) in faces:
        cv2.rectangle(img, (x,y), (x+w,y+h), (255,0,0), 2)
        #hinh anh, toa do trai, toa do ben duoi phai,  mau sac, do day vien
        count += 1 #so luong khuon mat khoi tao chay tang dan khi phat hien faces
        # Save the captured image into the datasets folder
        cv2.imshow('frame', img) # ve khung hinh khuon mat
        #print(gray[y:y+h,x:x+w])
        cv2.imwrite("dataset/User." + str(face_id) + '.' + str(count) + ".jpg", gray[y:y+h,x:x+w])
    k = cv2.waitKey(100) & 0xff # Press 'ESC' for exiting video
    #nhan de thoat video
    if k == 27:
        break
    elif count >= 100:
         break
# Do a bit of cleanup (don dep)
print("\n [INFO] Exiting Program and cleanup stuff")
cam.release()
cv2.destroyAllWindows()