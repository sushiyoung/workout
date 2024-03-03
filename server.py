from typing import List
from flask import Flask, request, redirect, render_template, flash, jsonify, Response, url_for
from datetime import datetime
import os
import json

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
    
    records, cols = db.selectAll(query)
    print(records, cols)
    user_workout_combine = []
    for record in records:
        workout = {}
        for col, rec in zip(cols, record):
            workout[col] = rec
        user_workout_combine.append(workout)
        
    return user_workout_combine
    # return []

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
