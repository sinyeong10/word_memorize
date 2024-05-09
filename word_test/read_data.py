#csv파일을 읽음
import pandas as pd
from datetime import datetime
from sys import stdin
import random

# n, k = 30, 1
def word_test(n, k):
    data_path = f'C:\sin\word_memorize\word_data\end_word\word_data.csv'
    existing_data = pd.read_csv(data_path)
    # print(existing_data.head())

    #정렬하여 인덱스로 찾아가서 해당 부분만 수정하기에 초기 데이터의 인덱스 순서는 불변함!!
    sorted_data = existing_data.sort_values(by=['value', '날짜'])
    # print(sorted_data.head())

    calculate_data = sorted_data.head(n*k)
    # print(calculate_data.shape)
    # print(calculate_data.head())
    # print(calculate_data.flags)
    for count in range(k):
        for i in range(count*n,(count+1)*n):
            row = calculate_data.iloc[i]
            print(f"{row['단어']}의 뜻은?")
            print("\n\n\n")
            tmp = stdin.readline().strip()
            print(row['뜻'])

            print("T,N,F로 맞춘 정도를 표시하시오 : ")
            tmp = stdin.readline().strip()
            print("\n\n\n")
            index = row['인덱스']
            # print(index)
            if row['단어'] != existing_data.loc[index-1, '단어']:
                print("error 발생!")
                print(f"{row['단어']}인데 {index}에서 {existing_data.loc[index-1, '단어']}가 적용됨!!")
            if tmp == "T" or tmp == "q":
                # print(existing_data.loc[index-1, '단어'], existing_data.iloc[index-1]['단어'])
                existing_data.loc[index-1, '날짜'] = datetime.now().strftime("%Y-%m-%d") #맞춘 날짜 갱신
                #후자는 안됨
                # existing_data.iloc[index-1]['날짜'] = datetime.now().strftime("%Y-%m-%d") #맞춘 날짜 갱신
                
                existing_data.loc[index-1, 'value'] += 30
            elif tmp == "N" or tmp == "w":
                existing_data.loc[index-1, 'value'] += 6
            elif tmp == "F" or tmp == "e":
                existing_data.loc[index-1, 'value'] += 3
                # tmp = stdin.readline().strip() #한번 쳐보면서 암기하기!
            else:
                print("일시 중지됨")
                existing_data.to_csv(data_path, index=False)
                print(f"{i+1}번까지 학습 끝")
                return
            # print(calculate_data.at[i, '단어']) #.at은 인덱스 기반으로 찾음! #여긴 없어서 에러!

            #A value is trying to be set on a copy of a slice from a DataFrame는 참조로 전체 중 일부를 가져왔기 때문에
            #수정이 일어날때 일부, 전체 중 어디에 수정해야할 지 몰라서 생기는 오류
            #EX) df[df['GROUP'] == 1]['VALUE'] = 10시 에러
            #df.loc[df['GROUP'] == 1, 'VALUE'] = 10 #원본 데이터 수정
            #copy를 활용해 #일부분 뽑은 데이터 수정
                
            # print((datetime.now()-datetime.strptime(calculate_data.iloc[i]['날짜'], "%Y-%m-%d")).days) #이전 학습일자와의 차이

        # existing_data.iloc[:n*k] = calculate_data
        # print(existing_data.head())

        existing_data.to_csv(data_path, index=False)
        print(f"{i+1}번까지 학습 끝")
    print("test end")
    # print(calculate_data.head())