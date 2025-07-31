# # Q5. Problem Statement: Flask API for Surface Area & Volume Calculation
# Objective:
# Create a Flask API that allows users to calculate the surface area or volume of geometric shapes through a web interface.
# Requirements:
# ✅ Step 1: Selection Page
# Dropdown 1: Select calculation type (Surface Area / Volume)
# Dropdown 2: Select shape (Circle, Square, Sphere, Cylinder, etc.)
# Submit button: Redirects to an input form
# ✅ Step 2: Dynamic Input Page
# Display required fields dynamically based on shape and calculation type selected.
# Examples:
# Circle (Surface Area): Input → Radius
# Cylinder (Volume): Input → Radius, Height
# ✅ Step 3: Display Result
# Show the calculated surface area or volume.
# Example Output:
# "The surface area of a sphere with radius 5 is 314.16 sq units."

from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def select():
    if request.method == "POST":
        calc_type = request.form["calc_type"]
        shape = request.form["shape"]
        return redirect(url_for("input_form", calc_type=calc_type, shape=shape))
    return render_template("selection.html")

@app.route("/input", methods=["GET", "POST"])
def input_form():
    calc_type = request.args.get("calc_type")
    shape = request.args.get("shape")

    if request.method == "POST":
        data = request.form
        result = calculate(calc_type, shape, data)
        return render_template("result.html", result=result)

    return render_template("input_form.html", calc_type=calc_type, shape=shape)

def calculate(calc_type, shape, data):
    from math import pi

    try:
        if shape == "Circle":
            r = float(data["radius"])
            if calc_type == "Surface Area":
                return f"The surface area of a circle with radius {r} is {round(pi * r * r, 2)} sq units."
        elif shape == "Sphere":
            r = float(data["radius"])
            if calc_type == "Surface Area":
                return f"The surface area of a sphere with radius {r} is {round(4 * pi * r**2, 2)} sq units."
            else:
                return f"The volume of a sphere with radius {r} is {round((4/3) * pi * r**3, 2)} cu units."
        elif shape == "Cylinder":
            r = float(data["radius"])
            h = float(data["height"])
            if calc_type == "Surface Area":
                return f"The surface area of a cylinder is {round(2 * pi * r * (r + h), 2)} sq units."
            else:
                return f"The volume of a cylinder is {round(pi * r**2 * h, 2)} cu units."
        elif shape == "Square":
            a = float(data["side"])
            if calc_type == "Surface Area":
                return f"The surface area of a square is {round(a * a, 2)} sq units."
    except:
        return "Invalid input."
    return "Unsupported combination."

if __name__ == "__main__":
    app.run(debug=True)
