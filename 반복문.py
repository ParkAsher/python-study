fruits = ['사과', '배', '감', '수박']

for fruit in fruits :
    print(fruit)


people = [
    {'name': 'bob', 'age': 20},
    {'name': 'carry', 'age': 38},
    {'name': 'john', 'age': 7},
    {'name': 'smith', 'age': 17},
    {'name': 'ben', 'age': 27},
    {'name': 'bobby', 'age': 57},
    {'name': 'red', 'age': 32},
    {'name': 'queen', 'age': 25}
]

for i, person in enumerate(people) :
    name = person['name']
    age = person['age']
    print(i, name, age)  


# 짝수만 출력하는 함수 만들기
num_list = [1, 2, 3, 6, 3, 2, 4, 5, 6, 2, 4]

for num in num_list:
    if num % 2 == 0:
        print(num)

# 짝수 갯수 출력
count = 0
for num in num_list:    
    if num % 2 == 0:
        count = count + 1

print(count)

# 모든 숫자 더하기
sum = 0
for num in num_list:
    sum += num

print(sum)

# 가장 큰 숫자 더하기
max = 0
for num in num_list:
    if max < num:
        max = num

print(max)