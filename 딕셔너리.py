a_dict = { 'name': 'bob', 'age': 27 }
a_dict['height'] = 180

result = ('height' in a_dict)

print(result)   # True

people = [
    {'name': 'bob', 'age': 27}, 
    {'name': 'john', 'age': 30}
]

print(people[1]['age']) # 30