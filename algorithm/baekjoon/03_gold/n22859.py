"""
0. Link
- https://www.acmicpc.net/problem/22859

1. Idea
- Implementation
- <main>, <div>, <p> 태그 등을 구분
- <div>의 attribute인 title을 우선 출력하고 안에 있는 <p>를 한 줄씩 출력
- <p> 안에 있는 태그와 시작과 끝에 있는 공백을 지우고 2개 이상의 공백을 하나로 변경
- 제목은 무조건 존재하고 태그 사이에는 공백이 없으며 태그는 올바른 쌍으로만 주어짐을 보장
- 정규 표현식을 활용해 조건에 맞는 문장을 파싱하고 불필요한 문자를 제거해 출력

2. Data Size
- source: str(1,000,000)
"""

import re

source = input()

main = re.findall('<main>(.*)</main>', source)[0]
div_list = re.findall('<div title="(.*?)">(.*?)</div>', main)

for title, paragraph in div_list:
    print('title :', title)
    p_list = re.findall('<p>(.*?)</p>', paragraph)
    for p in p_list:
        p = re.sub('(<.*?>)', '', p)
        p = re.sub('\s+', ' ', p.strip())
        print(p)