from sys import stdin
from word_data_trans.excel_to_pandas import add_data
from word_test.read_data import word_test

print("데이터 추가 : add\n학습은 바로 enter")
order = stdin.readline().strip()

first = False
if first:
    first_data_path = 'C:\\sin\\word_memorize\\word_data\\end_word\\초영단어.xlsx'
    second_data_path = 'C:\\sin\\word_memorize\\word_data\\end_word\\중영단어.xlsx'
    add_data(first_data_path)
    add_data(second_data_path)

if order == "add":
    print("없으면 enter 입력")
    new_data_path = stdin.readline().strip()
    while new_data_path != "":
        print(new_data_path,"가 입력됨", sep="")
        # add_data(new_data_path)
        new_data_path = stdin.readline().strip()

elif order == "":
    print("몇개를 몇 번 학습할지 입력하시오")
    count = stdin.readline().strip()
    if count == "":
        n, k = 10, 5
    else:
        n, k = list(map(int, count.split()))
    word_test(n, k)

print("종료 됨")

import time
import sys
# 10초 대기
time.sleep(3)

# 프로그램 종료
sys.exit()