from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app. config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:lolo22@127.0.0.1:5432/table4'
db = SQLAlchemy(app)

class Person (db.Model):
    __tablename__= 'persons'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(), nullable=False)

db.create_all()

@app.route('/')
def index():
    return 'Hello world with Flask web apps :D'




#@app is a decorator
#always include this at the bottom of your code
if __name__ == '__main__':
   app.run(host="0.0.0.0")
