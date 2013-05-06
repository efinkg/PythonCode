from flask import Flask
import threading
app = Flask(__name__)
from coffeetest import CoffeeMakerSingleton
coffee_maker=CoffeeMakerSingleton()

@app.route('/')
def index():
    return 'Index Page'

@app.route("/coffee")
def start_coffee():
    coffee_thread = threading.Thread(target=coffee_maker.makeCoffee)
    coffee_thread.start()
    return "started coffee"

if __name__ == '__main__':
    app.run(host='0.0.0.0')
