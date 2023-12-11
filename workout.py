import os
import glob
import shutil
import constant
from db_connect import BellGymDB
from user import User

global file_path


def workout_input(prompt):
    return input(f"{prompt}을 입력하세요: ")


def get_file_path(name):
    abspath = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(abspath, f'Bellgym_record{name}')


def get_file_path_v2(id):
    abspath = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(abspath, f'Bellgym_record/{id}')


def createFolder(name):
    try:
        folder_path = get_file_path(name)
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)
            print("*"*30+f"{name} 폴더가 생성되었습니다."+"*"*30)
        else:
            print("*"*30+f"{name} 폴더가 이미 존재합니다."+"*"*30)
    except OSError:
        print('Error: Creating directory.' + folder_path)


def createFolder_v2(id):
    try:
        folder_path = get_file_path_v2(id)
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)
            print("*"*30+f"{id} 폴더가 생성되었습니다."+"*"*30)
        else:
            print("*"*30+f"{id} 폴더가 이미 존재합니다."+"*"*30)
    except OSError:
        print('Error: Creating directory.' + folder_path)


def write_file(year, month, day, prepare, mainwork, wod, bulidup, name):
    try:
        folder_path = get_file_path(name)
        file_name = f"{name}-{year}-{month}-{day}.txt"
        file_workout = (
            f"이름 : {name}\n"
            f"입력날짜는 : {year}년 {month}월 {day}일 입니다.\n"
            f"오늘의 prepare는 : {prepare}\n"
            f"오늘의 mainwork은 : {mainwork}\n"
            f"오늘의 wod는 : {wod}\n"
            f"오늘의 buildup은 {bulidup}\n"
        )
        with open(folder_path + '\\' + file_name, 'w', encoding='utf-8') as f:
            f.write(file_workout)
    except OSError:
        print("Error: file path" + file_name)


def write_file_v2(year, month, day, prepare, mainwork, wod, bulidup, name, id):
    try:
        # folder_path : Bellgym_record/[id]/
        folder_path = get_file_path_v2(id)
        file_name = f"{year}-{month}-{day}.txt"
        file_workout = (
            f"이름 : {name}\n"
            f"입력날짜는 : {year}년 {month}월 {day}일 입니다.\n"
            f"오늘의 prepare는 : {prepare}\n"
            f"오늘의 mainwork은 : {mainwork}\n"
            f"오늘의 wod는 : {wod}\n"
            f"오늘의 buildup은 {bulidup}\n"
        )
        with open(folder_path + '\\' + file_name, 'w', encoding='utf-8') as f:
            f.write(file_workout)
    except OSError:
        print("Error: file path" + file_name)


def read_file(year, month, day, name):
    folder_path = get_file_path(name)
    file_name = f"{name}-{year}-{month}-{day}.txt"
    with open(folder_path + '\\' + file_name, 'r', encoding='utf-8') as f:
        file_workout = f.read()
    print(file_workout)


def read_file_v2(year, month, day, name, id):
    folder_path = get_file_path_v2(id)
    file_name = f"{year}-{month}-{day}.txt"
    with open(folder_path + '\\' + file_name, 'r', encoding='utf-8') as f:
        file_workout = f.read()
    print(file_workout)


def search_file():
    name = workout_input("이름")
    folder_path = get_file_path(name)
    if not os.path.exists(folder_path):
        print("*"*10+f"{name}님의 폴더가 존재하지 않습니다."+"*"*10)
        return

    file_name_list = glob.glob(folder_path + '\\*')
    print("*"*10 + f"{name}님의 대한 리스트 파일이 존재합니다"+"*"*10)
    for f in file_name_list:
        print(f)
    print("\n"+"*"*60)

    year, month, day = workout_input("날짜 (년-월-일):").split('-')
    file_name = f"{name}-{year}-{month}-{day}.txt"

    print("*" * 10 + "이 파일의 대한 결과입니다" + "*" * 10+"\n")

    if os.path.isfile(folder_path + '\\' + file_name):
        with open(folder_path + '\\' + file_name, 'r', encoding='utf-8') as f:
            file_workout = f.read()
            print(file_workout)
    else:
        print(f"{name}님의 운동기록이 없습니다")

    print("\n"+"*"*60)


