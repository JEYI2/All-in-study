#%% 시리즈 만들기

'''시리즈: 1차원 배열
(한 데이터 값에 대해 인덱스가 1개)

인덱스와 데이터 값의 관계 = 딕셔너리의 키와 데이터 값의 관계
딕셔너리: {k:v}의 형태, k = 키, v = 데이터 값. ex){'Mercury City Tower': 339.}
딕셔너리를 시리즈로 변환: 함수 Series()'''

#예제1-1: 딕셔너리를 시리즈로 변환
import pandas as pd
dict_data = {'a':1, 'b':3, 'c':5}
sr_1 = pd.Series(dict_data)
print(dict_data)
print('\n') #공백
print(sr_1) #데이터 값 자료형(dtype) = 정수형(in64)


#%% 인덱스 구조

'''인덱스: 정수형 "위치" 인덱스 or 인덱스 이름
sr_1 -> a: 정수형 위치 인덱스 = 0, 인덱스 이름 = a'''

#예제1-2: 시리즈의 인덱스 또는 데이터 값만 불러오기
import pandas as pd
list_data = ['2019-01-02', 3.14, 'ABC', 100, True]
sr_2 = pd.Series(list_data) #리스트를 시리즈로 변환
print(sr_2)
print('\n')
idx = sr_2.index
val = sr_2.values
print(idx)
print('\n')
print(val)
print('\n')
print(sr_1.index)


#%% 원소 선택

#데이터 값 선택
print(sr_1)
print('\n')
print(sr_1[1]) #정수형 위치 인덱스
print('\n')
print(sr_1[[0,1,2]])
print('\n')
print(sr_1[0:2])
print('\n')

print(type(sr_1[1])) #데이터 값 출력(int64)
print('\n')
print(type(sr_1[[0,1,2]])) #인덱스, 데이터 값 출력(series)
print('\n')

print(sr_1['a']) #인덱스 이름
print('\n')
print(sr_1[['a','b']])
print('\n')
print(sr_1['a':'c'])
print('\n')

#예제1-3
import pandas as pd
tup_data = ('영인', '2010-05-01', '여', True)
sr_3 = pd.Series(tup_data, index = ['이름', '생년월일', '성별', '학생여부']) 
#튜플을 시리즈로 변환, 인덱스 지정
print(sr_3)
print('\n')
print('영인' == sr_3[0] == sr_3['이름']) #정수형 위치 인덱스, 인덱스 이름 비교
print('\n')
print(sr_3[[2,3]])
print('\n')
print(sr_3['이름':'학생여부']) #끝 포함


#%% 데이터프레임 만들기

'''데이터프레임: 2차원 배열 <- 여러 개의 시리즈들(열벡터들). 행과 열로 구성
(한 데이터 값에 인덱스가 2개)'''

#예제1-4 딕셔너리를 데이터프레임으로 변환
import pandas as pd
dict_data = {'c0':[1,2,3], 'c1':[4,5,6], 'c2':[7,8,9] , 'c3':[10,11,12]} #리스트가 열이 됨
df_1 = pd.DataFrame(dict_data)
print(type(df_1))
print('\n')
print(df_1) # 열 이름: c0, c1, c2, c3 / 행 인덱스: 0, 1, 2
print('\n')

sr = pd.Series(dict_data)
print(sr)


#%% 행 인덱스/열 이름 설정

#예제1-5 2차원 배열을 데이터프레임으로 변환, 행 인덱스/ 열 이름 설정
import pandas as pd
two_dim = [[15,'남','덕영중'], [17,'여', '수리중']] #2차원 배열(리스트를 원소(한 행)로 갖는 리스트)
df_2 = pd.DataFrame(two_dim, index=['준서', '예은'], columns=['나이', '성별', '학교'])
print(two_dim)
print('\n')
print(df_2)
print('\n')
print(df_2.index) #행 인덱스
print('\n')
print(df_2.columns) #열 이름
print('\n')
type((df_2.index))
#행 인덱스/열 이름 변경하기
df_2.index = ['학생1', '학생2']
df_2.columns = ['연령', '남녀', '소속']
print(df_2) #원본 객체 변경
print('\n')
print(df_2.index) 
print('\n')
print(df_2.columns) 
print('\n')
type((df_2.index)) 

