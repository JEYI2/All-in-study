#%% 데이터 내용 미리보기

'''head(): 데이터프레임의 처음 일부 내용을 출력 / tail(): 데이터프레임의 마지막 일부 내용을 출력
인자, 정수 n -> 처음 n개의 행 또는 마지막 n개의 행을 출력 (디폴트 값: n=5)
앞부분 미리보기: DataFrame 객체.head(n)
뒷부분 미리보기: DataFrame 객체.tail(n)'''

#예제3-1
import pandas as pd
#csv 파일을 데이터프레임으로 변환, 변수 df에 저장
df = pd.read_csv(r"C:\Users\sungyedam\Desktop\study\파이썬 스터디\3주차\part3\auto-mpg.csv")
#print(df)
#열 이름 지정
df.columns = ['mpg','cylinders','displacement','horsepower','weight','acceleration','model year',
             'origin','name'] #원래 열 이름으로 설정되어 있던 첫 행이 삭제됨
print(df.head()) #처음 5개 행 출력
print('\n')
print(df.tail()) #마지막 5개 행 출력
print('\n')

#수정
df = pd.read_csv(r"C:\Users\sungyedam\Desktop\study\파이썬 스터디\3주차\part3\auto-mpg.csv",header=None)
df.columns = ['mpg','cylinders','displacement','horsepower','weight','acceleration','model year',
             'origin','name']
print(df.head()) 
print('\n')
print(df.tail()) 


#%% 데이터 요약 정보 확인하기

'''
데이터프레임의 크기(행, 열) -> DataFrame 객체.shape

데이터프레임의 기본 정보(클래스 유형, 행 인덱스 구성, 열 이름의 종류와 개수, 각 열의 자료형과 개수, 메모리 할당량)
-> DataFrame 객체.info()

각 열의 자료형 -> DataFrame 객체(.열 이름).dtypes

데이터프렘임의 기술 통계 정보 요약(평균, 표준편차, 최대값, 최소값, 중간값 등)
-> DataFrame 객체.describe(): 산술 데이터에만 적용
-> DataFrame 객체.describe(include='all'): 모든 데이터 적용(고유값 개수, 최빈값, 빈도수 추가, 유효한 값 없으면 NaN)
'''

#예제3-1
print(df.shape) #398개의 행, 9개의 열
print('\n')
print(df.info())
print('\n')
print(df.dtypes) #모든 열
print('\n')
print(df.mpg.dtypes) #특정 열
print('\n')
print(df.describe()) #'name' 열 제외, 'horsepower' 열 제외(?가 포함돼있어서)
print('\n')
print(df.describe(include='all')) #모든 데이터에 대한 정보


#%% 데이터 개수 확인

'''
각 열의 데이터 개수(유효한 값의 개수) -> DataFrame 객체.count()

각 열의 고유값(unique value) 개수 -> DataFrmae 객체["열 이름"].value_counts()
옵션: dropna=True -> NaN 제외, dropna=Flase -> NaN 포함 (디폴트값: dropna=Flase)
'''

#예제3-2
import pandas as pd
df = pd.read_csv(r"C:\Users\sungyedam\Desktop\study\파이썬 스터디\3주차\part3\auto-mpg.csv",header=None)
df.columns = ['mpg','cylinders','displacement','horsepower','weight','acceleration','model year',
             'origin','name']
print(df.count()) #각 열의 데이터 개수(유효한 값의 개수)
print(type(df.count()))
print('\n')
print(df["origin"].value_counts()) #특정 열의 고유값(unique value) 개수 
print(type(df["origin"].value_counts()))


#%% 평균값

#모든 열: DataFrmae 객체.mean(), 특정 열: DataFrame 객체["열 이름"].mean()
#문자열: 계산X

#예제3-3
import pandas as pd
df = pd.read_csv(r"C:\Users\sungyedam\Desktop\study\파이썬 스터디\3주차\part3\auto-mpg.csv",header=None)
df.columns = ['mpg','cylinders','displacement','horsepower','weight','acceleration','model year',
             'origin','name']
#모든 열
print(df.mean()) 
print('\n')
#특정 열
#print(df["name"].mean())
print(df["mpg"].mean())
print('\n')
print(df[["cylinders","displacement"]].mean()) #리스트 형태


#%% 중간값

#모든 열: DataFrame 객체.median(), 특정 열: DataFrame 객체["열 이름"].median()
#문자열: 계산X

#예제3-3
print(df.median())
print('\n')
print(df["mpg"].median())
print('\n')
print(df[["mpg","cylinders"]].median())


#%% 최대값

'''모든 열: DataFrame 객체.max(), 특정 열: DataFrame 객체["열 이름"].max()
#문자열 -> ASCⅡ(아스키) 숫자 변환, 아스키 숫자 비교'''

