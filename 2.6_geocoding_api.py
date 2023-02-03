'''3 API 활용하여 데이터 수집하기
API: 일반적으로 클라이언트와 서버가 서로 통신할 수 있게 하는 메커니즘
-> API를 통해 가져온 데이터를 판다스 데이터프레임으로 손쉽게 변환할 수 있음
클라이언트: 요청을 보내는 애플리케이션, ex) 클라이언트: 모바일 앱
서버: 응답을 보내는 애플리케이션, ex) 서버: 기상청의 날씨 데이터'''

#<예제 2-6> 구글 지오코딩 위치 정보
# -*- coding: utf-8 -*-

## google 지오코딩 API 통해 위도, 경도 데이터 가져오기 

# 라이브러리 가져오기
import googlemaps
import pandas as pd

my_key = "AIzaSyBaOmju9qD4kxSR2HJ4vlMzcn6mxXdmOpE"

# 구글맵스 객체 생성하기
maps = googlemaps.Client(key=my_key)  # my key값 입력

lat = []  #위도
lng = []  #경도

# 위치를 찾을 장소(또는 주소) 리스트
places = ["서울시청", "국립국악원", "해운대해수욕장"]

i=0
for place in places:   #for 구문: places에 담겨있는 정보들을 for 문으로 하나씩 딕셔너리자료형으로 넣어줌
    i = i + 1
    try:    #try except 코드: try 부분 -> 실행할 코드, except 부분 -> 예외가 발생했을 때 처리하는 코드
        print(i, place)
        # 지오코딩 API 결과값 호출하여 geo_location 변수에 저장
        '''지오코딩: 주소 (ex. '1600 Amphitheatre Parkway, Mountain View, CA') 를 지리적 좌표 (위도 37.423021, 경도 -122.083739) 로 변환하는 것을 말함'''
        geo_location = maps.geocode(place)[0].get('geometry')   #결과가 리스트의 첫 번째 원소로 전부 듣어가 있기 때문에 [0]으로 잡아서 좌표를 찾음
        lat.append(geo_location['location']['lat'])   #append는 덧붙인다는 뜻으로 괄호( ) 안에 값을 입력하면 새로운 요소를 array 맨 끝에 객체로 추가함
        lng.append(geo_location['location']['lng'])
        
    except:   #좌표를 가져오지 못한경우 아래 것들 실행
        lat.append('')
        lng.append('')
        print(i)

'''try~except문 사용 이유: 다른 방법으로 지오코딩을 시도했을 때, API 요청과 좌표 변환이 실패하여 위도, 경도가 0으로 저장된 경우가 2000건이 넘는 참사가 일어남
-> 이를 방지하기 위함'''

# 데이터프레임으로 변환하기
df = pd.DataFrame({'위도':lat, '경도':lng}, index=places)
print('\n')
print(df)
