#연습) student01과 student02의 파일의 내용을 읽어들여
#           각각 df1과 df2에 담아봅니다.

import numpy as np
import pandas as pd

df1 = pd.read_csv("../Data/student01", sep="::", engine="python")
# line terminate 은 engine이 c만가능해요        ==> 실험

df2 = pd.read_csv("../Data/student02", sep="::", engine="python")
# print(df1)
# print(df2)

df = pd.merge(df1, df2)
print(df)

