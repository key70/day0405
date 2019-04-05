import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# data = pd.read_csv("/Data/scores.csv")
df = pd.read_csv("../Data/scores.csv")
# print(data)

#학생들중에 1반학생만 뽑아 오고 싶어요
#Pandas의 DataFrame에 추출할 행에 조건식을 부여할 수 있어요

#df으로 부터 class 컬럼의 속성이 1인지 판별하여 boolean Array를 뽑아와요
# arr_1 = df['class']==1
# print(arr_1)
# class_1 =  df[arr_1]
# print(class_1)


#연습
#1반학생의 과목별 평균을 출력해 봅니다.
class_1 = df[  df['class'] == 1   ]
del class_1['class']
class_1.index = class_1['name']
del class_1['name']
print(class_1)
# print(class_1.mean())       #데이터분석에서는 "열", "특성"을 중요하게 생각해요
# print(class_1.mean(axis=1)) #학생별 평균, "행"으로 평균을 원한다면 axis=1

#연습
#1반학생들의 국어점수를 막대그래프로 나타내 봅니다.
# plt.bar(range(len(class_1.index)), class_1['kor'] )
# plt.xticks(range(len(class_1.index)), class_1.index  )
# plt.show()

# class_1.plot()
class_1.plot(kind='bar')
# class_1.plot(kind='bar',colormap='viridis')
# class_1.plot(kind='barh')
# class_1.plot(kind='box')
# class_1.plot(kind='line')
# class_1.plot(kind='hist')
# class_1.plot(kind='area')
# class_1.plot(kind='scatter')
plt.show()

# help( pd.DataFrame.plot  )      #Pandas라이브러리의 DataFrame이 제공하는 plot함수에 대한 도움말


# kind : str
#  |          - 'line' : line plot (default)
#  |          - 'bar' : vertical bar plot
#  |          - 'barh' : horizontal bar plot
#  |          - 'hist' : histogram
#  |          - 'box' : boxplot
#  |          - 'kde' : Kernel Density Estimation plot
#  |          - 'density' : same as 'kde'
#  |          - 'area' : area plot
#  |          - 'pie' : pie plot
#  |          - 'scatter' : scatter plot
#  |          - 'hexbin' : hexbin plot










