from flask import Flask, request, abort

app = Flask(__name__)

# --- Helper Functions for Calc ---
def add(a, b):
    """Add a and b."""
    return a + b

def sub(a, b):
    """Subtract b from a."""
    return a - b

def mult(a, b):
    """Multiply a and b."""
    return a * b

def div(a, b):
    """Divide a by b."""
    return a / b

# --- Greet Routes ---
@app.route('/welcome')
def welcome():
    return "welcome"

@app.route('/welcome/home')
def home():
    return "welcome home"

@app.route('/welcome/back')
def back():
    return "welcome back"

# --- Calc Routes ---
# Individual endpoints for each operation
@app.route('/add')
def add_route():
    a = int(request.args.get('a'))
    b = int(request.args.get('b'))
    return str(add(a, b))

@app.route('/sub')
def sub_route():
    a = int(request.args.get('a'))
    b = int(request.args.get('b'))
    return str(sub(a, b))

@app.route('/mult')
def mult_route():
    a = int(request.args.get('a'))
    b = int(request.args.get('b'))
    return str(mult(a, b))

@app.route('/div')
def div_route():
    a = int(request.args.get('a'))
    b = int(request.args.get('b'))
    return str(div(a, b))

# Consolidated dynamic route using a dictionary
ops = {
    'add': add,
    'sub': sub,
    'mult': mult,
    'div': div
}

@app.route('/math/<operation>')
def math(operation):
    if operation not in ops:
        abort(404)
    a = int(request.args.get('a'))
    b = int(request.args.get('b'))
    result = ops[operation](a, b)
    return str(result)

if __name__ == '__main__':
    app.run(debug=True)
