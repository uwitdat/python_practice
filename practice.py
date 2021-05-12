student = {
    'name': 'Maria',
    'course': 'SEI',
    'current_week': 7,
    'age': 27
}

student['current_week'] = 8

student.items()

if 'course' in student:
    print(f'{student["name"]} is in {student["course"]}')
else:
    print(f'{student["name"]} is not in any courses')

for key, val in student.items():
    print(f'{key} = {val}')

where_my_things_are = {
    'socks': 'closet',
    'wallet': 'table',
    'keys': 'carpet'
}

for key, val in where_my_things_are.items():
    print(f'my {key} is kept in {val}')

colors = ['red', 'green', 'blue']
more_colors = ['purple', 'orange']

all_colors = colors + more_colors

print(f'all colors: {all_colors}')

colors.append('black')
colors.extend(['brown', 'orange'])
print(colors)

colors.insert(1, 'yellow')
red = colors.pop(0)
del colors[2]
colors.remove('orange')

for idx, color in enumerate(colors):
    print(f'{idx+1}: {color}')

print(red)
print(colors)


nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

squares = [n * n for n in nums]
print(squares)

even_squares = [n * n for n in nums if (n * n) % 2 == 0]
print(even_squares)
