
#get의 방식
'''
import requests

x=requests.get('https://w3schools/.com')
print(x.status_code)
'''
#200출력 서버가 받은거임

'''
import requests
# 서버로 보낼 데이터 준비
data = {
    'name': 'Hong',
    'age': 23,
    'msg': 'Hello world!',
}
# POST 방식으로 데이터를 실어서 요청
response = requests.post('https://api.example.com/data', data=data)
'''
# import requests
# url = "https://example.com/upload" # 서버 URL
# data = {"key1": "value1", "key2": "value2"} # 일반 폼 데이터
# json_data = {"name": "John", "age": 30} # JSON 데이터
# # 파일 읽기
# file_path = "path/to/your/file.txt" # 파일 경로
# with open(file_path, 'rb') as file:
#     files = {'file': file}
# # POST 요청 전송
# response = requests.post(
#     url,
#     data=data,# 폼 데이터
#     json=json_data,# JSON 데이터
#     files=files# 파일
# )
# # 응답 확인
# print("Status Code:", response.status_code)

#https://httpbin.org/put 데이터가 보내지는 확인을 하는 주소 잘 갓다고 옴
'''

import requests

data = {"msg": "Hello!"}
r = requests.put("https://httpbin.org/put", data=data)

print(r.status_code)
print(r.json())


'''
# import requests

# data = {"name": "Hong", "age": 23}
# r = requests.post("https://httpbin.org/post", data=data)

# print(r.status_code)
# print(r.json()) 


#delete 방식
'''
import requests

x = requests.delete('https://w3schools.com/python/demopage.php')

print(x.status_code)
print(x.text)

'''
import requests

# JSON 데이터 준비
data = {
    'key': 'value',
    'name': 'Hong',
    'age': 23
}

# POST 방식으로 json 데이터를 실어서 요청하기
response = requests.post(
    'https://httpbin.org/post',
    json=data
)

print("Status Code:", response.status_code)
print("POST JSON:", response.json())


#세션을 이용한 로그인 유지
#쿠키로 저장을 하면서 기간동안 유지하게 만들어줌
#세션을 유지하기 위해서 쿠키를 사용