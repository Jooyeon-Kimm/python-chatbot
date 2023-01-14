# 전 세계 많은 파이썬 사용자들이 만들어놓은 함수들을 묶어서 공개하고 있는데,
# 이를 라이브러리라고 한다

# 사용자가 많은 라이브러리의 경우
# 문서화가 잘 되어 있어서
# 사용하는 데 큰 문제가 없다

""" sys """
# 파이썬 인터프리터와 관련된 정보와 기능을 제공하는 모듈
# 특히 명령행에서 인수를 전달받기 위해 많이 사용

# 명령 프롬프트에서 파이썬 프로그램을 실행할 때
# 인자를 추가할 수 있다
# python C:\Users\USER\PycharmProjects\pythonProject\External_Functions.py 'hello' 10
# 이 값은 sys.argv 리스트에 저장된다.

# 명령행에서 전달받은 인수를 이용해
# 메세지를 출력하는 방법
""" 
import sys
print(sys.argv)     # 시스템 인자로 들어온 리스트 내용 출력
msg = sys.argv[1]   # hello
cnt = int(sys.argv[2])  # 10

for i in range(cnt):
    print(i, msg)
# 0 hello
# 1 hello
# 2 hello
# 3 hello
"""

import sys
for n in range(100):
    print(n)
    if(n==10):  # n 이 10이 되면 멈추기
        break


# 0
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9
# 10




""" pickle() """
# 파이썬 객체를 파일로 저장하고
# 메모리로 읽어올 수 있도록 도와주는 모듈

# 객체를 메모리에 저장해놓은 상황에서 프로그램이 종료되면
# 객체 내용이 모두 사라진다

# 객체를 파일로 저장하는 예
import pickle
f = open('setting.txt', 'wb')   # open() 함수를 이용해 setting.txt 파일을
                                # 바이너리 쓰기 (wb) 모드로 파일을 읽을 수 있는 파일 객체를 반환
                                
setting = [ {'title:' 'python program'}, {'author': 'joo'} ]     # 딕셔너리를 요소로 가지는 리스트 정의
pickle.dump(setting, f)     # 리스트 객체 setting의 내용을 파일 객체 f에 저장
f.close()   # 파일 객체 f를 닫기



# 파일로 저장된 객체를 읽어오는 예
import pickle
f = open('setting.txt', 'rb')   # 바이너리 읽기 모드로 파일을 제어할 수 있는 파일 객체를 반환
setting = pickle.load(f)
f.close()
print(setting)  # {'title:' 'python program'}, {'author': 'joo'}


""" time """
# 시스템이 제공하는 시간과 관련된 유용한 함수들
import time
print(time.time()) # 1970년 1월 1일 0시 0분 0초 기준으로 경과한 시간을 초 단위로 반환
                   # 시간이 지날 수록 증가

import time
time.localtime(time.time())
# time.struct_time(tm_year=2023, tm_mon = 1, tm_mday = 14, tm_hour = 5, tm_min = 19, tm_sec = 23, tm_wday = 5, tm_yday = 31, tm_isdst = 0)
t = time.localtime(time.time())    # 원하는 형태로 날짜와 시간을 출력할 수 있다
format_time = time.strftime('%Y/%m/%d %H:%M:%S', t)
print(format_time)  # 2023/01/14 17:26:35

""" random """
# 난숫값을 생성하는 기능과 다양한 랜덤 관련 함수를 제공
import random
f = random.random() # 0과 1 사이의 실수
print(f)  # 0.28342066886540296


# time.uniform() 사용
uni = random.uniform(1, 2)  # 1 <= random < 2
print(uni)  # 1.133104882468217

uni = random.uniform(1, 2)  # 1 <= random < 2
print(uni)  # 1.083944354268618


# time.randint() 함수 사용

uni = random.randint(1, 5)    # 1 <= random <= 5
print(uni)  # 1

uni = random.randint(1, 5)    # 1 <= random <= 5
print(uni)  # 4