import csv
import random
import string

def create_initials(s: string):
    names = s.split()
    return f'{names[0]}{names[1]}{names[2][0]}'

def create_password():
    characters = string.ascii_letters
    password = ''.join(random.choice(characters) for i in range(10))
    return password

students_with_password = []

with open('students.csv', encoding='utf-8') as file:
    reader = list(csv.DictReader(file, delimiter = ',', quotechar = '"'))
    for row in reader:
        row['login'] = create_initials(row['Name'])
        row['password'] = create_password()
        students_with_password.append(row)

with open('students2.csv','w', newline = '', encoding = 'utf-8') as file:
    w = csv.DictWriter(file, fieldnames = ['id','Name','titleProject_id','class','score','login','password'])
    w.writeheader()
    w.writerows(students_with_password)
