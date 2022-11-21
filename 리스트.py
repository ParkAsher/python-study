a_list = ['사과', '배', '감']

print(a_list[0])    # 사과

b_list = [2, '배', 'false', ['사과', '감']]

print(b_list)

c_list = [2,5,7,1,0]
c_list.append(99)

print(c_list)   # [2, 5, 7, 1, 0, 99]


result = c_list[-1]
print(result)   # 99

c_list.sort()
print(c_list)

c_list.sort(reverse=True)
print(c_list)   #[99, 7, 5, 2, 1, 0]

result = (5 in c_list)
print(result)   # True