import cv2
import numpy
import os

def createFolder(directory):
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
    except OSError:
        print('Error: Creating directory. ' + directory)


face_detection = cv2.CascadeClassifier(r'haarcascade_frontalface_default.xml')

no_of_samples = 0
# static user_name =  # type: str
while True:
    try:
        user_name = raw_input("Enter your name:\n")
        print("Hi "+user_name+ "!")
        break
    except ValueError:
        print("Error: Please enter a name\n")
    finally:
        print("Welcome to face detection system")


cam = cv2.VideoCapture(0)
while True:
    ret, image = cam.read()
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    faces = face_detection.detectMultiScale(gray, 1.3, 5)

    # For the detected faces
    for (x_coordinates, y_coordinates, width, height) in faces:
        print("Face Detected!")
        user_folder = "Database\User - " + user_name
        createFolder("Database")
        createFolder(user_folder)
        temp_file_name = user_folder+"/User - " + user_name + "_" + str(no_of_samples)+".jpg"
        cv2.imwrite(temp_file_name, gray)
        cv2.rectangle(image, (x_coordinates, y_coordinates), (x_coordinates + width, y_coordinates + height),
                      (125, 125, 125), 2)
        no_of_samples += 1
        cv2.waitKey(10)
    cv2.imshow("Face", image)

    # Breakpoint
    if (cv2.waitKey(100) == ord('q')) and (no_of_samples >= 10) :
        # print("Database update success! {} inputs\nExit".format(no_of_samples))
        break

cam.release()
cv2.destroyAllWindows()
