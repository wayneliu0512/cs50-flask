import datetime
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    headline = 'index'
    now = datetime.datetime.now()
    new_year = now.month == 1 and now.day == 1
    # new_year = True
    return render_template('hello.html', headline=headline, new_year=new_year)

@app.route('/bye')
def bye():
    bye = 'bye'
    return render_template('bye.html', headline=bye)
