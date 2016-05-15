from flask import Flask, request, session, g, redirect, url_for, \
     abort, render_template, flash, jsonify
import datetime
import get_weather
import random

# configuration
# DATABASE = '/tmp/flaskr.db'
DEBUG = True
#SECRET_KEY = 'development key'
#USERNAME = 'admin'
#PASSWORD = 'default'


app = Flask(__name__)
app.config.from_object(__name__)

def get_compliment():
    hour = datetime.datetime.now().strftime("%H")
    word_string = ['Hey, you look nice!']
    if int(hour) <17:
        word_string = ['Have a good afternoon!', 'You are a super star!']
    if 17 < int(hour) < 19:
        word_string = ['Go out and have fun!', 'Have a nice evening!']
    if int(hour) >= 19:
        word_string = ['Hello, you are awesome!', 'Have a nice night!', 'You look nice!']
    #current_weather['compliment'] = random.choice(word_string)
    return (random.choice(word_string))

@app.route("/")
def hello():
    current_weather = get_weather.get_current_conditions()
    time_string = datetime.datetime.now().strftime("%a, %b-%d-%Y, %I:%M %p")
    current_weather['time'] = time_string
    #hour = datetime.datetime.now().strftime("%H")
    # word_string = ['Hey, you look nice!']
    # if int(hour) <17:
    #     word_string = ['Have a good afternoon!', 'You are a super star!']
    # if 17 < int(hour) < 19:
    #     word_string = ['Go out and have fun!', 'Have a nice evening!']
    # if int(hour) >= 19:
    #     word_string = ['Hello, you are awesome!', 'Have a nice night!', 'You look nice!']
    #current_weather['compliment'] = random.choice(word_string)
    current_weather['compliment'] = get_compliment()
    return render_template('index.html', **current_weather)

@app.route("/test")
def test():
    return render_template('test.html')


@app.route('/_get_update')
def _get_update():
    time_string = datetime.datetime.now().strftime("%a, %b-%d-%Y, %I:%M %p")
    compliment = get_compliment()
    #print('_get_time called')
    return jsonify(time=time_string, compliment = compliment)

if __name__ == '__main__':
    app.run()
