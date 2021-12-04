from flask import Flask
import sqlite3, numpy
import pandas as pd
import json

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
    print(cont)

    return "test"



if __name__ == '__main__':
    app.run()