#예제3-3
print(df.max())
print('\n')
#문자열 -> ASCⅡ(아스키) 숫자 변환, 아스키 숫자 비교
print(df["horsepower"].max()) #'?' 때문에 모든 데이터를 문자열로 인식
print('\n')
print(df["name"].max())
print('\n')

max='vw rabbit custom'
List = []
for i in range(len(max)):
    asc = ord(max[i])
    List.append(asc)
print(List)
print('\n')
Liststr = []
for i in range(len(List)):
    Liststr.append(str(List[i]))
print(Liststr)
print('\n')
sum=''
for i in Liststr:
    sum=sum+i
print(sum)
print('\n')
print(int(sum))


#%% 최소값

'''모든 열: DataFrame 객체.min(), 특정 열: DataFrame 객체["열 이름"].min()
#문자열 -> ASCⅡ(아스키) 숫자 변환, 아스키 숫자 비교'''

#예제3-3
print(df.min())
print('\n')
#문자열 -> ASCⅡ(아스키) 숫자 변환, 아스키 숫자 비교
print(df["name"].min())

min='amc ambassador brougham'
List = []
for i in range(len(min)):
    asc = ord(min[i])
    List.append(asc)
print(List)
print('\n')
Liststr = []
for i in range(len(List)):
    Liststr.append(str(List[i]))
print(Liststr)
print('\n')
sum=''
for i in Liststr:
    sum=sum+i
print(sum)
print('\n')
print(int(sum))

118119321149798981051163299117115116111109 > 97109993297109989711511597100111114329811411111710310497109
#?


#%% 표준편차

'''모든 열: DataFrame 객체.std(), 특정 열: DataFrame 객체["열 이름"].std()
문자열: 계산X'''

#예제3-3
print(df.std())
print('\n')
print(df["mpg"].std())


#%% 상관계수

'''산술데이터를 갖는 모든 열에 대하여 2개씩 서로 짝을 짓고, 각각의 경우에 대하여 상관계수를 계산
모든 열: DataFrame 객체.corr(), 특정 열: DataFrame 객체["열 이름"].corr()'''

#예제3-3
print(df.corr())
print('\n')
print(df[['mpg','weight']].corr())


#%% 판다스 내장 그래프 도구 활용

'''plot() 메소드를 적용하여 그래프를 그림.

그래프 종류 -> kind 옵션
kind 옵션     설명                         kind 옵션     설명
-----------------------------             -------------------------
'line'       선 그래프                     'kide'        커널 밀도 그래프
'bar'       수직 막대 그래프               'area'        면적 그래프
'barh'      수평 막대 그래프               'pie'         파이 그래프
'his'       히스토그램                    'scatter'     산점도 그래프
'box'       박스 플롯                     'hexbin'      고밀도산점도 그래프'''


#%% 선 그래프

'''plot(), 옵션 추가X -> 선 그래프
DataFrame 객체.plot()'''

#예제3-4
import pandas as pd
df = pd.read_excel(r"C:\Users\sungyedam\Desktop\study\파이썬 스터디\3주차\part3\남북한발전전력량.xlsx")
df_ns = df.iloc[[0,5],3:] #df.iloc: 원소 선택(0행&5행 선택, 3열부터 끝열까지 선택 -> 1991년부터 합계 데이터 선택)
df_ns.index = ['South','North'] #행 인덱스 설정
df_ns.columns = df_ns.columns.map(int) #열 이름(문자열)을 정수형 데이터로 변환
print(df_ns.head())
print('\n')
print(df_ns.plot()) #x축 데이터: 행 인덱스(왼쪽: South, 오른쪽: North)
#행, 열 전치
tdf_ns = df_ns.T
print(tdf_ns.head())
print('\n')
print(tdf_ns.plot())


#%% 막대 그래프

#DataFrame 객체.plot(kind='bar')

#예제3-5
import pandas as pd
df = pd.read_excel(r"C:\Users\sungyedam\Desktop\study\파이썬 스터디\3주차\part3\남북한발전전력량.xlsx")
df_ns = df.iloc[[0,5],3:]
df_ns.index = ['South','North']
df_ns.columns = df_ns.columns.map(int)
tdf_ns = df_ns.T
print(tdf_ns)
print('\n')
print(tdf_ns.plot(kind='bar'))

#전치X
df = pd.read_excel(r"C:\Users\sungyedam\Desktop\study\파이썬 스터디\3주차\part3\남북한발전전력량.xlsx")
df_ns = df.iloc[[0,5],3:] 
df_ns.index = ['South','North'] 
df_ns.columns = df_ns.columns.map(int) 
print(df_ns.head())
print('\n')
print(df_ns.plot(kind='bar'))


#%% 히스토그램

#DataFrame 객체.plot(kind='hist')

