from flask import Flask
import sqlite3, numpy
inport pandas as pd
import json

app = Flask(__name__)


conn=sqlite3.connect('database.sqlite3', check_same_thread=False)


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'

@app.route('/dashboard')
def dashboard():
    return 'dashboard'

@app.route('/datalog')
def datalog():
    c = conn.cursor()
    test_list = []
    for row in c.execute('SELECT * FROM test_env_log'):
        print(row)
        test_list[row] = row
    for i in test_list :
        testjson = json.dumps(test_list)
    print(testjson)

    return testjson



if __name__ == '__main__':
    app.run()
