#파이썬 머신러닝 판다스 데이터분석 1단원 정리

'''1-1 데이터과학자가 판다스를 배우는 이유
    데이터를 수집하고 분석이 가능한 형태로 정리하는 것이 데이터과학자가 하는 가장 중요한 일이기 때문'''

'''2 판다스 자료구조
   판다스: 시리즈와 데이터프레임이라는 구조화된 데이터 형식을 제공함
       시리즈: 1차원배열
       데이터프레임: 2차원배열
2-1 시리즈:  데이터가 순차적으로 나열된 1차원 배열의 형태
   -> 인덱스는 데이터 값과 일대일 대응이 됨 '''

#<예제 1-1> 딕셔너리 시리즈로 변환

import pandas as pd
dict_data = {'a' : 1, 'b' : 2, 'c' : 3}
sr_1 = pd.Series(dict_data)
print(type(sr_1))
print('\n')
print(sr_1)   #데이터 타입 : 정수형 (int 64)

'''인덱스 구조 (인덱수 종류): 정수형 위치 인덱스와 인덱스 이름
인덱스 속성 이용한 인덱스 배열 따로 선택하기: Series객체.index
데이터 값 배열 따로 선택하기 : Series객체.values'''

#<예제 1-2> 시리즈 인덱스 (리스트를 시리즈로 변환)

import pandas as pd
list_data = ['2023-01-26', 3.14, 'ABC', 100, True]
sr_2 = pd.Series(list_data)
print(sr_2)

idx = sr_2.index
val = sr_2.values
print(idx)
print('\n')
print(val)

'''원소선택: 인덱스를 이용하여 시리즈의 원소 선택
투플이나 리스트는 시리즈로 변환할 때 딕셔너리의 키에 해당하는 값이 없어서 정수형 위치 인덱스 자동 적용'''

#<예제 1-3> 시리즈 원소 선택 (투플을 시리즈로 변환)

import pandas as pd
tup_data = ('영인', '2023-01-26', '여', True)
sr_3 = pd.Series(tup_data, index = ['이름', '생년월일', '성별', '학생여부'])
print(sr_3)

#원소를 1개 선택
print(sr_3[0])  # sr의 1번째 원소를 선택 (정수형 위치 인덱스)
print(sr_3['이름'])   #'이름' 라벨을 가진 원소를 선택 (인덱스 이름)

#여러 개의 원소를 선택 (인덱스 리스트 활용)
print(sr_3[[1, 2]])
print('\n')
print(sr_3[['생년월일', '성별']])

#여러 개의 원소를 선택 (인덱스 범위 지정)
print(sr_3[1 : 2])
print('\n')
print(sr_3['생년월일': '성별'])

'''2-2 데이터프레임: 여러 개의 시리즈들이 한데 모여 데이터프레임을 이룸
여러 개의 열벡터들이 같은 행 인덱스를 기준으로 줄지어 결합된 2차원 벡터 또는 행렬임
행 인덱스: 개별 관측 대상에 대한 다양한 속성 데이터들의 모음
열 이름: 공통 속성을 갖는 일련의 데이터'''

'''데이터프레임 만들기: 딕셔너리의 여러 개의 시리즈(열)을 모아 놓은 집합으로,
딕셔너리의 값에 해당하는 각 리스트: 시리즈 배열로 변환되어 데이터프레임의 열이 됨
딕셔너리의 키: 시리즈의 이름으로 변환되어 데이터프레임의 열 이름이 됨'''

#<예제 1-4> 딕셔너리 -> 데이터프레임 변환

import pandas as pd
dict_data = {'c0': [1,2,3], 'c1': [4,5,6], 'c2': [7,8,9], 'c3': [10,11,12], 'c4': [13,14,15]}
df_1 = pd.DataFrame(dict_data)
print(type(df_1))
print('\n')
print(df_1)

'''행 인덱스/열 이름 설정
pandas.DataFrame (2차원 배열, index=행 인덱스 배열, columns=열 이름 배열)'''

#<예제 1-5> 행 인덱스/열 이름 설정

import pandas as pd
df_2 = pd.DataFrame([[15, '남', '덕영중'], [17, '여', '수리중']], index = ['준서', '예은'], columns = ['나이', '성별', '학교'])
print(df_2)
print('\n')
print(df_2.index)   #행 인덱스
print('\n')
print(df_2.columns) #열 이름

'''행 인덱스 변경: DataFrame 객체.rename(index={기존 인덱스: 새 인덱스, ...})
열 이름 변경: DataFrame 객체.rename(columns={기존 이름: 새 이름, ...})'''

#<예제 1-6> 행 인덱스/열 이름 변경

