#네이버 뉴스 내용 크롤링

import requests
# 네이버 뉴스 정치면 주소
url = 'https://news.naver.com/section/100'
response = requests.get(url) #request를 get 메서드를 이용함 
print(response.status_code) #내용을 변수 저장
print(response.text) #내용 출력
