f = open('workout.txt', 'w',encoding='utf-8')

d1 = input("날짜를 입력하세요 :")
d2 = input("월을 입력하세요 :")
d3 = input("일을 입려가세요 :")
d = d1+d2+d3

print(d)
f.write("\n날짜 :  ")


f.write("\nprepare:")
f.write(input("prepare를 입력하세요 :"))

f.close()
