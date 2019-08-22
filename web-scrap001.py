"""
0단계 : 대상 페이지의 URL 주소를 확보한다
1단계 : 대싱 페이지의 HTML 소스를 확보한다
2단계 : HTML 내에 데이터를 파싱한다. -> 어렵다!
3단계 : 파이썬 데이터로 만든다. (list, dicr... 즉, 메모리로 올린다.)
4단계 : 메모리에 있는 데이터를 저장(공유)한다.
"""

# 1단계 : 대싱 페이지의 HTML 소스를 확보한다 => "requests" 모듈 주당 100만 건 다운로드됨

import requests
# requests : 로봇으로 인식함 

# 옥션 스마일 배송 가전 파트
'''
res = requests.get('http://corners2.auction.co.kr/SmileDelivery/Category?categoryCode=1001001')
print(res.status_code)
print(res.text)
'''

#현재 멜론 및 쿠팡에서는 requests 로봇접속을 막음 => 요즘 사실 왠만한 사이트가 이걸 막아버림 파싱 금지
# 그러나 헤더 값중 User-Agent의 값을 알 수 있다면 해당 문제는 금방 해결이 가능하다. (google에서 my user agent 검색)
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36'
}
# 파싱 할때는 웹보다 모바일 소스가 더 편할수 있다.
# res2 = requests.get('https://m.app.melon.com/index.htm', headers=headers) #멜론
res2 = requests.get('https://www.coupang.com/np/campaigns/82/components/178155', headers=headers) # 쿠팡
print(res2.status_code)
print(res2.text)
#현재 멜론에서는 requests 로봇접속을 막음 => 요즘 사실 왠만한 사이트가 이걸 막아버림 파싱 금지