#예제1-6 행 인덱스/열 이름 일부 변경(rename()) -> 원본 객체 변경X, 새로운 데이터프레임 반환
print(df_2)
print('\n')
df_3 = df_2.rename(columns={'남녀':'성별'}) #새로운 데이터프레임
df_4 = df_2.rename(index={'학생1':'준서'}) #새로운 데이터프레임
print(df_2)
print('\n')
print(df_3)
print('\n')
print(df_4)
print('\n')
df_2.rename(columns={'남녀':'성별'},inplace=True) 
df_2.rename(index={'학생1':'준서'},inplace=True)
#inplace=True: 원본 객체 변경
print(df_2)


#%% 행/열 삭제

'''drop() ->  원본 객체 변경X, 새로운 객체 반환, inplace=True를 통해 원본 객체 변경 (False -> 원본 객체 변경X)
행 삭제 -> axis=0 또는 생략 / 열 삭제 -> axis=1 / 동시 삭제 -> 라스트 형태'''

#예제1-7 행 삭제
import pandas as pd
exam_data = {'수학':[90,80,70], '영어':[98,89,95], '음악':[85,95,100], '체육':[100,90,90]} #딕셔너리 셍성
df_5 = pd.DataFrame(exam_data, index=['서준','우현','인아']) #딕셔너리를 데이터프레임으로 변환, 행 인덱스 지정
print(df_5)
print('\n')
df_6 = df_5[:] #df_5를 복제하여 df2에 저장(df_5를 변경시키지 않기 위해)
df_6.drop('우현',inplace=True) #df_6의 행 1개 삭제, axis 생략
print(df_6)
print('\n')
df_7 = df_5[:]
df_7.drop(['우현','인아'],axis=0,inplace=True) #df_7의 행 2개 삭제
print(df_7)
print('\n')

df_8 = df_5[:]
df_8.drop('서준',axis=0) #열 1개 삭제, 새로운 객체 반환(기존 변수에 저장하여 대체됨-??)
print(df_8) #변경X
print('\n')
df_9 = df_8.drop('인아',axis=0) #열 1개 삭제, 새로운 객체 반환(새로운 변수에 저장)
print(df_8)
print('\n')
print(df_9)
print('\n')

#예제1-8 열 삭제
import pandas as pd
exam_data = {'수학':[90,80,70], '영어':[98,89,95], '음악':[85,95,100], '체육':[100,90,90]} #딕셔너리 셍성
df_5 = pd.DataFrame(exam_data, index=['서준','우현','인아']) #딕셔너리를 데이터프레임으로 변환, 행 인덱스 지정
print(df_5)
print('\n')
df_10 = df_5[:]
df_10.drop('수학',axis=1,inplace=True)
print(df_10)
print('\n')
df_11 = df_5[:]
df_11.drop(['영어','음악'],axis=1,inplace=True)
print(df_11)


#%% 행 선택

#인덱스 이름 -> loc (끝 포함) / 정수형 위치 인덱스 -> iloc (끝 제외)

#예제1-9
import pandas as pd
exam_data = {'수학':[90,80,70], '영어':[98,89,95], '음악':[85,95,100], '체육':[100,90,90]} #딕셔너리 셍성
df_5 = pd.DataFrame(exam_data, index=['서준','우현','인아']) #딕셔너리를 데이터프레임으로 변환, 행 인덱스 지정
print(df_5)
print('\n')
label_1 = df_5.loc['서준'] #1개 선택
positional_1 = df_5.iloc[0]
print(label_1)
print('\n')
print(positional_1)
print('\n')
label_2 = df_5.loc[['서준','우현']] #2개 선택
positional_2 = df_5.iloc[[0,1]]
print(label_2)
print('\n')
print(positional_2)
print('\n')
label_3 = df_5.loc['서준':'우현'] #여러 개 선택, 슬라이싱 기법, loc -> 끝 포함
positional_3 = df_5.iloc[0:1] #iloc -> 끝 제외
print(label_3) 
print('\n')
print(positional_3)  


#%% 열 선택

#예제1-10
import pandas as pd
exam_data2 = {'이름':['서준','우현','인아'],\
              '수학':[90,80,70],\
              '영어':[98,89,95],\
              '음악':[85,95,100],\
              '체육':[100,90,90]}
df1 = pd.DataFrame(exam_data2)
print(df1)
print('\n')
math1 = df1['수학'] #대괄호([]) -> 1개 선택, 대괄호 안에
print(math1)
print(type(math1)) #시리즈
print('\n')
english = df1.영어 #도트(.) -> 1개 선택, 열 이름이 문자열일 경우에만 가능
print(english)
print(type(english)) #시리즈
print('\n')
music_gym = df1[['음악','체육']] #2개 선택 -> 대괄호 안에 리스트
print(music_gym)
print(type(music_gym)) #데이터프레임
print('\n')
math2 = df1[['수학']] #1개 선택, type: 데이터프레임
print(math2) 
print(type(math2))
print('\n')