#예제3-5
import pandas as pd
df = pd.read_excel(r"C:\Users\sungyedam\Desktop\study\파이썬 스터디\3주차\part3\남북한발전전력량.xlsx")
df_ns = df.iloc[[0,5],3:]
df_ns.index = ['South','North']
df_ns.columns = df_ns.columns.map(int) #정수형 데이터로 변환 안됨
print(df_ns.dtypes) #자료형: object
print('\n')
'''
df_ns.astype(int)
print(df_ns.dtypes) #자료형: object <- 얘도 안됨
'''
tdf_ns = df_ns.T
tdf_ns[["South","North"]] = tdf_ns[["South","North"]].astype(int) #정수형 데이터로 변환됨
#또는 tdf_ns = tdf_ns.apply(pd.to_numeric)
print(tdf_ns)
print('\n')
tdf_ns.dtypes
tdf_ns.plot(kind='hist') #TypeError: no numeric data to plot
#x축: 발전량을 여러 구간으로 나눔, y축: 빈도(몇 개의 연도가 해당하는지)

#전치X
df_ns = tdf_ns.T
df_ns.plot(kind='hist')


#%% 산점도

#DataFrame 객체.plot(x='비교할 변수', y='비교할 변수', kind='scatter')

#예제3-7
import pandas as pd
df = pd.read_csv(r"C:\Users\sungyedam\Desktop\study\파이썬 스터디\3주차\part3\auto-mpg.csv", header=None)
df.columns = ['mpg','cylinders','displacement','horsepower','weight','acceleration','model year',
             'origin','name']
df.plot(x='weight',y='mpg',kind='scatter')
df.plot(x='weight',y='name',kind='scatter')


#%% 박스 플롯

#DataFrame 객체.plot(kind='box')

#예제3-8
import pandas as pd
df = pd.read_csv(r"C:\Users\sungyedam\Desktop\study\파이썬 스터디\3주차\part3\auto-mpg.csv", header=None)
df.columns = ['mpg','cylinders','displacement','horsepower','weight','acceleration','model year',
             'origin','name']
df.plot(kind='box')
df[['mpg','cylinders']].plot(kind='box') #특정 열
#plot: print() 할 필요 X


#%% Matplotlib-기본 그래프 도구

#Matplotlib: 시각화 도구


#%% 선 그래프

#연속하는 데이터 값들을 직선 또는 곡선으로 연결


#%% 기본 사용법

#plt.plot(x, y)

import pandas as pd
pd.set_option("display.unicode.east_asian_width", True)

#예제4-1
import pandas as pd
#PyPlot 모듈은 Matplotlib 모듈의 한 부분이므로 아래와 같이 import 함
import matplotlib.pyplot as plt
#Excel 데이터를 데이터프레임으로 변환 / 옵션: header=0 -> 첫 행을 열 이름으로 설정, fillna=0 -> NaN을 0으로 채움
#df = pd.read_excel(r"C:\Users\sungyedam\Desktop\study\파이썬 스터디\3주차\part4\시도별 전출입 인구수.xlsx",header=0,fillna=0)
#DataFrmae 객체.fillna()
df = pd.read_excel(r"C:\Users\sungyedam\Desktop\study\파이썬 스터디\3주차\part4\시도별 전출입 인구수.xlsx",header=0).fillna(0)
print(df.head())
#NaN을 앞 데이터로 채움: DataFrmae 객체.fillna(method='ffill')
df = pd.read_excel(r"C:\Users\sungyedam\Desktop\study\파이썬 스터디\3주차\part4\시도별 전출입 인구수.xlsx",header=0).fillna(method='ffill')
print(df.head())
#부산에서 다른 지역으로 이동하는 데이터만 추출(전출지: 부산, 전입지: 다른 지역)
df_Busan = df[(df['전출지별'] == '부산광역시') & (df['전입지별'] != '부산광역시')]
print(df_Busan.head())
df_Busan = df_Busan.drop(['전출지별'], axis=1) #axis=1(열), '전출지별' 열 삭제 
df_Busan.rename({'전입지별':'전입지'},axis=1, inplace=True) #'전입지별' 열 이름을 '전입지'로 변경
#또는 df_Busan.rename(columns={'전입지별':'전입지'}, inplace=True)
df_Busan.set_index('전입지',inplace=True) #'전입지' 열을 행 인덱스로 설정
print(df_Busan.head())
#부산에서 경기도로 이동하는 데이터
sr_one = df_Busan.loc['경기도'] #'경기도' 행 선택
print(sr_one.head())
plt.plot(sr_one.index, sr_one.values)
#또는 plt.plot(sr_one)
#plt.plot(sr_one.values, sr_one.index)


#%% 차트 제목, 축 이름 추가

'''
차트 제목: title()

x축 이름: xlabel()

y축 이름: ylabel()
'''

#예제4-2
plt.plot(sr_one)
plt.title('부산 -> 경기 인구 이동') #차트 제목 추가
plt.xlabel('기간') #x축 이름 추가
plt.ylabel('이동 인구수') #y축 이름 추가
plt.show() #변경사항 저장, 출력

