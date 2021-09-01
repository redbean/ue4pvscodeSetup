import sys, json
import os


appData = [os.environ['APPDATA'], 'Code', 'User', 'settings.json']
fullPath = os.path.join(*appData)
colorTheme = 'workbench.colorTheme'
usingColor = 'Default Dark+'
pythonKey = 'python.pythonPath'
autoCompleteKey = 'python.autoComplete.extraPaths'
schemaKey = 'json.schemas'
analKey = 'python.analysis.extraPaths'
#for maya
mayaScriptPath = os.path.join(*[os.environ['PROGRAMFILES'], 'Autodesk', 'Maya2020', 'devkit', 'other', 'pymel','extras','completion','py'])
#for ue4
ue4Path = os.path.join(*['d:',  '', 'Program Files', 'Epic Games', 'UE_4.26'])
ue4PythonPath = os.path.join(*['Engine', 'Binaries', 'ThirdParty', 'Python3', 'Win64'])
ue4PythonExe = os.path.join(ue4PythonPath, 'python.exe')

ue4Lib = os.path.join(ue4PythonPath, 'Lib')
ue4Dll = os.path.join(ue4PythonPath, 'Dlls')
ue4SmallLib = os.path.join(ue4PythonPath, 'lib')
ue4platWin = os.path.join(ue4PythonPath, 'lib', 'plat-win')
ue4tk = os.path.join(ue4PythonPath, 'lib', 'lib-tk')
ue4package = os.path.join(ue4PythonPath, 'lib', 'site-package')

projectFolder = ''
stub = os.path.join(projectFolder, 'Intermediate',  'PythonStub')

extraPathes = [ue4Lib, ue4Dll, ue4SmallLib, ue4tk, ue4platWin, ue4package, ue4PythonPath, stub ,mayaScriptPath]

def OverwriteJsonFile():
    with open (fullPath, 'r') as js:
        jsonObj = json.load(js)

    jsonObj[colorTheme] = usingColor
    jsonObj[autoCompleteKey] = extraPathes
    jsonObj[analKey] = extraPathes


    with open(fullPath, 'w') as js :
        jsonStr = json.dump(jsonObj, js, indent=2)


def CreateJsonFile():
    jsonObj = {}
    jsonObj[pythonKey] = "python"
    jsonObj[colorTheme] = usingColor
    jsonObj[autoCompleteKey] = extraPathes
    jsonObj[schemaKey] = []
    jsonObj[analKey] = extraPathes

    with open(fullPath, 'w') as js :
        jsonStr = json.dump(jsonObj, js, indent=2)

if os.path.isfile(fullPath) != False:
   OverwriteJsonFile()
   pass
CreateJsonFile()
