# 함수란 하나의 기능을 수행하는 코드들의 집합이다.

# 사용자 정의 함수
def add(a, b):  # 사용자 정의 함수 add 정의
    return a + b  # a+b 의 결과를 반환


result = add(10, 20)
print(result)  # 30


# print_user() 함수 사용
def print_user(user):  # 사용자 정보와 점수를 출력하는 함수
    print("name : %s" % user['name'])
    print("age : %d" % user['age'])
    print("score: %d" % score)

user = {'name': 'Joo', 'age': 100}  # user 정보 정의
score = 89

print_user(user)
"""
name : Joo
age : 100
score: 89
"""
