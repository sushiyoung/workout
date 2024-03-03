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
    search_query = request.args.get("search_query")
    print("RESULT QUERY : ", search_query)

    if search_query:
        search_results = search_user_workout(search_query)
        user_workout_combine = search_user_workout(search_query)
        return render_template('search_jhy.html', user_workout_combine=user_workout_combine, current_year=current_year, search_results = search_results)
    else:
        return "No Search by ID"


# -------------------------------------------------------------------------------------------------------

def get_user_workout_information():
    result = db.selectAll(
        "SELECT user.id, user.name, workout.date, workout.prepare, workout.mainwork, workout.wod, workout.buildup FROM user INNER JOIN workout ON user.id = workout.id")
    user_workout_combine = [{'id': record[0], 'name': record[1], 'date': record[2], 'prepare': record[3],
                             'mainwork': record[4], 'wod': record[5], 'buildup': record[6]} for record in result]
    return user_workout_combine


def search_user_workout(search_query):
    query = ("SELECT user.id, user.name, workout.date, workout.prepare, workout.mainwork, workout.wod, workout.buildup FROM user INNER JOIN workout ON user.id = workout.id WHERE user.id = %s" )
    
    records = db.selectAll(query, (search_query))
    user_workout_combine = [{'id': record[0], 'name': record[1], 'date': record[2], 'prepare': record[3],
                             'mainwork': record[4], 'wod': record[5], 'buildup': record[6]} for record in records]
    print("RESULT : " , records)
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
