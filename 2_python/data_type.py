
"""숫자"""
# 정수 계산
a = 10 + 5
b = (10-5) * 2

print(a)    # 15
print(b)    # 10

# 실수 계산
c = 2.2 * 5
d = 1.0 / 0.2
e = 3 / 2

print(c)    # 11.0
print(d)    # 5.0
print(e)    # 1.5
# 나눗셈 (/) 연산의 결과는 항상 실수 형태인 float 형
# 소수점을 사용하거나 기본적으로 계산 결과가 실수인 경우에는 float 형으로 처리


# /, //, % 연산자 사용
f = 3 / 2
g = 3 // 2
h = 5 / 2
i = 5 // 2
j = 5 % 2

print(f)    # 1.5
print(g)    # 1
print(h)    # 2.5
print(i)    # 2
print(j)    # 1


# 거듭제곱 계산
k = 2 ** 5
l = 2 ** 10

print(k)    # 32
print(l)    # 1024

# 변수 사용
m = 10
n = 20

print(m*n)  # 200

# 문자열
str1 = '1234'
str2 = 'hello'
str3 = "hello"

print(str1) # 1234
print(str2) # hello
print(str3) # hello

# 문자열 변수 사용
msg1 = '"Oh well", joo said'
print(msg1) # "Oh well", joo said

msg2 = "I'm joo"
print(msg2) # I'm joo


# 멀티라인 문자열
msg3 = "No breathe\nNo life"
print(msg3) # No breathe
            # No life

msg4 = '''you no longer look for happiness
because you know that
you already have it'''
print(msg4) # you no longer look for happiness
            # because you know that
            # you already have it

msg5 = """There are no 
accidents."""
print(msg5) # There are no
            # accidents.

"""리스트"""
numbers = [1, 2, 3, 4, 5]
print(numbers)  # [1, 2, 3, 4, 5]

real_numbers = [1.0, 2.0, 3.0, 4, 5]
print(real_numbers) # [1.0, 2.0, 3.0, 4, 5]

print(type(real_numbers))   # <class 'list'>



# 리스트 인덱싱 및 슬라이싱 (첫번째 요소는 0부터 시작)
numbers = [1, 2, 3, 4, 5]

n1 = numbers[1]  # 1번째 요소 인덱싱
print(n1)   # 2

n2 = numbers[-1]    # 뒤에서 1번째 요소 인덱싱
print(n2)   # 5

n3 = numbers[2:]    # 2번째 요소부터 슬라이싱, 새로운 리스트로 반환
print(n3)   # [3, 4, 5]

n4 = numbers[-2:]   # 뒤에서 2번째 요소부터 슬라이싱
print(n4)   # [4, 5]

n5 = numbers[1:-2]  # 1번째 요소에서 뒤에서 2번째 요소 앞까지 슬라이싱
print(n5)   # [2, 3]


# 리스트 요소 수정
numbers = [1, 2, 3, 4, 5]
print(numbers)  # [1, 2, 3, 4, 5]s

numbers[0] = 9  # 리스트 0번째 요소에 9 저장
print(numbers)  # [9, 2, 3, 4, 5]


# 리스트 요소 추가
numbers = [1, 2, 3, 4, 5]
numbers.append(9)
print(numbers)  # [1, 2, 3, 4, 5, 9]

# 리스트 요소 삽입
numbers = [1, 2, 3, 4, 5]
numbers.insert(1, 1.5)  # 리스트 1번 요소에 1.5 삽입
print(numbers)  # [1, 1.5, 2, 3, 4, 5]

# 리스트 요소 꺼내고 삭제 1
numbers = [1, 2, 3, 4, 5]
numbers.pop()   # 리스트의 맨 마지막 요소를 꺼내고 삭제
print(numbers)  # [1, 2, 3, 4]

# 리스트 요소 꺼내고 삭제 2
numbers = [1, 2, 3, 4, 5]
numbers.pop(2)  # 리스트의 2번째 요소를 꺼내고 삭제
print(numbers)  # [1, 2, 4, 5]

a = numbers.pop(3)  # 리스트의 3번쨰 요소를 꺼내서 변수 a에 저장
print(numbers)  # [1, 2, 4]


