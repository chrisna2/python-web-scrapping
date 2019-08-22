"""
0단계 : 대상 페이지의 URL 주소를 확보한다
1단계 : 대싱 페이지의 HTML 소스를 확보한다
2단계 : HTML 내에 데이터를 파싱한다. -> 어렵다!
3단계 : 파이썬 데이터로 만든다. (list, dicr... 즉, 메모리로 올린다.)
4단계 : 메모리에 있는 데이터를 저장(공유)한다.
"""

# 2단계 :  HTML 내에 데이터를 파싱한다. -> 어렵다! -> beautifulsoup

import requests
from bs4 import BeautifulSoup


headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36'
}
# 파싱 할때는 웹보다 모바일 소스가 더 편할수 있다.
# 멜론
# res = requests.get('https://m.app.melon.com/index.htm', headers=headers)
# 쿠팡
res = requests.get('https://www.coupang.com/np/campaigns/82/components/178155', headers=headers)

soup = BeautifulSoup(res.text, 'html.parser')
# [F12] > copy > copy selector : #\31 37145559 > a > dl > dd > div.name
# 위에 같이 아이디가 숫자로 시작되는 경우 \가 붙는데 여기에 \를 하나 더 붙여서 사용하면 정상 인식 됨 : 숫자라는 것을 인식시킴
tag = soup.select_one('#\\31 37145559 > a > dl > dd > div.name')

print(tag)
print(tag.text.strip())  # 공백값 제거
