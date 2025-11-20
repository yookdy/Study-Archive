import requests
import folium
import os
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

# --- 1. 데이터 수집 (기존 코드 활용) ---
#사고 건수를 확인을 하고 해당하는 적도 위도 위치를 크롬 브라우저로 지도가 열려서 보게 만듦

API_URL = "https://apis.data.go.kr/B552061/frequentzoneBicycle/getRestFrequentzoneBicycle"
service_key = "1WjJK6Pg4uW/fseRRuoa2IKNZ7tywHYK/umqBMWsdWdxp0LYAOmfF+SXV3sdAbG7e15D0dJ7I9QVeiOD5HNzkQ=="

params = {
    "ServiceKey": service_key,
    "searchYearCd": "2024",
    "siDo": "11",      # 서울
    "guGun": "680",    # 강남구
    "type": "json",    # JSON 형식
    "numOfRows": "10", 
    "pageNo": "1",
}

print("데이터 요청 중...")
response = requests.get(API_URL, params=params)

if response.status_code == 200:
    print("요청 성공")
    try:
        data = response.json()
        # 데이터 구조에 따라 items 위치 찾기 (공공데이터 포털 구조 대응)
        items = data.get("items", {}).get("item", [])
        
        # 만약 위 경로에 없으면 다른 경로 시도 (response > body > items > item 구조일 경우)
        if not items and 'response' in data:
             items = data['response']['body']['items']['item']
             
    except Exception as e:
        print("JSON 파싱 오류:", e)
        exit()
else:
    print("요청 실패:", response.status_code)
    exit()

if not items:
    print("데이터가 없습니다.")
    exit()

print(f"2024년 덕양구 자전거 사고 다발 지역: {len(items)}건 확인됨")


# --- 2. Folium으로 지도 생성 ---

# 지도의 중심을 첫 번째 데이터의 좌표로 설정
first_lat = float(items[0]['la_crd'])
first_lon = float(items[0]['lo_crd'])

# 지도 객체 생성 (Zoom 레벨 14)
m = folium.Map(location=[first_lat, first_lon], zoom_start=14)

for item in items:
    lat = float(item['la_crd'])
    lon = float(item['lo_crd'])
    
    # 팝업에 표시할 내용 (HTML 태그 사용 가능)
    popup_content = f"""
    <b>발생일시:</b> {item.get('occrrnc_dt')}<br>
    <b>사망자:</b> {item.get('dth_dnv_cnt')}명<br>
    <b>부상자:</b> {item.get('injpsn_cnt')}명
    """
    
    # 지도에 마커 추가
    folium.Marker(
        location=[lat, lon],
        popup=folium.Popup(popup_content, max_width=300),
        tooltip="사고 지점 클릭",
        icon=folium.Icon(color='red', icon='info-sign')
    ).add_to(m)

# HTML 파일로 저장 (절대 경로 사용 권장)
html_file = os.path.abspath("bicycle_accident_map.html")
m.save(html_file)
print(f"지도 파일 생성 완료: {html_file}")


# --- 3. Selenium으로 크롬 브라우저 실행 ---

print("브라우저를 실행합니다...")

# 브라우저 꺼짐 방지 옵션
chrome_options = Options()
chrome_options.add_experimental_option("detach", True) 

# 크롬 드라이버 자동 설치 및 실행
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

# 저장된 HTML 파일 열기 (file:// 프로토콜 사용)
driver.get("file://" + html_file)

print("완료! 브라우저를 확인하세요.")