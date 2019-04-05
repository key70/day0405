import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# 연습)
# 수학점수가 평균이하인 모든학생의
# 	성적을 막대그래프로 나타내 봅니다.


df = pd.read_csv("../Data/scores.csv")
# print(df)
# 데이터의 수가 너무 많을때 전체를 파악하기가 어려워요
# 앞에서 몇개만 파악한다던지 끝에서 몇개만 추출하여
# 아~ 데이터가 이렇게 생겼구나 라고 파악할 수 있어요.
#
# print(df.head())        #앞에서 5개만 뽑아줘
# print(df.tail())        #뒤에서 5개만 뽑아줘


# 컬럼의 수가 너무 많을때는 head() 5개만 뽑아 왔는데도
# 정신이 없을 수 있어요. 이때는 앞에 데이터 하나만 뽑아와서
# 데이터의 성격을 파악하고 싶어요
# print(df.head(1))
# print(df.tail(1))

#학생의 이름을 key로 설정해요
df.index = df['name']

#name칼럼을 삭제해요
del df['name']

print(df)


#수학점수의 평균을 계산해요
mean_math = df['mat'].mean()
print(mean_math)


#학생들 중에 수학점수가 평균(78) 이하인 학생들의 정보를 추출
lower_mean = df[ df['mat'] <= mean_math  ]
print(lower_mean)

lower_mean[['kor','eng','mat','bio']].plot(kind="bar", colormap="Oranges")
plt.show()



#연습)
#   help를 참고하여
#       막대그래프의 색상을 변경해 봅니다.

# print(plt.colormaps())
# print(len(plt.colormaps()))

'''['Accent', 'Accent_r', 'Blues', 'Blues_r', 'BrBG', 'BrBG_r', 'BuGn', 'BuGn_r', 'BuPu', 'BuPu_r', 'CMRmap', 'CMRmap_r', 'Dark2', 'Dark2_r', 'GnBu', 'GnBu_r', 'Greens', 'Greens_r', 'Greys', 'Greys_r', 'OrRd', 'OrRd_r', 'Oranges', 'Oranges_r', 'PRGn', 'PRGn_r', 'Paired', 'Paired_r', 'Pastel1', 'Pastel1_r', 'Pastel2', 'Pastel2_r', 'PiYG', 'PiYG_r', 'PuBu', 'PuBuGn', 'PuBuGn_r', 'PuBu_r', 'PuOr', 'PuOr_r', 'PuRd', 'PuRd_r', 'Purples', 'Purples_r', 'RdBu', 'RdBu_r', 'RdGy', 'RdGy_r', 'RdPu', 'RdPu_r', 'RdYlBu', 'RdYlBu_r', 'RdYlGn', 'RdYlGn_r', 'Reds', 'Reds_r', 'Set1', 'Set1_r', 'Set2', 'Set2_r', 'Set3', 'Set3_r', 'Spectral', 'Spectral_r', 'Wistia', 'Wistia_r', 'YlGn', 'YlGnBu', 'YlGnBu_r', 'YlGn_r', 'YlOrBr', 'YlOrBr_r', 'YlOrRd', 'YlOrRd_r', 'afmhot', 'afmhot_r', 'autumn', 'autumn_r', 'binary', 'binary_r', 'bone', 'bone_r', 'brg', 'brg_r', 'bwr', 'bwr_r', 'cividis', 'cividis_r', 'cool', 'cool_r', 'coolwarm', 'coolwarm_r', 'copper', 'copper_r', 'cubehelix', 'cubehelix_r', 'flag', 'flag_r', 'gist_earth', 'gist_earth_r', 'gist_gray', 'gist_gray_r', 'gist_heat', 'gist_heat_r', 'gist_ncar', 'gist_ncar_r', 'gist_rainbow', 'gist_rainbow_r', 'gist_stern', 'gist_stern_r', 'gist_yarg', 'gist_yarg_r', 'gnuplot', 'gnuplot2', 'gnuplot2_r', 'gnuplot_r', 'gray', 'gray_r', 'hot', 'hot_r', 'hsv', 'hsv_r', 'inferno', 'inferno_r', 'jet', 'jet_r', 'magma', 'magma_r', 'nipy_spectral', 'nipy_spectral_r', 'ocean', 'ocean_r', 'pink', 'pink_r', 'plasma', 'plasma_r', 'prism', 'prism_r', 'rainbow', 'rainbow_r', 'seismic', 'seismic_r', 'spring', 'spring_r', 'summer', 'summer_r', 'tab10', 'tab10_r', 'tab20', 'tab20_r', 'tab20b', 'tab20b_r', 'tab20c', 'tab20c_r', 'terrain', 'terrain_r', 'twilight', 'twilight_r', 'twilight_shifted', 'twilight_shifted_r', 'viridis', 'viridis_r', 'winter', 'winter_r']'''
