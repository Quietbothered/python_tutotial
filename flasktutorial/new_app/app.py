from flask import Flask , request, redirect , url_for, session, Response, render_template

app = Flask(__name__)
app.secret_key = "MUKA"

@app.route("/",methods= ['GET', "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        if username == "admin" and password == "123":
            session["user"] = username #stored in session 
            return redirect(url_for("welcome"))
        else:
            return Response("Invalid credentials. Try again", mimetype ="text/plain") #text/html
        
    return '''
            <h2>Login Page</h2>
            <form method="POST">
            Username:<input type = "text" name = "username"><br>
            Password: <input type = "text" name = "password"><br>
            <input type = "submit" value = "Login">
            </form>
'''

#welcome page after login

@app.route("/welcome")
def welcome():
    if "user" in session:
        return   f'''
                <h2> Welcome, {session["user"]}!</h2>
                <a href= {url_for('logout')}>Logout</a>
                
    '''
        
    return redirect(url_for('login'))


#logout route
@app.route("/logout")
def logout():
    session.pop("user", None)
    return redirect(url_for("login"))







# @app.route("/about")
# def about():
#     return  "this is about page"
# @app.route("/contact")
# def contact():
#     return "contact page"

# @app.route("/submit", )
# def submit():
#     if request.method == "POST" :
#         return " You sent data"
#     else:
#         return "You are only viewing form"
    
