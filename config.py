import pymysql

db = pymysql.connect(
    host ="localhost",
    user = "root",
    password = "1234",
    database = "bellgym",
    charset ="utf8mb4"
)

DB_URL = f"mysql+mysqlconnector://{db['user']}:{db['password']}@{db['host']}:{db['port']}/{db['database']}?charset=utf8"
