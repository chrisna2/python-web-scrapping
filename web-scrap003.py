"""
0단계 : 대상 페이지의 URL 주소를 확보한다
1단계 : 대싱 페이지의 HTML 소스를 확보한다
2단계 : HTML 내에 데이터를 파싱한다. -> 어렵다!
3단계 : 파이썬 데이터로 만든다. (list, dicr... 즉, 메모리로 올린다.)
4단계 : 메모리에 있는 데이터를 저장(공유)한다.
"""

# 3단계 : 파이썬 데이터로 만든다. (list, dicr... 즉, 메모리로 올린다.)

import requests
from bs4 import BeautifulSoup
import pandas as pd

# 1. 데이터 확보
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36'
}

res = requests.get('https://www.coupang.com/np/campaigns/82/components/178155', headers=headers)  # 쿠팡 > 가전

soup = BeautifulSoup(res.text, 'html.parser')

# 2. 데이터를 수집하여 list of list로 만든다.
product_list = []

# #productList > li 가 li_tag의 root tag다
for li_tag in soup.select('#productList > li'):
    # 1. 상품명 : [#\32 82796849 >] a > dl > dd > div.name
    # print(li_tag.select_one('a > dl > dd > div.name').text.strip())
    name = li_tag.select_one('a > dl > dd > div.name').text.strip()
    # 2. 가격 : [#\32 82796849 >] a > dl > dd > div.price-area > div.price-wrap > div.price > em > strong
    # print(int(li_tag.select_one('a > dl > dd > div.price-area > div.price-wrap > div.price > em > strong')
    #          .text.strip().replace(',', '')))
    price = int(li_tag.select_one('a > dl > dd > div.price-area > div.price-wrap > div.price > em > strong')
                .text.strip().replace(',', ''))
    try:
        # 3. 추천, 좋아요 : [#\31 37145559 >] a > dl > dd > div.other-info > div.rating-star > span.rating-total-count
        # print(li_tag.select_one('a > dl > dd > div.other-info > div.rating-star > span.rating-total-count')
        #       .text.strip()[1:-1])  # 양 옆에 붙은 것을 지운다고 할때.
        likes = li_tag.select_one('a > dl > dd > div.other-info > div.rating-star > span.rating-total-count').text.strip()[1:-1]
        # 만약 좋아요, 항목이 없는 부분이 존재하면 None 리턴 하기 때문에 예외 처리 함
    except Exception:
        print(0)
        likes = None
    # 4. 이미지 : [#\31 37145559 >] a > dl > dt > img
    # print('http:' + li_tag.select_one('a > dl > dt > img')['src'])  # url을 가져오기위해서 http 입력
    images = 'http:' + li_tag.select_one('a > dl > dt > img')['src']

    product_list.append([name, price, likes, images])

print(product_list)
# 3. 엑셀로 저장한다
# pandas 를 사용한다. 데이터 가공하는 모듈중 최강, AI 에도 연동, 웬만한 데이터는 처리가 가능하다.


# 4단계 : 메모리에 있는 데이터를 저장(공유)한다.
'''
DataFrame 이라는 구조의 데이터를 표현하는 데이터 타입
'''
df = pd.DataFrame(product_list)
df.columns = ['상품명', '가격', '좋아요', '이미지']

df.to_excel('D:\\tyn_dev\\workspace_pycham\\web-scrapping\\excel_files\\쿠팡로켓배송리스트.xlsx', index=False)


print('엑셀 저장 완료!')


