import cv2
import numpy

face_detection = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
cam = cv2.VideoCapture(0)
recognizer = cv2.createLBPHFaceRecognizer()

try:
    recognizer.load("Trainer Data\\trainerData.yml")
except:
    print("File Load Error!")
    exit()

id = 0
font = cv2.cv.InitFont(cv2.cv.CV_FONT_HERSHEY_COMPLEX_SMALL, 2, 1, 1, 1)
print(font)
while True:
    ret, image = cam.read()
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    faces = face_detection.detectMultiScale(gray, 1.3, 5)

    # For the detected faces
    for (x_coordinates, y_coordinates, width, height) in faces:
        cv2.rectangle(image, (x_coordinates, y_coordinates), (x_coordinates + width, y_coordinates + height),
                      (125, 125, 125), 2)
        id, conf = recognizer.predict(gray[y_coordinates:y_coordinates+height,x_coordinates:x_coordinates+width])
        if id == 1:
            id = "Ganindu"
        elif id == 2:
            id = "No Name"
        else:
            id = "New"
        cv2.cv.PutText(cv2.cv.fromarray(image), str(id), (x_coordinates, y_coordinates+height), font, 255)
        print("Face Detected!")
    cv2.imshow("Face", image)

    # Breakpoint
    if cv2.waitKey(1) == ord('q'):
        print("Exit")
        break

cam.release()
cv2.destroyAllWindows()
