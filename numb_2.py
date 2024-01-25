import csv

with open('students.csv', encoding = 'utf-8') as file:
    reader = list(csv.DictReader(file, delimiter = ',', quotechar = '"'))
    for i in range(len(reader)):
        j = i -1
        key = reader[i]
        while float(reader[j]['score'] if reader[j]['score'] != 'None' else 0) < float(key['score'] if key['score'] != 'None' else 0) and j >= 0:
            reader[j+1] = reader[j]
            j -= 1
        reader[j+1] = key
count = 1
for el in reader:
    if '10' in el['class']:
        surname, name, patronymic = el['Name'].split()
        print(f'{count} место: {name[0]}. {surname}')
        count += 1
    if count == 4:
        break
