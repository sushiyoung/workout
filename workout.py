def input_date():
    year, month, day = input("날짜를 입력하세요 :").split('-')  
    return year, month, day   

def input_prepare():
    prepare = input("prepare를 입력하세요 :")
    return prepare

def input_mainwork():
    mainwork = input("main운동을 입력하세요 :")
    return mainwork

def input_wod():
    wod = input("wod를 입력하세요 :")
    return wod

def input_bulidup():
    bulidup = input("bulidup을 입력하세요 :")
    return bulidup


def write_file(year,month,day,prepare,mainwork,wod,bulidup):    
    with open('workout.txt', 'w', encoding='utf-8') as f:
        date = "\n입력날짜는 : {}년 {}월{}일 입니다.".format(year, month, day)
        work1 ="\n오늘의 prepare는 : {} 입니다.".format(prepare)
        work2 ="\n오늘의 main운동은 : {} 입니다.".format(mainwork)
        work3 ="\n오늘의 wod는 : {} 입니다.".format(wod)
        work4 ="\n오늘의 buildup은 {} 입니다.".format(bulidup)
        f.write(date)
        f.write(work1)
        f.write(work2)
        f.write(work3)
        f.write(work4)
        

def print_file():              
    with open('workout.txt', 'r', encoding='utf-8') as f:
        workout = f.read()
    print(workout)

        

def main():                 
    year, month, day = input_date()
    prepare = input_prepare()
    mainwork = input_mainwork()
    wod = input_wod()
    bulidup = input_bulidup()     
    write_file(year, month, day, prepare, mainwork,wod,bulidup)        
    print_file()
    

if __name__ == "__main__":
    main()

