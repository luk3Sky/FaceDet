import os
import cv2
import numpy
from PIL import Image

recognizer = cv2.createLBPHFaceRecognizer()

database_Directory = "Database"

def getImageFilePaths(path):
    userDirectory = [os.path.join(path,f) for f in os.listdir(path)]
    print(userDirectory)
    for user in userDirectory:
        imageDirectory = [os.path.join(user, i) for i in os.listdir(user)]
        for imgdir in imageDirectory:
            print(imgdir)

getImageFilePaths(database_Directory)
