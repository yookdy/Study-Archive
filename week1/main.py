import pandas as pd

# data=[10,20,30,40,50]
# s=pd.Series(data, index=[1,2,3,4,5])#series라는 객체를 생성해서 data를 넣어줌
# s1=[1,2,3,4,5]

# va=s[2]
# f1=s>20
# f2= s[f1]
# re=s+s1
# print(f1)#
# print(f2)#true인 값만 출력해서 series로 만들어줌
# print(re)

dat = {
    'Name': ['John', 'Anna', 'Peter', 'Linda'],
    'Age': [28, 24, 35, 32],
    'City': ['New York', 'Paris', 'Berlin', 'London']
}
df = pd.DataFrame(dat)
# print(df)
# na=df['Name']
# print(type(na))
# print(na)


# dat = {
#     'Name': ['John', 'Anna', 'Peter', 'Linda'],
#     'Age': [28, 24, 35, 32],
#     'City': ['New York', 'Paris', 'Berlin', 'London']
# }
# df = pd.DataFrame(dat)
# co=df['Age']>30
# print(co)
# ad1=df[co]
# ad2=df[df['Age']>30]
# print(ad1)


# df=pd.read_csv('data.csv',sep=',')
# print(df.head())
# 데이터 프레임의 정보 출력
print(df.info())
# 데이터 프레임의 통계 요약 출력
print(df.describe())
# 첫 n개 데이터만 보기
print(df.head(5)) # 첫 5줄만 보기
# 마지막 n개 데이터만 보기
print(df.tail(2)) # 마지막 2줄만 보기


names = df['Name']
print(f'이름: \n{names}\n')#포멧으로 이름만 나오게 하는거

# 조건에 맞는 데이터 필터링 (예: Age가 30보다 큰 경우)
adults = df[df['Age'] > 30]#df['Age']시리즈
print(adults)

df2=pd.read_csv('data.tsv',sep='\t')
df2.sort_values(by='Age',inplace=True)#ascending은 오름차순----정렬을 하는 방법
print(df2)


#merge를 이용해서 정보를 통합하는 방식
employees=pd.read_csv('employees.csv')
sales=pd.read_csv('sales.tsv',sep='\t')
merged=pd.merge(employees,sales, on='EmployeeID')
print(merged.head())

#데이터 집계
emp=pd.read_csv('employees_100.csv')
grouped=emp.groupby('Department').agg('Age').mean()
print(grouped)

#그래프 시각화-----나중에 실행해보기
#emp = pd.read_csv('employees_100.csv’)
emp['Age'].hist()
# plt.xlabel('Age')
# plt.ylabel('Frequency')
# plt.savefig("파일 이름")
# plt.title('Age Distribution')
# plt.show()

