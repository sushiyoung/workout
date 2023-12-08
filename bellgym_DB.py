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
select_data_user = "SELECT * FROM user"
select_data_workout = "SELECT * FROM workout"




# 결과 출력1
cursor.execute(select_data_user)
result1 = cursor.fetchall()

# 결과 출력2
cursor.execute(select_data_workout)
result2 = cursor.fetchall()


ids =[]
pwds =[]
names =[]

for row in result1:
    ids.append(row[0]),
    pwds.append(row[1]),
    names.append(row[2])
    
    
print("*"*10 + "user informain" + "*"*10)
print(ids)
print(pwds)
print(names)


index_count =[]
ids_workout =[]
date =[]
prepare =[]
main =[]
sub =[]
wod =[]
buildup =[]


for row in result2:
    index_count.append(row[0])
    ids_workout.append(row[1])
    date.append(row[2])
    prepare.append(row[3])
    main.append(row[4])
    sub.append(row[5])
    wod.append(row[6])
    buildup.append(row[7])

print("*"*10 + "workout informain" + "*"*10)
print(index_count)
print(ids_workout)
print(date)
print(prepare)
print(main)
print(sub)
print(wod)
print(buildup)




# 연결 해제
cursor.close()
conn.close()