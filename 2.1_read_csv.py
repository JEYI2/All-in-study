'''Part2 데이터 입출력
외부 파일 읽어오기 
판다스는 다양한 형태의 외부 파일을 읽어와서 데이터프레임으로 변환하는 함수 제공
반대로 데이터프레임을 다양한 유형의 파일로 저장 가능
파일 확장자 예: .csv, .json, .xlsx 등'''

'''CSV 파일
csv: comma-separated values으로, 데이터 값을 쉼표로 구분하고 있다는 의미
-> 쉼표로 열을 구분하고 줄바꿈으로 행을 구분함
CSV 파일 -> 데이터프레임: pandas.read_csv("파일 경로(이름)")

read_csv() 함수의 header 옵션: 데이터프레임의 열 이름으로 사용할 행 지정
header=0 (기본 값: 0행을 열 지정): df = read_csv(file)
header=1 (1행을 열 지정): df = read_csv(file, header=1)
header=None (행을 열 지정하지 않음): df = read_csv(file, header=None)

index_col 옵션: 데이터프레임의 행 인덱스가 되는 열 지정
index_col=False (인덱스 지정하지 않음): df = read_csv(file, index_col=False)
index_col='c0' ('c0' 열을 인덱스 지정): df = read_csv(file, index_col='c0')
'''

#<예제 2-1> CSV 파일 읽기
# -*- coding: utf-8 -*-

# 라이브러리 불러오기
import pandas as pd

# 파일경로를 찾고, 변수 file_path에 저장
file_path = r'C:\Users\User\OneDrive\바탕 화면\All_in_study2-1\read_csv_sample.csv'

# read_csv() 함수로 데이터프레임 변환. 변수 df1에 저장
df1 = pd.read_csv(file_path)
print(df1)
print('\n')

# read_csv() 함수로 데이터프레임 변환. 변수 df2에 저장. header=None 옵션
df2 = pd.read_csv(file_path, header=None)
print(df2)
print('\n')

# read_csv() 함수로 데이터프레임 변환. 변수 df3에 저장. index_col=None 옵션
df3 = pd.read_csv(file_path, index_col=None)
print(df3)
print('\n')

# read_csv() 함수로 데이터프레임 변환. 변수 df4에 저장. index_col='c0' 옵션
df4 = pd.read_csv(file_path, index_col='c0')
print(df4)