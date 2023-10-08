f = open('workout.txt', 'w',encoding='utf-8')

year, month, day = input("날짜를 입력하세요 :").split('-')
print("입력날짜는 : {}년 {}월{}일 입니다.".format(year, month, day))

date = "입력날짜는 : {}년 {}월{}일 입니다.".format(year, month, day)

f.write(date)


f.write("\nprepare:")
f.write(input("prepare를 입력하세요 :"))

f.close()
