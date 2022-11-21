a = [1,3,2,4,5,8,6,1,3,5,2,4,5]

a_set = set(a)

print(a_set) # {1, 2, 3, 4, 5, 6, 8}

student_a = ['물리2','국어','수학1','음악','화학1','화학2','체육']
student_b = ['물리1','수학1','미술','화학2','체육']

a_set = set(student_a)
b_set = set(student_b)

print(a_set - b_set)