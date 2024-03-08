import mysql.connector
from mysql.connector import errorcode
from user import User


class BellGymDB:
    def __init__(self):
        self.config = {
            'host': '127.0.0.1',
            'user': 'root',
            'password': '1234',
            'database': 'bellgym'
        }
        self.conn = None
        self.cursor = None
        self.query = None

    def connect(self):
        self.conn = mysql.connector.connect(**self.config)
        self.cursor = self.conn.cursor()
        print("DB 가 정상적으로 연결 되었습니다. ")

    def close(self):
        self.cursor.close()
        self.conn.close()

    def select(self, query, record):
        try:
            self.cursor.execute(query, record)
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_NO_SUCH_TABLE:
                return -1

        return self.cursor.fetchall()
    
    def selectAll(self, query):
        try:
            self.cursor.execute(query)
            column_names = [i[0] for i in self.cursor.description]
            
            return self.cursor.fetchall(), column_names
        except mysql.connector.Error as err:
            print(err)
            return -1

    def selectAll_v2(self, query):
        try:
            self.cursor.execute(query)
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_NO_SUCH_TABLE:
                return -1

        return self.cursor.fetchall()


    def insert(self, query, record):
        self.cursor.execute(query, record)
        self.conn.commit()

    def delete(self, query, record):
        try:
            self.cursor.execute(query, record)
            self.conn.commit()
        except mysql.connector.Error as err:
            print("err code : ", err.errno)

    def update(self, query, record):
        self.cursor.execute(query, record)
        self.conn.commit()


# db = BellGymDB()
# db.connect()
# # db.insert("insert into user (id, password, name) values(%s, %s, %s)", ("a", "b", "c"))

# select_data_user = "SELECT * FROM user"
# # select_data_workout = "SELECT * FROM workout"

# cursor = db.cursor
# conn = db.conn
# cursor.execute(select_data_user)
# result1 = cursor.fetchall()


# # cursor.execute(select_data_workout)
# # result2 = cursor.fetchall()

# users = []
# for row in result1:
#     u = User(row[0], row[1], row[2])
#     users.append(u)


# print("*"*10 + "user informain" + "*"*10)
# for u in users:
#     u.introduceMyself()


# index_count =[]
# ids_workout =[]
# date =[]
# prepare =[]
# main =[]
# sub =[]
# wod =[]
# buildup =[]


# for row in result2:
#     index_count.append(row[0])
#     ids_workout.append(row[1])
#     date.append(row[2])
#     prepare.append(row[3])
#     main.append(row[4])
#     sub.append(row[5])
#     wod.append(row[6])
#     buildup.append(row[7])

# print("*"*10 + "workout informain" + "*"*10)
# print(index_count)
# print(ids_workout)
# print(date)
# print(prepare)
# print(main)
# print(sub)
# print(wod)
# print(buildup)
