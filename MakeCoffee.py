from flask import Flask
import os
import threading
from coffeetimethreading import CoffeeMaker 
from functools import wraps
from flask import request, Response


app = Flask(__name__)
app.secret_key = os.urandom(24)
app.debug = True
coffee_maker = CoffeeMaker()

html = """
<!DOCTYPE html>
<html>
<head>
<title>Coffee controller</title>
</head>
<body>
    <form method="post" action="/coffee">
        <INPUT TYPE="button" value="Start Coffee" type="submit">
    </form>
    
    <form method="post" action="/killall">
        <INPUT TYPE="button" value="Stop Coffee" type="submit">
    </form>
    How Much Coffee Would You Like? <INPUT TYPE="text" oz="ozCoffee">
    </form>
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

@app.route('/')
@requires_auth
def index():
    return html

@app.route("/coffee", methods=['GET', 'POST'])
@requires_auth
def start_coffee():
    coffee_maker.makeCoffee(ozCoffee)

@app.route("/killall", methods=['GET', 'POST'])
@requires_auth
def killall():
    coffee_maker.force_stop()
    print 'done force stopping'

if __name__ == '__main__':
    app.run(host='0.0.0.0')
