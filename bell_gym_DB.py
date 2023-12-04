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
for row in result:
    print(row)

ids = 
pwds = 
names = 


# 연결 해제
cursor.close()
conn.close()