import face_recognition
import cv2

path = "vid.mp4"
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()

    if ret == False:
        break
    
    face_locations = face_recognition.face_locations(frame)
    
    for index, face_loc in enumerate(face_locations):
        topLeftY, bottomRightX, bottomRightY, topLeftX = face_loc
        pt1 = (topLeftX, topLeftY)
        pt2 = (bottomRightX, bottomRightY)
        cv2.rectangle(frame, pt1, pt2, (255,0,0), 2)
        cv2.imshow("test", frame)
    
    cv2.waitKey(1)