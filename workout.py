def workout_input(prompt):
    return input(f"{prompt}을 입력하세요: ")


def write_file(year,month,day,prepare,mainwork,wod,bulidup):    
    file_name = f"{year}-{month}-{day}.txt"
    file_workout = (
        f"입력날짜는 : {year}년 {month}월 {day}일 입니다.\n"
        f"오늘의 prepare는 : {prepare}\n"
        f"오늘의 main운동은 : {mainwork}\n"
        f"오늘의 wod는 : {wod}\n"
        f"오늘의 buildup은 {bulidup}\n"
    )
    with open(file_name, 'w', encoding='utf-8') as f:
        f.write(file_workout)
        

def read_file(year,month,day):              
    file_name = f"{year}-{month}-{day}.txt"
    with open(file_name, 'r', encoding='utf-8') as f:
        file_workout = f.read()
    print(file_workout)

        

def main():                 
    year, month, day = workout_input("날짜 (년-월-일):").split('-')
    prepare = workout_input("prepare")
    mainwork = workout_input("main운동")
    wod = workout_input("WOD")
    bulidup = workout_input("Buildup")    
    
    write_file(year, month, day, prepare, mainwork,wod,bulidup)        
    read_file(year,month,day)
    

if __name__ == "__main__":
    main()