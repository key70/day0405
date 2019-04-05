#movies.dat
# 영화id::영화제목::장르
# movieid::title::genre
# 1::Toy Story (1995)::Animation|Children's|Comedy

#users.dat
#사용자id::성별::나이::직업::우편번호
#userid::gender::age::job::zipcode
# 1::F::1::10::48067

#rating.dat
#사용자id::영화id::별점::시간
#userid::movieid::rating::timestamp
# 1::1193::5::978300760

#연습
#3개의 파일을 읽어 들여 하나의 DataFrame으로 만들어 봅니다.


# help를 이용하여
# 파일을 읽어 들일때 컬럼헤더는 없어요 옵션을 설정하고
# 칼럼이름을 읽어들이때 movieId, title, genre 설정하도록 해 봅니다.

# help(pd.read_csv)

#나머지 두개의 파일도 위와 같은 방법으로
#읽어 들여 봅니다.



import numpy as np
import pandas as pd

# header='infer', names=None
movies = pd.read_csv("../ml-1m/movies.dat",sep="::",engine="python",
                     header=None,names=['movieid','title','genre'] )

# 1::F::1::10::48067
users = pd.read_csv("../ml-1m/users.dat",sep="::",engine="python",
                    header=None, names=['userid','gender','age','job','zipcode'])

# 1::1193::5::978300760
ratings = pd.read_csv("../ml-1m/ratings.dat",sep="::",engine="python",
                      header=None, names=['userid','movieid','rating','timestamp'])

# print(movies)
# 3880     3950  ...                           Drama
# 3881     3951  ...                           Drama
# 3882     3952  ...                  Drama|Thriller
#
# [3883 rows x 3 columns]


# print(users)
# 6037    6038      F   56    1   14706
# 6038    6039      F   45    0   01060
# 6039    6040      M   25    6   11106
#
# [6040 rows x 5 columns]


# print(ratings)
#
# 1000205    6040     1094       5  956704887
# 1000206    6040      562       5  956704746
# 1000207    6040     1096       4  956715648
# 1000208    6040     1097       4  956715569
#
# [1000209 rows x 4 columns]


#어떤 고객이 어떤영화에 대하여 어떤 평점을 내렸는지
#3개의 데이터프렘임을 하나로 합쳐봅시다.


#movies.dat
# movieid::title::genre


#users.dat
#userid::gender::age::job::zipcode

#rating.dat
#userid::movieid::rating::timestamp
# df  = pd.merge( pd.merge(movies,users), ratings)
# print(df)

# pandas.errors.MergeError:
# No common columns to perform merge on.
# Merge options: left_on=None, right_on=None, left_index=False, right_index=False


df =  pd.merge( pd.merge(movies, ratings), users)
# print(df)


# [1000209 rows x 10 columns]


print(df.head(1))










