# 예외 처리
# try: 정상 수행
# except: 예외 처리
# finally: 예외 발생 여부와 상관 없이 무조건 실행
# division by zero 예외 처리
try:
    a = 10
    b = 0
    c = a / b   # 0으로 나눌 수 없다
    print(c)
except Exception as e:
    print(e)

# division by zero


# 여러 개의 예외 처리
try:
    a = 10
    b = 'zero'  # 'zero'를 0으로 밖고 실행하면 예외 처리가 달라진다
    c = a / b
except ZeroDivisionError as e:
    print(e)
except TypeError as e:
    print(e)

# unsupported operand type(s) for /: 'int' and 'str'
