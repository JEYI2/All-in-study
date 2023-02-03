#%% 외부 파일 읽어오기

''' 다양한 형태의 외부 파일을 읽어와서 데이터프레임으로 변환
또는 데이터프레임을 다양한 유형의 파일로 저장

File Fomat                Reader                   Writer
----------------------------------------------------------------
CSV                       read_csv                 to_csv
JSON                      read_json                to_json
HTML                      read_html                to_html
Local clipboard           read_clipboard           to_clipboard
MS Excel                  read_Excel               to_excel
HDF5 Fomat                read_hdf                 to_hdf
SQL                       read_Sql                 to_sql       '''

#참고
pd.set_option("display.unicode.east_asian_width", True) #->데이터프레임 줄맞춤


#%%  CSV 파일

'''CSV 파일: 데이터 값을 쉼표로 구분하는 텍스트 파일
쉼표로 열을 구분하고 줄바꿈으로 행을 구분함

read_csv()을 통해 읽어와 데이터프레임으로 변환
pandas.read_csv("파일 경로(이름)", header=?, index_col=?)
header 옵션을 통해 데이터프레임의 열 이름으로 사용할 행 지정(옵션을 안쓰면 첫 행으로 지정(=0))
index_col 옵션을 통해 데이터프레임의 행 인덱스가 되는 열 지정(옵션을 안쓰면 정수로 지정)'''

#예제2-1
import pandas as pd
#파일을 변수 file_path에 저장
file_path = r'C:\Users\sungyedam\Desktop\study\파이썬 스터디\2주차\read_csv_sample.csv'
#문자열 앞의 수식어 r은 파이썬에게 이 문자열이 raw string 임을 알려주며, 
#문자열 내의 백슬래시가 확장 문자가 아니라 글자 그대로 해석되도록 한다.
df1 = pd.read_csv(file_path) #데이터프레임으로 변환, 변수 df1에 저장
print(df1) #첫 행: c0, c1, c2, c3 -> 열 이름으로 지정(header 옵션X) / 행 인덱스 0, 1, 2: 정수로 지정(index_col 옵션X)
print('\n') 
df2 = pd.read_csv(file_path, header=None)
print(df2) #header=None -> 열 이름 0, 1, 2, 3(정수로 지정)
print('\n')
df3 = pd.read_csv(file_path, index_col=None) #또는 False
print(df3) #index_col=None -> 행 인덱스 0, 1, 2(정수로 지정)
print('\n')
df4 = pd.read_csv(file_path, index_col='c0')
print(df4) #index_col='c0' -> 행 인덱스 0, 1, 5(c0 열이 행 인덱스로 지정)
print('\n')

#names, skiprows, parse_dates, skip_footer, encoding 등 다양한 옵션
df5 = pd.read_csv(file_path, names=['일','이','삼','사'], skiprows=[2])
print(df5)


#%% Excel 파일

'''Excel 파일의 행과 열은 데이터프레임의 행, 열로 일대일 대응
pandas.read_excel("파일 경로(이름"))'''

#예제2-2
import pandas as pd
file_path = r'C:\Users\sungyedam\Desktop\study\파이썬 스터디\2주차\남북한발전전력량.xlsx'
df1 = pd.read_excel(file_path) #첫 행이 열 이름
df2 = pd.read_excel(file_path, header=None) #열 이름 -> 0,1,2,...(정수)
print(df1)
print('\n')
print(df2)
print('\n')

df3 = pd.read_excel(file_path, header=None, index_col=[0,1])
print(df3)


#%% JSON 파일

#JSON 파일: key:value 구조

#예제2-3
import pandas as pd
file_path = r'C:\Users\sungyedam\Desktop\study\파이썬 스터디\2주차\read_json_sample.json'
df = pd.read_json(file_path)
print(df) 
print('\n')
print(df.index)


#%% HTML 웹 페이지에서 표 속성 가져오기

'''read_html("웹 페이지 주소" 또는 "HTML 파일 경로(이름) 또는 '') 
-> HTML 웹 페이지에 있는 <table> 태그에서 표 형식의 데이터를 모두 찾아 데이터프레임으로 모두 변환'''

