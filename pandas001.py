import pandas as pd
# 반드시 as pd를 붙여야 함 : 룰이란다..

'''
DataFrame 이라는 구조의 데이터를 표현하는 데이터 타입
'''

excel_df = pd.read_excel('D:\\tyn_dev\\workspace_pycham\\web-scrapping\\excel_files\\미결제명단.xlsx', sheet_name="미결제명단")
print(excel_df)


csv_df = pd.read_csv("D:\\tyn_dev\\workspace_pycham\\web-scrapping\\csv_files\\2017.12.csv")
print(csv_df)
# 파이썬은 기본적으로 숫자는 숫자 타입으로 변경한다.
print(csv_df['수강금액'].sum)
# 80만원 이상 수강 금액인 사용자 수집
print(csv_df.loc[csv_df['수강금액'] >= 800000])
new_df = csv_df.loc[csv_df['수강금액'] >= 800000]


# 엑셀로 바로 변환이 가능
new_df.to_excel('D:\\tyn_dev\\workspace_pycham\\web-scrapping\\excel_files\\고액수강생.xlsx', index=False)