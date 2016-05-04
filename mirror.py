from flask import Flask, request, session, g, redirect, url_for, \
     abort, render_template, flash
import datetime
import get_weather

# configuration
# DATABASE = '/tmp/flaskr.db'
DEBUG = True
#SECRET_KEY = 'development key'
#USERNAME = 'admin'
#PASSWORD = 'default'


app = Flask(__name__)
app.config.from_object(__name__)

@app.route("/")
def hello():
    time_string = datetime.datetime.now().strftime("%a, %b-%d-%Y, %I:%M %p")
    current_weather = get_weather.get_current_conditions()
    return render_template('index.html', time = time_string, weather = current_weather)


if __name__ == '__main__':
    app.run()
