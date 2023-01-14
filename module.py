import calc  # calc 모듈을 불렁모. main.py와 같은 경로에 있어야 함

a = calc.add(10, 20)  # calc 모듈의 add 함수
print("add = {}".format(a))     # add = 30

b = calc.mult(10, 20)
print("mult = {}".format(b))    # mult = 200

""" 
모듈에서 불러올 함수를 직접 지정하는 방법
from 모듈명 import 함수명, 함수명, ...
"""

""" 
모듈에서 모든 함수를 불러오는 방법
from 모둘명 import *
"""
