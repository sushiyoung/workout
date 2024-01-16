from flask import Flask, request, redirect, render_template
from flask_mysqldb import MySQL
from datetime import datetime

app = Flask(__name__)

app.config['MYSQL_HOST']= '127.0.0.1'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = '1234'
app.config['MYSQL_DB'] = 'bellgym'

mysql = MySQL(app)

# localhost:5001/

@app.route('/') 
def index():
    current_year = datetime.now().year
    users = get_users_from_db()
    workouts = get_workouts_from_db()
    return render_template('index.html', current_year=current_year, users=users, workouts=workouts)


def get_users_from_db():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM user")
    users = cur.fetchall()
    cur.close()
    return users

def get_workouts_from_db():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM workout")
    workouts = cur.fetchall()
    cur.close()
    return workouts



if __name__ == '__main__':
    app.run(port=5001, debug=True)
