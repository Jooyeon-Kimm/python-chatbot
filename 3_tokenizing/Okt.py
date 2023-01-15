"""
Okt는 트위터에서 개발한
Twitter 한국어 처리기에서 파생된
오픈소스 (아파치 2.0 라이선스) 한국어 처리기이다.

공식 홈페이지에 따르면 Okt는
빅데이터에서 간단한 한국어 처리를 통해
색인어를 추출하는 목표를 가지고 있기 때문에
완전한 수준의 형태소 분석을 지향하지 않습니다.

따라서 공식적으로는  Okt를
한국어 처리기라 표현하고 있다.
Okt는 띄어쓰기가 어느 정도 되어 있는 문장을 빠르게 분석할 때 많이 사용한다.

KoNLPy의 Okt 형태소 분석기를 사용하기 위해서는
다음과 같이 konlpy.tag 패키지의 Okt 모듈을 불러와야 한다.

from konlpy.tag import Okt
"""

from konlpy.tag import Okt

# Okt 형태소 분석기 객체 생성
okt = Okt()

text = "아버지가 방에 들어갑니다."

# 형태소 추출
morphs = okt.morphs(text)
print(morphs)
# ['아버지', '가', '방', '에', '들어갑니다', '.']

# 형태소와 품사 태그 추출
pos = okt.pos(text)
print(pos)
# [('아버지', 'Noun'), ('가', 'Josa'), ('방', 'Noun'), ('에', 'Josa'), ('들어갑니다', 'Verb'), ('.', 'Punctuation')]

# 명사만 추출
nouns = okt.nouns(text)
print(nouns)
# ['아버지', '방']

# 정규화, 어구 추출
text = "오늘 기분이 좋닿ㅎㅎ"
print(okt.normalize(text))  # 오늘 기분이 좋다ㅎㅎ
print(okt.phrases(text))    # ['오늘', '오늘 기분', '기분']