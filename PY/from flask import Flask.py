from flask import Flask

app = Flask(__name__)  # Create Flask app

@app.route("/")  # Home route
def home():
    return "Hello, Flask! voillla first web server deployment"

if __name__ == "__main__":
    app.run(debug=True)