#예제4-3
#matplotlib 한글 폰트 오류 문제 해결
from matplotlib import font_manager, rc
font_path = r"C:\Users\sungyedam\Desktop\study\파이썬 스터디\3주차\part4\malgun.ttf" #폰트 파일
font_name = font_manager.FontProperties(fname=font_path).get_name() #폰트 이름을 얻어옴
rc('font',family=font_name) #폰트 적용
#예제4-2 다시
plt.plot(sr_one)
plt.title('부산 -> 경기 인구 이동')
plt.xlabel('기간') 
plt.ylabel('이동 인구수') 
plt.show() 


#%% 그래프 꾸미기

'''
그림 사이즈: figure(figsize)

축 눈금: xticks(ticks, labels, size, rotation...) / yticks(ticks, labels, size, rotation...)

축 범위: xlim(), ylim()

범례: legend(labels, loc)

그래프 스타일: style.use()

마커, 선: plot(marker, markersize, markerfacecolor, color, linestyle, linewidth...)

주석(화살표 or 텍스트): annotate()
'''

#예제4-4
plt.figure(figsize=(14,5)) #그림 사이즈 지정
plt.plot(sr_one)
plt.xticks(rotation='vertical') #x축 눈금 라벨 회전
#차트 제목, 축 이름 추가
plt.title('부산 -> 경기 인구 이동') 
plt.xlabel('기간') 
plt.ylabel('이동 인구수') 
plt.legend(labels=['부산 -> 경기'], loc='best') #범례
#plt.legend(labels=['부산 -> 경기'], loc='upper left') #범례 위치 지정
plt.show() #변경사항 저장 후 출력

plt.figure(figsize=(14,5)) #그림 사이즈 지정
plt.plot(sr_one)
plt.xticks(rotation='vertical') #x축 눈금 라벨 회전
#차트 제목, 축 이름 추가
plt.title('부산 -> 경기 인구 이동') 
plt.xlabel('기간') 
plt.ylabel('이동 인구수') 
plt.legend(labels=['부산 -> 경기'], loc='best') #범례
#y축 눈금 설정(ticks, labels, size)
plt.yticks(ticks=range(5000,25000,5000),size=30) 
#plt.yticks(ticks=range(5000,25000,5000),labels=['5천','1만','1만5천','2만'])
plt.show() #변경사항 저장 후 출력

#예제4-5, 4-6
plt.style.available #그래프 스타일 종류
plt.figure(figsize=(14,5)) #그림 사이즈 지정
plt.style.use('Solarize_Light2') #그래프 스타일 지정
plt.plot(sr_one, marker='s', markersize=5, markerfacecolor='r', color='k', linestyle='--',linewidth=1,
         label='부산 -> 경기') #마커, 선 스타일, 범례
plt.xticks(rotation='vertical') #x축 눈금 라벨 회전
#차트 제목, 축 이름 추가
plt.title('부산 -> 경기 인구 이동') 
plt.xlabel('기간') 
plt.ylabel('이동 인구수') 
#범례
#plt.legend(labels=['부산 -> 경기'], loc='best') 
plt.legend(loc='best')
plt.show() #변경사항 저장 후 출력

#예제4-7
plt.figure(figsize=(14,5)) 
plt.plot(sr_one, marker='s', markersize=5, color='k', linewidth=1)
plt.xticks(rotation='vertical') 
plt.title('부산 -> 경기 인구 이동') 
plt.xlabel('기간') 
plt.ylabel('이동 인구수') 
plt.legend(labels=['부산 -> 경기'], loc='best') 
plt.ylim(0,40000) #y축 범위 설정
#주석 표시(화살표)
plt.annotate('',                                                  #텍스트 입력X
             xy=(35,22500),                                       #화살표 끝 위치(x값: 인덱스 번호, y값: 데이터)
             xytext=(0,7000),                                    #화살표 시작
             xycoords='data',                                    #좌표 체계('polar'...)
             arrowprops=dict(arrowstyle='->', color='r', lw=5), #화살표 서식
             )
plt.annotate('',
             xy=(48,16000),
             xytext=(35,22500),
             xycoords='data',
             arrowprops=dict(arrowstyle='->', color='b', lw=5),
             )
#주석 표시(텍스트)
plt.annotate('인구 이동 증가(1970-2004)', #텍스트 입력
             xy=(18,18000),               #위치(va, ha 기준)
             rotation = 12,               #각도
             va = 'center',               #상하 정렬
             ha = 'center',               #좌우 정렬
             fontsize=10,                 #텍스트 크기
             )
plt.annotate('인구 이동 감소(2005-2017)',
             xy=(38,21000),
             rotation = -12,
             va = 'center',
             ha = 'left',
             fontsize=10,
             )
