import mysql.connector


class Workout:
    def __init__(self, id, date, prepare, mainwork, wod, buildup):
        self.id = id
        self.date = date
        self.prepare = prepare
        self.mainwork = mainwork
        self.wod = wod
        self.buildup = buildup

    def introduceWorkout(self):
        print("*" * 40)
        print(f"{self.id}님 의 운동입니다")
        print("date : ", self.date)
        print("prepare : ", self.prepare)
        print("mainwork : ", self.mainwork)
        print("wod : ", self.wod)
        print("buildup : ", self.buildup)
        print("*" * 40)


# ----------------controller (시키는 사람) -----------------------#
# moonsu = user('moonsu', '1234', 'Kimmoonsu')
# moonsu.introduceMyself()

# sushiyoung = user('sushi', '1234', 'Jeong')
# sushiyoung.introduceMyself()


# -------------------------------------------------------------#
