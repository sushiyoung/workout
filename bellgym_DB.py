import mysql.connector

# MySQL 연결 정보 설정
config = {
    'host': '127.0.0.1',
    'user': 'root',
    'password': '1234',
    'database': 'bellgym'
}

# MySQL 연결 객체 생성
conn = mysql.connector.connect(**config)

# 커서 생성
cursor = conn.cursor()

# 예제: 데이터 조회
select_data_query = "SELECT * FROM user"
cursor.execute(select_data_query)



# 결과 출력
result = cursor.fetchall()

#id,pwds,names 를 각각 출력
# 반복문 돌면서 list에 넣어야함

ids =[]
pwds =[]
names =[]

for row in result:
    ids.append(row[0]),
    pwds.append(row[1]),
    names.append(row[2])
    
    
print(ids)
print(pwds)
print(names)


# 연결 해제
cursor.close()
conn.close()