# 넘파이 라이브러리는 C언어로 구현되어 있기 때문에
# 빠른 배열 처리와 고성능 수치 계산을 지원한다.

# 주로 벡터 및 행렬 연산에 필요한 기능을 제공한다.
# 넘파이는 데이터 분석에 필요한 다양한 기능을 포함하고 있으며,
# 파이썬의 기본 자료구조보다 효율적인 방법으로 데이터를 다룰 수 있어
# 팬더스나 맷플롯립 라이브러리에서 사용하고 있다.

# 수학적 개념을 넘파이로 표현만 가능하다면
# 텐서플로 같은 딥러닝 프레임워크 없이도
# 딥러닝 모델을 구현할 수 있도록 강력하다.

import numpy as np

arr = np.array([1, 2, 3])  # 1차원 배열 생성, 배열은 행렬 개념으로 사용된다
print(arr)  # [1 2 3]
print(type(arr))  # <class 'numpy.ndarray'>

"""오류
AttributeError: module 'numpy' has no attribute 'array' ERROR
numpy가 설치되어 있고 pycharm에 문제가 없다면, 혹시 numpy.py라는 파일은 없나 확인해보세요..
"""

# 2 X 3 행렬 표현
import numpy as np

matrix = np.array([[1, 2, 3], [4, 5, 6]])
print(matrix)
# [[1 2 3]
#  [4 5 6]]

# 2 X 2 행렬 덧셈 연산
import numpy as np

A = np.array([[1, 2], [3, 4]])
B = np.array([[1, 1], [1, 1]])
C = A + B  # 행렬 덧셈 연산
print(C)
# [[2 3]
#  [4 5]]


# A 행렬 (3 x 2) 과 B 행렬 (2 X 2) 의 곱셈
import numpy as np

A = np.array([[1, 2], [3, 4], [5, 6]])
B = np.array([[1, 2], [3, 4]])
C = np.matmul(A, B)
print(C)
# [[ 7 10]
#  [15 22]
#  [23 34]]

# 행렬의 스칼라 곱
import numpy as np

A = np.array([[1, 2], [3, 4]])  # 2 x 2 행렬
k = 10  # 스칼라
C = k * A  # 스칼라 곱
print(C)  # 결과는 2 x 2 행렬
# [[10 20]
#  [30 40]]
