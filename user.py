import mysql.connector


class user:
    def __init__(self, id, pwd, name):
        self.id = id
        self.pwd = pwd
        self.name = name

    def introduceMyself(self):
        print("제 소개를 시작하겠습니다!!!")
        print("id : " , self.id)
        print("pwd : ", self.pwd)
        print("name : ", self.name)



#----------------controller (시키는 사람) -----------------------#
# moonsu = user('moonsu', '1234', 'Kimmoonsu')
# moonsu.introduceMyself()

# sushiyoung = user('sushi', '1234', 'Jeong')
# sushiyoung.introduceMyself()


#-------------------------------------------------------------#