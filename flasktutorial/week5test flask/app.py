#Q2. How would you create a basic route in Flask that returns "Hello, World!" when accessed?
from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "<h2>Hello, World!</h2>"

if __name__ == "__main__":
    app.run(debug=True, port =5000)
