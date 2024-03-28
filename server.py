# Flask에서 secret_key를 설정하지 않으면 세션 데이터를 암호화하고 유지할 수 없음
# 따라서 Flask는 세션을 안전하게 유지할 수 없다는 에러 발생
# --------------------------------------------------------------------------------------------------------
from typing import List
from flask import Flask, request, redirect, render_template, flash, jsonify, Response, url_for, session
from datetime import datetime
import os

from user import User
from workout import Workout
from db_connect import BellGymDB

app = Flask(__name__)
app.secret_key = os.urandom(24) # 난수생성 24byte
db = BellGymDB()
db.connect()

# ---------------------------------------------------------------------------------------------------------

# localhost:5001/
####################로그인 페이지####################
@app.route('/', methods=['GET', 'POST'])
def main():
    error = None # 초기에는 오류가 없음을 나타냄
    login_success = False # 로그인 성공 여부를 기본적으로 False로 설정

    if request.method == 'POST':
        id = request.form['id']
        pwd =request.form['password']

        query = "SELECT id FROM user WHERE id = %s AND password = %s"
        record =(id, pwd) # 해당기록을 튜플형태로 준비
        try:
            result = db.select(query, record)

            #session : 서버와 클라이언트간의 상태를 유지하기 위한 것
            if result:
                session['login_user'] =id
                print("LOGIN SUCCESS :", id)
                login_success = True
                flash("로그인이 성공적으로 완료되었습니다.")
                return redirect(url_for('index'))
            else:
                error ="NO ID OR PASSWORD" # 추후에 회원가입이 필요합니다 회원가입 페이지 안내
        except Exception as e:
            error =str(e)
            print("ERROR :", error)

    return render_template('main.html', error = error, login_success = login_success)

################### 로그아웃 기능###################


@app.route('/logout', methods=['GET'])
def logout():
    if 'login_user' in session:
        logout_user = session['login_user']
        session.pop('login_user', None)
        print("LOGOUT SUCCESS :", logout_user)
    else:
        print("이미 로그아웃 완료되었습니다.")
    return redirect(url_for('main'))

####################운동기록 리스트####################
@app.route('/index')
def index():
    current_year = datetime.now().year
    if 'login_user' in session:
        login_user = session['login_user']
        user_workout_combine = get_user_workout_information(login_user)
        # print("USER WORKOUT INFOR :" , user_workout_combine)
        return render_template('index.html', user_workout_combine=user_workout_combine, current_year=current_year)
    else:
        return redirect(url_for('main'))


####################회원가입####################
@app.route('/register', methods = ['GET','POST'])
def register():
    error = None
    if request.method == 'POST':
        id = request.form['regi_id']
        password = request.form['regi_password']
        name = request.form['regi_name']

        print("Received form data:", id, password, name)

        
        query_check = "SELECT id FROM user WHERE id = %s"
        record_check = (id,)
        
        try:
            existing_user = db.select(query_check, record_check)
            
            if existing_user:
                error = "이미 가입 된 ID 입니다. 다른 ID를 입력하세요!"
            
            else:
                query_insert = "INSERT INTO user (id, password, name) VALUES (%s, %s, %s)"
                record_insert =(id,password,name)
                db.insert(query_insert, record_insert)
                db.commit()
                return redirect(url_for('main'))
        except Exception as e:
            error = str(e)
            print("ERROR : ", error)

    return render_template('register.html', error=error)

####################운동기록입력####################
@app.route('/add_workout', methods=['POST'])
def add_workout():
    try:
        workout_record = request.json

        query = """
                INSERT INTO workout (id, date, prepare, main, sub, wod, buildup) VALUES (%s, %s, %s, %s, %s, %s, %s)
                """

        workout_dict = (
            workout_record.get('date'),
            workout_record.get('prepare'),
            workout_record.get('main'),
            workout_record.get('sub'),
            workout_record.get('wod'),
            workout_record.get('buildup')
        )
        print("Insert Workout:", workout_dict)
        db.insert(query, workout_dict)

        return jsonify({'Message': 'Success insert workout'}), 200
    except Exception as e:
        return jsonify({'Error': str(e)}), 400

####################운동기록검색####################
@app.route('/search', methods = ['GET'])
def search():
    current_year = datetime.now().year
    search = request.args.get("select")
    search_query = request.args.get("search_query")

    # print("RESULT QUERY : ", search_query, search)

    if search_query:
    
        user_workout_combine = search_user_workout(search, search_query)
        return render_template('search.html', user_workout_combine=user_workout_combine, current_year=current_year)
    else:
        return "No Search by ID"

####################운동기록수정####################
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

####################운동기록삭제####################
# URL에서 받아올 변수의 데이터 타입을 지정하는 것, 고유식별자
@app.route('/delete/<string:id>/<string:date>', methods=['DELETE']) 
def delete(id,date):
    print("Recived ID : ", id)
    print("Recived Date : ", date)
    try:
       query = "DELETE FROM workout WHERE id = %s AND date =%s"
       db.delete(query, (id,date)) # 튜플형태로 값을 전달
       return jsonify ({'Message' : 'Success workout delete'}), 200
    except Exception as e:
        print("Error", str(e))
        return jsonify({'Error' : str(e)}), 400






# ----------------------------------------------------------------------------------------------------------------------------

def get_user_workout_information(login_user)->List[dict]: #[{}, {}] 이런 형태로 리턴
    query = f"""
            SELECT user.id, user.name, workout.date, workout.prepare, workout.main, workout.sub, workout.wod, workout.buildup 
            FROM user INNER JOIN workout ON user.id = workout.id
            WHERE user.id = '{login_user}'
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
    except Exception as e:
        print("ERROR : ", e)
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

# ----------------------------------------------------------------------------------------------------------------------------

