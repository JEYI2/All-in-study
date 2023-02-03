# -*- coding: utf-8 -*-
"""
Created on Thu Jan 26 18:44:33 2023

@author: dkwodk
"""
import pandas as pd

# 공공데이터 포털의 강원도  
file_path = 'C:/Users/dkwodk/Documents/python/spyder/week2/animal.csv'

#오류 발생'utf-8' codec can't decode byte 0xbd in position 0: invalid start bytedhf

df1 = pd.read_csv(file_path,encoding='euc-kr') # encoding='euc-kr', encoding='cp949'
print(df1)
print('\n')

# read_csv() 함수로 데이터프레임 변환,변환 df2에 저장, header=None 옵션
df2 = pd.read_csv(file_path, header=None, encoding='euc-kr')
print(df2)
print('\n')

# read_csv() 함수로 데이터프레임 변환,변환 df2에 저장, header=0 옵션
df3 = pd.read_csv(file_path, header=0, encoding='euc-kr')
print(df3)
print('\n')

# read_csv() 함수로 데이터프레임 변환,변환 df2에 저장, header=1 옵션
df4 = pd.read_csv(file_path, header=1, encoding='euc-kr')
print(df4)
print('\n')

# read_csv() 함수로 데이터 프레임변환, 변수 df3에 저장, index_col=None
df5 = pd.read_csv(file_path, index_col=None, encoding='euc-kr')
print(df5)
print('\n')

# read_csv() 함수로 데이터프레임 변환, 변수 df4에 저장. index_col= '시군명' 옵션
df6 = pd.read_csv(file_path, index_col='시군명', encoding='euc-kr')
print(df6)
#%%
### <예제 2-2> Excel 파일 읽기 ###
import pandas as pd

#read_excel ()함수로 데이터프레임 변환
df1 = pd.read_excel('C:/Users/dkwodk/Documents/python/spyder/week2/남북한발전전력량.xlsx')
#=>header=0 디폴트값
df2 = pd.read_excel('C:/Users/dkwodk/Documents/python/spyder/week2/남북한발전전력량.xlsx',header=None)

#데이터프레임 출력
print(df1)
print('\n')
print(df2)

#%%
### <예제 2-3>  JSON 파일 읽기
import pandas as pd

file = 'C:/Users/dkwodk/Documents/python/spyder/week2/test.json'
df1 = pd.read_json(file)
print(df1)
print('\n')
print(df1.index)

#%%
### <예제 2-4> HTML 표 속성 읽기 ###
import pandas as pd 
#!pip install html5lib
#!pip install lxml
#!pip install beautifulSoup4

#import html5lib
#import lxml
#from bs4 import BeautifulSoup

url='file:///C:/Users/dkwodk/Documents/python/spyder/week2/sample.html'
tables = pd.read_html(url)
#표 개수 확인
print(len(tables))
print('\n')

#tabled 리스트의 원소를 iteraction하면서 각각 화면 출력
for i in range(len(tables)):
    print("tables[%s]" % i)
    print(tables[i])
    print('\n')

# 파이썬 패키지 정보가 들어 있는 두 번쨰 데이터 프레임을 선택하여 df 변수에 저장
df = tables[1]

# name열을 인덱스로 지정
df.set_index(['name'], inplace= True)
print(df)
#%%
### <예제2-5> 미국 ETF리스트 가져오기###

#라이브러리 불러오기
from bs4 import BeautifulSoup
import requests
import re
import pandas as pd

#위키피디아 미국 ETF웹 페이지에서 필요한 보를 스크래핑하여 딕셔너리 형태로 변수 etf에 저장
url = "https://en.wikipedia.org/wiki/List_of_American_exchange-traded_funds"
resp= requests.get(url)
soup = BeautifulSoup(resp.text,'lxml')
rows = soup.select('div > ul > li')

etfs = {}
for row in rows:
    
    try:
        etf_name = re.findall('^(.*) \(NYSE', row.text)
        etf_market = re.findall('\((.*)\|', row.text)
        etf_ticker = re.findall('NYSE Arca\|(.*)\)', row.text)
        
        if (len(etf_ticker) > 0) & (len(etf_market) > 0) & (len(etf_name) > 0):
            etfs[etf_ticker[0]] = [etf_market[0], etf_name[0]]

    except AttributeError as err:
        pass    

print(etfs)
df = pd.DataFrame(etfs)
print(df)

#%%
### <예제 2-7> csv 파일로 저장 ###

import pandas as pd

# 판다스 DataFrame()함수로 데이터프레임 변환, 변수 df에 저장
data = {'name': ['jerry','Riah', 'paul'],
        'algol': ["A", "A+", "B"],
        'basic': ["C", "B","B+"],
        'C++' : ["B++", "C","C+"],
        }

df = pd.DataFrame(data)
df.set_index('name',inplace=True) #name열을 인덱스로 지정
print(df)

#to_csv() 메소드를 활용하여 csv파일로 내보내기, df_sample.csv로 저장
df.to_csv("C:/Users/dkwodk/Documents/python/spyder/week2/df_sample.csv")

#%%
### <예제 2-8> JSON 파일로 저장 ###

import pandas as pd

data = {'name': ['jerry','Riah', 'paul'],
        'algol': ["A", "A+", "B"],
        'basic': ["C", "B","B+"],
        'C++' : ["B++", "C","C+"],
        }

df = pd.DataFrame(data)
df.set_index('name', inplace=True)
print(df)

#to_json() 메소드를 활용
df.to_json("C:/Users/dkwodk/Documents/python/spyder/week2/df_sample.json")

#%%
import pandas as pd

#판다스 DataFrame() 함수로 데이터프레임 변환
data = {'name': ['jerry','Riah', 'paul'],
        'algol': ["A", "A+", "B"],
        'basic': ["C", "B","B+"],
        'C++' : ["B++", "C","C+"],
        }

df = pd.DataFrame(data)
df.set_index('name', inplace=True)
print(df)

# to_excel() 메소드 
df.to_excel("C:/Users/dkwodk/Documents/python/spyder/week2/df_sample.xlsx")

#%%
import pandas as pd 

# 판다스 DataFrame() 함수로 데이터프레임 변환, 변수  df1, df2에 저장
data1 =  {'name': ['jerry','Riah', 'paul'],
        'algol': ["A", "A+", "B"],
        'basic': ["C", "B","B+"],
        'C++' : ["B++", "C","C+"],
        }


data2 = {'c0':[1,2,3],
         'c1':[4,5,6],
         'c2':[7,8,9],
         'c3':[10,11,12],
         'c4':[13,14,15]}

df1 = pd.DataFrame(data1)
df1.set_index('name', inplace=True) #name 열을 인덱스로 지정
print(df1)

df2 = pd.DataFrame(data2)
df2.set_index('c0', inplace=True)  #c0 열을 인덱스로 지정
print(df2)

# df1을 'sheet1'으로 df2를 'sheet2'로 지정
writer = pd.ExcelWriter("C:/Users/dkwodk/Documents/python/spyder/week2/df_exelwriter.xlsx")
df1.to_excel(writer,sheet_name="sheet1")
df2.to_excel(writer,sheet_name="sheet2")
writer.save()




