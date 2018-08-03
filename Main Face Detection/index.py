import cv2
import numpy

face_detection = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
cam = cv2.VideoCapture(0)


while True:
    ret, image = cam.read()
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    faces = face_detection.detectMultiScale(gray, 1.3, 5)

    # For the detected faces
    for (x_coordinates, y_coordinates, width, height) in faces:
        cv2.rectangle(image, (x_coordinates, y_coordinates), (x_coordinates+width, y_coordinates+height), (125, 125, 125), 2)
        print("Face Detected!")
    cv2.imshow("Face", image)
    
    # Breakpoint
    if cv2.waitKey(1) == ord('q'):
        print("Exit")
        break

cam.release()
cv2.destroyAllWindows()
