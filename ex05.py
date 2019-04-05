#합치고자 하는 두개의 파일에
#데이터 수가 일치하지 않아요
#dan 학생의 점수정보는 없어요


import numpy as np
import pandas as pd

df1 = pd.read_csv("../Data/stu01", sep="::", engine="python")
df2 = pd.read_csv("../Data/stu02", sep="::", engine="python")


# 서로 일치 하지 않는 데이터
# dan의 정보도 나타내 봅니다. 그 학생의 점수는 0으로 출력합니다.


# help(pd.merge)

# how : {'left', 'right', 'outer', 'inner'}, default 'inner'
df = pd.merge(df1, df2, how="outer")
# df.fillna(0)   #결측치를 0으로 채워줘
# print(df)

# help(pd.merge)
# help(pd.fillna)

df.fillna(0, inplace=True)
print(df)






