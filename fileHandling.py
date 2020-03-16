import pathlib

def getFileNames():
    filepath = pathlib.Path.cwd() / 'copypastas'
    fileNames = []
    for path in sorted(filepath.rglob('*.txt')):
        fileNames.append(path.name)
        print(path.name)

    return fileNames
'''
listNames = []
pathNames = getFileNames()
'''