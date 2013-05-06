from flask import Flask
app = Flask(__name__)
from coffeetest import CoffeeMakerSingleton
coffee_maker=CoffeeMakerSingleton()

@app.route('/')
def index():
    return 'Index Page'

@app.route("/coffee")
def start_coffee():
    return coffee_maker.makeCoffee()

if __name__ == '__main__':
    app.run(host='0.0.0.0')