def search_file_v2():
    id = workout_input("id")
    folder_path = get_file_path_v2(id)
    if not os.path.exists(folder_path):
        print("*"*10+f"{id}님의 폴더가 존재하지 않습니다."+"*"*10)
        return constant.NOT_FOUND_FOLDER

    file_id_list = glob.glob(folder_path + '\\*')
    print("*"*10 + f"{id}님의 대한 리스트 파일이 존재합니다"+"*"*10)
    for f in file_id_list:
        print(f)
    print("\n"+"*"*60)

    year, month, day = workout_input("날짜 (년-월-일):").split('-')
    file_name = f"{year}-{month}-{day}.txt"

    print("*" * 10 + "이 파일의 대한 결과입니다" + "*" * 10+"\n")

    if os.path.isfile(folder_path + '\\' + file_name):
        with open(folder_path + '\\' + file_name, 'r', encoding='utf-8') as f:
            file_workout = f.read()
            print(file_workout)
    else:
        print(f"{id}님의 운동기록이 없습니다")

    print("\n"+"*"*60)


def update_file():
    try:
        name = workout_input("수정할 사람의 이름을 입력하세요")
        folder_path = get_file_path(name)
        if not os.path.exists(folder_path):
            print("*"*10+f"{name}님의 폴더가 존재하지 않습니다."+"*"*10)
            return
        file_name_list = glob.glob(folder_path + '\\*')
        print("*"*10 + f"{name}님의 대한 리스트 파일이 존재합니다"+"*"*10)
        for f in file_name_list:
            print(f)
        print("\n"+"*"*60)

        year, month, day = workout_input("수정할 날짜 (년-월-일):").split('-')
        file_name = f"{name}-{year}-{month}-{day}.txt"

        if os.path.isfile(folder_path + '\\' + file_name):
            print("1. Prepare 수정")
            print("2. Mainwork 수정")
            print("3. WOD 수정")
            print("4. Buildup 수정")
            choice = int(input(("수정할 부분을 선택하세요 (1번/2번/3번/4번: )")))

            with open(folder_path + '\\' + file_name, 'a', encoding='utf-8') as f:
                f.write("\n\n*** 추가 기록 ***\n")
                f.write(f"날짜: {year}-{month}-{day}\n")

                if choice == 1:
                    prepare = workout_input("수정할 prepare")
                    f.write(f"Prepare: {prepare}\n")
                elif choice == 2:
                    mainwork = workout_input("수정할 mainwork")
                    f.write(f"Mainwork: {mainwork}\n")
                elif choice == 3:
                    wod = workout_input("수정할 WOD")
                    f.write(f"WOD: {wod}\n")
                elif choice == 4:
                    buildup = workout_input("수정할 Buildup")
                    f.write(f"Buildup: {buildup}\n")
                else:
                    print("올바르지 않은 선택입니다. 업데이트를 취소합니다.")
                    return

            print(f"{name}님의 운동기록이 성공적으로 업데이트되었습니다.")
        else:
            print(f"{name}님의 해당 날짜에 대한 기존 운동기록이 존재하지 않습니다.")
    except OSError:
        print("Error : updatefile" + folder_path)


