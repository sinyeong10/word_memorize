import pandas as pd
import os


def add_data(new_data_path):
    # 엑셀 파일 읽기
    excel_data = pd.read_excel(new_data_path, usecols=range(5), header=0).dropna() #결측치 행은 패스

    # 데이터 확인
    # print(excel_data.tail(10))
    # print(excel_data.shape)

    #초기 가중치는 0
    value = [0] * excel_data.shape[0]
    excel_data.insert(0, "value", value)
    # print(excel_data.tail(10))

    data_path = f'word_data\\end_word\\word_data.csv'
    if not os.path.exists(data_path):
        excel_data.to_csv(data_path, index=False)
    else:
        existing_data = pd.read_csv(data_path)
        last_index = existing_data.index[-1]+1 if not existing_data.empty else 0 #1부터 시작함!
        # print(last_index)
        # print(existing_data.tail(10))
        excel_data["인덱스"] += last_index
        # print(excel_data.head(10))
        excel_data.to_csv(data_path, mode='a', header=False, index=False)
        
    # from datetime import datetime

    # # 현재 날짜 및 시간 가져와 데이터 생성
    # today = datetime.now().strftime('%Y-%m-%d')

    # excel_data.to_csv(f'word_data\\word_data_{today}.csv', index=False)
    print("end")