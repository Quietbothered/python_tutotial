from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime, timezone
import os

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
    date_created = db.Column(db.DateTime(timezone=True),
                             default=lambda: datetime.now(timezone.utc))

    def __repr__(self) -> str:
        return f"{self.sno} - {self.title}"

# Ensure DB is created
with app.app_context():
    try:
        db.create_all()
        print("✅ Database created successfully!")
        print("DB Path:", os.path.abspath("todo.db"))
    except Exception as e:
        print("❌ Error creating DB:", e)

@app.route('/')
def home(): 
    todo = Todo(title = "First todo", desc = "start investing in Stock markert manipulation")
    db.session.add(todo)
    db.session.commit()
    return render_template("index.html")
# @app.route('/show')
# def products():
#     alltodo = Todo.query.all()
#     return "this is product page"
@app.route('/show')
def products():
    alltodo = Todo.query.all()
    output = ""
    for todo in alltodo:
        output += f"{todo.sno}: {todo.title} - {todo.desc}<br>"
    return output if output else "No todos found."

    
if __name__ == "__main__":
    app.run(debug=True)
