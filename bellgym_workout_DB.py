import constant_DB
from db_connect import BellGymDB
from user import User
from workout import Workout
from datetime import datetime




def workout_input(prompt):
    return input(f"{prompt}을 입력하세요: ")


def connect_bellgym_db():
    db = BellGymDB()
    db.connect()
    return db

    
def main():
    db = connect_bellgym_db()
    while True:
        print("1. 회원가입")
        print("2. 회원정보 보기")
        print("3. 회원정보 수정")
        print("4. 회원정보 삭제")
        print("5. 운동기록 입력")
        print("6. 운동기록 검색")
        print("7. 운동기록 수정")
        print("8. 운동기록 삭제")
        
        print("-1. 종료")
        choice = int(input(("입력을 선택하세요 (1번~9번: )")))

        if choice == constant_DB.SIGNUP_USER:
            id = workout_input("ID")
            pwd = workout_input("PWD")
            name = workout_input("Name")
            record = (id, pwd, name)
            db.insert(
                "insert into user (id, password, name) values (%s, %s, %s)", record)
            print("*"*20+f"{name}님의 ID인 {id}가 등록되었습니다!!!"+"*"*20)
        
    
        elif choice == constant_DB.SELECT_USER:
            try:
                id = workout_input("검색할 ID")
                result1 = db.selectAll("select * from user")

                if not result1:
                    print("등록된 회원이 아닙니다.")
                    continue
                
                users = []
                for row in result1:
                    u = User(row[0], row[1], row[2])
                    users.append(u) 
        
                print("*"*10 + f"{id}님의 user informain" + "*"*10)
                sorted_users = [u for u in users if u.id == id]

                if not sorted_users:
                    print(f"{id}님은 등록되어있지 않은 회원입니다.")
                    continue

                for u in sorted_users:
                    u.introduceMyself()
                          
            except Exception as e:
                print(f"Error: {e}")

        elif choice == constant_DB.UPDATE_USER:
            id = workout_input("ID")
            pwd = workout_input("PWD")
            new_pwd = workout_input("NEW PWD")
            record = (new_pwd, id, pwd)
            db.update(
                "update user set password = %s where id = %s and password = %s", (
                    record)
            )
            print(f"{id}님의 비밀번호가 성공적으로 변경되었습니다.")

        elif choice == constant_DB.DELETE_USER:
            id = workout_input("ID")
            pwd = workout_input("PWD")
            name = workout_input("Name")
            record = (id, pwd, name)
            db.delete(
                "delete from user where id = %s and password = %s and name = %s", (
                    record)
            )
            print("*"*20+f"{name}님의 ID인 {id}가 삭제되었습니다!!!"+"*"*20)
        
        elif choice == constant_DB.INSERT_WORKOUT:
            try:
                id = workout_input("ID")

                double_check_query = f"select *from user where id = '{id}'"
                double_check_result = db.selectAll(double_check_query)

                if not double_check_result:
                    print("*"*10 + "회원가입 먼저 진행해주세요" + "*"*10)
                    continue

                name = workout_input("이름")
                year, month, day = map(int, workout_input("날짜 (년-월-일):").split('-'))
                prepare = workout_input("prepare")
                mainwork = workout_input("main")
                sub = workout_input("sub")
                wod = workout_input("WOD")
                buildup = workout_input("Buildup")
                date = datetime(year, month, day).date()
                record = (id, date, prepare, mainwork, sub, wod, buildup)
            
                db.insert(
                    "insert into workout (id, date, prepare, main, sub, wod, buildup) values (%s, %s, %s, %s, %s, %s,%s)", record)
                print("*"*20+f"{name}님의 WORKOUT 등록되었습니다!!!"+"*"*20)
            except Exception as e:
                print(f"Error: {e}")

        elif choice == constant_DB.SEARCH_WORKOUT:
            try:    
                id = workout_input("검색할 ID")
                result1 = db.selectAll(f"select * from workout where id = '{id}'")
        
                if not result1:
                    print(f"{id}님의 운동기록이 존재하지 않습니다.")
                    return
        
                print("*"*10 + f"{id}님의 workout 날짜 리스트" + "*"*10)
                date_list = set(row[2] for row in result1)
                for date in date_list:
                    print(date)
                print("*"*53)

                date_input = workout_input("검색할 날짜(년-월-일): ")
        
                workouts = []
                for row in result1:
                    u = Workout(row[1], row[2], row[3], row[4], row[5], row[6])
                    workouts.append(u)
        
                print("*"*10 + f"{id}님의 workout informain" + "*"*10)
                
                sorted_workouts = [u for u in workouts if u.date.strftime('%Y-%m-%d') == date_input]
                
                if not sorted_workouts:
                    print(f"{id}님의 {date} 날짜에 대한 운동기록이 존재하지 않습니다.")
                    return
                
                for u in sorted_workouts:
                    u.introduceWorkout()
    
            except Exception as e:
                print(f"Error: {e}")
        
        elif choice == constant_DB.UPDATE_WORKOUT:
            try:
                id = workout_input("ID")
                
                result1 = db.selectAll(f"select * from workout where id = '{id}'")

                if not result1:
                    print(f"{id}님의 운동기록이 존재하지 않습니다.")
                    return

                print("*"*10 + f"{id}님의 workout 날짜 리스트" + "*"*10)
                date_list = set(row[2] for row in result1)
                for date in date_list:
                    print(date)
                
                
                date_input = workout_input("수정할 날짜(년-월-일): ")

                workouts = []
                for row in result1:
                    u = Workout(row[1], row[2], row[3], row[4], row[5], row[6])
                    workouts.append(u)

                sorted_workouts = [u for u in workouts if u.date.strftime('%Y-%m-%d') == date_input]

                if not sorted_workouts:
                    print(f"{date_input}에 대한 운동 기록이 존재하지 않습니다.")
                    return

                print("*"*10 +f"{date_input}의 workout 정보" + "*" *10)

                for u in sorted_workouts:
                    u.introduceWorkout()

                prepare = workout_input("수정할 prepare")
                mainwork = workout_input("수정할 mainwork")
                wod = workout_input("수정할 wod")
                buildup = workout_input("수정할 buildup")
                record =(prepare, mainwork, wod, buildup,id, date_input)
                
                recheck = input("정말로 수정하시겠습니까? (1: 예, 2: 아니요)")
                if recheck == '1':
                    query = (
                            "UPDATE workout SET "
                            f"prepare = %s, "
                            f"mainwork = %s, "
                            f"wod = %s, "
                            f"buildup = %s "
                            f"WHERE id = %s AND date = %s"
                            )

                    db.update(query, record)
                    print(f"{id}님의 {date_input} 날짜의 운동이 성공적으로 수정되었습니다.")
                elif recheck == '2':
                    print("수정을 취소합니다.")
                else:
                    print("다시입력하세요!!!!")
            except Exception as e:
                print(f"Error: {e}")
        
        elif choice == constant_DB.DELETE_WORKOUT:
            try:
                id = workout_input("ID")
                pwd = workout_input("pwd")
                
                double_check_query = f"select *from user where id = '{id}' AND password = '{pwd}'"
                double_check_result = db.selectAll(double_check_query)

                if not double_check_result:
                    print("ID 또는 비밀번호가 올바르지 않습니다.")
                    return
                
                
                result1 = db.selectAll(f"select * from workout where id = '{id}'")

                if not result1:
                    print(f"{id}님의 운동기록이 존재하지 않습니다.")
                    return

                print("*"*10 + f"{id}님의 workout 날짜 리스트" + "*"*10)
                date_list = set(row[2] for row in result1)
                for date in date_list:
                    print(date)
                
                date_input = workout_input("삭제할 날짜(년-월-일): ")

                workouts = []
                for row in result1:
                    u = Workout(row[1], row[2], row[3], row[4], row[5], row[6])
                    workouts.append(u)

                sorted_workouts = [u for u in workouts if u.date.strftime('%Y-%m-%d') == date_input]

                if not sorted_workouts:
                    print(f"{date_input}에 대한 운동 기록이 존재하지 않습니다.")
                    return

                print("*"*10 +f"{date_input}의 workout 정보" + "*" *10)

                for u in sorted_workouts:
                    u.introduceWorkout()

                recheck = input("정말로 삭제하시겠습니까? (1: 예, 2: 아니요)")
                if recheck == '1':
                    query = "delete from workout where id = %s and date =%s"
                    record =(id, date_input)
                    db.delete(query, record)
                    print(f"{id}님으 {date_input} 날짜의 운동이 성공적으로 삭제되었습니다.")
                elif recheck =='2':
                    print("삭제를 취소합니다")

                else:
                    print("다시 입력하세요!!!!") 
            
            except Exception as e:
                print(f"Error: {e}")

        elif choice == constant_DB.FINISH_WORKOUT:
            print("*"*30+"프로그램을 종료합니다."+"*"*30+"\n")
            db.close()
            break
           

if __name__ == "__main__":
    main()