'''슬라이싱 [i:j:k]
i: 시작 인덱스, 생략 시 처음부터
j: 끝 인덱스, j-1까지 슬라이싱, 생략 시 마지막까지
k: 간격, 생략 시 1, 음수이면 역순으로'''

import pandas as pd
exam_data2 = {'이름':['서준','우현','인아'],\
              '수학':[90,80,70],\
              '영어':[98,89,95],\
              '음악':[85,95,100],\
              '체육':[100,90,90]}
df1 = pd.DataFrame(exam_data2)
print(df1)
print('\n')
print(df1.iloc[::2])
print('\n')
df1.iloc[0:3:2] == df1.iloc[::2]


#%% 원소 선택

'''데이터프레임에서 원소 선택
위치 지정 -> [행 인덱스, 열 이름]
인덱스 이름 -> DataFrame 객체.loc[행 인덱스, 열 이름]
정수형 위치 인덱스 -> DataFrame 객체.iloc[행 번호, 열 번호]

행 1개, 열 1개 -> 원소 1개 반환
행 2개 이상, 열 1개 또는 행 1개, 열 2개 이상 선택 -> 시리즈 반환
행 2개 이상, 열 2개 이상 -> 데이터프레임 반환'''

#예제1-11
import pandas as pd
exam_data = {'이름':['서준','우현','인아'],\
              '수학':[90,80,70],\
              '영어':[98,89,95],\
              '음악':[85,95,100],\
              '체육':[100,90,90]} 
df = pd.DataFrame(exam_data) #딕셔너리를 데이터프레임으로 변환, 변수 df에 저장
print(df)
print('\n')
df.set_index('이름',inplace=True) #'이름' 열을 새로운 인덱스로 지정(새로운 객체 반환), 원본 객체 변경
# 또는 df = df.set_index('이름')
print(df)
print('\n')

#원소 1개
a = df.loc['우현','영어'] #인덱스 이름
print(a)
b = df.iloc[1,1] #정수형 위치 인덱스
#'우현' 행의 정수형 위치 인덱스를 2로 착각
print(b)
print('\n')

#시리즈
c = df.loc['우현',['수학','체육']] #인덱스 이름, 2개 이상 -> 리스트 형태
print(c)
print('\n')
d = df.iloc[1,[0,3]] #정수형 위치 인덱스
print(d)
print('\n')
e = df.loc['우현','수학':'체육'] #슬라이싱 기법, loc -> 끝 포함. ref)행 선택
print(e)
print('\n')
f = df.iloc[1,0:4:] #슬라이싱 기법, iloc -> 끝 제외
print(f)
print('\n')

#데이터프레임
g = df.loc[['우현','인아'],['수학','영어']] #인덱스 이름
print(g)
print('\n')
h = df.iloc[[1,2],[0,1]] #정수형 위치 인덱스
print(h)
print('\n')
i = df.loc['우현':'인아','수학':'영어'] #인덱스 이름, 슬라이싱 기법
print(i)
print('\n')
j = df.iloc[1:3,0:2] #정수 위치 인덱스형, 슬라이싱 기법
print(j)
print('\n')
#------------------------------------------------------------------------------

#열 선택 
col1 = df.loc[:,['음악','체육']] #: -> 슬라이싱, 시작/끝 인덱스 생략 -> 처음부터 끝까지
col2 = df[['음악','체육']] #cf)열 선택
print(col1)
print('\n')
print(col2)


#%% 열 추가

'''DataFrame 객체['추가하려는 열 이름'] = 데이터 값
cf)열 선택 DataFrame['열 이름']'''
    
#예제1-12
import pandas as pd
exam_data = {'이름':['서준','우현','인아'],\
              '수학':[90,80,70],\
              '영어':[98,89,95],\
              '음악':[85,95,100],\
              '체육':[100,90,90]} 
df = pd.DataFrame(exam_data)
print(df)
print('\n')

df['국어'] = 80 #'국어' 열 추가, 데이터 값 = 80, 80, 80
print(df) #밀림
print('\n')
print(df['국어'])
print('\n')

df['미술'] = [100,90,80] #리스트 형태, 데이터 값 = 100, 90, 80
print(df)
print('\n')