plt.show() #변경사항 저장 후 출력


#%% 화면 분할하여 그래프 여러 개 그리기 - axe 객체 활용

'''
axe 객체는 각각 서로 다른 그래프를 표현할 수 있음.
화면을 여러 개로 분할하고, 분할된 화면마다 axe 객체를 하나씩 배정

fig = plt.figure(figsize): 그림틀 생성
fig.add_subplot(행의 크기, 열의 크기, 서브플롯 순서): 그림틀을 여러 개로 분할, 이때 나눠진 각 부분을 axe 객체라 부름
'''

#예제4-8
fig = plt.figure(figsize=(10,10)) #그림틀 생성
#화면 분할, axe 객체 배정
ax1 = fig.add_subplot(2,1,1)
ax2 = fig.add_subplot(2,1,2)
#ax1에 그래프 그리기, 설정
ax1.plot(sr_one, marker='o',color='r',label='부산 -> 경기')
ax1.legend(loc='best')
ax1.set_ylim(0,30000)
ax1.set_xticklabels(sr_one.index, rotation=75)
#ax2에 그래프 그리기, 설정
ax2.plot(sr_one, marker='s',color='b',linestyle='--',linewidth=1,label='부산 -> 경기')
ax2.legend(loc='best')
ax2.set_ylim(0,30000)
ax2.set_xticklabels(sr_one.index, rotation=75)
plt.show()

#예제4-9
fig = plt.figure(figsize=(20,5))
ax = fig.add_subplot(1,1,1) #1개의 그래프만 표시
#그래프 출력(마커, 선 스타일 설정)
ax.plot(sr_one,marker='o', markerfacecolor='orange', markersize=10, color='olive', linewidth=2) 
ax.legend(labels=['부산 -> 경기'], loc='best') #범례
ax.set_ylim(0,30000) #y축 범위 설정
#차트 제목, 축 제목 추가
ax.set_title('부산 -> 경기 인구 이동', size=18)
ax.set_xlabel('기간', size=12)
ax.set_ylabel('이동 인구수', size=12)
#눈금 설정
ax.set_xticklabels(sr_one.index, rotation=75)
ax.tick_params(axis="x",labelsize=10)
ax.tick_params(axis="y", labelsize=10)
plt.show() #변경 사항 저장 후 그래프 출력

#예제4-10
#부산에서 충남/경북/강원으로 이동하는 데이터 추출
print(df_Busan.head())
print('\n')
chung = df_Busan.loc['충청남도'] 
gyeong = df_Busan.loc['경상북도'] 
gang = df_Busan.loc['강원도'] 
print(chung.head())
print('\n')
print(gyeong.head())
print('\n')
print(gang.head())
plt.style.use('ggplot') #그래프 스타일 
fig = plt.figure(figsize=(20,5)) #그림 사이즈
ax = fig.add_subplot(1,1,1) #axe 객체 생성
#그래프 출력(마커, 선 스타일 설정)
ax.plot(chung.index, chung.values, marker='o', markerfacecolor='green', markersize=10, color='olive',linewidth=2)
ax.plot(gyeong.index, gyeong.values, marker='o', markerfacecolor='blue', markersize=10, color='skyblue',linewidth=2)
ax.plot(gang.index, gang.values, marker='o', markerfacecolor='red', markersize=10, color='magenta',linewidth=2)
#범례
ax.legend(labels=['부산 -> 충남','부산 -> 경북','부산 -> 강원'], loc='best')
#차트 제목
ax.set_title('부산 -> 충남, 경북, 강원 인구 이동', size=10)
#축 설정
ax.set_xlabel('기간',size=12)
ax.set_ylabel('이동 인구수',size=12)
ax.set_xticklabels(chung.index, rotation=90)
ax.tick_params(axis="x",labelsize=10)
ax.tick_params(axis="y",labelsize=10)
plt.show() #변경사항 저장 후 출력

