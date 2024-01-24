from flask import Flask, request, redirect, render_template, flash, jsonify, Response
from datetime import datetime
import os
import json

from user import User
from db_connect import BellGymDB

app = Flask(__name__)
db = BellGymDB()
db.connect()

# localhost:5001/
@app.route('/') 
def index():
    current_year = datetime.now().year
    # users = get_users_from_db()
    # workouts = get_workouts_from_db()
    return render_template('index.html', current_year=current_year, users=[], workouts=[])


@app.route('/go', methods=['GET'])
def go():
    return render_template('search_result.html')

@app.route('/test', methods=['GET'])
def test():
    # user_id = request.args.get("user_id")
    result = get_users()
    data = convertToJson(result)
    print(data)
    return convertToJson(result)

@app.route('/search', methods=['POST'])
def search():
    data = json.loads(request.data)
    user_id = data.get("search_user_id", "None")
    print("userid : ", user_id)
    
    
    # result = get_user_by_id(user_id)
    result = get_users()
    # return jsonify(result)
    return convertToJson(result)
    
    # if user:
    #     workouts = get_workouts_for_user(user['id'])
    #     return render_template('search.result.html', user=user, workouts=workouts)
    # else:
    #     flash("가입인원이 아닙니다. 회원가입을 먼저 진행해주세요!")
    #     return redirect('/')

def convertToJson(result):
    return json.dumps(result, default=lambda o: o.__dict__, sort_keys=True, ensure_ascii=False)


def get_users():
    # result1 = db.select("SELECT * FROM user where id = %s", (id,))
    result1 = db.selectAll("SELECT * FROM user")

    if not result1:
        return {"ERROR": "등록된 회원이 아닙니다."}
    
    user = [User(u[0], u[1], u[2]) for u in result1]
    return user

def get_user_by_id(id):
    result1 = db.select("SELECT * FROM user where id = %s", (id,))

    if not result1:
        return "등록된 회원이 아닙니다."
    
    users = []
    for u in result1:
        user = User(u[0], u[1], u[2])
        user.introduceMyself()
        users.append(user)
        
    return users


# def get_workouts_for_user(id):
#     cur = mysql.connection.cursor()
#     cur.execute("SELECT * FROM workout where id = %s", (id,))
#     workouts = cur.fetchall()
#     cur.close()
#     return workouts


# def get_users_from_db():
#     cur = mysql.connection.cursor()
#     cur.execute("SELECT * FROM user")
#     users = cur.fetchall()
#     cur.close()
#     return users

# def get_workouts_from_db():
#     cur = mysql.connection.cursor()
#     cur.execute("SELECT * FROM workout")
#     workouts = cur.fetchall()
#     cur.close()
#     return workouts



if __name__ == '__main__':
    app.run(port=5001, debug=True)