#열 이름이 기존 인덱스와 중복되는 경우 새로운 열을 추가하지 않고 기존 열의 원소값 변경
df['미술'] = [0,0,0]
print(df)


#%% 행 추가

'''DataFrame 객체.loc['새로운 행 이름'] = 데이터 값
cf)행 선택 -> DataFrame 객체.loc['행 인덱스']/DataFrame 객체.iloc['행 인덱스']
    
행 이름이 기존 인덱스와 중복되는 경우 새로운 행을 추가하지 않고 기존 행의 원소값 변경'''

#예제1-13
import pandas as pd
exam_data = {'수학':[90,80,70],\
             '영어':[98,89,95],\
             '음악':[85,95,100],\
             '체육':[100,90,90]}
df = pd.DataFrame(exam_data,index=['서준', '우현','인아'])
print(df)
print('\n')
df.loc['준서'] = [100,100,100,100] #'준서' 행 추가, 데이터 값 = 100, 100, 100, 100
print(df)
print('\n')
#------------------------------------------------------------------------------

#행 이름이 기존 인덱스와 중복되는 경우 새로운 행을 추가하지 않고 기존 행의 원소값 변경
df.loc['서준'] = [90,90,90,90] 
print(df)
#%% 원소 값 변경

'''DataFrame 원소 = 새로운 값
원소 선택 -> 인덱스 이름 -> DataFrame 객체.loc[행 인덱스, 열 이름]
            정수형 위치 인덱스 -> DataFrame 객체.iloc[행 번호, 열 번호]'''

#예제1-12
import pandas as pd
exam_data = {'이름':['서준','우현','인아'],\
              '수학':[90,80,70],\
              '영어':[98,89,95],\
              '음악':[85,95,100],\
              '체육':[100,90,90]} 
df = pd.DataFrame(exam_data)
print(df)
print('\n')
df.set_index('이름',inplace=True) #'이름' 열을 새로운 인덱스로 지정, 원본 객체 변경
print(df)
print('\n')

#원소 1개 선택
df.iloc[0,3] = 0 #df.iloc[0][3]
print(df)
print('\n')

df.loc['서준','체육'] = 100 #df.loc['서준']['체육']
print(df)
print('\n')

#여러 개 원소 선택
df.loc['서준',['수학','음악']] = [100,0] #2개 이상 -> 리스트 형태
print(df)
print('\n')
df.iloc[0,0:4] = 0 #슬라이싱, iloc 끝 제외
print(df)


#%% 행, 열의 위치 바꾸기

'''DataFrame 객체.transpose() 또는 DataFrame 객체.T
원본 객체 변경X, 새로운 객체 반환'''

#예제1-15
import pandas as pd
exam_data = {'이름':['서준','우현','인아'],\
              '수학':[90,80,70],\
              '영어':[98,89,95],\
              '음악':[85,95,100],\
              '체육':[100,90,90]} 
df = pd.DataFrame(exam_data)
print(df) #열 이름: 이름, 수학, 영어, 음악, 체육 / 행 이름: 0, 1, 2
print('\n')

df = df.transpose() #새로운 객체를 원래 변수에 저장(원본 객체 변경)
print(df)
print('\n') #행 이름: 이름, 수학, 영어, 음악, 체육 / 열 이름: 0, 1, 2

df = df.T
print(df)
print('\n')
#------------------------------------------------------------------------------

#print(df)
#print('\n')
#df.transpose(inplace=True)
#print(df)


#%% 특정 열을 행 인덱스로 설정


'''DataFrame 객체.set_index(['열 이름']) 또는 DataFrame 객체.set_index('열 이름')
새로운 객체 반환, 원본 객체 변경X
원본 객체 변경 -> inplace=True

행 인덱스를 새로 지정하면 기존 행 인덱스는 삭제됨'''

#예제 1-16
import pandas as pd
exam_data = {'이름':['서준','우현','인아'],\
              '수학':[90,80,70],\
              '영어':[98,89,95],\
              '음악':[85,95,100],\
              '체육':[100,90,90]} 
df = pd.DataFrame(exam_data)
print(df) 
print('\n')

ndf = df.set_index(['이름']) #'이름' 열을 행 인덱스로 설정
print(ndf)
print('\n')
ndf2 = ndf.set_index('수학') #기존에 있던 '이름' 행 인덱스는 삭제됨
print(ndf2)
print('\n')

ndf3 = df.set_index('수학','영어') #X
print(ndf3)
print('\n')
ndf4 = df.set_index(['수학','영어']) #2개 이상 -> 리스트 형태(대괄호 사용)
print(ndf4)
print('\n')