# del 키워드로 리스트 요소 삭제
numbers = [1, 2, 3, 4, 5]
del numbers[2]  # 리스트의 2번쨰 요소를 바로 삭제
print(numbers)  #[ 1, 2, 4, 5]

# 리스트 요소 개수 구하기
numbers = [1, 2, 3, 4, 5]
len = len(numbers)
print(len)  # 5


""" 튜플 """
# 한 번 생성되면 순서와 내용을 수정할 수 없다.
numbers = (1, 2, 3, 4, 5)
print(numbers)  # (1, 2, 3, 4, 5)

real_numbers = (1.0, 2.0, 3.0, 4, 'five', 'six')
print(real_numbers) # (1.0, 2.0, 3.0, 4, 'five', 'six')

t = type(real_numbers)
print(t)    # <class 'tuple'>


# 튜플 인덱싱 및 슬라이싱
numbers = (1, 2, 3, 4, 5)
n1 = numbers[1]     # 1번째 요소 인덱싱
n2 = numbers[-1]    # 뒤에서 1번째 요소 인덱싱
n3 = numbers[2:]    # 2번째 요소부터 슬라이싱, 새로운 튜플로 변환
n4 = numbers[-2:]   # 뒤에서 2번째 요소부터 슬라이싱
n5 = numbers[1:-2]  # 1번째 요소에서 뒤에서 2번째 요소 앞까지 슬라이싱

print(n1)   # 2
print(n2)   # 5
print(n3)   # (3, 4, 5)
print(n4)   # (4, 5)
print(n5)   # (2, 3)


# 튜플 요소 수정
numbers = (1, 2, 3, 4, 5)
# numbers[0] = 9  # 0번째 요소에 9 저장 불가 (튜플 요소 수정 불가)

new_numbers = numbers + (6, 7)  # 튜플 + 튜플
print(new_numbers)  # (1, 2, 3, 4, 5, 6, 7)

# 튜플 덧셈 연산 불가능
# numbers + (1)

# 튜플 덧셈 연산
numbers = numbers + (1,)  # 튜플 요소임을 알려줌
print(numbers)  # (1, 2, 3, 4, 5, 1)


""" 딕셔너리 """
user1 = {'name': '홍길동', 'age': 30, 'email': 'hong@gil.dong'}
print(user1)    # {'name': '홍길동', 'age': 30, 'email': 'hong@gil.dong'}

t = type(user1) # 타입 확인
print(t)        # <class 'dict'>


# 딕셔너리의 키가 문자열
dict1 = { 'K' : [1, 'hey', 3.3] }

e1 = dict1['K']       # Key가 K 인 Value 를 확인
print(e1)   # [1, 'hey', 3.3]

e2 = dict1['K'][1]    # Key가 K인 Value의 1번째 요소 확인
print(e2)   # hey



# 딕셔너리의 키가 숫자
dict2 = { 10: 'ten' }
e1 = dict2[10]
print(e1)   # 'ten'

# 딕셔너리의 데이터 쌍 추가 1
dict3 = { }         # 비어있는 딕셔너리 생성
dict3['a'] = 'A'    # 키가 'a'인 value에 'A'를 저장
dict3['b'] = 'B'    # 키가 'b'인 value에 'B'를 저장
print(dict3)        # {'a': 'A', 'b': 'B'}


# 딕셔너리의 데이터 쌍 추가 2
dict3[3] = [1, 2, 3]    # key가 3인 value에 리스트 저장
print(dict3)            # {'a': 'A', 'b': 'B', 3: [1, 2, 3]}

dict3[4] = { 'name': 'joo', 'age':100 }
print(dict3)            # {'a': 'A', 'b': 'B', 3: [1, 2, 3], 4: {'name': 'joo', 'age': 100}}



# 딕셔너리 데이터 쌍 삭제
del dict3['a']  # key 가 'a'인 데이터쌍 삭제
print(dict3)    # {'b': 'B', 3: [1, 2, 3], 4: {'name': 'joo', 'age': 100}}

del dict3[3]    # key 가 3인 데이터쌍 삭제
print(dict3)    # {'b': 'B', 4: {'name': 'joo', 'age': 100}}

dict3.clear()   # dict3 딕셔너리의 데이터 쌍 모두 삭제
print(dict3)    # {}



""" 불리언 """
check = True
uncheck = False

t = type(check)
print(t)        # <class 'bool'>

print(uncheck)  # False