def update_file_v2():
    try:
        id = workout_input("수정할 사람의 ID을 입력하세요")
        folder_path = get_file_path_v2(id)
        if not os.path.exists(folder_path):
            print("*"*10+f"{id}님의 폴더가 존재하지 않습니다."+"*"*10)
            return constant.NOT_FOUND_FOLDER
        file_id_list = glob.glob(folder_path + '\\*')
        print("*"*10 + f"{id}님의 대한 리스트 파일이 존재합니다"+"*"*10)
        for f in file_id_list:
            print(f)
        print("\n"+"*"*60)

        year, month, day = workout_input("수정할 날짜 (년-월-일):").split('-')
        file_name = f"{year}-{month}-{day}.txt"

        if os.path.isfile(folder_path + '\\' + file_name):
            print("1. Prepare 수정")
            print("2. Mainwork 수정")
            print("3. WOD 수정")
            print("4. Buildup 수정")
            choice = int(input(("수정할 부분을 선택하세요 (1번/2번/3번/4번: )")))

            with open(folder_path + '\\' + file_name, 'a', encoding='utf-8') as f:
                f.write("\n\n*** 추가 기록 ***\n")
                f.write(f"날짜: {year}-{month}-{day}\n")

                if choice == 1:
                    prepare = workout_input("수정할 prepare")
                    f.write(f"Prepare: {prepare}\n")
                elif choice == 2:
                    mainwork = workout_input("수정할 mainwork")
                    f.write(f"Mainwork: {mainwork}\n")
                elif choice == 3:
                    wod = workout_input("수정할 WOD")
                    f.write(f"WOD: {wod}\n")
                elif choice == 4:
                    buildup = workout_input("수정할 Buildup")
                    f.write(f"Buildup: {buildup}\n")
                else:
                    print("올바르지 않은 선택입니다. 업데이트를 취소합니다.")
                    return

            print(f"{id}님의 운동기록이 성공적으로 업데이트되었습니다.")
        else:
            print(f"{id}님의 해당 날짜에 대한 기존 운동기록이 존재하지 않습니다.")
    except OSError:
        print("Error : updatefile" + folder_path)


def Delete_file():
    try:
        name = workout_input("삭제할 사람의 이름을 입력하세요")
        folder_path = get_file_path(name)

        if not os.path.exists(folder_path):
            print("*"*10+f"{name}님의 폴더가 존재하지 않습니다."+"*"*10)
            return
        print("*"*30)
        print("삭제 옵션을 선택하세요:")
        print("1. 폴더 전체 삭제:")
        print("2. 특정 날짜txt 파일 삭제 ")
        print("*"*30)

        option_Choice = int(input("선택 (1번/2번/)"))

        if option_Choice == 1:
            recheck_delete = int(
                input(f"정말 {name}의 폴더를 삭제하시겠습니까? (1/예 2/아니오) : "))
            if recheck_delete == 1:
                shutil.rmtree(folder_path)
                print("*"*30 + f"{name}의 폴더가 삭제되었습니다."+"*"*30)
                return
            else:
                print("*"*30 + f"{name}의 폴더삭제를 취소합니다."+"*"*30)
        elif option_Choice == 2:
            file_name_list = glob.glob(folder_path + '\\*')
            print("*"*10 + f"{name}님의 대한 리스트 파일이 존재합니다"+"*"*10)

            for f in file_name_list:
                print(f)
            print("\n"+"*"*60)

        year, month, day = workout_input("삭제할 날짜 (년-월-일):").split('-')
        file_name = f"{name}-{year}-{month}-{day}.txt"

        if os.path.exists(folder_path + '\\' + file_name):
            recheck_delete = int(
                input(f"정말 {file_name}의 파일을 삭제하시겠습니까? (1/예 2/아니오) : "))
            if recheck_delete == 1:
                os.remove(folder_path + '\\' + file_name)
                print("*"*10+f"{file_name} 파일이 삭제되었습니다."+"*"*10)

            else:
                print("파일 삭제가 취소되었습니다.")

    except ValueError:
        print("숫자입력 다시하세요")

    except OSError:
        print("Error : 오류발생")


def Delete_file_v2():
    try:
        id = workout_input("삭제할 ID를 입력하세요")
        folder_path = get_file_path_v2(id)

        if not os.path.exists(folder_path):
            print("*"*10+f"{id}님의 폴더가 존재하지 않습니다."+"*"*10)
            return constant.NOT_FOUND_FOLDER
        print("*"*30)
        print("삭제 옵션을 선택하세요:")
        print("1. 폴더 전체 삭제:")
        print("2. 특정 날짜txt 파일 삭제 ")
        print("*"*30)

        option_Choice = int(input("선택 (1번/2번/)"))

        if option_Choice == 1:
            recheck_delete = int(
                input(f"정말 {id}의 폴더를 삭제하시겠습니까? (1/예 2/아니오) : "))
            if recheck_delete == 1:
                shutil.rmtree(folder_path)
                print("*"*30 + f"{id}의 폴더가 삭제되었습니다."+"*"*30)
                return
            else:
                print("*"*30 + f"{id}의 폴더삭제를 취소합니다."+"*"*30)
        elif option_Choice == 2:
            file_id_list = glob.glob(folder_path + '\\*')
            print("*"*10 + f"{id}님의 대한 리스트 파일이 존재합니다"+"*"*10)

            for f in file_id_list:
                print(f)
            print("\n"+"*"*60)

        year, month, day = workout_input("삭제할 날짜 (년-월-일):").split('-')
        file_name = f"{year}-{month}-{day}.txt"

        if os.path.exists(folder_path + '\\' + file_name):
            recheck_delete = int(
                input(f"정말 {file_name}의 파일을 삭제하시겠습니까? (1/예 2/아니오) : "))
            if recheck_delete == 1:
                os.remove(folder_path + '\\' + file_name)
                print("*"*10+f"{file_name} 파일이 삭제되었습니다."+"*"*10)

            else:
                print("파일 삭제가 취소되었습니다.")

    except ValueError:
        print("숫자입력 다시하세요")

    except OSError:
        print("Error : 오류발생")


