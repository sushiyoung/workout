def input_date():
    year, month, day = input("날짜를 입력하세요 :").split('-')  
    return year, month, day   

def write_file(year, month, day):    
    with open('workout.txt', 'w', encoding='utf-8') as f:
        date = "\n입력날짜는 : {}년 {}월{}일 입니다.".format(year, month, day)   
        f.write(date)

def print_file():              
    with open('workout.txt', 'r', encoding='utf-8') as f:
        workout = f.read()
    print(workout)

        

def main():                 
    year, month, day = input_date()     
    write_file(year, month, day)        
    print_file()
if __name__ == "__main__":
    main()

