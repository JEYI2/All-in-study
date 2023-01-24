# -*- coding: utf-8 -*-
"""
Created on Sun Jan 22 14:52:51 2023

@author: dkwodk
"""
#시리즈 연산 
#예제 1-21 시리즈 VS 숫자

#라이브러리 불러오기
import pandas as pd

# 딕셔너리 데이터로 판다스 시리즈 만들기
student1 = pd.Series({'국어':100 ,'영어':80,'수학':90}) #student1 변수. 
괄호 안 딕셔너리 데이터 -> 시리즈
print(student1)
#국어    100
#영어     80
#수학     90
#dtype: int64

print('\n')

#학생의 과목별 점수를 200으로 나누기
percentage = student1/200 
print(percentage) 
#국어    0.50 
#영어    0.40
#수학    0.45

print('\n') 

print(type(percentage)) #<class 'pandas.core.series.Series'>

'''시리즈 객체에 어떤 숫자를 덧셈뺄셈곱샘나눗셈(사칙연산) 하면 각각의 개별 원소에 
계산한 값을 시리즈 객체로 반환한다.'''
#%%

#예제1-22 시리즈 VS 시리즈

#라이브러리 불러오기
import pandas as pd

#딕셔너리 데이터로 판다스 시리즈 만들기
student1 = pd.Series({'국어':100 ,'영어':80,'수학':90})
student2 = pd.Series({'영어':80 ,'국어':90,'수학':80})

print(student1)
print('\n') 
print(student2)
print('\n') 

#두 학생의 점수로 사칙연산 수행
addition = student1 + student2 #덧셈
substraction = student1 - student2 #뺄셈
multipication = student1 * student2 #곱셈
division = student1 / student2 #나눗셈

print(type(division)) #<class 'pandas.core.series.Series'>
print(type(multipication)) #<class 'pandas.core.series.Series'>
print(type(substraction )) #<class 'pandas.core.series.Series'>
print(type(addition)) #<class 'pandas.core.series.Series'>
print('\n') 

#사칙연산 결과를 데이터프레임으로 합치기 (시리즈->데이터프레임)
result = pd.DataFrame([addition, substraction,multipication,division],
                      index=['덧셈','뺄셈','곱셈','나눗셈'])
print(result)
print(type(result)) #<class 'pandas.core.frame.DataFrame'>

'''판다스는 같은 인덱스를 찾아 정렬한 후 같은 인덱스의 데이터 값 끼리 사칙연산 수행
 1차원 배열의 값을 2차원 데이터 프레임으로 생성'''
#%%
#예제 1- 23 NaN 값이 있는 시리즈 연산
#판다스는 파이썬 데이터 처리를 위한 라이브러리
import pandas as pd 
#넘파이는 수치 데이터를 다루는 파이썬 패키지 수학적 연산을 하기 위한 라이브러리
import numpy as np #np.nan

#딕셔너리 데이터로 판다스 시리즈 만들기
student1 = pd.Series({'국어':np.nan,'영어':80,'수학':90})
student2 = pd.Series({'수학':80,'국어':90})

print(student1)
print('\n') 
#국어     NaN
#영어    80.0
#수학    90.0
print(student2)
print('\n') 
#수학    80
#국어    90

# 두 학생의 과목별 점수로 사칙연산 수행(시리즈 vs 시리즈)

addition = student1 + student2 #덧셈
substraction = student1 - student2 #뺄셈
multipication = student1 * student2 #곱셈
division = student1 / student2 #나눗셈
print(type(addition))
print('\n')

#사칙연산 결과를 데이터프레임으로 합치기(시리즈 -> 데이터프레임)
result = pd.DataFrame([addition,substraction,multipication,division],
                      index=['덧셈','뺄셈','곱셈','나눗셈'])
print(result)

#%%
#예제1 - 24 연산 메소드 사용
#라이브러리 불러오기
import pandas as pd
import numpy as np

#딕셔너리 데이터로 판다스 시리즈 만들기
student1 = pd.Series({'국어':np.nan,'영어':80,'수학':90})
student2 = pd.Series({'수학':80,'국어':90})

# 두 학생의 과목별 점수로 사칙연산 수행
# 연산 메소드 사용 : 시리즈1.add(시리즈2, fill_value=0)

sr_add = student1.add(student2, fill_value=0) #덧셈
sr_sub = student1.sub(student2, fill_value=0) #뺄셈
sr_mul = student1.mul(student2, fill_value=0) #곱셈
sr_div = student1.div(student2, fill_value=0) #나눗셈

#사칙연산 결과를 데이터프레임으로 합치기(시리즈->데이터프레임)


result= pd.DataFrame([sr_add,sr_sub,sr_mul,sr_div],index=['덧셈','뺄셈','곱셈','나눗셈'])
print(result)

  #     국어    수학     영어
#덧셈   90.0   170.000  80.0
#뺄셈  -90.0    10.000  80.0
#곱셈    0.0  7200.000   0.0
#나눗셈   0.0     1.125   inf
'''inf(무한대) student1(80) / student2(0)으로 나눈 값이기 때문이다.'''
#%%
#예제 1 - 25  데이터 프레임에 숫자 더하기
import pandas as pd 
import seaborn as sns
'''seaborn as 내장 데이터셋 종류 anscombc,ateention,brain_networks,car_crashes,diamonds,
dots,exercis,flights,fmri,gammas,iris,mpg,planets,tips,titanic'''

#titanic 데이터셋에서 age, fare 2개 열을 선택하여 데이터 프레임 만들기
titanic = sns.load_dataset('titanic')
print(titanic) 
print('\n')

df = titanic.loc[:,['age','fare']]
print(df.head()) # 첫 5행만 표시 0~4
print('\n')
print(type(df))

#데이터프레임에 숫자 10 더하기
addition = df + 10
print(addition.head())
print('\n')
print(type(addition))
#%%
#예제 1 - 26  데이터프레임 vs 데이터프레임 
'''같은 행과 열 동일한 위치의 원소끼리 사칙연산, 
어느 한쪽의 데이터값이 존재하지 않으면 NaN'''

import pandas as pd
import seaborn as sns

titanic = sns.load_dataset('titanic')
print(titanic) 
print('\n')

df = titanic.loc[:,['age','fare']]
print(df.tail()) # 마지막 5행만 표시 886~890
print('\n')
print(type(df))

# 데이터프레임끼리 연산하기 
# 데이터프레임에 숫자 10 더하기
addition = df + 10
print(addition.tail())
print('\n')
print(type(addition))
print('\n')

#데이터프레임끼리 연산하기(addition - df)
substraction = addition - df
print(substraction.tail())
print('\n')
print(type(substraction))
