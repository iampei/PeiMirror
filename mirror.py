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
    if  6 < int(hour) <=11:
        word_string = ['Have a beartestic day!', 'You are a super star!', 'Rock the day!', 'Looking good this morning!']
    if 11 < int(hour) <=14:
        word_string = ["It's meowlunch time!", "Go out and have fun"]
    if 14 < int(hour) <= 19:
        word_string = ['Have a good afternoon!', "Why don't you pick out a show to watch"]
    if 19 < int(hour) <= 23:
        word_string = ['Have a nice dream!', 'Sweet dreams!', 'Have a nice night!', 'You look nice this evening!']
    if 23 < int(hour) <= 24:
        word_string = ['You should go to bed now...', 'Why are you still up?']
    if int(hour) <=6 :
        word_string = ['Hey, you look nice!']
    #current_weather['compliment'] = random.choice(word_string)
    return (random.choice(word_string))

@app.route("/")
def hello():
    current_weather = get_weather.get_current_conditions()
    #URL = http://icons.wxug.com/i/c/i/ICON.gif
    #file = io.BytesIO(urlopen('http://icons.wxug.com/i/c/i/partlycloudy.gif').read())
    ICON = current_weather['icon']
    img = 'http://icons.wxug.com/i/c/k/%s.gif'%ICON
    #img = 'http://icons.wxug.com/i/c/i/partlycloudy.gif'
    #time_string = datetime.datetime.now().strftime("%a, %b-%d-%Y, %I:%M %p")
    time_string = datetime.datetime.now().strftime("%I:%M %p")
    date_string = datetime.datetime.now().strftime("%a, %b-%d-%Y")
    current_weather['time'] = time_string
    current_weather['date'] = date_string
    current_weather['compliment'] = get_compliment()
    current_weather['image'] = img
    return render_template('index.html', **current_weather)

@app.route("/test")
def test():
    return render_template('test.html')


@app.route('/_get_update')
def _get_update():
    
    #time_string = datetime.datetime.now().strftime("%a, %b-%d-%Y, %I:%M %p")
    update_dic ={}
    now = datetime.datetime.now()
    update_dic['time'] = now.strftime("%I:%M %p")
    #time_string = datetime.datetime.now().strftime("%I:%M %p")
    update_dic['date'] = now.strftime("%a, %b-%d-%Y")
    update_dic['compliment'] = get_compliment()
    #weather_update = current_weather['weather']
    #update_dic.update(current_weather)
    #temp_update = current_weather['current_temp']

    #print('_get_time called')
    return jsonify(**update_dic) 

#count = [0]
@app.route('/_get_newweather')
def _get_newweather():
    current_weather = get_weather.get_current_conditions()
    print('_get_newweather is called')
    #count[0] +=1
    #current_weather['weather'] = current_weather['weather'] + '%i' %count[0]

    return jsonify(**current_weather)


if __name__ == '__main__':
    app.run()
