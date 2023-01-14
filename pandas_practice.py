# 팬더스는 데이터 분석 및 처리를 위한 필수 라이브러리이다.
# 행과 열로 구성된 데이터 객체를 편리하게 관리할 수 있으며,

# 대용량 데이터를 처리하는 데 용이하다.
# 또한 가공된 데이터를 저장하거나 저장된 파일을 불러와
# 데이터 객체로 만들 수 있는 기능을 제공한다.

# 팬더스는 시리즈, 데이터프레임, 패널 등
# 세 가지 데이터 구조를 가지고 있다.

# Series 객체 사용
# 시리즈는 1차원 데이터로서 각 데이터값과 대응하는 인덱스를 지정할 수 있다.
# 인덱스를 생략할 경우 인덱스 번호가 자동으로 할당된다.
import pandas as pd

# 인덱스를 생략한 시리즈 객체
numbers = pd.Series([100, 200, 300])

# 시리즈 객체 출력
print(numbers)
# 0    100
# 1    200
# 2    300
# dtype: int64

# 인덱스를 지정한 시리즈 객체
scores = pd.Series([90, 80, 99], index=['국어', '수학', '영어'])

# 시리즈 객체 출력
print(scores.index)
# Index(['국어', '수학', '영어'], dtype='object')

# 시리즈 객체의 데이터값 출력
print(scores.values)
# [90 80 99]

# 원하는 위치의 인덱스, 데이터값 출력
print(scores.index[1], scores.values[1])
# 수학 80




# DataFrame 객체 사용
import pandas as pd

# 계절별 서울/부산 지역 온도 데이터 정의
temperatures = [[3.3, 34.5, 14.2, -10], [7.1, 32.1, 10.7, 2]]
seasons = ['Spring', 'Summer', 'Fall', 'Winter']
regions = ['Seoul', 'Busan']

# 데이터 프레임 객체 생성
data = pd.DataFrame(temperatures, index=regions, columns=seasons)

# 데이터프레임 객체의 데이터 출력
print(data)
print("=" * 50)
"""
       Spring  Summer  Fall  Winter
Seoul     3.3    34.5  14.2     -10
Busan     7.1    32.1  10.7       2
==================================================
"""


print(data.index)
print(data.columns)
print(data.values)
print("=" * 50)     # 구분선
"""
Index(['Seoul', 'Busan'], dtype='object')
Index(['Spring', 'Summer', 'Fall', 'Winter'], dtype='object')
[[  3.3  34.5  14.2 -10. ]
 [  7.1  32.1  10.7   2. ]]
==================================================
"""

# 서울의 봄 온도 데이터 출력
print(data['Spring']['Seoul'])
print("=" * 50)     # 구분선
"""
3.3
==================================================
"""
# 앞부분에서 2번째 행까지 조회
print(data.head(2))
print("=" * 50)     # 구분선
"""
       Spring  Summer  Fall  Winter
Seoul     3.3    34.5  14.2     -10
Busan     7.1    32.1  10.7       2
==================================================
"""
# 뒷부분에서 1번째 행까지 조회
print(data.tail(1))
"""
       Spring  Summer  Fall  Winter
Busan     7.1    32.1  10.7       2
"""




import pandas as pd
print("=" * 50)     # 구분선
# sample.xlsx 엑셀 파일 읽어오기
user_list = pd.read_excel('sample.xlsx', sheet_name='Sheet1')
print(user_list)
"""
==================================================
       이름   나이       전화번호
0  Juyeon  123  1234-1234
1  Suyeon   45  1234-5678
2    Hong   21  1234-4321
3      Go   79  4321-7777
4    Migz   98  4646-7979
"""

