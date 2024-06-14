from pathlib import Path
import os
import config
import pdb

def getAllFifFilesFromFolder(directory):
    fifFiles = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.fif') and 'eeg-1' not in file:
                filePath = os.path.join(root, file)
                fifFiles.append(filePath)
    return fifFiles

def getDirFromFolder(folderPath):
    entries = os.listdir(folderPath)
    directories = [entry for entry in entries if os.path.isdir(os.path.join(folderPath, entry))]
    directoriesWithPaths = [Path(folderPath, folder) for folder in directories]
    return directories, directoriesWithPaths

def getAllPreprocessedFiles(folderPath=config.preprocessedDatasetDir):
    allFilePaths = []
    _, subjectFolders = getDirFromFolder(folderPath)
    for subject in subjectFolders:
        _, sessionFolders = getDirFromFolder(subject)
        for session in sessionFolders:
            dirPath = Path(session, 'eeg')
            files = getAllFifFilesFromFolder(dirPath)
            for file in files:
                allFilePaths.append(file)
                
    allFilePaths = [filepath for filepath in allFilePaths if 'sub-013' not in filepath]
    for file in allFilePaths:
        print(file)
    
    return allFilePaths