from flask import Flask, render_template
import sqlite3, numpy
import pandas as pd
import json
from pprint import pprint

app = Flask(__name__)


conn = sqlite3.connect('database.sqlite3', check_same_thread=False)


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'

@app.route('/dashboard')
def dashboard():
    return 'dashboard'

@app.route('/datalog')
def datalog():
    c = conn.cursor()
    cont = pd.read_sql_query("SELECT * FROM test_env_log", conn)
    dict = cont.to_dict('records')
    param = json.dumps(dict)
    print(dict[0])



    return render_template('table.html', dict=dict)



if __name__ == '__main__':
    app.run()