#예제4-11
#부산에서 충남/경북/강원/전남으로 이동하는 데이터 추출
chung = df_Busan.loc['충청남도'] 
gyeong = df_Busan.loc['경상북도'] 
gang = df_Busan.loc['강원도'] 
jeon = df_Busan.loc['전라남도'] 
plt.style.use('ggplot') #그래프 스타일 
fig = plt.figure(figsize=(20,10)) #그림 사이즈
#화면 4개로 분할, axe 객체 4개 생성
ax1 = fig.add_subplot(2,2,1) 
ax2 = fig.add_subplot(2,2,2)
ax3 = fig.add_subplot(2,2,3)
ax4 = fig.add_subplot(2,2,4)
#그래프 출력(마커, 선 스타일 설정)
ax1.plot(chung.index, chung.values, marker='o', markerfacecolor='green', markersize=10, color='olive',linewidth=2)
ax2.plot(gyeong.index, gyeong.values, marker='o', markerfacecolor='blue', markersize=10, color='skyblue',linewidth=2)
ax3.plot(gang.index, gang.values, marker='o', markerfacecolor='red', markersize=10, color='magenta',linewidth=2)
ax4.plot(jeon.index, jeon.values, marker='o', markerfacecolor='orange', markersize=10, color='yellow',linewidth=2)
#범례
ax1.legend(labels=['부산 -> 충남'], loc='best')
ax2.legend(labels=['부산 -> 경북'], loc='best')
ax3.legend(labels=['부산 -> 강원'], loc='best')
ax4.legend(labels=['부산 -> 전남'], loc='best')
#차트 제목
ax1.set_title('부산 -> 충남', size=15)
ax2.set_title('부산 -> 경북', size=15)
ax3.set_title('부산 -> 강원', size=15)
ax4.set_title('부산 -> 전남', size=15)
#축 눈금 설정
ax1.set_xticklabels(chung.index, rotation=90)
ax2.set_xticklabels(chung.index, rotation=90)
ax3.set_xticklabels(chung.index, rotation=90)
ax4.set_xticklabels(chung.index, rotation=90)
plt.show() #변경사항 저장 후 출력

#예제4-12
#matplotlib 색상 종류
import matplotlib
colors={}
for name, hex in matplotlib.colors.cnames.items():
    colors[name] = hex
print(colors)


#%% 면적 그래프

'''각 열의 데이터를 선 그래프로 구현, 선 그래프와 x축 사이의 공간에 색이 입혀짐.

plot(kind='area')
옵션 -> stacked: 누적 여부(기본값=True), alpha: 투명도(기본값=0.5)'''

#예제4-13
import pandas as pd
import matplotlib.pyplot as plt
#엑셀 파일을 데이터프레임으로 변환
df = pd.read_excel(r"C:\Users\sungyedam\Desktop\study\파이썬 스터디\3주차\part4\시도별 전출입 인구수.xlsx",header=0).fillna(method='ffill')
#서울에서 다른 지역으로 이동하는 데이터만 추출
df_seoul = df[(df['전출지별'] == '서울특별시') & (df['전입지별'] != '서울특별시')]
df_seoul = df_seoul.drop(['전출지별'], axis=1) #axis=1(열), '전출지별' 열 삭제 
df_seoul.rename({'전입지별':'전입지'},axis=1, inplace=True) #'전입지별' 열 이름을 '전입지'로 변경
df_seoul.set_index('전입지',inplace=True) #'전입지' 열을 행 인덱스로 설정
#서울에서 충남/경북/강원/전남으로 이동하는 데이터만 추출
df_4= df_seoul.loc[['충청남도','경상북도','강원도','전라남도']]
df_4 = df_4.T
#print(df_4)
#그래프 스타일 설정
plt.style.use('ggplot')
#문자열인 행 인덱스(1970, 1970,...)를 정수형으로 변경
df_4.index = df_4.index.map(int)
#면적 그래프 그리기(stacked=False: 누적X)
df_4.plot(kind='area',stacked=False,alpha=0.2,figsize=(20,10))
plt.title('서울 -> 타시도 인구 이동', size=30)
plt.ylabel('이동 인구 수', size=20)
plt.xlabel('기간',size=20)
plt.legend(loc='best',fontsize=15)
plt.show()

#예제4-14
#stacked=True(누적O)
df_4.plot(kind='area',stacked=True,alpha=0.2,figsize=(20,10))
plt.title('서울 -> 타시도 인구 이동', size=30)
plt.ylabel('이동 인구 수', size=20)
plt.xlabel('기간',size=20)
plt.legend(loc='best',fontsize=15)
plt.show()

#예제4-15
#axe 객체 생성
ax = df_4.plot(kind='area',stacked=True,alpha=0.2,figsize=(20,10))
#axe 객체 설정 변경
ax.set_title('서울 -> 타시도 인구 이동', size=30, color='brown', weight='bold')
ax.set_ylabel('이동 인구 수', size=20, color='blue')
ax.set_xlabel('기간', size=20, color='blue')
ax.legend(loc='best',fontsize=15)
plt.show()


#%% 막대 그래프

'''
데이터 값의 크기에 비례하여 높이를 갖는 직사각형 막대로 표현

세로형: plot(kind='bar')
가로형: plot(kind='barh')
'''

#예제4-16
#2010~2017년 데이터만 추출
col_years = list(map(str,range(2010,2018)))
df_4= df_seoul.loc[['충청남도','경상북도','강원도','전라남도'],col_years]
df_4 = df_4.T
print(df_4)
#그래프 스타일 설정
plt.style.use('ggplot')
#문자열인 행 인덱스(2010, 2011...)를 정수형으로 변경
df_4.index = df_4.index.map(int)
#막대 그래프 그리기(세로형)
df_4.plot(kind='bar', figsize=(20,10), width=0.7, color=['orange','green','skyblue','blue'])
plt.title('서울 -> 타시도 인구 이동', size=30)
plt.ylabel('이동 인구 수', size=20)
plt.xlabel('기간',size=20)
plt.legend(loc='upper right',fontsize=15)
plt.show()

