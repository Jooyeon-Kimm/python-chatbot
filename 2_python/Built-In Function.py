""" 내장 함수 """

""" format() """
# 문자열 포매팅 방법 1 : %d 를 이용한 문자열 포매팅 방법
# 문자열 포매팅 방법 2 : format()
print('integer : {} , float : {} , string : {}'.format(10, 3.14, "hi"))
# integer : 10 , float : 3.14 , string : hi

print('integer : {0} , float : {1} , string : {2}'.format(10, 3.14, "hi"))
# integer : 10 , float : 3.14 , string : hi

print('float : {1} , integer : {0} , string : {2}'.format(10, 3.14, "hi"))
# float : 3.14 , integer : 10 , string : hi


""" enumerate() """
numbers = [11, 12, 13, 14, 15]
for idx, val in enumerate(numbers):
    print('index:{}, value:{}'.format(idx, val))

"""
index:0, value:11
index:1, value:12
index:2, value:13
index:3, value:14
index:4, value:15
"""


""" str() """
# 입력으로 들어운 데이터를 문자열 객체로 반환합니다.
str1 = str(10)
print(str1) # 10

t = type(str1)
print(t)    # <class 'str'>

str2 = str("hi")
print(str2) # hi

str3 = str("HELLO").lower()
print(str3) # hello

str4 = str([1, 2, 3, 4])
print(str4) # [1, 2, 3, 4]


""" join() """
# 리스트에 포함되어 있는 요소들을
# 지정한 구문자로 구분해
# 문자열로 반환하는 함수

# 리스트 내 요소들을
# 문자열로 합칠 때 많이 사용

names = ['Juyeon', 'Suyeon', 'Gyuyeon', 'Jiyeon', 'Miyeon']
a = ' / '.join(names)
print(a)    # Juyeon / Suyeon / Gyuyeon / Jiyeon / Miyeon

a = ' , '.join(names)
print(a)    # Juyeon , Suyeon , Gyuyeon , Jiyeon , Miyeon


""" split() """
# join() 함수와 반대로
# 문자열을 특정 구분자를 기준으로 분리해
# 리스트로 반환하는 함수
names = ['Juyeon', 'Suyeon', 'Gyuyeon', 'Jiyeon', 'Miyeon']

a = ','.join(names)
print(a)    # Juyeon,Suyeon,Gyuyeon,Jiyeon,Miyeon

b = a.split(',')
print(b)    # ['Juyeon', 'Suyeon', 'Gyuyeon', 'Jiyeon', 'Miyeon']



""" id () """
# 객체를 입력받아 객체의 고유 주솟값 (레퍼런스) 를 반환하는 함수
# 해당 객체가 어떤 주소에 할당 되어 있는지 확인하는 용도
a = 10
id_a = id(a)
print(id_a) # 140703307261000

b = a
id_b = id(b)
print(id_b) # 140703307261000

# a 와 b의 주소가 동일하기 때문에
# a 와 b 는 같은 객체



""" find() """
# 특정 문자열을 찾기 위해 사용하는 함수

# 찾으려는 문자열을 입력받으면
# 그 문자열의 시작 위치를 반환한다

# 해당 문자열을 찾지 못하면
# -1을 반환

str = "I want to be a great programmer."
be = str.find("be") # 'be' 의 시작 위치는 10
print(be)   # 10

I = str.find("I")   # 'I'의 시작 위치는 0
print(I)   # 0

i = str.find("i")   # 'i'의 시작 위치는 -1
print(i)   # -1




""" strip() """
# 주어진 문자열 양쪽 끝의 공백을 제거하는 함수
str = "I want to be a great programmer.   "
new_str = str.strip()
print(new_str)  # I want to be a great programmer.


""" filter() """
# 개별 요소를 반복적으로 셀 수 있는 객체를 입력받아
# 각 요소를 함수로 수행한 후
# 결과가 True 인 것만 묶어서 반환

# 숫자 리스트에서 짝수만 필터링하는 예제
def is_even(number):
    return number % 2 == 0  # 짝수면 True 반환

numbers = range(1, 21)  # 1에서 20까지 수
even_list = list( filter(is_even, numbers) )
print(even_list)    # [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]



""" lambda() """
# 함수를 생성할 때 사용하는 키워드
# 익명 함수이기 때문에
# 한 번 사용되고 나면 메모리 영역에서 삭제되어
# 메모리 관리에 효율적인 장점

# 복잡한 함수는 def 키워드로,
# 간단한 함수는 lambda 키워드로


f = lambda x: x**2
print(f(2)) # 4
print(f(5)) # 25

# filter() 함수에 lambda 함수 사용
numbers = range(1, 21)  # 1에서 20까지 수
even_list = list(filter(lambda n: n%2 == 0, numbers))
print(even_list)    # [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]



""" map() """
# 개별 요소를 반복적으로 셀 수 있는 객체를 입력받아
# 각 요소를 함수로 수행한 후 결과를 묶어서 반환

# map 함수는 바로바로 계산하지 않기 때문에
# 게으른 연산 (lazy evaluation)을 한다

# 계산 결괏값이 필요할 때까지 게으름을 피우고 있다가
# 계산 시점에 오면 계산을 한다

# 계산이 필요할 때만 메모리를 사용하기 때문에
# 메모리 절약의 효과가 있다

numbers = range(1,5)    # 1에서 4까지 수
square_list = list(map(lambda x : x**2, numbers))
print(square_list)  # [1, 4, 9, 16]
