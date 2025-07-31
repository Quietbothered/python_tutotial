# Q4. How can you handle GET and POST requests in Flask?
# Write a route that accepts a form with a name field via POST request and displays "Hello, <name>!" on the webpage.


from flask import Flask, render_template, url_for, request , session , redirect

app = Flask(__name__)
app.secret_key = "MUKA"

@app.route("/", methods = ["POST", "GET"])
def home():
    if request.method == "POST":
        username = request.form.get("username")
        session['name']=username
        return redirect(url_for('welcome'))
    return '''<h2>Login Page</h2>
            <form method="POST">
            Username:<input type = "text" name = "username"><br>
            <input type = "submit" value = "enter">
            </form>
            '''
@app.route("/welcome")
def welcome():
    
    return f"""
        welcome {session['name']}
        

"""
if __name__ == "__main__":
    app.run(debug=True, port =5000)
