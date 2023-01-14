""" if 조건문 """
check = True
if check:  # check 변수가 True 인지 감사
    print('*' * 15)
    print('check is true')
    print('*' * 15)

"""
***************
check is true
***************
"""


# if 조건문 사용
check = False
if not check:   # check 변수가 False 인지 검사
    print('-' * 15)
    print('check is false')
    print('-' * 15)

"""
---------------
check is false
---------------
"""

# if 조건문 사용
check = False
if check == False:   # check 변수가 False 인지 검사
    print('*' * 15)
    print('check is false')
    print('*' * 15)
"""
***************
check is false
***************
"""

# if 조건문 사용
check = False
if check != True:   # check 변수가 False 인지 검사
    print('-' * 15)
    print('check is false')
    print('-' * 15)
"""
---------------
check is false
---------------
"""


# if 조건문 사용
age = 20
if age >= 19:   # 나이가 19세 이상인지 검사
    print('You are an adult')
else:
    print('You are not an adult')
# You are an adult


# if 조건문 사용
score = 84

if score >= 90:
    print('Grade A')
elif score>=80:
    print('Grade B')
elif score >= 70:
    print('Grade C')
else:
    print('Grade D')
# Grade B


# if 조건문 사용
dist = 300
if dist >= 0 and dist <= 50:    # 거리가 0이상 50 이하일 때
    print('0~50')
elif 50 < dist <= 100:   # 거리가 50초과 100 이하일 때
    print('50~100')
else:   # 100 초과
    print('100~')
# 100~


""" while 반복문 """
i = 1
while i <= 10:
    print('i = %d' % i)
    i = i + 1
"""
i = 1
i = 2
i = 3
i = 4
i = 5
i = 6
i = 7
i = 8
i = 9
i = 10
"""


# while 반복문 사용
"""
while True: # 무한루프
    print('input number: ')
    menu = int(input())
    if menu == 0: break # 무한루프 중단
    elif menu == 1: print('number one')
    elif menu == 99: continue   # continue는 조건 검사 없이 다음 루프 실행
    elif menu == 2: print('number two')
    else: print('another number')
    
input number: 
2
number two
input number: 
1
number one
input number: 
99
input number: 
0

Process finished with exit code 0
"""


""" for 반복문 """
# for 문 사용
numbers = [1, 2, 3, 4, 5]
for n in numbers:
    print(n)
"""
1
2
3
4
5
"""


# for 문 사용
numbers = range(1, 6)   # 1에서 5까지 리스트 작성
for n in numbers:
    print(n)

"""
1
2
3
4
5
"""


# 여러 개의 변수에 자동 대입되는 for 반복문
points = [ (0,0), (1, 2), (3, 4)]
for x, y in points:
    print(x, y)
"""
0 0
1 2
3 4
"""

# 딕셔너리의 keys() 함수
user = {'name': 'Key', 'age':100, 'nationality':'Korea'}
key = user.keys()
print(key)  # dict_keys(['name', 'age', 'nationality'])


# 딕셔너리의 key 리스트 출력
user = {'name': 'Key', 'age':100, 'nationality':'Korea'}
for k in user.keys():
    print(k)
"""
name
age
nationality
"""

# 딕셔너리 value 리스트 출력
user = {'name': 'Key', 'age':100, 'nationality':'Korea'}
value =  user.values()
print(value)    # dict_values(['Key', 100, 'Korea'])



# 딕셔너리의 values() 함수 사용
user = {'name': 'Key', 'age':100, 'nationality':'Korea'}
for v in user.values():
    print(v)
"""
Key
100
Korea
"""


# 딕셔너리의 key, value 리스트 출력
user = {'name': 'Key', 'age':100, 'nationality':'Korea'}
for k, v in user.items():
    print(k, ',', v)
"""
name , Key
age , 100
nationality , Korea
"""



