import os
import shutil
import time

path = input("Enter Path of File: ")

def getFileAge(path):
    ctime = os.stat(path).st_ctime
    return ctime   

secondsIn30Days = time.time() - (30*24*60*60)

if os.path.exists(path):
    for mainFolder, subFolders, files in os.walk(path):
        if secondsIn30Days >= getFileAge(mainFolder):
            shutil.rmtree(mainFolder)
            break
        else:
            for subFolder in subFolders:
                folderPath = os.path.join(mainFolder, subFolder)
                if secondsIn30Days >= getFileAge(folderPath):
                    shutil.rmtree(folderPath)

            for file in files:
                filePath = os.path.join(mainFolder, file)
                if secondsIn30Days >= getFileAge(filePath):
                    os.remove(filePath)
    else:
        if secondsIn30Days >= getFileAge(path):
            os.remove(path)
else:
    print("Sorry, File/Folder not found. Please try again!")