import pandas as pd
df_3 = pd.DataFrame([[15, '남', '덕영중'], [17, '여', '수리중']], index = ['준서', '예은'], columns = ['나이', '성별', '학교'])
print(df_3)
print('\n')

df_3.rename(columns={'나이' : '연령', '성별' : '남녀', '학교' : '소속'}, inplace=True)
df_3.rename(index={'준서' : '학생1', '예은' : '학생2'}, inplace=True)
print(df_3)

'''행 삭제: DataFrame 객체.drop (행 인덱스 또는 배열, axis=0)
열 삭제: DataFrame 객체.drop (열 이름 또는 배열, axis=1)'''

#<예제 1-7> 행 삭제 

import pandas as pd
exam_data = {'수학' : [90, 80, 70], '영어' : [98, 89, 95], '음악' : [85, 95, 100], '체육' : [100, 90, 90]}
df_4 = pd.DataFrame(exam_data, index = ['서준', '우현', '인아'])
print(df_4)
print('\n')

df_5 = df_4[:]
df_5.drop('우현', inplace=True)
print(df_5)
print('\n')

df_6 = df_4[:]
df_6.drop(['우현', '인아'], axis=0, inplace=True)
print(df_6)

#<예제 1-8> 열 삭제 

import pandas as pd
exam_data = {'수학' : [90, 80, 70], '영어' : [98, 89, 95], '음악' : [85, 95, 100], '체육' : [100, 90, 90]}
df_7 = pd.DataFrame(exam_data, index = ['서준', '우현', '인아'])
print(df_7)
print('\n')

df_8 = df_7[:]
df_8.drop('수학', axis=1, inplace=True)
print(df_8)
print('\n')

df_9=df_7[:]
df_9.drop(['영어', '음악'], axis=1, inplace=True)
print(df_9)

'''행 선택
탐색 대상: 인덱스 이름 -> loc 사용 (범위 지정시 범위의 끝 포함)
탐색 대상: 정수형 위치 인덱스 -> iloc (범위 지정시 범위의 끝 제외)'''

#<예제 1-9> 행 선택 

import pandas as pd
exam_data = {'수학' : [90, 80, 70], '영어' : [98, 89, 95], '음악' : [85, 95, 100], '체육' : [100, 90, 90]}
df_10 = pd.DataFrame(exam_data, index=['서준', '우현', '인아'])
print(df_10)
print('\n')

#행 인덱스 사용하여 행 1개 선택
labell = df_10.loc['서준']
position1 = df_10.iloc[0]
print(labell)
print('\n')
print(position1)

#행 인덱스 사용하여 2개 이상의 행 선택
label2 = df_10.loc[['서준', '우현']]
position2 = df_10.iloc[[0, 1]]
print(label2)
print('\n')
print(position2)

#행 인덱스의 범위를 지정하여 행 선택
label3 = df_10.loc['서준' : '우현']
position3 = df_10.iloc[0:1]
print(label3)
print('\n')
print(position3)

'''열 선택
열 1개 선택(시리즈 생성): DataFrame 객체['열 이름'] 또는 DataFrame 객체.열 이름
열 n개 선택(데이터 프레임 생성): DataFrame 객체.[[열1, 열2, ..., 열n]]'''

#<예제 1-10> 열 선택

import pandas as pd
exam_data = {'이름' : ['서준', '우현', '인아'], '수학' : [90, 80, 70], '영어': [98, 89, 95], '음악' : [85, 95, 100], '체육' : [100, 90, 90]}
df_11 = pd.DataFrame(exam_data)
print(df_11)
print(type(df_11))
print('\n')

math1 = df_11['수학'] #'수학' 점수 데이터만 선택. 변수 math1에 저장
print(math1)
print(type(math1))
print('\n')

english = df_11.영어  #'영어' 점수 데이터만 선택. 변수 english에 저장
print(english)
print(type(english))

music_gym = df_11[['음악', '체육']] #'음악', '체육' 점수 데이터를 선택. 변수 music_gym에 저장
print(music_gym)
print(type(music_gym))
print('\n')

math2 = df_11[['수학']]
print(math2)
print(type(math2))
print('\n')

'''범위 슬라이싱 활용: DataFrame 객체.iloc[시작 인덱스 : 끝 인덱스 : 슬라이싱 간격]
ex1) 데이터 프레임 df의 모든 행에 대하여 0행부터 2행 간격으로 선택하려면 df.iloc[: : 2]라고 입력
ex2) 데이터 프레임 df의 0헹부터 2행까지 2행 간격으로 선택하려면 df.iloc [0 : 3 : 2]라고 입력
ex3) 데이터 프레임 df의 모든 행을 선택하여 역순으로 정렬하려면 df.iloc[: : -1]라고 입력'''

df_12 = df_11.iloc[: : -1]
print(df_12)
print(type(df_12))



