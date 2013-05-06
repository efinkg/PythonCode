from flask import Flask
import threading
app = Flask(__name__)
from coffeetime import CoffeeMakerSingleton
coffee_maker=CoffeeMakerSingleton()
from functools import wraps
from flask import request, Response

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
    coffee_thread = threading.Thread(target=coffee_maker.makeCoffee)
    coffee_thread.start()
    return "started coffee"

if __name__ == '__main__':
    app.run(host='0.0.0.0')
