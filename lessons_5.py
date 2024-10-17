# num = 1 #int
# name = 'Jhon' #str
# float = 10.3 #float
# bool = True #bool
#                   key  : value
# student_exsams = {"Ivanov":60, "Petrov":78,"Sidorov":85}

# # methods 

# print(student_exsams.keys())# показывает все ключи
# print(student_exsams.get('Ivanov')) покаазывает все значение по ключу
# print(student_exsams.pop('Ivanov')) удаляет ключ и значение
# print(student_exsams.popitem()) удаляет последний ключ и значение 
# print(student_exsams.update({'Ivanov':60})) добавляет ключ и значение
# student_exsams.update({"Ivano4" : 620}) 
# student_exsams["Petro2"] = 80 изменяет значение по ключу
# student_exsams["Ivanov"] = 80 
# del student_exsams["Ivanov"] удаляет ключ и значение 
# student_exsams.setdefault('Ivanov3',80) добавляет ключ и значение

# a = student_exsams.fromkeys(['Ivanov2','Petrov2'],80) создает новый словарь с ключами
# b = student_exsams.copy() копирует словарь

# print(student_exsams,a,b)

# students = {'Jhon': 85, 'Emily': 92, 'Michael':78, 'Sophia': 95, 'David': 87}
# average_score = sum(students.values())/len(students)
# print(average_score)

# people = {'Jhon':25, 'Alice':30, "Bob":22}
# oldest_person = max(people, key=people.get)
# print(oldest_person)

# students = {"Jhon":[5,4,3],"Alice":[2,4,5],"Bob":[4,4,4]}

# fruits = {"apple":2,"banana":4,"cherry":3}
# highest_price_fruits = max(fruits, key=fruits.get)
# print(highest_price_fruits)