#%% 행 인덱스 재배열

'''DataFrame 객체.reindex(새로운 인덱스 배열)
새로운 객체 반환'''

#예제1-17
import pandas as pd
dict_data = {'c0':[1,2,3], 'c1':[4,5,6],'c2' :[7,8,9], 'c3':[10,11,12], 'c4':[13,14,15]}
df = pd.DataFrame(dict_data, index=['r0','r1','r2'])
print(df)
print('\n')

new_index = ['r0','r1','r2','r3','r4'] #기존 데이터프레임에 존재하지 않는 행 인덱스가 추가되는 경우
ndf = df.reindex(new_index)             #그 행의 데이터 값에 NaN 값이 입력
print(ndf)
print('\n')

new_index = ['r0','r1','r2','r3','r4'] 
ndf2 = df.reindex(new_index,fill_value=0) #fill_value -> NaN값 채우기
print(ndf2)  
print('\n')
#------------------------------------------------------------------------------

df.index = ['r0','r1','r2','r3','r4'] #길이가 같을 떄에만 사용
print(df)

new_index = ['r0','r1','r2','r3','r4'] 
#ndf2 = df.reindex(new_index,fill_value=[[16,17,18,19,20],[21,22,23,24,25]]) #NaN값 각각 지정
ndf2 = df.reindex(new_index,fill_value=0)
print(ndf2)  
print('\n')
ndf2.iloc[3,::] = [16,17,18,19,20]
print(ndf2)


#%% 행 인덱스 초기화

'''reset_index() -> 행 인덱스를 정수형 위치 인덱스로 초기화, 기존 행 인덱스는 열로 이동
새로운 객체 반환'''

#예제1-18
import pandas as pd
dict_data = {'c0':[1,2,3], 'c1':[4,5,6],'c2' :[7,8,9], 'c3':[10,11,12], 'c4':[13,14,15]}
df = pd.DataFrame(dict_data,index=['r0','r1','r2']) #행 인덱스 지정
print(df)
print('\n')

ndf = df.reset_index() #r1, r2, r3에서 0, 1, 2로 변경
print(ndf)


#%% 행 인덱스를 기준으로 데이터프레임 정렬

'''sort_index(ascending=False) -> 내림차순
   sort_index(ascending=True) -> 오름차순
새로운 객체 반환'''

#예제1-19
import pandas as pd
dict_data = {'c0':[1,2,3], 'c1':[4,5,6],'c2' :[7,8,9], 'c3':[10,11,12], 'c4':[13,14,15]}
df = pd.DataFrame(dict_data,index=[100,300,50]) 
print(df)
print('\n')
ndf = df.sort_index(ascending=False)
print(ndf)
print('\n')

ndf2 = df.sort_index(ascending=True)
print(ndf2)
print('\n')
df2 = pd.DataFrame(dict_data,index=['c100','a50','ㅇ50']) #문자열일 경우 순서?
ndf3 = df2.sort_index(ascending=True)
print(ndf3)
print('\n')

#특정 열의 데이터 값을 기준으로 데이터프레임 정렬하기 sort_values()
import pandas as pd
dict_data = {'c0':[1,2,3], 'c1':[4,5,6],'c2' :[7,8,9], 'c3':[10,11,12], 'c4':[13,14,15]}
df = pd.DataFrame(dict_data,index=['r0','r1','r2'])
print(df)
print('\n')
ndf = df.sort_values(by='c1',ascending=False) #'c1' 열 4, 5, 6 정렬
print(ndf)


#%% 시리즈 vs 숫자

'''시리즈와 숫자 연산 -> 시리즈의 모든 개별 원소와 숫자를 연산
Series 객체 + 연산자(+,-,*,/) + 숫자'''

#예제1-21
import pandas as pd
student1 = pd.Series({'국어':100, '영어':80,'수학':90})
print(student1)
print('\n')
mul = student1*0.5 #곱셈
print(mul)
print('\n')

div = student1/100
add = student1+3
sub = student1-5

print(div) #나눗셈
print('\n')
print(add) #덧셈
print('\n')
print(sub) #뺄셈
print('\n')


#%% 시리즈 vs 시리즈
'''시리즈의 같은 인덱스를 가진 원소끼리 계산 (정수형 위치 인덱스가 아니라 인덱스 이름을 기준으로 함)
Series 객체 + 연산자(+,-,*,/) + Series 객체'''