#예제2-4
import pandas as pd
url = r'C:\Users\sungyedam\Desktop\study\파이썬 스터디\2주차\sample.html' #html 파일을 변수 url에 저장
tables = pd.read_html(url) #html 웹 페이지의 표를 데이터프레임으로 변환
#print(tables)
print('\n')
print(len(tables)) #표의 개수 확인(2)
print('\n')
for i in range(len(tables)): #i: 0, 1
    print("tables[%s]" % i) #$s: 문자열 포맷팅(문자열 안에 어떤 값을 삽입)
    print(tables[i])
    print('\n')
df = tables[1] #두번째 데이터프레임을 df 변수에 저장
df.set_index(['name'],inplace=True) #''name' 열을 행 인덱스로 지정
print(df)
print('\n')


#문자열 포맷팅을 안하면
for i in range(len(tables)): 
    print("tables[i]") 
    print(tables[i])
    print('\n')
#format 방법을 이용하면
for i in range(len(tables)): 
    print("tables[{}]".format(i))
    print(tables[i])
    print('\n')
#f-string 방법을 이용하면
for i in range(len(tables)): 
    print(f"tables[{i}]")
    print(tables[i])
    print('\n')


#%% 웹 스크래핑

'''스크래핑 -> 파이썬 리스트 or 딕셔너리 등으로 정리 -> 데이터프레임으로 변환'''

#예제2-5
import requests #requests: 데이터를 호출함
from bs4 import BeautifulSoup #BeautifulSoup: 데이터를 파싱(parsing)
import re #regular expression
import pandas as pd
url = "https://en.wikipedia.org/wiki/List_of_American_exchange-traded_funds"
resp = requests.get(url) #url에서 데이터를 get해옴
soup = BeautifulSoup(resp.text, 'lxml') #get해온 데이터(text)를 xml형식으로 parsing
#soup.prettify()
rows = soup.select('div>ul>li') #<div> 태그 안에 있는 <ul> 태그 안에 있는 <li> 태그를 불러옴
etfs = {}
'''re.findall: 정규표현식과 매치되는 모든 문자열을 리스트 형식으로 리턴함, 
정규표현식: 특정한 규칙을 가진 문자열의 집합을 표현하는 데 사용하는 형식 언어'''
for row in rows:
    print(row.text)
    try: #try-except(세트)
        etf_name = re.findall('^(.*) \(NYSE', row.text)
        etf_market = re.findall('\((.*)\|', row.text)
        etf_ticker = re.findall('NYSE Arca\|(.*)\)', row.text)
        #print(etf_name, etf_market, etf_ticker)
        if (len(etf_ticker) > 0) & (len(etf_market) > 0) & (len(etf_name) > 0):
            etfs[etf_ticker[0]] = [etf_market[0], etf_name[0]]
    except AttributeError as err:
        pass    
print(etfs) #etfs 딕셔너리 출력
print('\n')
df = pd.DataFrame(etfs) #etfs 딕셔너리를 데이터프레임으로 변환
print(df)
#??


#%% API 활용하여 데이터 수집하기

#구글 지오코딩 API: 장소 이름 또는 주소를 위도와 경도 좌표 정보로 변환해주는 서비스

#예제2-6
'''#라이브러리 가져오기
import googlemaps
import pandas as pd
my_key = "----발급받은 API 키를 입력-----"
#구글맵스 객체 생성하기
maps = googlemaps.Client(key=my_key)
lat = []  #위도
lng = []  #경도
#장소 리스트
places = ["서울시청", "국립국악원", "해운대해수욕장"]
i=0
for place in places:   
    i = i + 1
    try:
        print(i, place)
        #지오코딩 API 결과값을 호출하여 geo_location 변수에 저장
        geo_location = maps.geocode(place)[0].get('geometry')
        lat.append(geo_location['location']['lat'])
        lng.append(geo_location['location']['lng'])
    except:
        lat.append('')
        lng.append('')
        print(i)
df = pd.DataFrame({'위도':lat, '경도':lng}, index=places) # 데이터프레임으로 변환하기
print('\n')
print(df)'''


#%% CSV 파일로 저장

