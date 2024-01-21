from flask import Flask, request, redirect, render_template, flash
from flask_mysqldb import MySQL
from datetime import datetime
import os

app = Flask(__name__)
app.secret_key = os.urandom(24)

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

@app.route('/search', methods=['POST'])
def search():
    search_user = request.form.get('search_user', '')
    user = get_user_by_name(search_user)

    if user:
        workouts = get_workouts_for_user(user['id'])
        return render_template('search.result.html', user=user, workouts=workouts)
    else:
        flash("가입인원이 아닙니다. 회원가입을 먼저 진행해주세요!")
        return redirect('/')

def get_user_by_name(name):
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM user where name = %s", (name,))
    user = cur.fetchone()
    cur.close()
    return user


def get_workouts_for_user(id):
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM workout where id = %s", (id,))
    workouts = cur.fetchall()
    cur.close()
    return workouts


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
