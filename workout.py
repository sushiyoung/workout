import os

global file_path

file_path = 'c:\\Bellgym_record\\'

def workout_input(prompt):
    return input(f"{prompt}을 입력하세요: ")

def createFolder(file_path,name):
    try:
        if not os.path.exists(file_path + name):
            os.makedirs(file_path + name)
            print("폴더가 생성되었습니다.")
        else:
            print("폴더가 이미 존재합니다.")
    except OSError:
        print('Error: Creating directory.' + file_path + name)

def write_file(year,month,day,prepare,mainwork,wod,bulidup,name):
    try:    
        file_name = f"{name}-{year}-{month}-{day}.txt"
        file_workout = (
            f"이름 : {name}\n"
            f"입력날짜는 : {year}년 {month}월 {day}일 입니다.\n"
            f"오늘의 prepare는 : {prepare}\n"
            f"오늘의 mainwork은 : {mainwork}\n"
            f"오늘의 wod는 : {wod}\n"
            f"오늘의 buildup은 {bulidup}\n"
        )
        with open(file_path+ name +'\\' + file_name, 'w', encoding='utf-8') as f:
            f.write(file_workout)
    except OSError:
        print("Error: file path" + file_name)  

def read_file(year,month,day,name):              
    file_name = f"{name}-{year}-{month}-{day}.txt"
    with open(file_path+ name +'\\' + file_name, 'r', encoding='utf-8') as f:
        file_workout = f.read()
    print(file_workout)

        

def main(): 
    name = workout_input("이름")
    year, month, day = workout_input("날짜 (년-월-일):").split('-')
    prepare = workout_input("prepare")
    mainwork = workout_input("mainwork")
    wod = workout_input("WOD")
    bulidup = workout_input("Buildup")    
    createFolder(file_path,name)
    write_file(year, month, day, prepare, mainwork,wod,bulidup,name)        
    read_file(year,month,day,name)
    

if __name__ == "__main__":
    main()