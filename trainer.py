import os
import cv2
import numpy
from PIL import Image

recognizer = cv2.createLBPHFaceRecognizer()

database_Directory = "Database"

# returns the image file paths relative to the current directory
def getImageFilePaths(path):
    database = []
    userDirectory = [os.path.join(path,f) for f in os.listdir(path)]
    print(userDirectory)
    for user in userDirectory:
        imageDirectory = [os.path.join(user, i) for i in os.listdir(user)]
        for imgdir in imageDirectory:
            # print(imgdir)
            database.append(imgdir)
    return database

def getImageFacesandUsername(database):
    faces = []
    usernames = []
    for imagepath in database:
        face_image = Image.open(imagepath).convert('L')
        numpy_face = numpy.array(face_image, 'uint8')
        faces.append(numpy_face)
        username = imagepath.split("User - ")[-1].split("_")[0]
        print(username)
        usernames.append(username)
        cv2.imshow("Training", numpy_face)
        cv2.waitKey(10)

    return usernames, faces


image_database = getImageFilePaths(database_Directory)
usernames, faces = getImageFacesandUsername(image_database)
recognizer.train(faces, numpy.array(usernames))
