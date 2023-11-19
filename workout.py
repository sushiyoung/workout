import os
import glob

global file_path

def workout_input(prompt):
    return input(f"{prompt}을 입력하세요: ")

def get_file_path(name):
    abspath = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(abspath, f'Bellgym_record{name}')
    
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

def write_file(year,month,day,prepare,mainwork,wod,bulidup,name):
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
        with open(folder_path +'\\' + file_name, 'w', encoding='utf-8') as f:
            f.write(file_workout)
    except OSError:
        print("Error: file path" + file_name)  

def read_file(year,month,day,name):              
    folder_path = get_file_path(name)
    file_name = f"{name}-{year}-{month}-{day}.txt"
    with open(folder_path +'\\' + file_name, 'r', encoding='utf-8') as f:
        file_workout = f.read()
    print(file_workout)


def search_file():
    name = workout_input("이름")
    folder_path = get_file_path(name)
    if not os.path.exists(folder_path):
        print("*"*10+f"{name}님의 폴더가 존재하지 않습니다."+"*"*10)
        return
    
    file_name_list = glob.glob(folder_path+ '\\*' )
    print("*"*10+ f"{name}님의 대한 리스트 파일이 존재합니다"+"*"*10)
    for f in file_name_list:
        print(f)
    print("\n"+"*"*60)
    
    year, month, day = workout_input("날짜 (년-월-일):").split('-')
    file_name = f"{name}-{year}-{month}-{day}.txt"
    
    print("*" * 10 + "이 파일의 대한 결과입니다" +"*" * 10+"\n")

    if os.path.isfile(folder_path+ '\\' +file_name):
        with open(folder_path +'\\' + file_name, 'r', encoding='utf-8') as f:
            file_workout = f.read()
            print(file_workout)
    else:
        print(f"{name}님의 운동기록이 없습니다") 
    
    print("\n"+"*"*60)

def main(): 
    while True:
        print("1. 운동기록입력")
        print("2. 운동기록검색")
        print("3. 종료")
        choice = int(input(("입력을 선택하세요 (1번/2번/3번: )")))
    
        if choice == 1:
            name = workout_input("이름")
            year, month, day = workout_input("날짜 (년-월-일):").split('-')
            prepare = workout_input("prepare")
            mainwork = workout_input("mainwork")
            wod = workout_input("WOD")
            bulidup = workout_input("Buildup")    
            createFolder(name)
            write_file(year, month, day, prepare, mainwork,wod,bulidup,name)        
            read_file(year,month,day,name)
        elif choice == 2:
            search_file()
        elif choice == 3:
            print("운동 프로그램을 종료합니다.")
            break
        else:
            print("번호를 다시입력하세요")
    

if __name__ == "__main__":
    main()