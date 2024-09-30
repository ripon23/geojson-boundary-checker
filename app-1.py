from flask import Flask, render_template, jsonify
import json

app = Flask(__name__)

# Load your .json boundary file (assuming it's in the same directory)
with open('Dhaka-Dhaka.json') as f:
    boundary_data = json.load(f)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/boundary')
def boundary():
    return jsonify(boundary_data)

if __name__ == '__main__':
    app.run(debug=True)
