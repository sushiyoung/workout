import mysql.connector
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

    def close(self):
        self.cursor.close()
        self.conn.close()

    def selectAll(self, query):
        self.cursor.execute(query)
        return self.cursor.fetchall()
    


# db = BellGymDB()
# db.connect()

# select_data_user = "SELECT * FROM user"
# select_data_workout = "SELECT * FROM workout"

# cursor = db.cursor
# conn = db.conn
# cursor.execute(select_data_user)
# result1 = cursor.fetchall()


# cursor.execute(select_data_workout)
# result2 = cursor.fetchall()

# users =[]
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