#데이터프레임을 CSV 파일로 저장: DataFrame 객체.to_csv("파일 이름(경로)" 또는 ' ')

#예제2-7

import pandas as pd #라이브러리를 불러옴

data = {'name': ['Jerry', 'Riah', 'Paul'],
        'algol': ["A","A+","B+"],
        'basic': ["C","B","C+"],
        'c++':["B+","C","C+"]} #딕셔너리 생성

df = pd.DataFrame(data) #딕셔너리를 데이터프레임으로 변환
print(df)
print('\n')

df.set_index('name',inplace=True) #'name' 열을 행 인덱스로 지정
print(df)

df.to_csv(r"C:\Users\sungyedam\Desktop\study\파이썬 스터디\2주차 예제\df_sample.csv")
#문자열 앞의 수식어 r은 파이썬에게 이 문자열이 raw string 임을 알려주며, 문자열 내의 백슬래시를 확장 문자가 아니라 글자 그대로 해석되도록 함.


#%% JSON 파일로 저장

#데이터프레임을 JSON 파일로 저장: DataFrame 객체.to_json("파일 이름(경로)" 또는 ' ')

#예제2-8

import pandas as pd #라이브러리를 불러옴

data = {'name': ['Jerry', 'Riah', 'Paul'],
        'algol': ["A","A+","B+"],
        'basic': ["C","B","C+"],
        'c++':["B+","C","C+"]} #딕셔너리 생성

df = pd.DataFrame(data) #딕셔너리를 데이터프레임으로 변환
print(df)
print('\n')

df.set_index('name',inplace=True) #'name' 열을 행 인덱스로 지정
print(df)

df.to_json(r"C:\Users\sungyedam\Desktop\study\파이썬 스터디\2주차 예제\df_sample.json")

#print(pd.read_json(r"C:\Users\sungyedam\Desktop\study\파이썬 스터디\2주차 예제\df_sample.json"))


#%% Excel 파일로 저장

'''데이터프레임을 Excel 파일로 저장: DataFrame 객체.to_excel("파일 이름(경로)" 또는 ' ')

to_excel() 메소드를 사용하려면 openpyxl 라이브러리를 설치해야 하며,
openpyxl은 python에서 Excel 파일을 읽고 쓸 수 있는 모듈임 (아나콘다 기본 제공)'''

#예제2-9

import pandas as pd #라이브러리를 불러옴

data = {'name': ['Jerry', 'Riah', 'Paul'],
        'algol': ["A","A+","B+"],
        'basic': ["C","B","C+"],
        'c++':["B+","C","C+"]} #딕셔너리 생성

df = pd.DataFrame(data) #딕셔너리를 데이터프레임으로 변환
print(df)
print('\n')

df.set_index('name',inplace=True) #'name' 열을 행 인덱스로 지정
print(df)

df.to_excel(r"C:\Users\sungyedam\Desktop\study\파이썬 스터디\2주차 예제\df_sample.xlsx")


#%% 여러 개의 데이터프레임을 하나의 Excel 파일로 저장

#pandas.ExcelWriter("파일 이름(경로)")

#예제2-10

#라이브러리 불러오기
import pandas as pd

#딕셔너리 생성
data1 = {'name': ['Jerry', 'Riah', 'Paul'],
        'algol': ["A","A+","B+"],
        'basic': ["C","B","C+"],
        'c++':["B+","C","C+"]}

data2 = {'c0':[1,2,3],
         'c1':[4,5,6],
         'c3':[7,8,9],
         'c4':[10,11,12],
         'c5':[13,14,15]}

#딕셔너리를 데이터프레임으로 변환
df1 = pd.DataFrame(data1)
df1.set_index('name',inplace=True)

df2 = pd.DataFrame(data2)
df2.set_index('c0',inplace=True)

print(df1)
print('\n')
print(df2)

#엑셀 파일 생성
writer = pd.ExcelWriter(r"C:\Users\sungyedam\Desktop\study\파이썬 스터디\2주차 예제\df_excelwriter.xlsx")

#엑셀 파일에  두 데이터프레임을 저장
df1.to_excel(writer,sheet_name="shee1")
df2.to_excel(writer,sheet_name="sheet2")

writer.save()