#예제4-17
df_4 = df_4.T
print(df_4)
print('\n')
#열 추가
df_4['합계'] = df_4.sum(axis=1)
print(df_4)
print('\n')
#sort_values(): 특정 열의 데이터 값을 기준으로 데이터프레임 정렬하기
df_total = df_4[['합계']].sort_values(by='합계',ascending=True)
print(df_total)
plt.style.use('ggplot')
#막대 그래프 그리기(가로형)
df_total.plot(kind='barh', figsize=(10,5), width=0.5, color=['cornflowerblue'])
plt.title('서울 -> 타시도 인구 이동')
plt.ylabel('전입지')
plt.xlabel('이동 인구 수')
plt.show()

#예제4-18
import pandas as pd
import matplotlib.pyplot as plt
#엑셀 파일을 데이터프레임으로 변환, convert_float=True: 숫자 데이터를 float형으로 가져옴
df = pd.read_excel(r"C:\Users\sungyedam\Desktop\study\파이썬 스터디\3주차\part4\남북한발전전력량.xlsx", convert_float=True)
df=df.loc[5:9] #5행부터 8행까지 추출(북한 데이터)
df.drop('전력량 (억㎾h)',axis=1,inplace=True) #열 삭제
df.set_index('발전 전력별',inplace=True) #행 인덱스 설정
df = df.T #전치
print(df)
print('\n')
df=df.rename(columns={'합계':'총발전량'}) #열 이름 변경
df['총발전량 - 1년'] = df['총발전량'].shift(1) #열 추가, shift(1): 1행씩 뒤로
df['증감률'] = ((df['총발전량']/df['총발전량 - 1년']) - 1) * 100 #열 추가(전년 대비 변동율)
print(df)
#그래프 출력
plt.style.use('ggplot')
plt.rcParams['axes.unicode_minus']=False #마이너스 부호 출력 설정
'''matplotlib은 -(minus) 기호를 표시할 때 
unicode minus(U+2212)를 ASCII hypen(U+002D) 보다 우선적으로 사용함.
plt.rcParams["axes.unicode_minus"] = False 를 통해 ASCII hypen을 우선 사용하도록 변경'''
ax1 = df[['수력','화력']].plot(kind='bar',figsize=(20,10),width=0.7,stacked=True) #세로형 막대 그래프, 누적O
ax2=ax1.twinx() #쌍둥이 axe 객체
ax2.plot(df.index,df.증감률,ls='--',marker='o',markersize=20,color='g',label='전년대비 증감률(%)') #선 그래프
ax1.set_ylim(0,500)
ax2.set_ylim(-50,50)
ax1.set_xlabel('연도',size=20)
ax1.set_ylabel('발전량(억kWh)',size=20)
ax2.set_ylabel('전년 대비 증감률(%)')
plt.title('북한 전력 발전량(1990~2016)',size=30)
ax1.legend(loc='upper left')
plt.show()


#%% 히스토그램

'''
x축: 같은 크기의 여러 구간
y축: 각 구간에 속하는 데이터 값의 개수(빈도)

plot(kind='hist')
'''

#예제4-19
#csv파일을 데이터프레임으로 변환, header->열 이름: 정수(0, 1, 2, ...)
df = pd.read_csv(r"C:\Users\sungyedam\Desktop\study\파이썬 스터디\3주차\part4\auto-mpg.csv",header=None)
df.columns = ['mpg','cylinders','displacement','horsepower','weight','acceleration','model year',
             'origin','name'] #열 이름 지정
plt.style.use('classic') #그래프 스타일
#히스토그램 출력, bins: 구간 개수
df['mpg'].plot(kind='hist',bins=10,color='coral',figsize=(10,5)) 
plt.title('Histogram')
plt.xlabel('mpg')
plt.show()


#%% 산점도

'''
산점도: 2개의 연속 변수를 각각 x축, y축에 놓고 데이터 값이 위치하는 (x, y)좌표를 점으로 표시

plot(kind='scatter')
'''

#예제4-20
#csv파일을 데이터프레임으로 변환, header->열 이름: 정수(0, 1, 2, ...)
df = pd.read_csv(r"C:\Users\sungyedam\Desktop\study\파이썬 스터디\3주차\part4\auto-mpg.csv",header=None)
df.columns = ['mpg','cylinders','displacement','horsepower','weight','acceleration','model year',
             'origin','name'] #열 이름 지정
