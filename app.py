from flask import Flask, render_template, request, jsonify
import math

app = Flask(__name__)

@app.route('/')
def index():
    """Render the main calculator page"""
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    """Handle calculator operations via API"""
    try:
        data = request.get_json()
        expression = data.get('expression', '')
        
        # Basic validation
        if not expression:
            return jsonify({'error': 'No expression provided'}), 400
        
        # Evaluate the expression safely
        result = evaluate_expression(expression)
        
        return jsonify({
            'result': result,
            'expression': expression
        })
        
    except Exception as e:
        return jsonify({'error': str(e)}), 400

def evaluate_expression(expression):
    """Safely evaluate mathematical expressions"""
    # Remove any potentially dangerous characters
    allowed_chars = set('0123456789+-*/.() ')
    if not all(c in allowed_chars for c in expression):
        raise ValueError("Invalid characters in expression")
    
    try:
        # Use eval with restricted globals for safety
        result = eval(expression, {"__builtins__": {}}, {})
        
        # Handle division by zero
        if isinstance(result, (int, float)) and math.isinf(result):
            raise ValueError("Division by zero")
        
        return result
    except ZeroDivisionError:
        raise ValueError("Division by zero")
    except Exception as e:
        raise ValueError(f"Invalid expression: {str(e)}")

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000) 