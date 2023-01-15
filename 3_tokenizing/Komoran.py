"""
Komoran은 Shineware에서 자바로 개발한
한국어 형태소 분석기이다.

코모란으로 발음하며
Apache 라이선스 2.0을 따르는 오픈소스 소프트웨어이다.

다른 형태소 분석기와 다르게
공백이 포함된 형태소 단위로도 분석이 가능해서
많이 사용한다.

KoNLPy의 코모란 형태소 분석기를 사용하기 위해서는
다음과 같이 konlpy.tag 패키지의 Komoran 모듈을 불러와야 한다.
from konlpy.tag import Komoran
"""

from konlpy.tag import Komoran

# 코모란 형태소 분석기 객체 생성
komoran = Komoran()

text = "아버지가 방에 들어갑니다."

# 형태소 추출
morphs = komoran.morphs(text)
print(morphs)
# ['아버지', '가', '방', '에', '들어가', 'ㅂ니다', '.']

# 형태소와 품사 태그 추출
pos = komoran.pos(text)
print(pos)
# [('아버지', 'NNG'), ('가', 'JKS'), ('방', 'NNG'), ('에', 'JKB'), ('들어가', 'VV'), ('ㅂ니다', 'EF'), ('.', 'SF')]

# 명사만 추출
nouns = komoran.nouns(text)
print(nouns)
# ['아버지', '방']