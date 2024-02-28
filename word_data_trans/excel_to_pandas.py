import pandas as pd
path = 'C:\\Users\\cbrnt\\Desktop\\영단어.xlsx'

# 엑셀 파일 읽기
excel_data = pd.read_excel(path, usecols=range(5), header=0).dropna() #결측치 행은 패스

# 데이터 확인
# print(excel_data.tail())
# print(excel_data.shape)

#초기 가중치는 100
value = [100] * excel_data.shape[0]
excel_data.insert(0, "value", value)
# print(excel_data.tail())

from datetime import datetime

# 현재 날짜 및 시간 가져와 데이터 생성
today = datetime.now().strftime('%Y-%m-%d')

excel_data.to_csv(f'word_data\\word_data_{today}.csv', index=False)