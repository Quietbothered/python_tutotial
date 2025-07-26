from flask import render_template, Flask, request, url_for , redirect , jsonify
from  datetime import datetime , timezone
import os


app = Flask(__name__)

@app.route('/', methods = ['GET', 'POST'])
def home():
    
    reversed_string = None

    if request.method == 'POST':
        input_str = request.form.get('input_string', '')
        reversed_string = input_str[::-1]  # Reverse the string
    return render_template('index.html', reversed_string = reversed_string)

@app.route('/api/reverse', methods=['POST'])
def reverse_api():
    data = request.get_json()
    original = data.get('string', '')
    reversed_str = original[::-1]
    return jsonify({
        'original': original,
        'reversed': reversed_str
    })


if __name__ == "__main__":
    app.run(debug=True, port=8000)