#연습) 고객파일, 영화파일, 별점파일을 읽어 들여
#           하나의 데이터프레임으로 반환하는 함수를 만들고 호출합니다.

import numpy as np
import pandas as pd

import movieUtil
df = movieUtil.getData()
# print(df.head(1))


#연습)남자의 평점의 평균을 출력
# a = df['gender']=='M'
# print(a)
# a = df[ df['gender'] == 'M']['rating'].mean()
# print(a)


#연습)여자의 평점의 평균을 출력

# b = df[ df['gender'] == 'F']['rating'].mean()
# print(b)


#연습) Toy Story (1995) 영화에 대한 평점의 평균을 출력
# c = df[df['title'] == 'Toy Story (1995)']['rating'].mean()
# print(c)
# 4.146846413095811

#연습) Toy Story (1995) 영화를 평가한 건수를 출력
# d = len( df[df['title'] == 'Toy Story (1995)'])
# print(d)
# 2077

#연습) Toy Story (1995) 영화를 평가한 사람들의 평균나이를 출력
# e = df[df['title']=='Toy Story (1995)']['age'].mean()
# print(e)
# 27.700529610014446

#연습) 평점5점을 받은 영화의 제목을 모두 출력합니다.
# f = df[ df['rating'] == 5 ]['title']
# print(f)


#연습) 평균 평점5점을 받은 영화의 제목을 모두 출력합니다.
#     영화제목별로 평점은 평균을 알고
#           그중에 평균값이 5점이상인 데이터를 출력

#       ===> group by
#   select title, avg(rating) from df group by title
#      ===> 이런결과를 얻기 위해서는 pivot_table을 이용합니다.


# help(pd.DataFrame.pivot_table)
#연습) 영화제목별로 평균을 평균을 출력해 봅니다.

g = df.pivot_table(values='rating', index='title', aggfunc='mean')
r  = g[g['rating']==5]
print(r)


#연습)
#적어도 100명이상이 평가한 영화중에
#평균평점이 5점인 영화가 있는지 조사해봅니다.


#연습)
#영화별 평가한 사람의 수를 출력해 봅니다.


#연습)
#영화별 평가한 사람의 수가 높은 100개의 영화중에
#평균평점이 가장 높은 5개의 영화제목를 출력

# select title, count(rating) from df group by title
a  = df.pivot_table(values='rating',index='title', aggfunc='count')
# b=a.sort_values(by="rating")[::-1]
b=a.sort_values(by="rating",ascending=False)
titles = b.iloc[:100].index
print(titles)

#원래데이터 중에 영화제목이 titles에 해당하는 영화들의
#평균평점이 가장 높은 상위 5개의 영화제목 출력

c = pd.DataFrame(titles,range(100))
d = pd.merge(df, c)
print(d)

e = d.pivot_table(values='rating', index='title',aggfunc='mean').sort_values(by="rating",ascending=False).head()
print(e)


#남자가 더 좋아하는 영화 5개를 뽑아 봅니다.
#여자가 더 좋아하는 영화 5개를 뽑아 봅니다.
#나이대별 평점의 평균
#나이대별 성별별 평점의 평균
#나이대별 평점이 가장 높은 영화를 뽑아봅니다.





















