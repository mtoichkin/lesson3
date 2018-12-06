import csv
CSVList = [
           {'name': 'Маша', 'age': 25, 'job': 'Scientist'},
           {'name': 'Вася', 'age': 8, 'job': 'Programmer'},
           {'name': 'Эдуард', 'age': 48, 'job': 'Big boss'},
        ]

with open('csv1.csv', 'w', encoding='utf-8', newline="") as FileTemp:
    Fields = ['name', 'age', 'job']
    FileNew = csv.DictWriter(FileTemp, Fields, delimiter=';')
    FileNew.writeheader()
    for UserList in CSVList:
        FileNew.writerow(UserList)