#예제1-22
import pandas as pd
student1 = pd.Series({'국어':100, '영어':80,'수학':90})
student2 = pd.Series({'영어':70, '국어':80,'수학':100})
print(student1)
print('\n')
print(student2)
print('\n')
add = student1 + student2 #덧셈
sub = student1 - student2 #뺄셈
mul = student1 * student2 #곱셈
div = student1 / student2 #나눗셈
print(add) 
print('\n')
print(sub) 
print('\n')
print(mul) 
print('\n')
print(div)
print('\n')
result = pd.DataFrame([add,sub,mul,div],index=['덧셈','뺄셈','곱셈','나눗셈']) #여러 개의 시리즈를 한 데이터프레임으로 변환
print(result)
print('\n')

#연산을 하는 두 시리즈의 크기가 다를 경우, 동일한 인덱스가 없으면 결과값은 NaN +한쪽 원소가 NaN일 경우

#예제1-23
import pandas as pd
import numpy as np
student1 = pd.Series({'국어':np.nan,'영어':80,'수학':90})
student2 = pd.Series({'수학':80,'국어':90})
add = student1 + student2 #덧셈
sub = student1 - student2 #뺄셈
mul = student1 * student2 #곱셈
div = student1 / student2 #나눗셈
print(add) 
print('\n')
print(sub) 
print('\n')
print(mul) 
print('\n')
print(div)
print('\n')
#'국어' 숫자+NaN -> NaN, student2에 '영어' 인덱스X -> NaN
result = pd.DataFrame([add,sub,mul,div],index=['덧셈','뺄셈','곱셈','나눗셈'])
print(result)
print('\n')

#student1 = pd.Series({'국어':'미응시','영어':80,'수학':90})
#student2 = pd.Series({'수학':80,'국어':90})
#add = student1 + student2 #문자열 -> 오류
#print(add)

#student1 = pd.Series({'국어':100,'영어':'미응시','수학':90})
#student2 = pd.Series({'수학':80,'국어':90})
#add = student1 + student2 #문자열 -> 오류
#print(add)


#%% 연산 메소드

'''NaN에 숫자 채우기
시리즈 객체.add/sub/mul/div(시리즈 객체, fill_vaule=숫자)'''

#예제1-24
import pandas as pd
import numpy as np
student1 = pd.Series({'국어':np.nan,'영어':80,'수학':90}) #0
student2 = pd.Series({'수학':80,'국어':90}) #0
add = student1.add(student2,fill_value=0) 
sub = student1.sub(student2,fill_value=0)
mul = student1.mul(student2,fill_value=0)
div = student1.div(student2,fill_value=0)
result = pd.DataFrame([add,sub,mul,div],index=['덧셈','뺄셈','곱셈','나눗셈'])
print(result) #0으로 나누어서 inf


#%% 데이터프레임 vs 숫자

'''시리즈와 같음. 데이터프레임의 각각의 모든 원소와 숫자를 연산
DataFrame 객체 + 연산자 + 숫자'''

#예제1-25
import pandas as pd
import seaborn as sns
titanic = sns.load_dataset('titanic') #seaborn 라이브러리에서 제공하는 데이터셋 중 타이타닛 데이터셋
df = titanic.loc[:,['age','fare']] #원소 선택, 행 전체(2개 이상)와 열 'age', 'fare'(2개 이상) -> 데이터프레임 반환
print(df.head()) #.head() -> 첫 5행만 표시
print('\n')
print(type(df))
print('\n')
add = df + 100
print(add.head())


#%% 데이터프레임 vs 데이터프레임

'''시리즈와 같음. 같은 인덱스를 가진 원소끼리 계산 (정수형 위치 인덱스가 아니라 인덱스 이름을 기준으로 함)
DataFrame 객체 + 연산자(+,-,*,/) + DataFrame객체

동일한 인덱스가 없거나 한쪽 원소가 NaN이라면 결과값은 NaN'''

#예제1-26
import pandas as pd
import seaborn as sns
titanic = sns.load_dataset('titanic') #seaborn 라이브러리에서 제공하는 데이터셋 중 타이타닛 데이터셋
df = titanic.loc[:,['age','fare']] #원소 선택, 행 전체(2개 이상)와 열 'age', 'fare'(2개 이상) -> 데이터프레임 반환
print(df.tail()) #.tail() -> 마지막 5행만 표시
print('\n')
add = df + 100
sub_100 = add - df #888행, age열: NaN -> 연산값 = NaN
print(sub_100.tail())
