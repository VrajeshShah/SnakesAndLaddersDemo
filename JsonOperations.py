import json

def JsonToObject(jsonFilePath):
    data={}
    with open(jsonFilePath,'r') as jsonFile:
        data = json.load(jsonFile)

    return data