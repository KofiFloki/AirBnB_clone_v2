#!/usr/bin/python3
"""
Starts Flask web application
Web app listens on 0.0.0.0 port 5000
/hbnb page include
/c/<text> page included
/python/(<text>) page included
/number/<n> page included
/number_template/<n> page included
/number_odd_or_even/<n> page included
"""
from models import storage
from models import *
from flask import Flask, render_template
app = Flask(__name__)


@app.teardown_appcontext
def teardown_db(self):
    """After each request, remove the current session"""
    storage.close()


@app.route('/cities_by_states', strict_slashes=False)
def cities_list():
    """displays a HTML page with the list of cities and the states
    they fall under"""
    sorted_states = storage.all("State").values()
    return render_template('8-cities_by_states.html', states=sorted_states)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
