# Q3. Explain how to pass a variable from a Flask route to an HTML template.
# Create a route that passes a username to a template and displays it in the browser.


from flask import Flask, render_template, url_for, request

app = Flask(__name__)

@app.route("/", methods = ["POST","GET"])
def home():
    name = "shubham"
    return render_template("index.html", username = name)
if __name__ == "__main__":
    app.run(debug=True, port =5000)




