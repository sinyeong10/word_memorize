import pandas as pd

# 데이터프레임 생성 (예시)
data = {
    '이름': ['Alice', 'Bob', 'Charlie'],
    '나이': [25, 30, None],  # 데이터가 없는 열 포함
    '직업': ['Engineer', None, 'Artist']  # 데이터가 없는 열 포함
}
df = pd.DataFrame(data)

# 데이터프레임에서 데이터가 있는 열만 추출
df_filtered = df.dropna(axis=1, how='all')

print(df_filtered.head())