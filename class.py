# 객체지향 언어에서는 객체를 생성하기 위해 언어 차원에서 클래스를 지원합니다.
# 파이썬에서 사용하는 모든 자료형은 객체이다.
# 프로그램 내부 코드는 상태와 동작 행위로 구성되어 있다.
# 이때 데이터 상태와 동작 행위를 가지는 코드 그룹을 객체라고 한다.
# 이러한 객체는 메모리에 적재되어야 사용할 수 있으며,
# 보통 하나의 객체는 어떤 문제를 해결하기 위해 동일한 목적을 갖는 상태와 동작 행위를 가지고 있다.
# 객체를 이용해 프로그래밍하는 방법론을 객체지향 프로그래밍이라고 한다.
# 객체가 어떤 클래스를 나타내는 경우에는 인스턴스라고 부른다.

# 파이썬에서는 모든 데이터를 객체로 보고 있으며,
# 모든 객체는 어떤 기능을 하는 클래스의 인스턴스.
# 파이썬에서 생성하는 모든 객체는 인스턴스

""" 클래스
class 클래스명:
"""


# 챗봇 클래스
class Chatbot:
    def sayHello(self):
        print("hello")

    def sayMyName(self):
        print("My name is Jbot :D")


# 챗봇 인스턴스 생성
chatbot = Chatbot()
chatbot.sayHello()  # hello
chatbot.sayMyName()  # My name is Jbot :D

# 생성자 및 소멸자
""" 생성자
class 클래스명:
    def __init__(self, 인자, ...):
"""

""" 소멸자
class 클래스명:
    def __del__(self):
"""


class SimpleObj:
    def __init__(self):
        print('call ___init__()')

    def __del__(self):
        print('call __del--()')


obj = SimpleObj()
print('obj instance is alive...')
del obj

# call ___init__()
# obj instance is alive...
# call __del--()


# 메서드와 인스턴스 변수
# 클래스는 메서드와 인스턴스 변수로 구성되어 있습니다.
# 클래스 내부에서 사용되는 함수는 메서드,
# 클래스 안에서 전역적으로 사용되는 변수는 인스턴스 변수라고 생각하자

"""
class 클래스명:
    def 메서드명(self, 인자):
        코드
        코드
"""


# 사칙연산 클래스
class Calc:
    def __init__(self, init_value):
        self.value = init_value

    def add(self, n):
        return self.value + n

    def sub(self, n):
        return self.value - n

    def mult(self, n):
        return self.value * n

    def div(self, n):
        return self.value / n


cal = Calc(100)
print("value = {0}".format(cal.value))  # value = 100

a = cal.add(100)
b = cal.sub(50)
c = cal.mult(2)
d = cal.div(2)

print("a = {0}, b = {1}, c = {2}, d = {3}".format(a, b, c, d))
# a = 200, b = 50, c = 200, d = 50.0