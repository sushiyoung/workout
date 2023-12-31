import mysql.connector


class User:
    def __init__(self, id, pwd, name):
        self.id = id
        self.pwd = pwd
        self.name = name

    def introduceMyself(self):
        print("*"* 40)
        print(f"{self.id}님 의 정보입니다")
        print("id : " , self.id)
        print("pwd : ", self.pwd)
        print("name : ", self.name)
        print("*" * 40)


#----------------controller (시키는 사람) -----------------------#
# moonsu = user('moonsu', '1234', 'Kimmoonsu')
# moonsu.introduceMyself()

# sushiyoung = user('sushi', '1234', 'Jeong')
# sushiyoung.introduceMyself()


#-------------------------------------------------------------#