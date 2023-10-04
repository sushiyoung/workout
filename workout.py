f = open('workout.txt', 'a',encoding='utf-8')

year = input("연도를 입력하세요 :")
month = input("월을 입력하세요 :")
date = input("일을 입력하세요 :")

print("입력날짜는", year + "년", month +"월",date + "일 입니다.")
f.write("\n날짜 :" + year + "-" + month + "-" + date)

f.write("\nprepare:")
f.write(input("prepare를 입력하세요 :"))

f.close()
