from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app. config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:lolo22@127.0.0.1:5432/mytodoapp'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Todo(db.Model):
    __tablename__= 'todos'
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(), nullable=False)

    def __repr__(self):
        return f'<Todo {self.id} {self.description}>'

with app.app_context():
   db.create_all()

@app.route('/')
def index():
  return render_template('index.html', data=Todo.query.all())

if __name__ == '__main__':
   app.run(host="0.0.0.0", port=3000)
