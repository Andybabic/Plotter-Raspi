import cv2
import os
import time

classifier = cv2.CascadeClassifier(cv2.data.haarcascades+"haarcascade_frontalface_default.xml")

dirFace = 'cropped_face'

cropp= 20
counter=0
counterdelete=10

# Create if there is no cropped face directory
if not os.path.exists(dirFace):
    os.mkdir(dirFace)
    print("Directory " , dirFace ,  " Created ")
else:    
    print("Directory " , dirFace ,  " has found.")

webcam = cv2.VideoCapture(0) # Camera 0 according to USB port
# video = cv2.VideoCapture(r"use full windows path") # video path

while (True):
    (f, im) = webcam.read() # f returns only True, False according to video access
    # (f, im) = video.read() # video 
    
    if f != True:
       break

    # im=cv2.flip(im,1,0) #if you would like to give mirror effect

    # detectfaces 
    faces = classifier.detectMultiScale(
        im, # stream 
        scaleFactor=1.05, # change these parameters to improve your video processing performance
        minNeighbors=60, 
        minSize=(50, 50) # min image detection size
        ) 

    # Draw rectangles around each face
    
    
    for (x, y, w, h) in faces:

        cv2.rectangle(im, (x-cropp, y-cropp), (x + w+cropp, y + h+cropp),(0,0,0),thickness=0)
        # saving faces according to detected coordinates 
        sub_face = im[y-cropp:y+h+cropp, x-cropp:x+w+cropp]
        FaceFileName = "cropped_face/face_"+ ".jpg" # folder path and random name image
        cv2.imwrite(FaceFileName, sub_face)
        counter = 0
        
    if os.path.exists("cropped_face/face_.jpg"):
        counter = counter+1
        time.sleep(0)
        if counter == counterdelete:
            os.remove("cropped_face/face_.jpg")

    # Video Window
    cv2.imshow('Video Stream',im)
    key = cv2.waitKey(5) & 0xFF
    # q for exit
    if key == ord('q'): 
        break
webcam.release()