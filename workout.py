# with open('workout.txt', 'a', encoding='utf-8') as f:
        
#     year, month, day = input("날짜를 입력하세요 :").split('-')

#     date = "입력날짜는 : {}년 {}월{}일 입니다.".format(year, month, day)

#     print(date)
#     f.write(date)


#     f.write("\nprepare:")
#     f.write(input("prepare를 입력하세요 :"))


def input_date():
    print(input("날짜를 입력하세요 :"))


def write_file():
    with open('workout.txt', 'w', encoding='utf-8') as f:
        year, month, day = input("날짜를 입력하세요 :").split('-')
        date = "입력날짜는 : {}년 {}월{}일 입니다.".format(year, month, day)   
        f.write(date)

def print_file():
    pass

def main():                 # 키오스크 처럼 생각(1주문,2주문..) 무조건 메인부터 실행
    input_date()
    write_file()
    
if __name__ == "__main__":
    main()