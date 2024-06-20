from bs4 import BeautifulSoup
from googletrans import Translator
import json


#initialize
translator = Translator()

#reads XML file using Beautiful Soup
def readXmlFile(xmlFile):
    with open(xmlFile, 'r', encoding='utf-8') as newXmlFile:
        soup = BeautifulSoup(newXmlFile, 'xml')
    return soup

#takes XML file and returns translated text
def xmlFileTranslation(xmlFile, newLanguage):
    soup = readXmlFile(xmlFile)
    text=soup.find_all(text=True)
    for element in text:
        translation = translator.translate(element, dest=newLanguage).text
        return translation



#reads JSON file
def readJsonFile(jsonFile):
    with open(jsonFile, 'r', encoding='utf-8') as newJsonFile:
        return json.load(newJsonFile)

#takes JSON file and returns translated text
def jsonFileTranslation(jsonFile, newLanguage):
    jsonFileContent=readJsonFile(jsonFile)

    #recursive function to cover nested dictionaries
    def translateDictionary(dictionary):
        for key, value in d.items():
            if isinstance(value, dict):
                translateDictionary(value)
            else:
                dictionary[key] = translator.translate(value, dest=newLanguage).text
        return dictionary

    translation = translateDictionary(jsonFileContent)
    return translation



#reads .txt file
def readTextFile(textFile):
    with open(textFile, 'r', encoding='utf-8') as readTextFile:
        return readTextFile.read()

#takes .txt file and returns translated text
def textFileTranslation(textFile, newLanguage): 
    textFileContent=readTextFile(textFile) 
    translation = translator.translate(textFileContent, dest=newLanguage)
    return translation

#takes string and returns translated text
def stringTranslation(string, newLanguage):
    translation = translator.translate(string, dest=newLanguage)
    return translation.text



#string example
exampleString = "Hi, my name is Emma Enkhbold."  
translateToGerman = 'de'  #this is the language code for German
translateToHindi = 'hi' #this is the language code for Hindi
translateToSpanish = 'es' #this is the language code for Spanish
translateToChinese = 'zh-cn' #this is the language code for Chinese (Simplified)

#print the result
print(stringTranslation(exampleString, translateToGerman))
print(stringTranslation(exampleString, translateToHindi))
print(stringTranslation(exampleString, translateToSpanish))
print(stringTranslation(exampleString, translateToChinese))

