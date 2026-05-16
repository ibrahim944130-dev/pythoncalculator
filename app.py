from flask import Flask, render_template, request, jsonify
from src.simple_project.calculator import (
    add, subtract, multiply, divide, 
    square_root, power, sine, cosine, tangent, logarithm
)

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    data = request.get_json()
    operation = data.get('operation')
    a = float(data.get('a'))
    
    # Binary operations need 'b'
    b_raw = data.get('b')
    b = float(b_raw) if b_raw is not None else None
    
    try:
        if operation == 'add':
            result = add(a, b)
        elif operation == 'subtract':
            result = subtract(a, b)
        elif operation == 'multiply':
            result = multiply(a, b)
        elif operation == 'divide':
            result = divide(a, b)
        elif operation == 'sqrt':
            result = square_root(a)
        elif operation == 'pow':
            result = power(a, b)
        elif operation == 'sin':
            result = sine(a)
        elif operation == 'cos':
            result = cosine(a)
        elif operation == 'tan':
            result = tangent(a)
        elif operation == 'log':
            result = logarithm(a)
        else:
            return jsonify({'success': False, 'error': 'Invalid operation'}), 400
        
        return jsonify({'success': True, 'result': result})
    except ValueError as e:
        return jsonify({'success': False, 'error': str(e)}), 400
    except Exception as e:
        return jsonify({'success': False, 'error': 'An unexpected error occurred'}), 500

if __name__ == '__main__':
    app.run(debug=True, port=5001)
