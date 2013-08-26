from flask import Flask
import os
import threading
from coffeetimethreading import CoffeeMaker 
from functools import wraps
from flask import request, Response
import json
from datetime import datetime

app = Flask(__name__)
app.secret_key = os.urandom(24)
app.debug = True
coffee_maker = CoffeeMaker()

html = """ 
<!DOCTYPE html>
<html>
<head>
       <style type="text/css">
               input#stopbutton {
                       width: 250px;
                       height: 100px;
                       font-size: 28px;
                       color: #FF0000;
               }
               input#coffeebutton {
                       width: 250px;
                       height: 100px;
                       font-size: 28px;
                       color: #008000;
               }
               input#coffeeoz {
                       width: 80px;
                       height: 60px;
                       font-size: 28px;
                       text-align: center;
               }
       </style>
<title>Coffee controller</title>
<script src="http://code.jquery.com/jquery-1.9.1.js"></script>
<script>
    $(document).ready(function(){
        $("#coffeebutton").click(function(){
            $.ajax({
                type: "POST",
                url: "/coffee",
                data: {"size": $("#coffeeoz").val()}
            })
        });
        $("#stopbutton").click(function(){
            $.post('/killall')
        });
    });
</script>
</head>
<body>
<font size = 16>
    I want to make <br>&nbsp;<input id="coffeeoz" type="number" name="quantity" min="12" max="100" value="16">&nbsp;ounces of coffee<br>
    <input id="coffeebutton" value="Start Coffee" type="submit">
    <input id="stopbutton" value="Stop Coffee" type="submit">
</font>
</body>
</html>
"""

def check_auth(username, password):
     return username == 'admin' and password == 'secret'

def authenticate():
    """Sends a 401 response that enables basic auth"""
    return Response(
    'Could not verify your access level for that URL.\n'
    'You have to login with proper credentials', 401,
    {'WWW-Authenticate': 'Basic realm="Login Required"'})

def requires_auth(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        auth = request.authorization
        if not auth or not check_auth(auth.username, auth.password):
            return authenticate()
        return f(*args, **kwargs)
    return decorated

def whenStart(startTime, default="just now"):
     now = datetime.utcnow()
     diff = startTime - now

     periods = (
        (diff.days / 365, "year", "years"),
        (diff.days / 30, "month", "months"),
        (diff.days / 7, "week", "weeks"),
        (diff.days, "day", "days"),
        (diff.seconds / 3600, "hour", "hours"),
        (diff.seconds / 60, "minute", "minutes"),
        (diff.seconds, "second", "seconds"),
     )

     for period, singular, plural in periods:

          if period:
            return "%d %s from now" % (period, singular if period == 1 else plural)

    return default


     

@app.route('/')
@requires_auth
def index():
    return html

@app.route("/coffee", methods=['GET', 'POST'])
@requires_auth
def start_coffee():
    size = 12
    try:
        size = int(request.form['size'])
    except:
        pass # if it isn't an int, or data wasn't sent
    print 'I am making you %d ounces of coffee.' % size
    coffee_maker.makeCoffee(size)

@app.route("/killall", methods=['GET', 'POST'])
@requires_auth
def killall():
    coffee_maker.force_stop()
    print 'done force stopping'

if __name__ == '__main__':
    app.run(host='0.0.0.0')
