"""
Simple Flask Web Application for Teaching CI/CD
This is a basic calculator app that demonstrates:
- A simple Python web framework (Flask)
- API endpoints
- HTML/CSS/JavaScript frontend
- Testing concepts
"""

from flask import Flask, request, jsonify, render_template

app = Flask(__name__)


def add(a, b):
    """Add two numbers"""
    return a + b


def subtract(a, b):
    """Subtract two numbers"""
    return a - b


def multiply(a, b):
    """Multiply two numbers"""
    return a * b


def divide(a, b):
    """Divide two numbers"""
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b


@app.route('/', methods=['GET'])
def home():
    """Home endpoint - serves the HTML interface"""
    return render_template('index.html')


@app.route('/add', methods=['GET'])
def add_endpoint():
    """REST API endpoint for addition"""
    try:
        a = float(request.args.get('a', 0))
        b = float(request.args.get('b', 0))
        result = add(a, b)
        return jsonify({'result': result, 'operation': 'add'}), 200
    except ValueError:
        return jsonify({'error': 'Invalid input'}), 400


@app.route('/subtract', methods=['GET'])
def subtract_endpoint():
    """REST API endpoint for subtraction"""
    try:
        a = float(request.args.get('a', 0))
        b = float(request.args.get('b', 0))
        result = subtract(a, b)
        return jsonify({'result': result, 'operation': 'subtract'}), 200
    except ValueError:
        return jsonify({'error': 'Invalid input'}), 400


@app.route('/multiply', methods=['GET'])
def multiply_endpoint():
    """REST API endpoint for multiplication"""
    try:
        a = float(request.args.get('a', 0))
        b = float(request.args.get('b', 0))
        result = multiply(a, b)
        return jsonify({'result': result, 'operation': 'multiply'}), 200
    except ValueError:
        return jsonify({'error': 'Invalid input'}), 400


@app.route('/divide', methods=['GET'])
def divide_endpoint():
    """REST API endpoint for division"""
    try:
        a = float(request.args.get('a', 0))
        b = float(request.args.get('b', 1))
        result = divide(a, b)
        return jsonify({'result': result, 'operation': 'divide'}), 200
    except ValueError as e:
        return jsonify({'error': str(e)}), 400


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
