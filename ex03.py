import numpy as np
import pandas as pd

# sep=',', delimiter=None
df = pd.read_csv("../Data/student",sep="::", engine="python")
# df = pd.read_csv("../Data/student",delimiter="::", engine="python")
print(df)

#help를 이용하여
#파일의 내용을 :으로 구분하여
#바람직하게 읽어들이도록 합니다

# help(pd.read_csv)


#서로 관련있는 두개의 데이터파일을 읽어들여
#하나의 데이터프레임으로 만들어 봅시다.