def connect_bellgym_db():
    db = BellGymDB()
    db.connect()
    return db


def main():
    db = connect_bellgym_db()
    while True:
        print("1. 운동기록입력")
        print("2. 운동기록검색")
        print("3. 운동기록수정")
        print("4. 운동기록삭제")
        print("5. 회원가입")
        print("6. 회원정보 보기")
        print("7. 회원정보 삭제")
        print("8. 종료")
        choice = int(input(("입력을 선택하세요 (1번~8번: )")))

        if choice == constant.INPUT_WORKOUT:
            id = workout_input("ID")
            name = workout_input("이름")
            year, month, day = workout_input("날짜 (년-월-일):").split('-')
            prepare = workout_input("prepare")
            mainwork = workout_input("mainwork")
            wod = workout_input("WOD")
            bulidup = workout_input("Buildup")

            # v1
            createFolder(name)
            write_file(year, month, day, prepare, mainwork, wod, bulidup, name)
            read_file(year, month, day, name)

            # v2
            createFolder_v2(id)
            write_file_v2(year, month, day, prepare,
                          mainwork, wod, bulidup, name, id)
            read_file_v2(year, month, day, name, id)

        elif choice == constant.SEARCH_WORKOUT:
            print("*"*30+"운동기록을 검색합니다"+"*"*30+"\n")
            val = search_file_v2()
            if val == constant.NOT_FOUND_FOLDER:
                search_file()

        elif choice == constant.UPDATE_WORKOUT:
            print("*"*30+"운동기록을 수정합니다"+"*"*30+"\n")
            val = update_file_v2()
            if val == constant.NOT_FOUND_FOLDER:
                update_file()

        elif choice == constant.DELETE_WORKOUT:
            print("*"*30+"운동기록을 삭제합니다"+"*"*30+"\n")
            val = Delete_file_v2()
            if val == constant.NOT_FOUND_FOLDER:
                Delete_file()

        elif choice == constant.SIGNUP_USER:
            id = workout_input("ID")
            pwd = workout_input("PWD")
            name = workout_input("Name")
            record = (id, pwd, name)
            db.insert(
                "insert into user (id, password, name) values (%s, %s, %s)", record)
            print("*"*20+f"{name}님의 ID인 {id}가 등록되었습니다!!!"+"*"*20)

        elif choice == constant.SELECT_USER:
            result1 = db.selectAll("select * from user")

            users = []
            for row in result1:
                u = User(row[0], row[1], row[2])
                users.append(u)

            print("*"*10 + "user informain" + "*"*10)
            for u in users:
                u.introduceMyself()

        elif choice == constant.DELETE_USER:
            id = workout_input("ID")
            pwd = workout_input("PWD")
            name = workout_input("Name")
            record = (id, pwd, name)
            db.delete(
                "delete from user where id = %s and password = %s and name = %s", (
                    record)
            )
            print("*"*20+f"{name}님의 ID인 {id}가 삭제되었습니다!!!"+"*"*20)

        elif choice == constant.FINISH_WORKOUT:
            print("*"*30+"프로그램을 종료합니다."+"*"*30+"\n")
            db.close()
            break

        else:
            print("번호를 다시입력하세요"+"\n")


if __name__ == "__main__":
    main()
