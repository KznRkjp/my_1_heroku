from bottle import route, run, view
from datetime import datetime as dt
from random import random
import horoscope, os


@route("/")
@view("predictions")
def index():
  now = dt.now()

  x = random()

  return {
    "date": f"{now.year}-{now.month}-{now.day}",
    "predictions": horoscope.generate_prophecies(5,3),
    "special_date": x > 0.5,
    "x": x,
  }


if os.environ.get('APP_LOCATION') == 'heroku':
    run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
else:
    run(host='localhost', port=8081, debug=True)

