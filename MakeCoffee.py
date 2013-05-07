from flask import Flask
import threading
app = Flask(__name__)
from coffeetimethreading import CoffeeMakerSingleton
from functools import wraps
from flask import request, Response

coffee_maker = CoffeeMakerSingleton()

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
def index():
    return 'Index Page'

@app.route("/coffee")
@requires_auth
def start_coffee():
    coffee_maker.makeCoffee()
    return "Started Coffee"

@app.route("/killall")
def killall():
    coffee_maker.force_stop()
    print 'done force stopping'
    return 'Its dead, Jim'

if __name__ == '__main__':
    app.run(host='0.0.0.0')
