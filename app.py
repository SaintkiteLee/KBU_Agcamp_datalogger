from flask import Flask
import sqlite3

app = Flask(__name__)




@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'

@app.route('/dashboard')
def dashboard():
    return 'dashboard'

@app.route('/datalog')
def datalog():
    return 'datalog'



if __name__ == '__main__':
    app.run()
