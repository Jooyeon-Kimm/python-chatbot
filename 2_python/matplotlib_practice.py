# 맷플롯립 라이브러리는 데이터를 플롯이나 차트로 시각화할 수 있도록 도와주는 도구입니다.
# 맷플롯립 라이브러리는 라인플롯, 바차트, 파이차트, 히스토그램 등 다양한 차트와 플롯 스타일을 지원합니다.
# 데이터를 분석할 때 시각화 도구는 매우 중요합니다.

""" 직선 그래프 """
import matplotlib.pyplot as plt

# x 축, y축 데이터 정의
x = [a for a in range(0,11)]
y = list(range(0, 11))
# 리스트 안에 for 구문을 이용해서 직관적으로 리스트를 생성할 수 있다.
# 이를 리스트 내포 list comprehension 기능이라고 한다.

# range() 함수에서 만든 0에서 10까지의 숫자를
# for 반복문을 이용해 리스트 요소로 순서대로 대입한다.

# lambda for 반복문 앞에 있는 변수 a는 표현식이다.
# lambda 따라서 수식이나 람다 함수를 사용해
# 계산된 결괏값을 리스트에 포함시킬 수 있다.

# x축, y축 데이터 출력
print('x축', x)  # x축 [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print('y축', y)  # y축 [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


# 그래프 출력
plt.plot(x,y)
plt.show()

""" 2차 함수 그래프 """
# 2차 함수 정의
# f(x) = x^2
f = lambda x: x**2

# x, y축 데이터 정의
x = [x for x in range(-10, 10)]
y = [f(y) for y in range(-10, 10)]

# x축, y축 데이터 출력
print('x축', x)  # x축 [-10, -9, -8, -7, -6, -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print('y축', y)  # y축 [100, 81, 64, 49, 36, 25, 16, 9, 4, 1, 0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

# 그래프 출력
plt.plot(x,y)
plt.show()


""" 계절별 온도 바 차트 """
import matplotlib.pyplot as plt

# 데이터 정의
temperatures = [3.3, 34.5, 14.2, -10]
x = list(range(4))
x_labels = ['Spring', 'Summer', 'Fall', 'Winter']

# 바 차트 출력
plt.title("Bar Chart")
plt.bar(x, temperatures)
plt.xticks(x, x_labels)             # x.ticks() 함수를 이용해 각각의 x축 데이터 위치에 지정된 텍스트를 표시 (Spring, Summer, Fall, Winter)

plt.yticks(sorted(temperatures))    # y.ticks() 함수를 이용해 오름차순으로 정렬된 온돗값을 y축 데이터 위치에 표시
# sorted() 함수는 인자로 들어온 리스트 요소를 오름차순으로 정렬해주는 역할을 한다.

plt.xlabel("season")
plt.ylabel("temperature")
plt.show()
