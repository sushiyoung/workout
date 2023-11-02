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
    file_name = f"{year}-{month}-{day}.txt"
    with open(file_name, 'w', encoding='utf-8') as f:
        date = f"\n입력날짜는 : {year}년 {month}월{day}일 입니다."
        work1 =f"\n오늘의 prepare는 : {prepare} 입니다."
        work2 =f"\n오늘의 main운동은 : {mainwork} 입니다."
        work3 =f"\n오늘의 wod는 : {wod} 입니다."
        work4 =f"\n오늘의 buildup은 {bulidup} 입니다."
        f.write(date)
        f.write(work1)
        f.write(work2)
        f.write(work3)
        f.write(work4)
        

def print_file(year,month,day):              
    file_name = f"{year}-{month}-{day}.txt"
    with open(file_name, 'r', encoding='utf-8') as f:
        file_content = f.read()
    print(file_content)

        

def main():                 
    year, month, day = input_date()
    prepare = input_prepare()
    mainwork = input_mainwork()
    wod = input_wod()
    bulidup = input_bulidup()     
    write_file(year, month, day, prepare, mainwork,wod,bulidup)        
    print_file(year,month,day)
    

if __name__ == "__main__":
    main()