from flask import Flask, request, redirect, render_template, flash, jsonify, Response
from datetime import datetime
import os
import json

from user import User
from workout import Workout
from db_connect import BellGymDB

app = Flask(__name__)
db = BellGymDB()
db.connect()


# localhost:5001/
@app.route('/')
def index():
    user_records = get_users_information()
    users = [User(record[0], record[1], record[2]) for record in user_records]
    print("User information!!!!!!!!!:", users)

    workout_records = get_workout_information()
    workouts = [Workout(record[1], record[2], record[3], record[4], record[5], record[6]) for record in workout_records]
    print("Workout information!!!!!!!!!:", workouts)

    user_workout_combine = [{'user': user, 'workout': workout}
                          for user, workout in zip(users, workouts)]

    
    return render_template('index.html', user_workout_combine=user_workout_combine)


# @app.route('/go', methods=['GET'])
# def go():
#     return render_template('search_result.html')

# @app.route('/test', methods=['GET'])
# def test():
#     # user_id = request.args.get("user_id")
#     result = get_users()
#     data = convertToJson(result)
#     print(data)
#     return convertToJson(result)

@app.route('/search', methods=['GET'])
def search():
    current_year = datetime.now().year
    user_id = request.args.get("search_id")
    print("userid : ", user_id)
    searched_users = search_users_information(user_id)
    print("searched_users : " , searched_users)
    return render_template('search_jhy.html', current_year=current_year, searched_user_list = searched_users)
   
    
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

# def convertToJson(result):
#     return json.dumps(result, default=lambda o: o.__dict__, sort_keys=True, ensure_ascii=False)


# def get_users():
#     # result1 = db.select("SELECT * FROM user where id = %s", (id,))
#     result1 = db.selectAll("SELECT * FROM user")

#     if not result1:
#         return {"ERROR": "등록된 회원이 아닙니다."}
    
#     user = [User(u[0], u[1], u[2]) for u in result1]
#     return user


def get_users_information():
    result1 = db.selectAll("SELECT * FROM user")
    return result1

def get_workout_information():
    result1 = db.selectAll("SELECT * FROM workout")
    return result1

def search_users_information(id):
    result = db.selectAll(f"SELECT * FROM user where id = '{id}'")
    return result


# def get_workouts_for_user(id):
#     cur = mysql.connection.cursor()
#     cur.execute("SELECT * FROM workout where id = %s", (id,))
#     workouts = cur.fetchall()
#     cur.close()
#     return workouts


# def get_users_from_db():
#     cur = mysql.connector.cursor()
#     cur.execute("SELECT * FROM user")
#     users = cur.fetchall()
#     cur.close()
#     print(users)
#     return users

# def get_workouts_from_db():
#     cur = mysql.connection.cursor()
#     cur.execute("SELECT * FROM workout")
#     workouts = cur.fetchall()
#     cur.close()
#     return workouts



if __name__ == '__main__':
    app.run(port=5001, debug=True)
