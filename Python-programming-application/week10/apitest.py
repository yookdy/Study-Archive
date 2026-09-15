# File: api.py
import requests

API_URL = "https://apis.data.go.kr/B552061/frequentzoneBicycle/getRestFrequentzoneBicycle"

# 반드시 Encoding된 인증키 그대로 사용
service_key = "1WjJK6Pg4uW/fseRRuoa2IKNZ7tywHYK/umqBMWsdWdxp0LYAOmfF+SXV3sdAbG7e15D0dJ7I9QVeiOD5HNzkQ=="

#쿼리 스트링을 이용을 하는데 딕셔너리로 상세 정보를 넣어줌
params = {
    "ServiceKey": service_key,
    "searchYearCd": "2024",
    "siDo": "11",      # 경기도
    "guGun": "680",    # 덕양구
    "type": "json",    # 수신할 데이터 구조
    "numOfRows": "10", # 한 페이지 결과 수
    "pageNo": "1",
}


# API 호출
response = requests.get(API_URL, params=params) #params를 안쓸려면 API_URL에 ?붙여서 다 붙여야함 API_URL는 엔드포인트
#검색을 해서 정보를 저장을 하는게 response를 역활을 하는 거임

#방어 코드 역활을 하는 거임
if response.status_code == 200:
    print("요청 성공:", response.url)
    data = response.json() #response를 json에서 딕셔너리 형태로 가져오는 거임
else:
    print("요청 실패:", response.status_code, response.text)
    exit()

# 데이터 파싱
items = data.get("items", {}).get("item", []) #데이터의 정보를 data.get으로 가져오는 거
#items에서 item을 가져오는 거임

print(f"\n 2024년 덕양구 자전거 사고 건수: {len(items)}건")

# 주요 정보 출력
#for문으로 item을 쭉 돌리는 거임
for idx, item in enumerate(items[:10], 1):  # 첫 10건만 출력
    print(f"\n--- 사고 {idx} ---")
    print(f"발생일시: {item.get('occrrnc_dt')}")
    print(f"사망자수: {item.get('dth_dnv_cnt')}")
    print(f"부상자수: {item.get('injpsn_cnt')}")
    print(f"위도: {item.get('la_crd')}")
    print(f"경도: {item.get('lo_crd')}")
    print(f"좌표: {item.get('la_crd')}, {item.get('lo_crd')}")
    
    # 네이버 지도 URL 구성
    lat = float(item.get("la_crd"))
    lon = float(item.get("lo_crd"))
    naver_url = f"https://map.naver.com/v5/search/{lat},{lon}"
    print(f"사고 {idx}: {naver_url}")
