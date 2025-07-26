#crud operations create read update delete

from flask import Flask, render_template , request , redirect , url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime, timezone
import os
# import requests

app = Flask(__name__)

# Database URI - SQLite (file will be created in current directory)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///todo.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # Suppress deprecation warning

# Initialize database
db = SQLAlchemy(app)

# Todo Model
class Todo(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    desc = db.Column(db.String(500), nullable=False)
    date_created = db.Column(db.DateTime(timezone=True),default=lambda: datetime.now(timezone.utc))

    def __repr__(self) -> str:
        return f"{self.sno} - {self.title}"

# Ensure DB is created
with app.app_context():
    try:
        print("123") 
        db.create_all()
        print("✅ Database created successfully!")
        print("DB Path:", os.path.abspath("todo.db"))
    except Exception as e:
        print("❌ Error creating DB:", e)

@app.route('/' , methods = ['GET', 'POST'])
def home(): 
    if request.method == "POST" :
        # print("POST", request.form['title'])
        title = request.form['title']
        desc = request.form['desc']
        todo = Todo(title = title ,desc = desc )
        db.session.add(todo)
        db.session.commit()
        return redirect(url_for('home'))
    alltodo = Todo.query.all()
    return render_template("index.html" , alltodo = alltodo)
# @app.route('/show')
# def products():
#     alltodo = Todo.query.all()
#     return "this is product page"

@app.route('/delete/<int:sno>')
def delete(sno):
    todo = Todo.query.filter_by(sno= sno).first()
    db.session.delete(todo)
    db.session.commit()
    return redirect("/")

@app.route('/update/<int:sno>' ,  methods = ['GET', 'POST'])
def update(sno):
    if request.method == "POST" :
        title = request.form['title']
        desc = request.form['desc']
        todo = Todo.query.filter_by(sno= sno).first()
        todo.title = title
        todo.desc = desc
        db.session.add(todo)
        db.session.commit()
        return redirect(url_for('home'))
    todo = Todo.query.filter_by(sno = sno).first()
    return render_template('update.html',todo = todo )
    
if __name__ == "__main__":
    app.run(debug=True, port= 8000)
