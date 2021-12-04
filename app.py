from flask import Flask, render_template, request, jsonify, make_response
import sqlite3, numpy
import pandas as pd
import json
import datetime as dt
from pprint import pprint

app = Flask(__name__)


conn = sqlite3.connect('database.sqlite3', check_same_thread=False)




@app.route('/')
def index():  # put application's code here
    return render_template("index.html")\


@app.route('/base')
def base():  # put application's code here
    return render_template("base.html")

@app.route('/dashboard')
def dashboard():
    return 'dashboard'

@app.route('/datalog')
def datalog():
    c = conn.cursor()
    try:
        cont = pd.read_sql_query("SELECT * FROM internel_env_log", conn)
        dict = cont.to_dict('records')
        param = json.dumps(dict)
        print(dict[0])
    except :
        dict = ""



    return render_template('tables.html', dict=dict)


@app.route('/api/in_topic', methods=['POST'])
def in_topic():

    x = dt.datetime.now()

    if request.method == 'GET':
        return "GET은 허용되지 않았습니다"

    if request.method == 'POST':
        response_d = request.get_json()
        print(response_d)
        param2 = {
            'date': x.strftime("%Y.%m.%d"),
            'time': x.strftime("%H:%M"),
            'temp_a': response_d['temp'],
            'temp_b': response_d['temp'],
            'humidity_a': response_d['humidity'],
            'humidity_b': response_d['humidity'],
            'co2': response_d['co2']
        }

        df = pd.DataFrame.from_records([param2])
        df_r = df.set_index('date')

        df_r.to_sql('internel_env_log', conn, if_exists='append')


    return "200"


if __name__ == '__main__':
    app.run()