plt.style.use('default') #그래프 스타일
#산점도 출력(s: 점의 크기)
df.plot(kind='scatter', x='weight',y='mpg',c='coral',s=10,figsize=(10,5))
plt.title('Scatter Plot - mpg vs weight')
plt.show()

#예제4-21
#실린더 개수의 상대적 비율을 계산하여 시리즈 생성
cylinders_size = df.cylinders/df.cylinders.max() * 300
#점의 크기 -> 실린더 개수 (실린더 개수가 많으면 점의 크기가 크게 찍힘)
df.plot(kind='scatter', x='weight',y='mpg',c='coral',s=cylinders_size,figsize=(10,5),alpha=0.3)
plt.title('Scatter Plot - mpg-weight-cylinders')
plt.show()

#예제4-22
#산점도 출력(cmap: 색상을 정함)
df.plot(kind='scatter',marker='+', x='weight',y='mpg',c=cylinders_size,cmap='viridis',s=50, figsize=(10,5),alpha=0.3)
#그림 파일로 저장
plt.savefig(r"C:\Users\sungyedam\Desktop\study\파이썬 스터디\3주차\scatter.png")
#transparent=True -> 배경 투명
plt.savefig(r"C:\Users\sungyedam\Desktop\study\파이썬 스터디\3주차\scatter_transparent.png",transparent=True)
plt.show()
#콘솔창 위 Plots, 우클릭 -> save plot as


#%% 파이 차트(원 차트)

#plot(kind='pie')

#예제4-23
#csv파일을 데이터프레임으로 변환, header->열 이름: 정수(0, 1, 2, ...)
df = pd.read_csv(r"C:\Users\sungyedam\Desktop\study\파이썬 스터디\3주차\part4\auto-mpg.csv",header=None)
df.columns = ['mpg','cylinders','displacement','horsepower','weight','acceleration','model year',
             'origin','name'] #열 이름 지정
df['count']=1 #열 추가
#groupby(): df의 모든 데이터를 'origin' 열 값을 기준으로 3개의 그룹으로 나눔, sum(): 각 그룹별 데이터를 합함
df_origin = df.groupby('origin').sum()
print(df_origin.head()) #origin 값이 1 또는 2 또는 3인 데이터들을 합함, count->개수 카운트
df_origin.index=['USA','EU','JPN'] #행 인덱스 지정
print(df_origin.head())
#그래프 출력
plt.style.use('default')
df_origin['count'].plot(kind='pie',figsize=(7,5),
                        autopct='%1.1f%%', #퍼센트 표시(문자열 포맷팅, 소수점 이하 첫째자리까지 표기)
                         startangle=10,    #시작 각도
                         colors=['r','g','b'])
plt.title('Model Origin',size=20)
plt.axis('equal') #파이 차트의 비율을 같게 조정(원에 가깝게 조정)
plt.legend(labels=df_origin.index,loc='best')
plt.show()


#%% 박스 플롯

''' 최소값, 1분위값(25%), 중간값, 3분위값(75%), 최대값 제공

boxplot()'''

#예제4-24
#csv파일을 데이터프레임으로 변환, header->열 이름: 정수(0, 1, 2, ...)
df = pd.read_csv(r"C:\Users\sungyedam\Desktop\study\파이썬 스터디\3주차\part4\auto-mpg.csv",header=None)
df.columns = ['mpg','cylinders','displacement','horsepower','weight','acceleration','model year',
             'origin','name'] #열 이름 지정
plt.style.use('seaborn-poster')
plt.rcParams['axes.unicode_minus'] = False #마이너스 부호 - ASCII hypen을 우선 사용하도록 변경
#matplotlib 한글 폰트 오류 문제 해결
from matplotlib import font_manager, rc
font_path = r"C:\Users\sungyedam\Desktop\study\파이썬 스터디\3주차\part4\malgun.ttf" #폰트 파일
font_name = font_manager.FontProperties(fname=font_path).get_name() #폰트 이름을 얻어옴
rc('font',family=font_name) #폰트 적용
fig = plt.figure(figsize=(15,5)) #그림 사이즈
#화면 분할 후 axe 객체 생성
ax1 = fig.add_subplot(1,2,1)
ax2=fig.add_subplot(1,2,2)
#ax1 그래프 그리기(수직)
ax1.boxplot(x=[df[df['origin']==1]['mpg'],
               df[df['origin']==2]['mpg'],
               df[df['origin']==3]['mpg']], 
         labels=['USA', 'EU', 'JAPAN'])
#ax2 그래프 그리기(수평)
ax2.boxplot(x=[df[df['origin']==1]['mpg'],
               df[df['origin']==2]['mpg'],
               df[df['origin']==3]['mpg']], 
         labels=['USA', 'EU', 'JAPAN'],
         vert=False)
ax1.set_title('제조국가별 연비 분포(수직 박스 플롯)')
ax2.set_title('제조국가별 연비 분포(수평 박스 플롯)')
plt.show()
