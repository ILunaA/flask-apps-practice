from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello world with Flask web apps :D'




#@app is a decorator
#always include this at the bottom of your code
if __name__ == '__main__':
   app.run(host="0.0.0.0")
