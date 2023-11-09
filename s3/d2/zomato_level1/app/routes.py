from . import app

@app.route('/')
def hello_zesty_zomato():
    return "Hello, Zesty Zomato!"
