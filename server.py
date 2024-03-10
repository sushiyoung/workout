from typing import List
from flask import Flask, request, redirect, render_template, flash, jsonify, Response, url_for
from datetime import datetime
import os

from user import User
from workout import Workout
from db_connect import BellGymDB

app = Flask(__name__)
db = BellGymDB()
db.connect()

# ---------------------------------------------------------------------------------------------------------

# localhost:5001/
@app.route('/')
def index():
    current_year = datetime.now().year
    user_workout_combine = get_user_workout_information()
    # print("USER WORKOUT INFOR :" , user_workout_combine)
    return render_template('index.html', user_workout_combine = user_workout_combine, current_year = current_year)
    

@app.route('/search', methods = ['GET'])
def search():
    current_year = datetime.now().year
    search = request.args.get("select")
    search_query = request.args.get("search_query")

    print("RESULT QUERY : ", search_query, search)

    if search_query:
    
        user_workout_combine = search_user_workout(search, search_query)
        return render_template('search_jhy.html', user_workout_combine=user_workout_combine, current_year=current_year)
    else:
        return "No Search by ID"


@app.route('/update/<string:id>/<string:date>', methods=['PUT'])
def update(id, date): #update 할 workout 식별 매개변수
    try:
        update_record = request.json # 클라이언트로 전송된 JSON 데이터를 가져와서 저장
      
        query = """
                UPDATE workout SET date = %s, prepare = %s, main = %s, sub = %s, wod = %s, buildup = %s 
                WHERE id = %s AND date = %s
                """
        data = (
            update_record.get('date'),
            update_record.get('prepare'),
            update_record.get('main'),
            update_record.get('sub'),
            update_record.get('wod'),
            update_record.get('buildup'),
            id,
            date
        )
        print("Modified Workout:", data)
        db.update(query, data)

        return jsonify({'Message': 'Success workout update'}), 200
    except Exception as e:
        return jsonify({'Error': str(e)}), 400


# URL에서 받아올 변수의 데이터 타입을 지정하는 것, 고유식별자
@app.route('/delete/<string:id>/<string:date>', methods=['DELETE']) 
def delete(id,date):
    print("Recived ID : ", id)
    print("Recived Date : ", date)
    try:
       query = "delete from workout where id = %s and date =%s"
       db.delete(query, (id,date)) # 튜플형태로 값을 전달
       return jsonify ({'Message' : 'Success workout delete'}), 200
    except Exception as e:
        print("Error", str(e))
        return jsonify({'Error' : str(e)}), 400

# -------------------------------------------------------------------------------------------------------

def get_user_workout_information()->List[dict]: #[{}, {}] 이런 형태로 리턴
    query = """
            SELECT user.id, user.name, workout.date, workout.prepare, workout.main, workout.sub, workout.wod, workout.buildup 
            FROM user INNER JOIN workout ON user.id = workout.id
            """
    try:
        records, cols = db.selectAll(query)
        user_workout_combine = []
        for record in records:
            workout = {}
            for col, rec in zip(cols, record):
                workout[col] = rec
            user_workout_combine.append(workout)
        return user_workout_combine
    except:
        return []

    

def search_user_workout(search, search_query):
    print(search)
    query = f"""
            SELECT user.id, user.name, workout.date, workout.prepare, workout.main, workout.sub, workout.wod, workout.buildup 
            FROM user INNER JOIN workout ON user.id = workout.id
            WHERE user.{search} = "{search_query}"
            """
            #search의 값과 search_query의 값이 일치할 경우만 id = id를 입력해야 검색완료
    
    records, cols = db.selectAll(query)
    print(records, cols)
    user_workout_combine = []
    for record in records:
        workout = {}
        for col, rec in zip(cols, record):
            workout[col] = rec
        user_workout_combine.append(workout)
        
    return user_workout_combine



if __name__ == '__main__':
    app.run(port=5001, debug=True)



# 원본index,search
# -------------------------------------------------------------------------------------------
# @app.route('/')
# def index():
#     user_records = get_users_information()
#     users = [User(record[0], record[1], record[2]) for record in user_records]
#     # print("User information!!!!!!!!!:", users)

#     workout_records = get_workout_information()
#     workouts = [Workout(record[1], record[2], record[3], record[4],
#                         record[5], record[6]) for record in workout_records]
#     # print("Workout information!!!!!!!!!:", workouts)

#     user_workout_combine = [{'user': user, 'workout': workout}
#                             for user, workout in zip(users, workouts)]

#     return render_template('index.html', user_workout_combine=user_workout_combine)
    

# @app.route('/search', methods=['GET'])
# def search():
#     current_year = datetime.now().year
#     search_id = request.args.get("search_id")
#     print("Search ID: ", search_id)

#     if search_id:
#         searched_user_records = search_users_by_id(search_id)
#         searched_workout_records = search_workout_by_id(search_id)
#         users = [User(record[0], record[1], record[2])
#                  for record in searched_user_records]
#         workouts = [Workout(record[0], record[1], record[2], record[3], record[4], record[5])
#                     for record in searched_workout_records]
#         user_workout_combine = [{'user': user, 'workout': workout}
#                                 for user, workout in zip(users, workouts)]
#         # print("User information!!!!!!!!!:", users)
#         return render_template('search_jhy.html', current_year=current_year, user_workout_combine=user_workout_combine)
#     else:
#         return ("ID를 눌러주세요!")


# def search_users_by_id(id):
#     result = db.selectAll(f"SELECT * FROM user where id = '{id}'")
#     # print("Result from search_users_by_id :", result)
#     return result


# def search_workout_by_id(id):
#     result = db.selectAll(f"SELECT * FROM workout where id = '{id}'")
#     print("Result from search_workout_by_id :", result)
#     return result


# def search_users_by_name(name):
#     result = db.selectAll(f"SELECT * FROM user where name = '{name}'")
#     print("Result from search_users_by_name :", name)
#     return result


# def search_users_information(id):
#     result = db.selectAll(f"SELECT * FROM user where id = '{id}'")
#     return result


# -----------------------------------------------------------------------------------------
