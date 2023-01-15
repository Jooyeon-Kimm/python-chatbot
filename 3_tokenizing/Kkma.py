"""
Kkma는 서울대학교 IDS 연구실에서
자연어 처리를 위해 개발한
한국어 형태소 분석기이다.

Kkma는 '꼬꼬마'로 발음하며,
GPL v2 라이선스를 따른다.

문장에 따라 정확한 형태소 분석이 안 될 수도 있다.

KoNLPy의 꼬꼬마 형태소 분석기를 사용하기 위해서는
다음과 같이 konlpy.tag 패키지의 Kkma 모듈을 불러와야 한다.

from konlpy.tag import Kkma
"""

from konlpy.tag import Kkma

# 꼬꼬마 형태소 분석기 객체 생성
kkma = Kkma()

text = "아버지가 방에 들어갑니다."

# 형태소 추출
morphs = kkma.morphs(text)
print(morphs)
# ['아버지', '가', '방', '에', '들어가', 'ㅂ니다', '.']

# 형태소와 품사 태그 추출
pos = kkma.pos(text)
print(pos)
# [('아버지', 'NNG'), ('가', 'JKS'), ('방', 'NNG'), ('에', 'JKM'), ('들어가', 'VV'), ('ㅂ니다', 'EFN'), ('.', 'SF')]

# 명사만 추출
nouns = kkma.nouns(text)
print(nouns)
# ['아버지', '방']

# 문장 분리
sentences = "내 휴대폰이 어디에 있는지 모르겠어. 혹시 전화해줄 수 있어?"
s = kkma.sentences(sentences)
print(s)
# ['내 휴대폰이 어디에 있는지 모르겠어.', '혹시 전화해 줄 수 있어?']

