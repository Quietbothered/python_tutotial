





# from flask import Flask , request, redirect , url_for, session, Response, render_template
# app = Flask(__name__)


# @app.route("/")
# def login():
#     return render_template("login.html")


# @app.route("/submit", methods = ["POST"])
# def submit():
#     username = request.form.get("username")
#     password = request.form.get("password")
    
#     '''if username == "sagar123" and password == "pass":
#         return render_template("welcome.html", name = username)
#     '''
#     valid_users = {
#         "admin": 'pass',
#         'rajat' : '123',
#         'rajat': 'raj'
        
#     }
#     if username in valid_users and password == valid_users[username]:
#         return render_template("welcome.html", name = username)
#     else:
#         return "invalid credentials "