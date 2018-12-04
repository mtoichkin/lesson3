#import re

with open('referat.txt', 'r', encoding='utf-8') as FileTemp, open('referat2.txt', 'w', encoding='utf-8') as FileNew:
    FileWords = 0
    FileCharacters = 0
    for FileLine in FileTemp:
        FileLine = FileLine.replace(".", "!")
        FileNew.write(FileLine)
        FileCharacters = FileCharacters + len(FileLine)
        #FileLine = re.sub('[!@#$.,«»]', '', FileLine)
        #FileLine = FileLine.translate({ord(c): None for c in '!@#$.,«»'})
        FileWordsList = FileLine.split()
        FileWords = FileWords + len(FileWordsList)
print("Длина файла:", FileCharacters)
print('Количество слов в тексте:', FileWords)
