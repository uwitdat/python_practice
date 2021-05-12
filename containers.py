# EX 1:
print('|---------- EX:1 ---------|')

students = ['Mark', 'Mack', 'Max', 'Matt', 'Mike']

print(students[1])
print(students[-1])

# EX 2:
print('|---------- EX:2 ---------|')

foods = ('pizza', 'ice cream', 'chips', 'cookies', 'almonds')


for food in foods:
    print(f'{food} is a good food')


# EX 3:
print('|---------- EX:3 ---------|')

for food in foods[-2:]:
    print(food)

# EX 4:
print('|---------- EX:4 ---------|')

home_town = {
    'city': 'chicago',
    'state': 'illinois',
    'population': '2,700,000'
}

print(
    f'i was born in {home_town["city"]}, {home_town["state"]} - population of {home_town["population"]}')

# EX 5:
print('|---------- EX:5 ---------|')

for key, value in home_town.items():
    print(f'{key} = {value}')

# EX 6:
print('|---------- EX:6 ---------|')

cohort = []
index_range = range(5)
for index in index_range:
    cohort.append({"student": students[index], "fav_food": foods[index]})
for item in cohort:
    print(item)

# EX 7:
print('|---------- EX:7 ---------|')

awesome_students = [(f'{student} is awesome!') for student in students]
for student in awesome_students:
    print(student)
