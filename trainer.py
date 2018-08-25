import os
import cv2
import numpy
from PIL import Image

recognizer = cv2.createLBPHFaceRecognizer()

database_Directory = "Database"

def createFolder(directory):
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
    except OSError:
        print('Error: Creating directory. ' + directory)

# returns the image file paths relative to the current directory
def getImageFilePaths(path):
    database = []
    userDirectory = [os.path.join(path,f) for f in os.listdir(path)]
    # print(userDirectory)
    for user in userDirectory:
        imageDirectory = [os.path.join(user, i) for i in os.listdir(user)]
        for imgdir in imageDirectory:
            # print(imgdir)
            database.append(imgdir)
    return database

def getUserID_Username_ImageFace(database):
    userIds = []
    userNames = []
    faces = []
    for imagepath in database:
        face_image = Image.open(imagepath).convert('L')
        numpy_face = numpy.array(face_image, 'uint8')
        faces.append(numpy_face)
        userName = imagepath.split("User - ")[-1].split("_")[0].split("-")[0]
        userId = imagepath.split("User - ")[-1].split("_")[0].split("-")[-1]
        print(userId)
        userIds.append(int(userId))
        userNames.append(userName)
        # cv2.imshow("Training", numpy_face)
        cv2.waitKey(10)

    return userIds, userNames, faces


image_database = getImageFilePaths(database_Directory)
userIds, userNames, faces = getUserID_Username_ImageFace(image_database)
recognizer.train(faces, numpy.array(userIds))
createFolder("Trainer Data")
recognizer.save('Trainer Data/trainerData.yml')
cv2.destroyAllWindows()