from flask import Flask , render_template, request,url_for, redirect, flash
app = Flask(__name__)

@app.route("/", methods = ["GET", "POST"])
def form():
    if request.form == "POST" :
        name = request.form.get("name")
        if not name :
            flash("Name cannot be empty")
            return redirect(url_for("form"))
        flash(f"thanks {name} , your feedback was saved")
        return render_template("thankyou.html")
    
    return render_template("form.html")

@app.route("/thankyou")
def thankyou():
    return render_template("thankyou.html")
# @app.route("/feedback", methods = ["post","GET"])
# def feedback():
#     if request.method == "POST":
#         name = request.form.get("username")
#         message = request.form.get("message")
#         return render_template("thankyou.html", user = name, message=message)
#     return render_template("feedback.html")

if __name__ == "__main__":
    app.run(debug=True, port= 8000)
