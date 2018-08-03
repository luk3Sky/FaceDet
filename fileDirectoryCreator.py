import os

# createFolder('./data/')
# Creates a folder in the current directory called data

def createFolder(directory):
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)


    except OSError:
        print('Error: Creating directory. ' + directory)




# Example
